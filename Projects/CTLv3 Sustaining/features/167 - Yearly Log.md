---
feature_number: "167"
description: "Yearly Log document template with date navigation links"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/167 - Yearly Log/"
---

# Feature 167 — Yearly Log

## Description
The Yearly Log template provides a yearly tracking document in the Logs domain with navigation links to adjacent years.

## Requirements
### 167-001 — Template file exists `[quantitative]`
The file `Logs/Templates/Yearly Log.md` must exist in the vault.

### 167-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 167-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 167-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.

### 167-005 — Date navigation links use dateAdd/formatDate helpers `[quantitative]`
The template must use `dateAdd`/`formatDate` helpers to generate previous-year and next-year navigation links.
