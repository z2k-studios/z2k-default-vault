#!/usr/bin/env python3
from __future__ import annotations

"""
CTLv3 Sustaining — Feature 002: Working System

Validates the full rendering pipeline using a real template file via templatePath,
including system block injection. This is the "real" hello world smoke test.

Exit codes:
    0 — all tests passed
    1 — one or more tests failed
    2 — test execution error (infrastructure failure)
"""

import sys
from pathlib import Path

FEATURE_DIR = Path(__file__).resolve().parent
TESTS_DIR = FEATURE_DIR.parent
SHARED_DIR = TESTS_DIR / "shared"

sys.path.insert(0, str(SHARED_DIR))

from config import (
    COMMAND_QUEUE_TIMEOUT_SECONDS,
    VAULT_ROOT,
)
from output_formatter import FeatureResult, diag, print_fail, print_feature_summary, print_pass, print_skip
from result_writer import RunResult, write_results
from test_utils import (
    cleanup_output,
    diff_output,
    get_error_log_position,
    get_new_error_log_entries,
    normalize_dynamic_fields,
    read_output,
    submit_packet,
    wait_for_output,
)

FEATURE_NUM = "002"
FEATURE_NAME = "Working System"

JSON_PACKETS_DIR = FEATURE_DIR / "json_packets"
EXPECTED_DIR = FEATURE_DIR / "expected"
BASIC_PACKET = JSON_PACKETS_DIR / "basic.json"
BASIC_EXPECTED = EXPECTED_DIR / "basic_expected.md"

# Output location: destDir in basic.json is "System/Test Output"
OUTPUT_PATH = VAULT_ROOT / "System" / "Test Output" / "ctlv3-working-system-test.md"


