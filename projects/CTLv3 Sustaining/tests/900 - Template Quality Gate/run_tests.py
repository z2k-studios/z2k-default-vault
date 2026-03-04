#!/usr/bin/env python3
from __future__ import annotations

"""
CTLv3 Sustaining — Feature 900: Template Quality Gate

Aggregation gate that validates all individual template features (100–899)
have been tested recently and passed their qualitative requirements.
Does NOT perform any AI assessment — reads existing results only.

Exit codes:
    0 — all tests passed
    1 — one or more tests failed
    2 — test execution error (infrastructure failure)
"""

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------

FEATURE_DIR = Path(__file__).resolve().parent        # tests/900 - Template Quality Gate/
TESTS_DIR = FEATURE_DIR.parent                       # tests/
SHARED_DIR = TESTS_DIR / "shared"

sys.path.insert(0, str(SHARED_DIR))

from output_formatter import FeatureResult, print_pass, print_fail, print_skip, print_feature_summary
from result_writer import RunResult, write_results

FEATURE_NUM = "900"
FEATURE_NAME = "Template Quality Gate"

STALENESS_HOURS = 24


# ---------------------------------------------------------------------------
# YAML frontmatter parser (minimal — reads top-level scalar keys + requirements list)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter. Returns dict with scalar keys and 'requirements' list."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    end_idx = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}

    data: dict = {}
    requirements: list[dict] = []
    current_req: dict | None = None

    for line in lines[1:end_idx]:
        # Detect start of requirements list
        if line.strip() == "requirements:":
            continue

        # List item start
        if re.match(r'^\s+-\s+id:', line):
            if current_req is not None:
                requirements.append(current_req)
            m = re.match(r'^\s+-\s+id:\s*(.*)', line)
            current_req = {"id": m.group(1).strip() if m else ""}
            continue

        # Continuation of a list item
        if current_req is not None and re.match(r'^\s{4,}\w+:', line):
            m = re.match(r'^\s+(\w+):\s*(.*)', line)
            if m:
                key = m.group(1)
                raw_val = m.group(2).strip().strip('"').strip("'")
                current_req[key] = raw_val
            continue

        # End of list item context
        if current_req is not None and not line.startswith(" "):
            requirements.append(current_req)
            current_req = None

        # Top-level scalar
        m = re.match(r'^(\w+):\s*(.*)', line)
        if m:
            key = m.group(1)
            raw_val = m.group(2).strip().strip('"').strip("'")
            data[key] = raw_val

    if current_req is not None:
        requirements.append(current_req)

    data["requirements"] = requirements
    return data


# ---------------------------------------------------------------------------
# Template feature discovery
# ---------------------------------------------------------------------------

