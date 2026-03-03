---
feature_number: "171"
description: "Completed Project document template with NON-z2k YAML output"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/171 - Completed Project/"
---

# Feature 171 — Completed Project

## Description
The Completed Project template provides a document template for finished projects in the Projects domain. It uses a NON-z2k YAML structure, meaning the rendered output should not contain `z2k_*` fields due to the system-block-stop mechanism.

## Requirements
### 171-001 — Template file exists `[quantitative]`
The file `Projects/Templates/Completed Project.md` must exist in the vault.

### 171-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 171-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 171-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.

### 171-005 — Rendered output does not contain z2k_* YAML fields `[quantitative]`
The rendered document's YAML frontmatter must NOT contain any `z2k_*` fields. The system-block-stop mechanism must strip all z2k internal fields from the output, leaving only the project-specific NON-z2k YAML structure.
