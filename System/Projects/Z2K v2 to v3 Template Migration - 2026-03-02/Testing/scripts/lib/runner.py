#!/usr/bin/env python3
"""Shared test runner infrastructure for CTL v3 testing."""

import json
import os
import sys
import time
from pathlib import Path


def assert_path_exists(path):
    """Assert that a file or directory exists. Returns (passed, message)."""
    p = Path(path)
    if p.exists():
        kind = "directory" if p.is_dir() else "file"
        return True, f"{kind} exists: {path}"
    return False, f"MISSING: {path}"


def write_command_file(queue_dir, filename, payload):
    """Write a JSON command file to the command queue folder."""
    queue_path = Path(queue_dir)
    queue_path.mkdir(parents=True, exist_ok=True)
    target = queue_path / filename
    with open(target, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    return str(target)


def poll_for_output(output_path, timeout_s=30):
    """Wait for a file to appear at output_path. Returns content or raises TimeoutError."""
    deadline = time.time() + timeout_s
    p = Path(output_path)
    while time.time() < deadline:
        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                return f.read()
        time.sleep(1)
    raise TimeoutError(f"Timed out waiting for {output_path} after {timeout_s}s")


def normalize_dynamic_fields(content):
    """Replace dynamic values with stable placeholders for golden-file comparison."""
    import re
    # Replace wikilink dates like [[2026-03-02]] with placeholder
    content = re.sub(r'\[\[\d{4}-\d{2}-\d{2}\]\]', '<TODAY_WIKILINK>', content)
    # Replace bare dates like 2026-03-02
    content = re.sub(r'\d{4}-\d{2}-\d{2}', '<DATE>', content)
    return content


def compare_to_golden(actual_normalized, golden_path):
    """Compare actual output to golden file. Save golden if absent. Returns (passed, message)."""
    gp = Path(golden_path)
    if not gp.exists():
        gp.parent.mkdir(parents=True, exist_ok=True)
        with open(gp, "w", encoding="utf-8") as f:
            f.write(actual_normalized)
        return True, f"Golden file created: {golden_path} (first run — review manually)"

    with open(gp, "r", encoding="utf-8") as f:
        expected = f.read()

    if actual_normalized == expected:
        return True, f"Matches golden file: {golden_path}"

    # Build a simple diff summary
    actual_lines = actual_normalized.splitlines()
    expected_lines = expected.splitlines()
    diffs = []
    max_lines = max(len(actual_lines), len(expected_lines))
    for i in range(max_lines):
        a = actual_lines[i] if i < len(actual_lines) else "<missing>"
        e = expected_lines[i] if i < len(expected_lines) else "<missing>"
        if a != e:
            diffs.append(f"  line {i+1}: expected '{e}' got '{a}'")
        if len(diffs) >= 10:
            diffs.append(f"  ... ({max_lines - i - 1} more lines)")
            break

    return False, f"MISMATCH vs golden file:\n" + "\n".join(diffs)


def run_suite(tests):
    """Run a list of test functions. Each returns (passed, message). Prints summary, exits non-zero on failure."""
    passed = 0
    failed = 0
    results = []

    for test_fn in tests:
        name = test_fn.__name__
        try:
            ok, msg = test_fn()
            if ok:
                passed += 1
                results.append(f"  PASS  {name}: {msg}")
            else:
                failed += 1
                results.append(f"  FAIL  {name}: {msg}")
        except Exception as e:
            failed += 1
            results.append(f"  ERROR {name}: {e}")

    print(f"\n{'='*60}")
    print(f"Test Results: {passed} passed, {failed} failed, {passed + failed} total")
    print(f"{'='*60}")
    for r in results:
        print(r)
    print()

    sys.exit(1 if failed > 0 else 0)
