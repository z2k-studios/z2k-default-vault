---
feature_number: "138"
description: "Quote a Source document template for attributed quotations in the Thoughts domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/138 - Quote a Source (Thoughts)/"
---

# Feature 138 — Quote a Source (Thoughts)

## Description
The Quote a Source (Thoughts) template is a document template in the Thoughts domain for capturing quotations with explicit source attribution. It uses a source type of Quotation and provides structured fields for recording the quoted text along with its originating source, enabling proper citation and reference tracking.

## Requirements
### 138-001 — Template file exists `[quantitative]`
Template file exists at `Thoughts/Templates/Quote a Source.md`.

### 138-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 138-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 138-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.

### 138-005 — Correct source type `[quantitative]`
YAML contains `z2k_source_type: Quotation`.
