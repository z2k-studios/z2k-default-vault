#!/usr/bin/env python3
from __future__ import annotations

"""
CTLv3 Sustaining — Test Result Tabulator

Reads last-run-results.md from every feature test folder and produces a
timestamped summary table in tests/~Result Summaries/.

Usage:
    python3 scripts/tabulate-results.py
    python3 scripts/tabulate-results.py --print   # Print to stdout instead of writing file

Output file: tests/~Result Summaries/Test Result Summary - YYYY-MM-DD - HH MM AM|PM.md
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPTS_DIR = Path(__file__).resolve().parent              # scripts/
PROJECT_DIR = SCRIPTS_DIR.parent                           # CTLv3 Sustaining/
TESTS_DIR = PROJECT_DIR / "tests"
SUMMARIES_DIR = TESTS_DIR / "~Result Summaries"


# ---------------------------------------------------------------------------
# YAML frontmatter parser (minimal — reads top-level scalar keys only)
# ---------------------------------------------------------------------------

def _find_frontmatter_lines(text: str) -> list[str] | None:
    """Return the lines between the opening and closing --- fences, or None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            return lines[1:i]
    return None


def parse_frontmatter(text: str) -> dict:
    """
    Extract YAML frontmatter from a markdown file.
    Reads top-level scalar keys (strings, numbers) plus the requirements list.
    Returns an empty dict if no frontmatter is found.
    """
    fm_lines = _find_frontmatter_lines(text)
    if fm_lines is None:
        return {}

    data: dict = {}
    requirements: list[dict] = []
    current_req: dict | None = None
    in_requirements = False

    for line in fm_lines:
        # Detect start of requirements block
        if line.rstrip() == "requirements:" or line.startswith("requirements:"):
            in_requirements = True
            continue

        if in_requirements:
            # A non-indented line ends the requirements block
            if line and not line[0].isspace():
                in_requirements = False
                # Fall through to scalar parsing below
            else:
                stripped = line.strip()
                if stripped.startswith("- id:"):
                    if current_req:
                        requirements.append(current_req)
                    val = stripped[len("- id:"):].strip().strip('"').strip("'")
                    current_req = {"id": val}
                elif current_req:
                    m = re.match(r'(\w+):\s*(.*)', stripped)
                    if m:
                        key = m.group(1)
                        val = m.group(2).strip().strip('"').strip("'")
                        current_req[key] = val
                continue

        # Top-level scalar keys
        if line.startswith(" ") or line.startswith("\t") or line.startswith("-"):
            continue
        m = re.match(r'^(\w+):\s*(.*)', line)
        if not m:
            continue
        key = m.group(1)
        raw_val = m.group(2).strip()
        if (raw_val.startswith('"') and raw_val.endswith('"')) or \
           (raw_val.startswith("'") and raw_val.endswith("'")):
            raw_val = raw_val[1:-1]
        data[key] = raw_val

    if current_req:
        requirements.append(current_req)
    if requirements:
        data["_requirements"] = requirements

    return data


# ---------------------------------------------------------------------------
# Feature result discovery
# ---------------------------------------------------------------------------

def discover_feature_results() -> list[dict]:
    """
    Find all last-run-results.md files in NNN - * test folders, sorted by feature number.
    Returns list of dicts with parsed frontmatter fields.
    """
    pattern = re.compile(r'^(\d+)\s+-\s+')
    folders = [
        d for d in TESTS_DIR.iterdir()
        if d.is_dir() and pattern.match(d.name)
    ]
    folders.sort(key=lambda d: int(pattern.match(d.name).group(1)))

    results = []
    for folder in folders:
        results_file = folder / "last-run-results.md"
        if not results_file.exists():
            # Feature has no results yet
            num_match = pattern.match(folder.name)
            feature_num = num_match.group(1) if num_match else "???"
            feature_name = folder.name[len(num_match.group(0)):] if num_match else folder.name
            results.append({
                "feature_number": feature_num,
                "feature_name": feature_name,
                "date_run": "—",
                "result": "NO RESULTS",
                "passed": "—",
                "failed": "—",
                "skipped": "—",
                "quality_score": None,
                "_no_results": True,
            })
            continue

        text = results_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        results.append(fm)

    return results


# ---------------------------------------------------------------------------
# Score display
# ---------------------------------------------------------------------------

def format_score(row: dict) -> str:
    """Format the score column for this feature row."""
    result = row.get("result", "")
    quality_score = row.get("quality_score")
    passed = row.get("passed", "—")
    failed = row.get("failed", "—")
    skipped = row.get("skipped", "—")

    if quality_score and quality_score not in ("", "OVERRIDE", None):
        try:
            return f"{float(quality_score):.1f}%"
        except (ValueError, TypeError):
            if quality_score == "OVERRIDE":
                return "OVERRIDE"

    # Quantitative: show pass/fail/skip counts
    if passed != "—" or failed != "—":
        return f"{passed}P / {failed}F / {skipped}S"

    return "—"


