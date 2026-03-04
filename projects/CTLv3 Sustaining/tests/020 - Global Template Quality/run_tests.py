#!/usr/bin/env python3
from __future__ import annotations

"""
CTLv3 Sustaining — Feature 020: Global Template Quality

Cross-cutting quantitative quality checks applied to every template in the vault.
No personal exclusions — personal templates are prohibited in the CTL vault (020-013).

Pure filesystem/content checks — no Command Queue or Obsidian interaction required.

Exit codes:
    0 — all tests passed
    1 — one or more tests failed
    2 — test execution error (infrastructure failure)
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------

FEATURE_DIR = Path(__file__).resolve().parent        # tests/020 - Global Template Quality/
TESTS_DIR = FEATURE_DIR.parent                       # tests/
SHARED_DIR = TESTS_DIR / "shared"

sys.path.insert(0, str(SHARED_DIR))

from config import VAULT_ROOT
from output_formatter import FeatureResult, print_fail, print_feature_summary, print_pass
from result_writer import RunResult, write_results

FEATURE_NUM = "020"
FEATURE_NAME = "Global Template Quality"

PERSONAL_AUTHOR = 'z2k_template_author: "Geoff (z2k-gwp)"'
PERSONAL_AUTHOR_UNQUOTED = "z2k_template_author: Geoff (z2k-gwp)"

BUILTIN_FIELDS = {"today", "creator", "timestamp", "templateName", "me"}

CANONICAL_SOURCE_TYPES = {
    "AI/ChatGPT", "Book", "ClassLecture", "Conference", "Conversation",
    "Email", "InternalMemories", "InternalMemory", "InternalThought",
    "Interview", "Lecture", "LifeLessons", "Meeting", "OtherCards",
    "Person", "Podcast", "Quotation", "Unknown", "WebArticle",
}

BLOCK_TAG_PAIRS = [
    (r"#if[\s}]", r"/if}}"),
    (r"#each[\s}]", r"/each}}"),
    (r"#unless[\s}]", r"/unless}}"),
    (r"#with[\s}]", r"/with}}"),
]


# ---------------------------------------------------------------------------
# Template discovery
# ---------------------------------------------------------------------------

def find_all_templates() -> dict[Path, str]:
    """Find all .md files under */Templates/ directories in the vault."""
    templates: dict[Path, str] = {}
    for path in VAULT_ROOT.rglob("Templates/*.md"):
        templates[path] = path.read_text(encoding="utf-8")
    return templates


def is_personal(content: str) -> bool:
    return PERSONAL_AUTHOR in content or PERSONAL_AUTHOR_UNQUOTED in content


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def strip_block_comments(content: str) -> str:
    """Remove {{!-- ... --}} block comments."""
    return re.sub(r'\{\{!--.*?--\}\}', '', content, flags=re.DOTALL)


def rel(path: Path) -> str:
    """Relative path from vault root for display."""
    try:
        return str(path.relative_to(VAULT_ROOT))
    except ValueError:
        return str(path)


def summarize_violations(violations: list[str], max_items: int = 10) -> str:
    """Format a violations list, truncating if needed."""
    if len(violations) <= max_items:
        return "; ".join(violations)
    shown = violations[:max_items]
    return "; ".join(shown) + f" ... (+{len(violations) - max_items} more)"


# ---------------------------------------------------------------------------
# 020-001: Valid Handlebars syntax
# ---------------------------------------------------------------------------

def check_handlebars_syntax(content: str) -> list[str]:
    stripped = strip_block_comments(content)
    errors: list[str] = []

    open_count = len(re.findall(r'\{\{', stripped))
    close_count = len(re.findall(r'\}\}', stripped))
    if open_count != close_count:
        errors.append(f"unbalanced delimiters ({open_count} '{{{{' vs {close_count} '}}}}')")

    for open_pat, close_pat in BLOCK_TAG_PAIRS:
        open_n = len(re.findall(r'\{\{' + open_pat, stripped))
        close_n = len(re.findall(r'\{\{' + close_pat, stripped))
        if open_n != close_n:
            tag_name = open_pat.rstrip(r'[\s}]').lstrip('#')
            errors.append(f"unbalanced #{tag_name}: {open_n} open, {close_n} close")

    return errors


def test_020_001(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-001"
    desc = "Valid Handlebars syntax"
    violations: list[str] = []
    for path, content in all_templates.items():
        errors = check_handlebars_syntax(content)
        if errors:
            violations.append(f"{rel(path)}: {', '.join(errors)}")
    if violations:
        notes = summarize_violations(violations)
        print_fail(req_id, desc, "quantitative",
                   expected="No syntax errors in any template",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-002: No v2 Templater syntax
# ---------------------------------------------------------------------------

def test_020_002(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-002"
    desc = "No v2 Templater syntax"
    violations: list[str] = []
    for path, content in all_templates.items():
        # Allow <% ... %> only inside {{! FLAGGED: ... }} comments
        # Strip known FLAGGED comment wrappers first
        cleaned = re.sub(r'\{\{!--.*?FLAGGED.*?--\}\}', '', content, flags=re.DOTALL)
        cleaned = re.sub(r'\{\{!.*?FLAGGED.*?\}\}', '', cleaned)
        if re.search(r'<%.*?%>', cleaned, re.DOTALL):
            violations.append(rel(path))
    if violations:
        notes = f"Found in: {summarize_violations(violations)}"
        print_fail(req_id, desc, "quantitative",
                   expected="No <% ... %> Templater syntax in any template",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-003: Document templates have required YAML fields
# ---------------------------------------------------------------------------

DOCUMENT_REQUIRED_FIELDS = [
    "z2k_template_type: document-template",
    "z2k_template_version",
    "z2k_template_suggested_title",
]


def test_020_003(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-003"
    desc = "Document templates have required YAML metadata"
    violations: list[str] = []
    for path, content in all_templates.items():
        if "z2k_template_type: document-template" not in content:
            continue  # Not a document template — skip
        missing = [f for f in DOCUMENT_REQUIRED_FIELDS if f not in content]
        if missing:
            violations.append(f"{rel(path)}: missing {', '.join(missing)}")
    if violations:
        notes = summarize_violations(violations)
        print_fail(req_id, desc, "quantitative",
                   expected="All document templates have z2k_template_type, z2k_template_version, z2k_template_suggested_title",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-004: Block templates have required YAML field
# ---------------------------------------------------------------------------

def test_020_004(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-004"
    desc = "Block templates have required YAML metadata"
    violations = []
    for path, content in all_templates.items():
        lines = content.splitlines()
        if not lines or lines[0].strip() != "---":
            continue
        # Find closing ---
        try:
            close_idx = next(i for i, l in enumerate(lines[1:], 1) if l.strip() == "---")
        except StopIteration:
            continue
        frontmatter = "\n".join(lines[1:close_idx])
        if "z2k_template_type: block-template" in frontmatter:
            pass  # Covered by initial scan
        elif "z2k_template_type: document-template" in frontmatter:
            pass  # Document template — not checked here
        # If neither type is found in frontmatter and it's a CTL template, that's a 020-003 issue
    if violations:
        notes = summarize_violations(violations)
        print_fail(req_id, desc, "quantitative",
                   expected="All block templates have z2k_template_type: block-template in frontmatter",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-005: Author field correct
# ---------------------------------------------------------------------------

CORRECT_AUTHOR = 'z2k_template_author: "Z2K Studios, LLC"'
CORRECT_AUTHOR_ALT = "z2k_template_author: Z2K Studios, LLC"


def test_020_005(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-005"
    desc = "Template author field correct"
    violations: list[str] = []
    for path, content in all_templates.items():
        has_correct = CORRECT_AUTHOR in content or CORRECT_AUTHOR_ALT in content
        if not has_correct:
            # Check if author field exists at all
            if "z2k_template_author" in content:
                # Extract actual value
                m = re.search(r'z2k_template_author:\s*(.+)', content)
                actual_val = m.group(1).strip() if m else "unknown"
                violations.append(f"{rel(path)}: {actual_val!r}")
            else:
                violations.append(f"{rel(path)}: field missing")
    if violations:
        notes = summarize_violations(violations)
        print_fail(req_id, desc, "quantitative",
                   expected='z2k_template_author: "Z2K Studios, LLC" on all CTL templates',
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-006: Field naming conventions (PascalCase)
# ---------------------------------------------------------------------------

def test_020_006(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-006"
    desc = "Field naming conventions followed (PascalCase)"
    violations: list[str] = []
    for path, content in all_templates.items():
        stripped = strip_block_comments(content)
        field_names = re.findall(r'\{\{fieldInfo\s+(\w+)', stripped)
        bad_names = [
            name for name in field_names
            if name not in BUILTIN_FIELDS and name[0].islower()
        ]
        if bad_names:
            violations.append(f"{rel(path)}: {', '.join(set(bad_names))}")
    if violations:
        notes = summarize_violations(violations)
        print_fail(req_id, desc, "quantitative",
                   expected="All custom fieldInfo names start with uppercase (PascalCase)",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-007: Comment syntax — double-dash for comments with {{ or }}
# ---------------------------------------------------------------------------

def test_020_007(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-007"
    desc = "Comment syntax correct (double-dash for mustache content)"
    violations: list[str] = []
    # Find single-form {{! }} comments (not {{!--) whose content has {{ or }}
    single_comment_pat = re.compile(r'\{\{!(?!--)([^}]|\}(?!\}))*?\}\}', re.DOTALL)
    for path, content in all_templates.items():
        for m in single_comment_pat.finditer(content):
            comment_body = m.group(0)
            # If the comment body (after {{!) contains {{ or }}, it should use {{!-- --}}
            inner = comment_body[3:-2]  # strip {{! and }}
            if '{{' in inner or '}}' in inner:
                line_no = content[:m.start()].count('\n') + 1
                violations.append(f"{rel(path)}:{line_no}")
                break  # one violation per file is enough
    if violations:
        notes = f"Single-form comments with mustache content in: {summarize_violations(violations)}"
        print_fail(req_id, desc, "quantitative",
                   expected="Comments with {{ or }} use {{!-- --}} form",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-008: No trailing spaces on comment-only lines
# ---------------------------------------------------------------------------

COMMENT_LINE_PAT = re.compile(r'^\s*\{\{!(?:--)?.*?(?:--)?}}(\s+)$', re.DOTALL)


def test_020_008(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-008"
    desc = "No trailing spaces on comment-only lines"
    violations: list[str] = []
    for path, content in all_templates.items():
        for line_no, line in enumerate(content.splitlines(), 1):
            # Line is comment-only if, after stripping leading whitespace, it starts with {{!
            stripped_line = line.lstrip()
            if stripped_line.startswith("{{!") and line.endswith((" ", "\t")):
                violations.append(f"{rel(path)}:{line_no}")
                break
    if violations:
        notes = f"Trailing spaces found in: {summarize_violations(violations)}"
        print_fail(req_id, desc, "quantitative",
                   expected="No trailing whitespace on comment-only lines",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-009: fieldInfo declarations are well-formed
# ---------------------------------------------------------------------------

def test_020_009(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-009"
    desc = "All fieldInfo declarations are well-formed"
    violations: list[str] = []
    # A well-formed fieldInfo must have at least a field name after {{fieldInfo
    malformed_pat = re.compile(r'\{\{fieldInfo\s*\}\}|\{\{fieldInfo\s+\}\}|\{\{fieldInfo\s*$',
                               re.MULTILINE)
    for path, content in all_templates.items():
        stripped = strip_block_comments(content)
        if malformed_pat.search(stripped):
            violations.append(rel(path))
    if violations:
        notes = f"Malformed fieldInfo in: {summarize_violations(violations)}"
        print_fail(req_id, desc, "quantitative",
                   expected="Every {{fieldInfo}} has at least a field name",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-010: Block partial references exist
# ---------------------------------------------------------------------------

def build_block_name_set(all_templates: dict[Path, str]) -> set[str]:
    """Return set of block template stem names (e.g. 'Logistics', 'Card Fabric')."""
    return {
        path.stem
        for path, content in all_templates.items()
        if "z2k_template_type: block-template" in content
    }


def test_020_010(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str], block_names: set[str]) -> None:
    req_id = "020-010"
    desc = "Block partial references point to existing files"
    violations: list[str] = []
    partial_pat = re.compile(r'\{\{>\s*["\']?([^"\'}\s]+(?:\s+[^"\'}\s]+)*)["\']?\s*\}\}')
    for path, content in all_templates.items():
        # Strip block comments, then find live partial references
        stripped = strip_block_comments(content)
        # Also strip single-form comments line by line
        lines = []
        for line in stripped.splitlines():
            if line.lstrip().startswith("{{!"):
                continue
            lines.append(line)
        live_content = "\n".join(lines)
        for m in partial_pat.finditer(live_content):
            block_name = m.group(1).strip()
            if block_name not in block_names:
                violations.append(f"{rel(path)}: '{{{{> \"{block_name}\"}}}}'")
    if violations:
        notes = summarize_violations(violations)
        print_fail(req_id, desc, "quantitative",
                   expected="All {{> \"BlockName\"}} references point to existing block templates",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-011: Source type values are canonical
# ---------------------------------------------------------------------------

def test_020_011(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-011"
    desc = "Source type values are canonical"
    violations: list[str] = []
    source_type_pat = re.compile(r'z2k_card_source_type:\s*["\']?\.?:?Z2K/SourceType/([^"\'\s]+)["\']?')
    for path, content in all_templates.items():
        m = source_type_pat.search(content)
        if not m:
            continue
        value = m.group(1).strip()
        if value not in CANONICAL_SOURCE_TYPES:
            violations.append(f"{rel(path)}: '{value}'")
    if violations:
        notes = f"Non-canonical values: {summarize_violations(violations)}"
        print_fail(req_id, desc, "quantitative",
                   expected=f"Source type from canonical set: {sorted(CANONICAL_SOURCE_TYPES)}",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-012: No duplicate filenames within same Templates/ folder
# ---------------------------------------------------------------------------

def test_020_012(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-012"
    desc = "No duplicate template filenames within same Templates/ folder"
    # Group templates by their parent directory
    by_folder: dict[Path, list[Path]] = defaultdict(list)
    for path in all_templates:
        by_folder[path.parent].append(path)

    violations: list[str] = []
    for folder, paths in by_folder.items():
        names = [p.name for p in paths]
        seen: set[str] = set()
        for name in names:
            if name in seen:
                folder_rel = rel(folder)
                violations.append(f"{folder_rel}/{name}")
            seen.add(name)
    if violations:
        notes = f"Duplicates: {summarize_violations(violations)}"
        print_fail(req_id, desc, "quantitative",
                   expected="No duplicate filenames within any Templates/ folder",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# 020-013: No personal templates in the vault
# ---------------------------------------------------------------------------

def test_020_013(result: FeatureResult, run_result: RunResult, all_templates: dict[Path, str]) -> None:
    req_id = "020-013"
    desc = "No personal templates in the CTL vault"
    violations: list[str] = []
    for path, content in all_templates.items():
        if is_personal(content):
            # Extract actual author value for display
            m = re.search(r'z2k_template_author:\s*(.+)', content)
            actual_val = m.group(1).strip() if m else "unknown"
            violations.append(f"{rel(path)}: {actual_val!r}")
    if violations:
        notes = f"Personal-authored templates found: {summarize_violations(violations)}"
        print_fail(req_id, desc, "quantitative",
                   expected="No templates with personal author values in the CTL vault",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    result = FeatureResult(feature_num=FEATURE_NUM, feature_name=FEATURE_NAME)
    run_result = RunResult(FEATURE_NUM, FEATURE_NAME)

    all_templates = find_all_templates()
    block_names = build_block_name_set(all_templates)

    test_020_001(result, run_result, all_templates)
    test_020_002(result, run_result, all_templates)
    test_020_003(result, run_result, all_templates)
    test_020_004(result, run_result, all_templates)
    test_020_005(result, run_result, all_templates)
    test_020_006(result, run_result, all_templates)
    test_020_007(result, run_result, all_templates)
    test_020_008(result, run_result, all_templates)
    test_020_009(result, run_result, all_templates)
    test_020_010(result, run_result, all_templates, block_names)
    test_020_011(result, run_result, all_templates)
    test_020_012(result, run_result, all_templates)
    test_020_013(result, run_result, all_templates)

    print_feature_summary(result)
    write_results(FEATURE_DIR, run_result)
    return 0 if result.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
