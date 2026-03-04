---
feature: "900 - Template Quality Gate"
feature_file: "features/900 - Template Quality Gate.md"
quality_override: false
---

# Test Plan — Feature 900: Template Quality Gate

## Feature Reference

- **Feature file:** `features/900 - Template Quality Gate.md`
- **Requirements:** 900-001, 900-002, 900-003 (all quantitative)

## Overview

Feature 900 is an aggregation gate. It performs no AI assessment — it reads `last-run-results.md` from every individual template feature (100–899) and validates completeness, recency, and qualitative pass status.

This feature is designed to run **after** all individual template features in the numerical execution order.

**Mode:** Under `--no-quality`, all requirements are `[SKIP]`. This is consistent with other features, even though 900's own requirements are quantitative — the `--no-quality` flag signals that qualitative assessments were skipped upstream, making the gate check meaningless.

## Staleness Window

Results are valid if `date_run` is within **24 hours** of the current time. This allows individual template tests to be run ahead of a regression pass.

## Test Assertion Table

| Req ID | Description | Tier | Automated | Passes if |
|---|---|---|---|---|
| 900-001 | All individual template features have results | Quantitative | Yes | Every `1XX - *` test folder has `last-run-results.md` |
| 900-002 | All results are within the staleness window | Quantitative | Yes | Every `date_run` is within 24 hours of now |
| 900-003 | All qualitative requirements passed | Quantitative | Yes | No qualitative requirement has result "FAIL" in any template feature |

## Coverage Checklist

- [x] Every requirement ID from the feature file appears in the test assertion table
- [x] No test rows reference requirement IDs that do not exist
- [x] No qualitative tests (all are quantitative gate checks)
- [x] No manual tests

## Notes

- If no `1XX - *` test folders exist, 900-001 reports FAIL with a note that no template features have test infrastructure yet.
- 900-003 only checks requirements with `tier: qualitative`. Quantitative failures in individual templates are their own concern.
- The gate is intentionally conservative: any missing, stale, or failed result causes a FAIL.
