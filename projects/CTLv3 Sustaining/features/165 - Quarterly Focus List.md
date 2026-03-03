---
feature_number: "165"
description: "Quarterly Focus List document template for the Logs domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/165 - Quarterly Focus List/"
---

# Feature 165 — Quarterly Focus List

## Description
The Quarterly Focus List template provides a quarterly goal-setting and focus-tracking document in the Logs domain.

## Requirements
### 165-001 — Template file exists `[quantitative]`
The file `Logs/Templates/Quarterly Focus List.md` must exist in the vault.

### 165-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 165-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 165-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.
