#!/usr/bin/env python3
from __future__ import annotations

"""
CTLv3 Sustaining — Feature 001: Infrastructure Test

Validates project structure, Python environment, Command Queue connectivity,
Obsidian availability, and error log monitoring.

Exit codes:
    0 — all tests passed
    1 — one or more tests failed
    2 — test execution error (infrastructure failure)
"""

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Path setup — allow running from any working directory
# ---------------------------------------------------------------------------

FEATURE_DIR = Path(__file__).resolve().parent        # tests/001 - Infrastructure Test/
TESTS_DIR = FEATURE_DIR.parent                       # tests/
SHARED_DIR = TESTS_DIR / "shared"

sys.path.insert(0, str(SHARED_DIR))

from config import (
    COMMAND_QUEUE_DIR,
    COMMAND_QUEUE_TIMEOUT_SECONDS,
    ERROR_LOG_PATH,
    INLINE_TEMPLATE_OUTPUT_DIR,
    PROJECT_DIR,
    TESTS_DIR,
    VAULT_ROOT,
)
from output_formatter import FeatureResult, diag, print_fail, print_feature_summary, print_pass
from result_writer import RunResult, write_results
from test_utils import (
    cleanup_output,
    format_error_log_entries,
    get_error_log_position,
    get_new_error_log_entries,
    read_output,
    submit_packet,
    wait_for_output,
    wait_for_queue_done,
)

FEATURE_NUM = "001"
FEATURE_NAME = "Infrastructure Test"

JSON_PACKETS_DIR = FEATURE_DIR / "json_packets"
HELLO_WORLD_PACKET = JSON_PACKETS_DIR / "hello_world.json"
HELLO_WORLD_OUTPUT = INLINE_TEMPLATE_OUTPUT_DIR / "ctlv3-hello-world-test.md"


