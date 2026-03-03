---
feature_number: "162"
description: "Yearly Summary document template for the Journals domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/162 - Yearly Summary/"
---

# Feature 162 — Yearly Summary

## Description
The Yearly Summary template provides a year-end reflective summary document in the Journals domain.

## Requirements
### 162-001 — Template file exists `[quantitative]`
The file `Journals/Templates/Yearly Summary.md` must exist in the vault.

### 162-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 162-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 162-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.
