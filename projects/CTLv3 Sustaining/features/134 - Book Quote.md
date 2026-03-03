---
feature_number: "134"
description: "Book Quote document template for capturing quotations from books"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/134 - Book Quote/"
---

# Feature 134 — Book Quote

## Description
The Book Quote template is a document template in the Thoughts domain for capturing quotations sourced from books. It provides structured fields for the quote text, book title, author, page reference, and related context, with a source type of Quotation.

## Requirements
### 134-001 — Template file exists `[quantitative]`
Template file exists at `Thoughts/Templates/Book Quote.md`.

### 134-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 134-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 134-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.

### 134-005 — Correct source type `[quantitative]`
YAML contains `z2k_source_type: Quotation`.
