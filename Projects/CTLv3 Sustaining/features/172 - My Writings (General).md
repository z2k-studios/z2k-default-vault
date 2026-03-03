---
feature_number: "172"
description: "My Writings (General) document template — domain default for Projects/My Writings"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/172 - My Writings (General)/"
---

# Feature 172 — My Writings (General)

## Description
The My Writings (General) template is the domain default document template for the Projects/My Writings sub-domain. The "(General)" postfix is a workaround for GH #182.

## Requirements
### 172-001 — Template file exists `[quantitative]`
The file `Projects/My Writings/Templates/My Writings (General).md` must exist in the vault.

### 172-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 172-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 172-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.
