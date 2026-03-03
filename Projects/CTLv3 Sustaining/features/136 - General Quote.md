---
feature_number: "136"
description: "General Quote document template for capturing quotations from any source"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/136 - General Quote/"
---

# Feature 136 — General Quote

## Description
The General Quote template is a document template in the Thoughts domain for capturing quotations from any source — conversations, articles, speeches, media, or other non-book origins. It uses a source type of Quotation and provides fields for the quote text, attribution, and context.

## Requirements
### 136-001 — Template file exists `[quantitative]`
Template file exists at `Thoughts/Templates/General Quote.md`.

### 136-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 136-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 136-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.

### 136-005 — Correct source type `[quantitative]`
YAML contains `z2k_source_type: Quotation`.
