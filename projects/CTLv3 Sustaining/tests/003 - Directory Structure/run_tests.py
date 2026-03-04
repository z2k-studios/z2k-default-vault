#!/usr/bin/env python3
from __future__ import annotations

"""
CTLv3 Sustaining — Feature 003: Directory Structure

Validates that the CTL vault folder structure is complete and correct:
13 domain root folders, their Templates/ subfolders, root Templates/,
Projects/My Writings/, System/Templates/, Body and AI domain folders.

Pure filesystem checks — no Command Queue or Obsidian interaction required.

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

FEATURE_DIR = Path(__file__).resolve().parent        # tests/003 - Directory Structure/
TESTS_DIR = FEATURE_DIR.parent                       # tests/
SHARED_DIR = TESTS_DIR / "shared"

sys.path.insert(0, str(SHARED_DIR))

from config import VAULT_ROOT
from output_formatter import FeatureResult, print_fail, print_feature_summary, print_pass
from result_writer import RunResult, write_results

FEATURE_NUM = "003"
FEATURE_NAME = "Directory Structure"

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


def test_003_001_domain_root_folders(result: FeatureResult, run_result: RunResult) -> None:
    """003-001: All 13 domain root folders exist."""
    req_id = "003-001"
    desc = "All 13 domain root folders exist"
    missing = [d for d in DOMAIN_FOLDERS if not (VAULT_ROOT / d).is_dir()]
    if missing:
        notes = f"Missing: {', '.join(missing)}"
        print_fail(req_id, desc, "quantitative",
                   expected="All 13 domain folders exist",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_003_002_domain_templates_subfolders(result: FeatureResult, run_result: RunResult) -> None:
    """003-002: All 13 domain folders have a Templates/ subfolder."""
    req_id = "003-002"
    desc = "All domains have Templates/ subfolders"
    missing = [d for d in DOMAIN_FOLDERS if not (VAULT_ROOT / d / "Templates").is_dir()]
    if missing:
        notes = f"Missing Templates/ in: {', '.join(missing)}"
        print_fail(req_id, desc, "quantitative",
                   expected="All 13 domain folders contain Templates/",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_003_003_root_templates(result: FeatureResult, run_result: RunResult) -> None:
    """003-003: Root Templates/ folder exists at vault root."""
    req_id = "003-003"
    desc = "Root Templates/ folder exists"
    target = VAULT_ROOT / "Templates"
    if not target.is_dir():
        notes = "Directory not found"
        print_fail(req_id, desc, "quantitative",
                   expected=f"{target} exists",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_003_004_my_writings_structure(result: FeatureResult, run_result: RunResult) -> None:
    """003-004: Projects/My Writings/ and Projects/My Writings/Templates/ exist."""
    req_id = "003-004"
    desc = "Projects/My Writings/ structure exists"
    my_writings = VAULT_ROOT / "Projects" / "My Writings"
    my_writings_templates = my_writings / "Templates"
    missing = []
    if not my_writings.is_dir():
        missing.append("Projects/My Writings/")
    if not my_writings_templates.is_dir():
        missing.append("Projects/My Writings/Templates/")
    if missing:
        notes = f"Missing: {', '.join(missing)}"
        print_fail(req_id, desc, "quantitative",
                   expected="Both directories exist",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_003_005_system_templates(result: FeatureResult, run_result: RunResult) -> None:
    """003-005: System/Templates/ exists."""
    req_id = "003-005"
    desc = "System/Templates/ exists"
    target = VAULT_ROOT / "System" / "Templates"
    if not target.is_dir():
        notes = "Directory not found"
        print_fail(req_id, desc, "quantitative",
                   expected=f"{target} exists",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_003_006_body_and_ai_domains(result: FeatureResult, run_result: RunResult) -> None:
    """003-006: Body/, Body/Templates/, AI/, AI/Templates/ all exist."""
    req_id = "003-006"
    desc = "Body and AI domains exist"
    targets = [
        VAULT_ROOT / "Body",
        VAULT_ROOT / "Body" / "Templates",
        VAULT_ROOT / "AI",
        VAULT_ROOT / "AI" / "Templates",
    ]
    missing = [str(t.relative_to(VAULT_ROOT)) for t in targets if not t.is_dir()]
    if missing:
        notes = f"Missing: {', '.join(missing)}"
        print_fail(req_id, desc, "quantitative",
                   expected="All 4 directories exist",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def main() -> int:
    result = FeatureResult(feature_num=FEATURE_NUM, feature_name=FEATURE_NAME)
    run_result = RunResult(FEATURE_NUM, FEATURE_NAME)

    test_003_001_domain_root_folders(result, run_result)
    test_003_002_domain_templates_subfolders(result, run_result)
    test_003_003_root_templates(result, run_result)
    test_003_004_my_writings_structure(result, run_result)
    test_003_005_system_templates(result, run_result)
    test_003_006_body_and_ai_domains(result, run_result)

    print_feature_summary(result)
    write_results(FEATURE_DIR, run_result)
    return 0 if result.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
