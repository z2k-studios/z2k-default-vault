#!/usr/bin/env python3
from __future__ import annotations

"""
CTLv3 Sustaining — Feature 004: System Blocks

Validates that the root and 13 domain system blocks exist with correct fields,
YAML delimiters, domain values, ratings fields, privacy fields, and stops.

Pure filesystem/content checks — no Command Queue or Obsidian interaction required.

Exit codes:
    0 — all tests passed
    1 — one or more tests failed
    2 — test execution error (infrastructure failure)
"""

import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Path setup — allow running from any working directory
# ---------------------------------------------------------------------------

FEATURE_DIR = Path(__file__).resolve().parent        # tests/004 - System Blocks/
TESTS_DIR = FEATURE_DIR.parent                       # tests/
SHARED_DIR = TESTS_DIR / "shared"

sys.path.insert(0, str(SHARED_DIR))

from config import VAULT_ROOT
from output_formatter import FeatureResult, print_fail, print_feature_summary, print_pass
from result_writer import RunResult, write_results

FEATURE_NUM = "004"
FEATURE_NAME = "System Blocks"

DOMAIN_FOLDERS = [
    "Information",
    "Thoughts",
    "Beliefs",
    "Memories",
    "Interactions",
    "Journals",
    "Logs",
    "Locations",
    "Projects",
    "Entities",
    "Body",
    "AI",
    "System",
]

RATINGS_DOMAINS = {"Information", "Thoughts", "Beliefs", "Memories"}
RATINGS_FIELDS = ["z2k_rating_depth", "z2k_rating_surprisal", "z2k_rating_passion"]

DOMAIN_VALUES = {
    "Information":  ".:Z2K/Domain/Information",
    "Thoughts":     ".:Z2K/Domain/Thoughts",
    "Beliefs":      ".:Z2K/Domain/Beliefs",
    "Memories":     ".:Z2K/Domain/Memories",
    "Interactions": ".:Z2K/Domain/Interactions",
    "Journals":     ".:Z2K/Domain/Journals",
    "Logs":         ".:Z2K/Domain/Logs",
    "Locations":    ".:Z2K/Domain/Locations",
    "Projects":     ".:Z2K/Domain/Projects",
    "Entities":     ".:Z2K/Domain/Entities",
    "Body":         ".:Z2K/Domain/Body",
    "AI":           ".:Z2K/Domain/AI",
    "System":       ".:Z2K/Domain/System",
}

ROOT_REQUIRED_FIELDS = [
    "z2k_metadata_version",
    "z2k_metadata_variant",
    "z2k_metadata_copyright",
    "z2k_metadata_reference",
    "z2k_creation_creator",
    "z2k_creation_date",
    "z2k_creation_timestamp",
    "z2k_creation_template",
    "z2k_creation_language",
    "z2k_creation_library_version",
    "z2k_card_source_type",
]

ROOT_DEPRECATED_FIELDS = [
    "z2k_creation_domain",
    "z2k_card_build_state",
    "z2k_card_status",
]


def has_yaml_delimiters(content: str) -> bool:
    """Return True if content has opening and closing --- delimiters."""
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return False
    # Look for a closing --- after the first line
    return any(line.strip() == "---" for line in lines[1:])


# ---------------------------------------------------------------------------
# Root system block tests
# ---------------------------------------------------------------------------