def test_001_001_project_structure(result: FeatureResult, run_result: RunResult) -> None:
    """001-001: Required project directories exist."""
    req_id = "001-001"
    desc = "Project folder structure exists"
    required_dirs = [
        PROJECT_DIR / "features",
        PROJECT_DIR / "tests",
        PROJECT_DIR / "tests" / "shared",
        PROJECT_DIR / "drop",
    ]
    missing = [str(d.relative_to(PROJECT_DIR)) for d in required_dirs if not d.is_dir()]
    if missing:
        notes = f"Missing: {', '.join(missing)}"
        print_fail(req_id, desc, "quantitative",
                   expected="All directories exist",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def test_001_002_python_version(result: FeatureResult, run_result: RunResult) -> None:
    """001-002: Python 3.8+ is available."""
    req_id = "001-002"
    desc = "Python 3.x available (≥ 3.8)"
    try:
        proc = subprocess.run(
            ["python3", "--version"],
            capture_output=True, text=True, timeout=10
        )
        version_str = (proc.stdout + proc.stderr).strip()
        # Parse "Python X.Y.Z"
        parts = version_str.replace("Python ", "").split(".")
        major, minor = int(parts[0]), int(parts[1])
        if major >= 3 and (major > 3 or minor >= 8):
            print_pass(req_id, desc, "quantitative")
            result.passed += 1
            run_result.add_req(req_id, desc, "PASS")
        else:
            notes = f"Found: {version_str}"
            print_fail(req_id, desc, "quantitative",
                       expected="Python ≥ 3.8",
                       actual=notes)
            result.failed += 1
            run_result.add_req(req_id, desc, "FAIL", notes=notes)
    except Exception as exc:
        notes = str(exc)
        print_fail(req_id, desc, "quantitative",
                   expected="python3 executes successfully",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)


def test_001_003_run_all_importable(result: FeatureResult, run_result: RunResult) -> None:
    """001-003: run_all_tests.py exists and imports without error."""
    req_id = "001-003"
    desc = "run_all_tests.py exists and is importable"
    run_all = TESTS_DIR / "run_all_tests.py"
    if not run_all.exists():
        notes = "File not found"
        print_fail(req_id, desc, "quantitative",
                   expected=f"{run_all} exists",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
        return
    proc = subprocess.run(
        [sys.executable, str(run_all), "--help"],
        capture_output=True, text=True, timeout=15
    )
    # --help should exit 0 (argparse) or at least not crash with a traceback
    if proc.returncode in (0, 1) and "Traceback" not in proc.stderr:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")
    else:
        notes = proc.stderr[:500] if proc.stderr else f"exit code {proc.returncode}"
        print_fail(req_id, desc, "quantitative",
                   expected="No import errors",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)


def test_001_006_command_queue_folder(result: FeatureResult, run_result: RunResult) -> None:
    """001-006: Command Queue directory exists and is writable. Run before 001-004."""
    req_id = "001-006"
    desc = "Command Queue folder exists and is writable"
    if not COMMAND_QUEUE_DIR.exists():
        notes = "Directory not found — ensure Obsidian is running with Command Queues enabled"
        print_fail(req_id, desc, "quantitative",
                   expected=f"{COMMAND_QUEUE_DIR} exists",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
        return

    # Test writability
    try:
        probe = COMMAND_QUEUE_DIR / ".write_probe"
        probe.write_text("probe")
        probe.unlink()
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")
    except Exception as exc:
        notes = str(exc)
        print_fail(req_id, desc, "quantitative",
                   expected="Directory is writable",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)


def test_001_004_005_command_queue_smoke(result: FeatureResult, run_result: RunResult) -> list | None:
    """001-004 + 001-005: Hello world Command Queue test + Obsidian running check."""
    req_id_cq = "001-004"
    req_id_obs = "001-005"
    desc_cq = "Command Queue is operational (hello world)"
    desc_obs = "Obsidian is running"

    # Clean up any leftover output from a previous run
    cleanup_output(HELLO_WORLD_OUTPUT)

    # Record error log position before submitting
    log_position = get_error_log_position()

    # Submit the hello world packet
    try:
        queued = submit_packet(HELLO_WORLD_PACKET)
    except Exception as exc:
        notes = str(exc)
        print_fail(req_id_cq, desc_cq, "quantitative",
                   expected="Packet submitted to Command Queue",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id_cq, desc_cq, "FAIL", notes=notes)
        notes_obs = "Cannot determine — packet submission failed"
        print_fail(req_id_obs, desc_obs, "quantitative",
                   expected="Obsidian processing Command Queue",
                   actual=notes_obs)
        result.failed += 1
        run_result.add_req(req_id_obs, desc_obs, "FAIL", notes=notes_obs)
        return None

    diag(f"  Submitted: {queued.name}")
    diag(f"  Waiting up to {COMMAND_QUEUE_TIMEOUT_SECONDS}s for output at: {HELLO_WORLD_OUTPUT}")

    # Poll for output file
    found = wait_for_output(HELLO_WORLD_OUTPUT, timeout=COMMAND_QUEUE_TIMEOUT_SECONDS)

    if not found:
        notes_cq = f"No output after {COMMAND_QUEUE_TIMEOUT_SECONDS}s — Obsidian may not be running or Command Queues may be disabled"
        print_fail(req_id_cq, desc_cq, "quantitative",
                   expected="Output file appears within timeout",
                   actual=notes_cq)
        result.failed += 1
        run_result.add_req(req_id_cq, desc_cq, "FAIL", notes=notes_cq)
        notes_obs = "Timeout — Obsidian did not process the packet"
        print_fail(req_id_obs, desc_obs, "quantitative",
                   expected="Obsidian processes Command Queue packet",
                   actual=notes_obs)
        result.failed += 1
        run_result.add_req(req_id_obs, desc_obs, "FAIL", notes=notes_obs)
        return None

    # Obsidian is responsive — 001-005 passes
    print_pass(req_id_obs, desc_obs, "quantitative")
    result.passed += 1
    run_result.add_req(req_id_obs, desc_obs, "PASS")

    # Read and verify output content
    content = read_output(HELLO_WORLD_OUTPUT)
    if "Hello World!" not in content:
        notes_cq = f"Content: {content[:200]!r}"
        print_fail(req_id_cq, desc_cq, "quantitative",
                   expected='Output contains "Hello World!"',
                   actual=notes_cq)
        result.failed += 1
        run_result.add_req(req_id_cq, desc_cq, "FAIL", notes=notes_cq)
    else:
        print_pass(req_id_cq, desc_cq, "quantitative")
        result.passed += 1
        run_result.add_req(req_id_cq, desc_cq, "PASS")

    # Check error log for new entries
    new_entries = get_new_error_log_entries(log_position)

    # Clean up output file
    cleanup_output(HELLO_WORLD_OUTPUT)

    return new_entries  # propagate to 001-007 test


def test_001_007_error_log_monitoring(result: FeatureResult, run_result: RunResult, error_log_entries: list) -> None:
    """001-007: Error log monitoring is operational; hello world produces no errors."""
    req_id = "001-007"
    desc = "Error log monitoring operational; hello world produces no Warning-or-above entries"

    if error_log_entries is None:
        # smoke test didn't run — mark as failed
        notes = "Cannot determine — Command Queue test did not complete"
        print_fail(req_id, desc, "quantitative",
                   expected="No error log entries from hello world render",
                   actual=notes)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes)
        return

    if error_log_entries:
        notes = f"{len(error_log_entries)} new entry/entries detected"
        print_fail(req_id, desc, "quantitative",
                   expected="No Warning-or-above entries in error log",
                   actual=notes,
                   error_log_entries=error_log_entries)
        result.failed += 1
        run_result.add_req(req_id, desc, "FAIL", notes=notes + ": " + "; ".join(str(e) for e in error_log_entries[:3]))
    else:
        print_pass(req_id, desc, "quantitative")
        result.passed += 1
        run_result.add_req(req_id, desc, "PASS")


def main() -> int:
    result = FeatureResult(feature_num=FEATURE_NUM, feature_name=FEATURE_NAME)
    run_result = RunResult(FEATURE_NUM, FEATURE_NAME)

    test_001_001_project_structure(result, run_result)
    test_001_002_python_version(result, run_result)
    test_001_003_run_all_importable(result, run_result)
    test_001_006_command_queue_folder(result, run_result)

    # Smoke test returns error log entries for 001-007
    error_log_entries = test_001_004_005_command_queue_smoke(result, run_result)

    test_001_007_error_log_monitoring(result, run_result, error_log_entries)

    print_feature_summary(result)
    write_results(FEATURE_DIR, run_result)
    return 0 if result.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
