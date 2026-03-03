---
feature_number: "168"
description: "Yearly Strategic Plan document template for the Logs domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/168 - Yearly Strategic Plan/"
---

# Feature 168 — Yearly Strategic Plan

## Description
The Yearly Strategic Plan template provides a strategic planning document in the Logs domain for annual goal-setting and strategy definition.

## Requirements
### 168-001 — Template file exists `[quantitative]`
The file `Logs/Templates/Yearly Strategic Plan.md` must exist in the vault.

### 168-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 168-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 168-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.
