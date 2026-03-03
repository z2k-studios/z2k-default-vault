---
feature_number: "173"
description: "Personal Writing document template (renamed from Extended Journal Writing)"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/173 - Personal Writing/"
---

# Feature 173 — Personal Writing

## Description
The Personal Writing template provides a document template for personal writing projects in the Projects/My Writings sub-domain. This template was renamed from "Extended Journal Writing."

## Requirements
### 173-001 — Template file exists `[quantitative]`
The file `Projects/My Writings/Templates/Personal Writing.md` must exist in the vault.

### 173-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 173-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 173-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.
