---
feature_number: "176"
description: "Contact (General) document template — minimal starting point for the Entities domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/176 - Contact (General)/"
---

# Feature 176 — Contact (General)

## Description
The Contact (General) template provides a minimal starting-point document template for the Entities domain. Full CRM functionality is deferred to a future project.

## Requirements
### 176-001 — Template file exists `[quantitative]`
The file `Entities/Templates/Contact (General).md` must exist in the vault.

### 176-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 176-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 176-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.
