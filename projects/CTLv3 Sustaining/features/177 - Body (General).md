---
feature_number: "177"
description: "Body (General) document template for the Body domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/177 - Body (General)/"
---

# Feature 177 — Body (General)

## Description
The Body (General) template provides a general body/health card document template in the Body domain.

## Requirements
### 177-001 — Template file exists `[quantitative]`
The file `Body/Templates/Body (General).md` must exist in the vault.

### 177-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 177-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 177-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.
