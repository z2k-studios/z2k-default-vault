---
feature_number: "133"
description: "Thoughts (General) document template — domain default for the Thoughts domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/133 - Thoughts (General)/"
---

# Feature 133 — Thoughts (General)

## Description
The Thoughts (General) template is the domain default document template for the Thoughts domain. It captures internal thoughts with a source type of InternalThought. This is the primary template users encounter when creating a new Thoughts card without selecting a specific template variant.

## Requirements
### 133-001 — Template file exists `[quantitative]`
Template file exists at `Thoughts/Templates/Thoughts (General).md`.

### 133-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 133-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 133-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.

### 133-005 — Correct source type `[quantitative]`
YAML contains `z2k_source_type: InternalThought`.
