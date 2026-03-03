---
feature_number: "179"
description: "System (General) document template for the System domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/179 - System (General)/"
---

# Feature 179 — System (General)

## Description
The System (General) template provides the general-purpose document template for the System domain.

## Requirements
### 179-001 — Template file exists `[quantitative]`
The file `System/Templates/System (General).md` must exist in the vault.

### 179-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 179-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 179-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.
