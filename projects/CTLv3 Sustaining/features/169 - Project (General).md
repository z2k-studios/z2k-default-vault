---
feature_number: "169"
description: "Project (General) document template — domain default with NON-z2k YAML output"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/169 - Project (General)/"
---

# Feature 169 — Project (General)

## Description
The Project (General) template is the domain default document template for the Projects domain. It uses a NON-z2k YAML structure, meaning the rendered output should not contain `z2k_*` fields due to the system-block-stop mechanism.

## Requirements
### 169-001 — Template file exists `[quantitative]`
The file `Projects/Templates/Project (General).md` must exist in the vault.

### 169-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 169-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 169-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.

### 169-005 — Rendered output does not contain z2k_* YAML fields `[quantitative]`
The rendered document's YAML frontmatter must NOT contain any `z2k_*` fields. The system-block-stop mechanism must strip all z2k internal fields from the output, leaving only the project-specific NON-z2k YAML structure.
