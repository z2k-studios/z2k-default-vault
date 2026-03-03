---
feature_number: "170"
description: "Active Project document template with NON-z2k YAML output"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/170 - Active Project/"
---

# Feature 170 — Active Project

## Description
The Active Project template provides a document template for in-progress projects in the Projects domain. It uses a NON-z2k YAML structure, meaning the rendered output should not contain `z2k_*` fields due to the system-block-stop mechanism.

## Requirements
### 170-001 — Template file exists `[quantitative]`
The file `Projects/Templates/Active Project.md` must exist in the vault.

### 170-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 170-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 170-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.

### 170-005 — Rendered output does not contain z2k_* YAML fields `[quantitative]`
The rendered document's YAML frontmatter must NOT contain any `z2k_*` fields. The system-block-stop mechanism must strip all z2k internal fields from the output, leaving only the project-specific NON-z2k YAML structure.
