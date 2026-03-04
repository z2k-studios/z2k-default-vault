---
feature_number: "900"
description: "Aggregation gate — validates all individual template qualitative assessments are present, recent, and passing"
status: "Describing"
date_added: "2026-03-03"
test_folder: "tests/900 - Template Quality Gate/"
---

# Feature 900 — Template Quality Gate

## Description

This feature is an aggregation gate that validates the qualitative health of the entire template library without performing any AI assessment itself. Each individual template feature (100–899) owns its own qualitative check against the Template Quality Scorecard. Feature 900 verifies that all of those checks have been run recently and passed.

This feature runs **after** all individual template features in the numerical execution order. It does not call the AI quality agent — it reads results that already exist.

## Relationship to the Scorecard

The Template Quality Scorecard (`CTLv3 Sustaining - Template Quality Scorecard.md`) defines the qualitative criteria and rubrics. Individual template features invoke the AI agent against the scorecard for their specific template. Feature 900 does not interact with the scorecard directly — it only reads the pass/fail outcomes from individual template results.

## Staleness Window

Results are considered valid if `date_run` in the feature's `last-run-results.md` is within **24 hours** of the current time. This allows templates to be tested individually or in batches ahead of a regression run. As long as all templates have been assessed within the window, the gate passes.

## Requirements

### 900-001 — All individual template features have results `[quantitative]`

Every template feature folder (matching `1XX - *` in `tests/`) has a `last-run-results.md` file. Missing result files indicate untested templates.

### 900-002 — All results are within the staleness window `[quantitative]`

Every `last-run-results.md` has a `date_run` value within the last 24 hours. Stale results require re-running the individual template's tests.

### 900-003 — All qualitative requirements passed `[quantitative]`

No individual template feature has a qualitative requirement with result "FAIL". Quantitative failures in individual templates are not checked here — those are reported by the individual features themselves.
