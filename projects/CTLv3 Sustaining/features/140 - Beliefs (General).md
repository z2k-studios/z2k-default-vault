---
feature_number: "140"
description: "Beliefs (General) document template — domain default for the Beliefs domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/140 - Beliefs (General)/"
---

# Feature 140 — Beliefs (General)

## Description
The Beliefs (General) template is the domain default document template for the Beliefs domain. It captures personal beliefs, convictions, and value statements with a source type of InternalThought, reflecting that beliefs originate from the user's own internal reasoning and perspective.

## Requirements
### 140-001 — Template file exists `[quantitative]`
Template file exists at `Beliefs/Templates/Beliefs (General).md`.

### 140-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 140-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 140-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.

### 140-005 — Correct source type `[quantitative]`
YAML contains `z2k_source_type: InternalThought`.
