from __future__ import annotations

"""
CTLv3 Sustaining — Standardized Test Output Formatter

All output conforms to the contract defined in Testing Plan §5.
Structured results go to stdout; diagnostics go to stderr.
"""

import sys
from dataclasses import dataclass, field


SEPARATOR = "=" * 40


@dataclass
class FeatureResult:
    feature_num: str
    feature_name: str
    passed: int = 0
    failed: int = 0
    skipped: int = 0
    quality_score: float | None = None
    quality_override: bool = False
    quality_threshold: float = 70.0

    @property
    def total(self) -> int:
        return self.passed + self.failed + self.skipped

    @property
    def all_passed(self) -> bool:
        return self.failed == 0


# ---------------------------------------------------------------------------
# Per-requirement output
# ---------------------------------------------------------------------------

def print_pass(req_id: str, description: str, tier: str, score: float | None = None) -> None:
    tier_label = f"[{tier}]"
    score_str = f" (score: {score:.0f}%)" if score is not None else ""
    print(f"[PASS] {req_id}: {description} {tier_label}{score_str}")


def print_fail(
    req_id: str,
    description: str,
    tier: str,
    expected: str | None = None,
    actual: str | None = None,
    score: float | None = None,
    threshold: float | None = None,
    suggestions: str | None = None,
    error_log_entries: list[str] | None = None,
) -> None:
    tier_label = f"[{tier}]"
    score_str = (
        f" (score: {score:.0f}%, threshold: {threshold:.0f}%)"
        if score is not None and threshold is not None
        else ""
    )
    print(f"[FAIL] {req_id}: {description} {tier_label}{score_str}")
    if expected is not None:
        print(f"  \u2192 Expected: {expected}")
    if actual is not None:
        print(f"  \u2192 Actual:   {actual}")
    if suggestions:
        print(f"  \u2192 Suggestions: {suggestions}")
    if error_log_entries:
        print(f"  \u2192 Error log entries:")
        for entry in error_log_entries:
            for line in entry.splitlines():
                print(f"      {line}")


def print_skip(req_id: str, description: str, reason: str) -> None:
    print(f"[SKIP] {req_id}: {description} [qualitative]")
    print(f"  \u2192 Reason: {reason}")


# ---------------------------------------------------------------------------
# Feature summary
# ---------------------------------------------------------------------------

def print_feature_summary(result: FeatureResult) -> None:
    print()
    print(SEPARATOR)
    print(f"Feature {result.feature_num} - {result.feature_name}")
    print(f"  Passed:  {result.passed}")
    print(f"  Failed:  {result.failed}")
    print(f"  Skipped: {result.skipped}")
    print(f"  Total:   {result.total}")

    if result.quality_score is not None:
        print(
            f"  Quality Score: {result.quality_score:.0f}% "
            f"(threshold: {result.quality_threshold:.0f}%)"
        )
    elif result.quality_override:
        print("  Quality Score: OVERRIDE")
    else:
        print("  Quality Score: N/A")

    print(SEPARATOR)


# ---------------------------------------------------------------------------
# Regression summary
# ---------------------------------------------------------------------------

@dataclass
class RegressionSummary:
    mode: str = "full"
    feature_results: list[FeatureResult] = field(default_factory=list)
    total_reqs: int = 0
    total_passed: int = 0
    total_failed: int = 0
    total_skipped: int = 0
    quality_assessments: int = 0
    quality_overrides: int = 0

    def add(self, result: FeatureResult) -> None:
        self.feature_results.append(result)
        self.total_reqs += result.total
        self.total_passed += result.passed
        self.total_failed += result.failed
        self.total_skipped += result.skipped
        if result.quality_score is not None:
            self.quality_assessments += 1
        if result.quality_override:
            self.quality_overrides += 1

    @property
    def features_passed(self) -> int:
        return sum(1 for r in self.feature_results if r.all_passed)

    @property
    def features_failed(self) -> int:
        return sum(1 for r in self.feature_results if not r.all_passed)

    @property
    def overall_pass(self) -> bool:
        return self.features_failed == 0


def print_regression_summary(summary: RegressionSummary) -> None:
    n = len(summary.feature_results)
    print()
    print(SEPARATOR)
    print("REGRESSION TEST SUMMARY")
    print(f"  Mode: {summary.mode}")
    print(f"  Features tested:  {n}")
    print(f"  Features passed:  {summary.features_passed} (all requirements met)")
    print(f"  Features failed:  {summary.features_failed}")
    print()
    print(f"  Total requirements: {summary.total_reqs}")
    print(f"  Passed:  {summary.total_passed}")
    print(f"  Failed:  {summary.total_failed}")
    print(f"  Skipped: {summary.total_skipped}")
    print()
    print(f"  Quality assessments: {summary.quality_assessments} (of {n} features)")
    print(f"  Quality overrides:   {summary.quality_overrides}")
    print(SEPARATOR)
    print(f"RESULT: {'PASS' if summary.overall_pass else 'FAIL'}")


def diag(msg: str) -> None:
    """Write a diagnostic message to stderr."""
    print(msg, file=sys.stderr)
