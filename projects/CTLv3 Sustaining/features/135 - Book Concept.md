---
feature_number: "135"
description: "Book Concept document template for capturing concepts and ideas from books"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/135 - Book Concept/"
---

# Feature 135 — Book Concept

## Description
The Book Concept template is a document template in the Thoughts domain for capturing concepts, ideas, and key takeaways encountered while reading books. It uses a source type of InternalThought, reflecting that the captured content represents the user's interpretation and synthesis of book material rather than a direct quotation.

## Requirements
### 135-001 — Template file exists `[quantitative]`
Template file exists at `Thoughts/Templates/Book Concept.md`.

### 135-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 135-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 135-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.

### 135-005 — Correct source type `[quantitative]`
YAML contains `z2k_source_type: InternalThought`.