def format_result(result_str: str) -> str:
    """Apply ==FAILED== highlighting for failed results."""
    if result_str in ("FAIL", "FAILED"):
        return "==FAILED=="
    return result_str


# ---------------------------------------------------------------------------
# Table alignment helpers
# ---------------------------------------------------------------------------

_LINK_RE = re.compile(r'\[([^\]]*)\]\(<[^>]*>\)')

def display_width(text: str) -> int:
    """Visible width of a cell — markdown links count only as their display text."""
    return len(_LINK_RE.sub(r'\1', text))


def pad_cell(text: str, target_width: int) -> str:
    """Pad a cell to target_width based on its display width."""
    return text + " " * (target_width - display_width(text))


# ---------------------------------------------------------------------------
# Summary generation
# ---------------------------------------------------------------------------

def build_summary(run_time: datetime, feature_rows: list[dict]) -> str:
    lines = []

    # Header
    lines.append("---")
    lines.append(f'date_generated: "{run_time.strftime("%Y-%m-%d %H:%M:%S")}"')
    lines.append("document_type: Test Result Summary")
    lines.append("---")
    lines.append("")
    lines.append(f"# Test Result Summary — {run_time.strftime('%Y-%m-%d %I:%M %p')}")
    lines.append("")

    # Aggregate counts
    total_features = len(feature_rows)
    passed_features = sum(1 for r in feature_rows if r.get("result") == "PASS")
    failed_features = sum(1 for r in feature_rows if r.get("result") in ("FAIL", "FAILED"))
    no_results = sum(1 for r in feature_rows if r.get("_no_results"))

    lines.append(f"**Features:** {total_features} total — {passed_features} passed, {failed_features} failed, {no_results} no results")
    lines.append("")

    # Table — collect rows first, then align columns
    headers = ["Feature", "Name", "Date Run", "Result", "Score"]
    table_rows: list[list[str]] = []

    for row in feature_rows:
        feature_num = row.get("feature_number", "???")
        feature_name = row.get("feature_name", "Unknown")
        date_run = row.get("date_run", "—")
        result_str = row.get("result", "—")
        score_str = format_score(row)
        result_display = format_result(result_str)

        # Truncate date to date+time (drop seconds for readability)
        if date_run and date_run != "—" and len(date_run) >= 16:
            date_run = date_run[:16]

        # Link to last-run-results.md (relative from ~Result Summaries/)
        if row.get("_no_results"):
            name_cell = feature_name
        else:
            folder = f"{feature_num} - {feature_name}"
            name_cell = f"[{feature_name}](<../{folder}/last-run-results.md>)"

        table_rows.append([feature_num, name_cell, date_run, result_display, score_str])

    # Column widths from display text (ignoring hidden link URLs)
    col_widths = [len(h) for h in headers]
    for cells in table_rows:
        for i, cell in enumerate(cells):
            col_widths[i] = max(col_widths[i], display_width(cell))

    # Emit aligned header, separator, and data rows
    lines.append("| " + " | ".join(h.ljust(w) for h, w in zip(headers, col_widths)) + " |")
    lines.append("|" + "|".join("-" * (w + 2) for w in col_widths) + "|")
    for cells in table_rows:
        lines.append("| " + " | ".join(pad_cell(c, w) for c, w in zip(cells, col_widths)) + " |")

    lines.append("")

    # Failed features detail section
    failed_rows = [r for r in feature_rows if r.get("result") in ("FAIL", "FAILED")]
    if failed_rows:
        lines.append("## Failed Features")
        lines.append("")
        for row in failed_rows:
            feature_num = row.get("feature_number", "???")
            feature_name = row.get("feature_name", "Unknown")
            folder = f"{feature_num} - {feature_name}"
            link = f"[{feature_num} — {feature_name}](<../{folder}/last-run-results.md>)"
            lines.append(f"- **{link}**: {row.get('failed', '?')} requirement(s) failed")

            # List individual failed requirements
            reqs = row.get("_requirements", [])
            for req in reqs:
                if req.get("result") in ("FAIL", "FAILED"):
                    req_id = req.get("id", "???")
                    desc = req.get("description", "")
                    lines.append(f"  - {req_id} — {desc}")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="CTLv3 Sustaining — Test Result Tabulator"
    )
    parser.add_argument(
        "--print",
        action="store_true",
        dest="print_only",
        help="Print summary to stdout instead of writing to file.",
    )
    args = parser.parse_args()

    run_time = datetime.now()

    feature_rows = discover_feature_results()
    if not feature_rows:
        print("No test folders found.", file=sys.stderr)
        return 2

    summary = build_summary(run_time, feature_rows)

    if args.print_only:
        print(summary)
        return 0

    # Write to test-result-summaries/
    SUMMARIES_DIR.mkdir(exist_ok=True)
    timestamp = run_time.strftime("%Y-%m-%d - %I %M %p")
    out_path = SUMMARIES_DIR / f"Test Result Summary - {timestamp}.md"
    out_path.write_text(summary, encoding="utf-8")
    print(f"Summary written to: {out_path}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
