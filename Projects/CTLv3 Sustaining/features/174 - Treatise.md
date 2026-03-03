---
feature_number: "174"
description: "Treatise document template for the Projects/My Writings sub-domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/174 - Treatise/"
---

# Feature 174 — Treatise

## Description
The Treatise template provides a document template for long-form treatise writing in the Projects/My Writings sub-domain.

## Requirements
### 174-001 — Template file exists `[quantitative]`
The file `Projects/My Writings/Templates/Treatise.md` must exist in the vault.

### 174-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 174-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 174-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.
