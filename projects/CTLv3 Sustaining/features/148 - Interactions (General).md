---
feature_number: "148"
description: "Interactions (General) document template — domain default for the Interactions domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/148 - Interactions (General)/"
---

# Feature 148 — Interactions (General)

## Description
The domain-default document template for the Interactions domain. Used when no more specific interaction template applies.

## Requirements
### 148-001 — Template file exists `[quantitative]`
Template file exists at `Interactions/Templates/Interactions (General).md`.

### 148-002 — All fields have fieldInfo declarations `[quantitative]`
Every field defined in the template has a corresponding `fieldInfo` declaration.

### 148-003 — Renders correctly via Command Queue `[quantitative]`
Template renders a complete card without errors when invoked through the Command Queue.

### 148-004 — Quality meets scorecard threshold `[qualitative]`
Rendered output meets the quality scorecard threshold defined in the project standards.
