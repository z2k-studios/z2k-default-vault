---
feature_number: "166"
description: "Weekly Log document template with date navigation links"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/166 - Weekly Log/"
---

# Feature 166 — Weekly Log

## Description
The Weekly Log template provides a weekly tracking document in the Logs domain with navigation links to adjacent weeks.

## Requirements
### 166-001 — Template file exists `[quantitative]`
The file `Logs/Templates/Weekly Log.md` must exist in the vault.

### 166-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 166-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 166-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.

### 166-005 — Date navigation links use dateAdd/formatDate helpers `[quantitative]`
The template must use `dateAdd`/`formatDate` helpers to generate previous-week and next-week navigation links.