def test_004_001_root_exists(result: FeatureResult, run_result: RunResult) -> Path | None:
    """004-001: Root system block exists."""
    req_id = "004-001"
    desc = "Root system block exists"
    path = VAULT_ROOT / ".system-block.md"
    if not path.exists():
        notes = "File not found"
        print_fail(req_id, desc, "quantitative",
                   expected=f"{path} exists",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
        return None
    print_pass(req_id, desc, "quantitative")
    result.passed += 1
    run_result.add_req(req_id, desc, "PASS")
    return path


def test_004_002_root_yaml_delimiters(result: FeatureResult, run_result: RunResult, content: str) -> None:
    """004-002: Root system block has YAML frontmatter delimiters."""
    req_id = "004-002"
    desc = "Root system block has YAML delimiters"
    if has_yaml_delimiters(content):
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")
    else:
        notes = "Missing or malformed YAML frontmatter delimiters"
        print_fail(req_id, desc, "quantitative",
                   expected="File starts with --- and has closing ---",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)


def test_004_003_root_required_fields(result: FeatureResult, run_result: RunResult, content: str) -> None:
    """004-003: Root system block has all required fields."""
    req_id = "004-003"
    desc = "Root system block required fields present"
    missing = [f for f in ROOT_REQUIRED_FIELDS if f not in content]
    if missing:
        notes = f"Missing: {', '.join(missing)}"
        print_fail(req_id, desc, "quantitative",
                   expected="All 11 required fields present",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_004_004_root_deprecated_absent(result: FeatureResult, run_result: RunResult, content: str) -> None:
    """004-004: Root system block has no deprecated fields."""
    req_id = "004-004"
    desc = "Root system block deprecated fields absent"
    present = [f for f in ROOT_DEPRECATED_FIELDS if f in content]
    if present:
        notes = f"Found deprecated fields: {', '.join(present)}"
        print_fail(req_id, desc, "quantitative",
                   expected="No deprecated fields in root system block",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_004_005_root_me_fieldinfo(result: FeatureResult, run_result: RunResult, content: str) -> None:
    """004-005: Root system block body contains {{fieldInfo me value="me"}}."""
    req_id = "004-005"
    desc = 'Root system block has me fieldInfo'
    target = '{{fieldInfo me value="me"}}'
    if target in content:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")
    else:
        notes = "String not found in root system block"
        print_fail(req_id, desc, "quantitative",
                   expected=f'Body contains: {target}',
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)


# ---------------------------------------------------------------------------
# Domain system block tests
# ---------------------------------------------------------------------------

def load_domain_blocks() -> dict[str, str | None]:
    """Read all 13 domain system blocks. Value is content string or None if missing."""
    blocks: dict[str, str | None] = {}
    for domain in DOMAIN_FOLDERS:
        path = VAULT_ROOT / domain / ".system-block.md"
        if path.exists():
            blocks[domain] = path.read_text(encoding="utf-8")
        else:
            blocks[domain] = None
    return blocks


def test_004_006_domain_blocks_exist(result: FeatureResult, run_result: RunResult, blocks: dict[str, str | None]) -> None:
    """004-006: All 13 domain system blocks exist."""
    req_id = "004-006"
    desc = "All 13 domain system blocks exist"
    missing = [d for d, content in blocks.items() if content is None]
    if missing:
        notes = f"Missing in: {', '.join(missing)}"
        print_fail(req_id, desc, "quantitative",
                   expected="All 13 .system-block.md files exist",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_004_007_domain_values(result: FeatureResult, run_result: RunResult, blocks: dict[str, str | None]) -> None:
    """004-007: Each domain system block has the correct z2k_creation_domain value."""
    req_id = "004-007"
    desc = "Domain system blocks have correct z2k_creation_domain"
    wrong: list[str] = []
    for domain, content in blocks.items():
        if content is None:
            wrong.append(f"{domain} (file missing)")
            continue
        expected_value = DOMAIN_VALUES[domain]
        if "z2k_creation_domain" not in content or expected_value not in content:
            wrong.append(f"{domain} (expected {expected_value!r})")
    if wrong:
        notes = f"Incorrect: {'; '.join(wrong)}"
        print_fail(req_id, desc, "quantitative",
                   expected="All domains have correct canonical domain value",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_004_008_ratings_fields_present(result: FeatureResult, run_result: RunResult, blocks: dict[str, str | None]) -> None:
    """004-008: Ratings domains have all 3 ratings fields."""
    req_id = "004-008"
    desc = "Ratings domains have ratings fields"
    wrong: list[str] = []
    for domain in RATINGS_DOMAINS:
        content = blocks.get(domain)
        if content is None:
            wrong.append(f"{domain} (file missing)")
            continue
        missing_fields = [f for f in RATINGS_FIELDS if f not in content]
        if missing_fields:
            wrong.append(f"{domain} missing: {', '.join(missing_fields)}")
    if wrong:
        notes = "; ".join(wrong)
        print_fail(req_id, desc, "quantitative",
                   expected="Information, Thoughts, Beliefs, Memories all have 3 ratings fields",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_004_009_ratings_fields_absent(result: FeatureResult, run_result: RunResult, blocks: dict[str, str | None]) -> None:
    """004-009: Non-ratings domains do NOT have ratings fields."""
    req_id = "004-009"
    desc = "Non-ratings domains lack ratings fields"
    wrong: list[str] = []
    for domain in DOMAIN_FOLDERS:
        if domain in RATINGS_DOMAINS:
            continue
        content = blocks.get(domain)
        if content is None:
            continue  # Existence already checked in 004-006
        present_fields = [f for f in RATINGS_FIELDS if f in content]
        if present_fields:
            wrong.append(f"{domain} has: {', '.join(present_fields)}")
    if wrong:
        notes = "; ".join(wrong)
        print_fail(req_id, desc, "quantitative",
                   expected="No ratings fields in non-ratings domains",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_004_010_privacy_fields(result: FeatureResult, run_result: RunResult, blocks: dict[str, str | None]) -> None:
    """004-010: Journals and Logs have correct privacy field values."""
    req_id = "004-010"
    desc = "Privacy fields correct"
    wrong: list[str] = []
    checks = {
        "Journals": '.:Z2K/Privacy/Private/Journal',
        "Logs":     '.:Z2K/Privacy/Private/Log',
    }
    for domain, expected_value in checks.items():
        content = blocks.get(domain)
        if content is None:
            wrong.append(f"{domain} (file missing)")
            continue
        if "z2k_card_privacy" not in content or expected_value not in content:
            wrong.append(f"{domain} (expected z2k_card_privacy: {expected_value!r})")
    if wrong:
        notes = "; ".join(wrong)
        print_fail(req_id, desc, "quantitative",
                   expected="Journals and Logs have correct z2k_card_privacy values",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_004_011_ai_perspective(result: FeatureResult, run_result: RunResult, blocks: dict[str, str | None]) -> None:
    """004-011: AI domain system block has z2k_creation_perspective: "AI"."""
    req_id = "004-011"
    desc = "AI domain has perspective field"
    content = blocks.get("AI")
    if content is None:
        notes = "AI system block file missing"
        print_fail(req_id, desc, "quantitative",
                   expected='z2k_creation_perspective: "AI" present',
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
        return
    if "z2k_creation_perspective" in content and '"AI"' in content:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")
    else:
        notes = "Field or value not found in AI system block"
        print_fail(req_id, desc, "quantitative",
                   expected='z2k_creation_perspective: "AI"',
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)


def test_004_012_system_block_stop(result: FeatureResult, run_result: RunResult) -> None:
    """004-012: .system-block-stop exists in Projects/My Writings/."""
    req_id = "004-012"
    desc = "Projects has system block stops"
    target = VAULT_ROOT / "Projects" / "My Writings" / ".system-block-stop"
    if target.exists():
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")
    else:
        notes = "File not found"
        print_fail(req_id, desc, "quantitative",
                   expected=f"{target} exists",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)


def test_004_013_domain_yaml_delimiters(result: FeatureResult, run_result: RunResult, blocks: dict[str, str | None]) -> None:
    """004-013: All 13 domain system blocks have YAML frontmatter delimiters."""
    req_id = "004-013"
    desc = "Domain system blocks have YAML delimiters"
    wrong: list[str] = []
    for domain, content in blocks.items():
        if content is None:
            continue  # Existence already checked in 004-006
        if not has_yaml_delimiters(content):
            wrong.append(domain)
    if wrong:
        notes = f"Missing delimiters in: {', '.join(wrong)}"
        print_fail(req_id, desc, "quantitative",
                   expected="All domain system blocks have --- frontmatter delimiters",
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

    # Root system block
    root_path = test_004_001_root_exists(result, run_result)
    if root_path is not None:
        root_content = root_path.read_text(encoding="utf-8")
        test_004_002_root_yaml_delimiters(result, run_result, root_content)
        test_004_003_root_required_fields(result, run_result, root_content)
        test_004_004_root_deprecated_absent(result, run_result, root_content)
        test_004_005_root_me_fieldinfo(result, run_result, root_content)
    else:
        # Root file missing — mark remaining root tests as failed
        for req_id, desc in [
            ("004-002", "Root system block has YAML delimiters"),
            ("004-003", "Root system block required fields present"),
            ("004-004", "Root system block deprecated fields absent"),
            ("004-005", "Root system block has me fieldInfo"),
        ]:
            print_fail(req_id, f"[blocked — {desc}]", "quantitative",
                       expected="Root system block exists",
                       actual="Skipped due to 004-001 failure")
            result.failed += 1
            run_result.add_req(req_id, desc, "FAIL", notes="Blocked by 004-001 failure (root system block missing)")

    # Domain system blocks
    blocks = load_domain_blocks()
    test_004_006_domain_blocks_exist(result, run_result, blocks)
    test_004_007_domain_values(result, run_result, blocks)
    test_004_008_ratings_fields_present(result, run_result, blocks)
    test_004_009_ratings_fields_absent(result, run_result, blocks)
    test_004_010_privacy_fields(result, run_result, blocks)
    test_004_011_ai_perspective(result, run_result, blocks)
    test_004_012_system_block_stop(result, run_result)
    test_004_013_domain_yaml_delimiters(result, run_result, blocks)

    print_feature_summary(result)
    write_results(FEATURE_DIR, run_result)
    return 0 if result.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
