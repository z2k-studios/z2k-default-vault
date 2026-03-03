---
feature_number: "164"
description: "Monthly Log document template with date navigation links"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/164 - Monthly Log/"
---

# Feature 164 — Monthly Log

## Description
The Monthly Log template provides a monthly tracking document in the Logs domain with navigation links to adjacent months.

## Requirements
### 164-001 — Template file exists `[quantitative]`
The file `Logs/Templates/Monthly Log.md` must exist in the vault.

### 164-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 164-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 164-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.

### 164-005 — Date navigation links use dateAdd/formatDate helpers `[quantitative]`
The template must use `dateAdd`/`formatDate` helpers to generate previous-month and next-month navigation links.
