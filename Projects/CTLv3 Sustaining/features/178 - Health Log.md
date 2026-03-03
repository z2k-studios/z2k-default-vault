---
feature_number: "178"
description: "Health Log block template with preserved Flame fields for the Body domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/178 - Health Log/"
---

# Feature 178 — Health Log

## Description
The Health Log template is a **block template** in the Body domain. It preserves all Flame-style field references exactly as they existed in v2. As a block template, it does not have version or suggested_title requirements.

## Requirements
### 178-001 — Template file exists `[quantitative]`
The file `Body/Templates/Health Log.md` must exist in the vault.

### 178-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 178-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 178-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for block templates.

### 178-005 — All Flame-* field references preserved verbatim `[quantitative]`
All `Flame-*` field references from the v2 template must be preserved exactly as-is in the v3 template, with no renaming, removal, or modification.
