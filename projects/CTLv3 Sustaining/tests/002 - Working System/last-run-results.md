---
feature_number: "002"
feature_name: "Working System"
date_run: "2026-03-03 12:43:42"
result: FAIL
passed: 4
failed: 2
skipped: 0
requirements:
  - id: 002-001
    description: "Template renders via templatePath"
    result: PASS
    tier: quantitative
  - id: 002-002
    description: "Root system block YAML injected"
    result: FAIL
    tier: quantitative
    notes: "Missing: z2k_metadata_version (value starting with 3), z2k_creation_library_version: 3.0.0"
  - id: 002-003
    description: "Domain system block YAML injected"
    result: PASS
    tier: quantitative
  - id: 002-004
    description: "Field values resolved"
    result: PASS
    tier: quantitative
  - id: 002-005
    description: "Dynamic fields resolve"
    result: PASS
    tier: quantitative
  - id: 002-006
    description: "Output matches expected golden file"
    result: FAIL
    tier: quantitative
    notes: "17 diff line(s)"
---
# Feature 002 — Working System — Last Run Results
**Date:** 2026-03-03 12:43:42
**Overall Result:** FAIL

## Requirements

| Req ID | Description | Result | Tier |
|--------|-------------|--------|------|
| 002-001 | Template renders via templatePath | PASS | quantitative |
| 002-002 | Root system block YAML injected | FAIL | quantitative |
| 002-003 | Domain system block YAML injected | PASS | quantitative |
| 002-004 | Field values resolved | PASS | quantitative |
| 002-005 | Dynamic fields resolve | PASS | quantitative |
| 002-006 | Output matches expected golden file | FAIL | quantitative |

## Failures

### 002-002 — Root system block YAML injected
Missing: z2k_metadata_version (value starting with 3), z2k_creation_library_version: 3.0.0

### 002-006 — Output matches expected golden file
17 diff line(s)
