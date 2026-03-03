#!/usr/bin/env python3
from __future__ import annotations

"""
CTLv3 Sustaining — Master Regression Script

Discovers all feature test folders (matching NNN - * naming pattern) and
executes run_tests.py in each, in numerical order. Aggregates results and
emits a regression summary per Testing Plan §5.3.

Usage:
    python3 run_all_tests.py                   # Full regression (quantitative + qualitative)
    python3 run_all_tests.py --no-quality      # Script-only (skips AI qualitative tests)
    python3 run_all_tests.py --feature 001     # Run tests for Feature 001 only
    python3 run_all_tests.py --fix             # Enable AI fix mode (requires confirmation)

Exit codes (per Testing Plan §5.1):
    0 — all tests passed
    1 — one or more tests failed
    2 — test execution error (infrastructure failure)
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Add shared/ to path so output_formatter is importable
TESTS_DIR = Path(__file__).resolve().parent
SHARED_DIR = TESTS_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from output_formatter import (
    FeatureResult,
    RegressionSummary,
    diag,
    print_regression_summary,
)


def discover_feature_folders(tests_dir: Path) -> list[Path]:
    """Return all NNN - <Name>/ subdirectories, sorted numerically."""
    pattern = re.compile(r'^(\d+)\s+-\s+')
    folders = [
        d for d in tests_dir.iterdir()
        if d.is_dir() and pattern.match(d.name)
    ]
    folders.sort(key=lambda d: int(pattern.match(d.name).group(1)))
    return folders


def run_feature(folder: Path, extra_args: list[str]) -> subprocess.CompletedProcess:
    """Execute run_tests.py in the given feature folder."""
    script = folder / "run_tests.py"
    if not script.exists():
        diag(f"WARNING: No run_tests.py found in {folder.name} — skipping.")
        return subprocess.CompletedProcess(args=[], returncode=2, stdout="", stderr="")

    cmd = [sys.executable, str(script)] + extra_args
    return subprocess.run(cmd, capture_output=False, text=True)


def parse_feature_result_from_output(returncode: int, feature_num: str, feature_name: str) -> FeatureResult:
    """
    Create a FeatureResult from a subprocess returncode.

    The detailed counts (passed/failed/skipped) are printed directly by the
    feature's run_tests.py; we track only pass/fail at the regression level
    to avoid parsing stdout. A future enhancement could parse structured output.
    """
    result = FeatureResult(
        feature_num=feature_num,
        feature_name=feature_name,
    )
    if returncode == 0:
        result.passed = 1  # Treat the feature as a single unit for regression tracking
    elif returncode == 1:
        result.failed = 1
    else:
        result.failed = 1  # Exit code 2 = infrastructure error, also counted as failed
    return result


def confirm_fix_mode() -> bool:
    """Prompt the user to confirm fix mode. Returns True if confirmed."""
    print()
    print("WARNING: Fix mode will modify template files in the vault.")
    print("All changes can be reviewed via git diff.")
    response = input("Proceed with fix mode? [y/N] ").strip().lower()
    return response == "y"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CTLv3 Sustaining — Master Regression Script"
    )
    parser.add_argument(
        "--no-quality",
        action="store_true",
        help="Skip all qualitative (AI) tests.",
    )
    parser.add_argument(
        "--feature",
        metavar="NNN",
        help="Run tests for a single feature number only (e.g., 001).",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Enable AI fix mode for qualitative tests (requires user confirmation).",
    )
    args = parser.parse_args()

    # Fix mode requires confirmation
    if args.fix and not confirm_fix_mode():
        print("Fix mode cancelled.")
        return 0

    # Build extra args to pass to each feature's run_tests.py
    extra_args: list[str] = []
    if args.no_quality:
        extra_args.append("--no-quality")
    if args.fix:
        extra_args.append("--fix")

    mode = "script-only" if args.no_quality else "full"

    # Discover features
    all_folders = discover_feature_folders(TESTS_DIR)
    if not all_folders:
        print("No feature test folders found. Nothing to run.", file=sys.stderr)
        return 2

    # Filter to a single feature if requested
    if args.feature:
        target = args.feature.lstrip("0") or "0"
        all_folders = [
            f for f in all_folders
            if re.match(r'^(\d+)', f.name) and
               int(re.match(r'^(\d+)', f.name).group(1)) == int(target)
        ]
        if not all_folders:
            print(f"No test folder found for feature {args.feature}.", file=sys.stderr)
            return 2

    summary = RegressionSummary(mode=mode)
    overall_exit = 0

    for folder in all_folders:
        num_match = re.match(r'^(\d+)\s+-\s+(.*)', folder.name)
        feature_num = num_match.group(1) if num_match else "???"
        feature_name = num_match.group(2) if num_match else folder.name

        proc = run_feature(folder, extra_args)

        result = parse_feature_result_from_output(proc.returncode, feature_num, feature_name)
        summary.add(result)

        if proc.returncode != 0:
            overall_exit = 1

        # Feature 001 is the infrastructure gatekeeper — abort on failure
        if feature_num.lstrip("0") == "1" and proc.returncode != 0:
            print()
            print("ABORT: Feature 001 (Infrastructure Test) failed.")
            print("Testing infrastructure is broken. Fix Feature 001 before running other tests.")
            print_regression_summary(summary)
            return 2

    print_regression_summary(summary)
    return overall_exit


if __name__ == "__main__":
    sys.exit(main())