def discover_template_features() -> list[Path]:
    """Return all 1XX–8XX test folders, sorted numerically."""
    pattern = re.compile(r'^(\d{3})\s+-\s+')
    folders = []
    for d in TESTS_DIR.iterdir():
        if not d.is_dir():
            continue
        m = pattern.match(d.name)
        if m and 100 <= int(m.group(1)) <= 899:
            folders.append(d)
    folders.sort(key=lambda d: int(re.match(r'^(\d+)', d.name).group(1)))
    return folders


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_900_001_results_exist(
    result: FeatureResult,
    run_result: RunResult,
    features: list[Path],
) -> dict[Path, dict]:
    """900-001: All individual template features have last-run-results.md."""
    req_id = "900-001"
    desc = "All individual template features have results"

    if not features:
        notes = "No template feature test folders found (100–899 range)"
        print_fail(req_id, desc, "quantitative",
                   expected="At least one 1XX test folder exists",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
        return {}

    parsed: dict[Path, dict] = {}
    missing: list[str] = []

    for folder in features:
        results_file = folder / "last-run-results.md"
        if not results_file.exists():
            missing.append(folder.name)
        else:
            text = results_file.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            parsed[folder] = fm

    if missing:
        notes = f"{len(missing)} of {len(features)} missing: {'; '.join(missing[:10])}"
        if len(missing) > 10:
            notes += f" ... (+{len(missing) - 10} more)"
        print_fail(req_id, desc, "quantitative",
                   expected="All template feature folders have last-run-results.md",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")

    return parsed


def test_900_002_staleness(
    result: FeatureResult,
    run_result: RunResult,
    parsed: dict[Path, dict],
    now: datetime,
) -> None:
    """900-002: All results are within the staleness window (24 hours)."""
    req_id = "900-002"
    desc = "All results are within the staleness window"

    if not parsed:
        notes = "No results to check (blocked by 900-001)"
        print_fail(req_id, desc, "quantitative",
                   expected="All results have recent date_run",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
        return

    cutoff = now - timedelta(hours=STALENESS_HOURS)
    stale: list[str] = []

    for folder, fm in parsed.items():
        date_str = fm.get("date_run", "")
        if not date_str:
            stale.append(f"{folder.name} (no date_run)")
            continue
        try:
            run_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            stale.append(f"{folder.name} (unparseable date: {date_str!r})")
            continue
        if run_date < cutoff:
            stale.append(f"{folder.name} ({date_str})")

    if stale:
        notes = f"{len(stale)} stale: {'; '.join(stale[:10])}"
        if len(stale) > 10:
            notes += f" ... (+{len(stale) - 10} more)"
        print_fail(req_id, desc, "quantitative",
                   expected=f"All date_run within last {STALENESS_HOURS} hours",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_900_003_qualitative_passed(
    result: FeatureResult,
    run_result: RunResult,
    parsed: dict[Path, dict],
) -> None:
    """900-003: All qualitative requirements in individual template features passed."""
    req_id = "900-003"
    desc = "All qualitative requirements passed"

    if not parsed:
        notes = "No results to check (blocked by 900-001)"
        print_fail(req_id, desc, "quantitative",
                   expected="All qualitative requirements have result PASS",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
        return

    failed_quality: list[str] = []

    for folder, fm in parsed.items():
        reqs = fm.get("requirements", [])
        for req in reqs:
            tier = req.get("tier", "quantitative")
            req_result = req.get("result", "")
            if tier == "qualitative" and req_result == "FAIL":
                req_id_inner = req.get("id", "?")
                failed_quality.append(f"{folder.name} ({req_id_inner})")

    if failed_quality:
        notes = f"{len(failed_quality)} failed: {'; '.join(failed_quality[:10])}"
        if len(failed_quality) > 10:
            notes += f" ... (+{len(failed_quality) - 10} more)"
        print_fail(req_id, desc, "quantitative",
                   expected="No qualitative requirements with result FAIL",
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
    parser = argparse.ArgumentParser(description="Feature 900 — Template Quality Gate")
    parser.add_argument("--no-quality", action="store_true",
                        help="Skip all gate checks (qualitative tests were skipped upstream)")
    parser.add_argument("--fix", action="store_true",
                        help="Not applicable for gate feature (ignored)")
    args, _ = parser.parse_known_args()

    result = FeatureResult(feature_num=FEATURE_NUM, feature_name=FEATURE_NAME)
    run_result = RunResult(FEATURE_NUM, FEATURE_NAME)

    if args.no_quality:
        for req_id, desc in [
            ("900-001", "All individual template features have results"),
            ("900-002", "All results are within the staleness window"),
            ("900-003", "All qualitative requirements passed"),
        ]:
            print_skip(req_id, desc, "--no-quality mode (upstream qualitative tests skipped)")
            result.skipped += 1
            run_result.add_req(req_id, desc, "SKIP",
                               notes="--no-quality mode (upstream qualitative tests skipped)")
        print_feature_summary(result)
        write_results(FEATURE_DIR, run_result)
        return 0

    now = datetime.now()
    features = discover_template_features()

    parsed = test_900_001_results_exist(result, run_result, features)
    test_900_002_staleness(result, run_result, parsed, now)
    test_900_003_qualitative_passed(result, run_result, parsed)

    print_feature_summary(result)
    write_results(FEATURE_DIR, run_result)
    return 0 if result.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