def run_tests(result: FeatureResult, run_result: RunResult) -> None:
    # Clean up any leftover output
    cleanup_output(OUTPUT_PATH)

    # Record error log position before rendering
    log_position = get_error_log_position()

    # Submit the packet
    try:
        queued = submit_packet(BASIC_PACKET)
    except Exception as exc:
        notes = str(exc)
        for req_id in ["002-001", "002-002", "002-003", "002-004", "002-005", "002-006"]:
            print_fail(req_id, f"[blocked by packet submission failure]", "quantitative",
                       expected="Packet submitted",
                       actual=notes)
            result.failed += 1
            run_result.add_req(req_id, f"[blocked by packet submission failure]", "FAIL",
                               notes=f"Blocked: {notes}")
        return

    diag(f"  Submitted: {queued.name}")
    diag(f"  Waiting up to {COMMAND_QUEUE_TIMEOUT_SECONDS}s for output at: {OUTPUT_PATH}")

    # 002-001: Output file appears
    found = wait_for_output(OUTPUT_PATH, timeout=COMMAND_QUEUE_TIMEOUT_SECONDS)
    if not found:
        notes_001 = f"No output after {COMMAND_QUEUE_TIMEOUT_SECONDS}s"
        print_fail("002-001", "Template renders via templatePath", "quantitative",
                   expected="Output file created within timeout",
                   actual=notes_001)
        result.failed += 1
        run_result.add_req("002-001", "Template renders via templatePath", "FAIL", notes=notes_001)
        # Remaining tests cannot run without the output file
        for req_id, desc in [
            ("002-002", "Root system block YAML injected"),
            ("002-003", "Domain system block YAML injected"),
            ("002-004", "Field values resolved"),
            ("002-005", "Dynamic fields resolve"),
            ("002-006", "Output matches expected golden file"),
        ]:
            print_fail(req_id, "[blocked — no output file]", "quantitative",
                       expected="Output file exists",
                       actual="Skipped due to 002-001 failure")
            result.failed += 1
            run_result.add_req(req_id, desc, "FAIL", notes="Blocked by 002-001 failure (no output file)")
        return

    print_pass("002-001", "Template renders via templatePath", "quantitative")
    result.passed += 1
    run_result.add_req("002-001", "Template renders via templatePath", "PASS")

    content = read_output(OUTPUT_PATH)

    # 002-002: Root system block fields.
    # Note: YAML float 3.00 serializes as 3 (trailing zeros stripped). Check for
    # "z2k_metadata_version: 3" which matches both "3" and "3.00" as substrings.
    has_metadata_version = "z2k_metadata_version: 3" in content
    has_library_version = "z2k_creation_library_version" in content and "3.0.0" in content
    if has_metadata_version and has_library_version:
        print_pass("002-002", "Root system block YAML injected", "quantitative")
        result.passed += 1
        run_result.add_req("002-002", "Root system block YAML injected", "PASS")
    else:
        missing = []
        if not has_metadata_version:
            missing.append("z2k_metadata_version (value starting with 3)")
        if not has_library_version:
            missing.append("z2k_creation_library_version: 3.0.0")
        notes = f"Missing: {', '.join(missing)}"
        print_fail("002-002", "Root system block YAML injected", "quantitative",
                   expected="Both fields present in output",
                   actual=notes)
        result.failed += 1
        run_result.add_req("002-002", "Root system block YAML injected", "FAIL", notes=notes)

    # 002-003: Domain system block field
    if "z2k_creation_domain" in content and ".:Z2K/Domain/Beliefs" in content:
        print_pass("002-003", "Domain system block YAML injected", "quantitative")
        result.passed += 1
        run_result.add_req("002-003", "Domain system block YAML injected", "PASS")
    else:
        notes = "Field missing or value incorrect"
        print_fail("002-003", "Domain system block YAML injected", "quantitative",
                   expected='z2k_creation_domain: ".:Z2K/Domain/Beliefs"',
                   actual=notes)
        result.failed += 1
        run_result.add_req("002-003", "Domain system block YAML injected", "FAIL", notes=notes)

    # 002-004: Supplied field values appear in output
    expected_text = "Testing the CTLv3 template rendering pipeline"
    if expected_text in content:
        print_pass("002-004", "Field values resolved", "quantitative")
        result.passed += 1
        run_result.add_req("002-004", "Field values resolved", "PASS")
    else:
        notes = f'Text not found: "{expected_text}"'
        print_fail("002-004", "Field values resolved", "quantitative",
                   expected=f'Output contains: "{expected_text}"',
                   actual="Text not found in output")
        result.failed += 1
        run_result.add_req("002-004", "Field values resolved", "FAIL", notes=notes)

    # 002-005: Dynamic fields resolved — no raw Handlebars in output
    if "{{" in content or "}}" in content:
        # Find the raw expressions
        import re
        raw = re.findall(r'\{\{[^}]+\}\}', content)
        notes = f"Found raw expressions: {raw[:5]}"
        print_fail("002-005", "Dynamic fields resolve", "quantitative",
                   expected="No raw {{...}} expressions in output",
                   actual=f"Found: {raw[:5]}")
        result.failed += 1
        run_result.add_req("002-005", "Dynamic fields resolve", "FAIL", notes=notes)
    else:
        print_pass("002-005", "Dynamic fields resolve", "quantitative")
        result.passed += 1
        run_result.add_req("002-005", "Dynamic fields resolve", "PASS")

    # 002-006: Diff against golden expected file
    if not BASIC_EXPECTED.exists():
        print_skip(
            "002-006",
            "Output matches expected golden file",
            reason=(
                f"Golden file not yet created: {BASIC_EXPECTED}. "
                "Run the template once, normalize dynamic fields, and save as expected/basic_expected.md."
            ),
        )
        result.skipped += 1
        run_result.add_req("002-006", "Output matches expected golden file", "SKIP",
                           notes="Golden file not yet created")
    else:
        normalized = normalize_dynamic_fields(content)
        diff = diff_output(normalized, BASIC_EXPECTED)
        if diff:
            notes = f"{len(diff)} diff line(s)"
            print_fail("002-006", "Output matches expected golden file", "quantitative",
                       expected="Empty diff",
                       actual=f"{len(diff)} diff line(s):\n" + "".join(diff[:20]))
            result.failed += 1
            run_result.add_req("002-006", "Output matches expected golden file", "FAIL", notes=notes)
        else:
            print_pass("002-006", "Output matches expected golden file", "quantitative")
            result.passed += 1
            run_result.add_req("002-006", "Output matches expected golden file", "PASS")

    # Error log check
    new_entries = get_new_error_log_entries(log_position)
    if new_entries:
        diag(f"\nWARNING: {len(new_entries)} error log entry/entries detected during Feature 002:")
        for entry in new_entries:
            diag(f"  {entry}")

    # Clean up output file
    cleanup_output(OUTPUT_PATH)


def main() -> int:
    result = FeatureResult(feature_num=FEATURE_NUM, feature_name=FEATURE_NAME)
    run_result = RunResult(FEATURE_NUM, FEATURE_NAME)
    run_tests(result, run_result)
    print_feature_summary(result)
    write_results(FEATURE_DIR, run_result)
    return 0 if result.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
