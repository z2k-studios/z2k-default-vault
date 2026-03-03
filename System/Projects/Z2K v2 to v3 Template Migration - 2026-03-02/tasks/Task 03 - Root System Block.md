---
task_id: "Task-03"
ip_tasks: ["2.1"]
execution_phase: "Phase 2"
status: "Pending"
domain: "Global"
parallelizable: true
parallel_group: "Can run with Tasks 04–09 after Task 02 is complete"
---
# Task 03 — Root System Block

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Rewrite the root `.system-block.md` to v3 schema: remove deprecated fields, add `z2k_creation_library_version`, add `{{fieldInfo me}}` body.

## Dependencies
- Task 02 (vault structure) must be complete

## References to Read First
- REF-B: `Docs/z2k-system-docs/4 - Z2K Reference Docs/4b - Data Formats/Z2K Card Metadata - YAML.md`
- REF-C: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Intro to System Blocks.md`
- REF-D: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Using System Blocks and fieldInfo.md`

## Target File
`Data/Vaults/z2k-default-vault/.system-block.md` — in-place rewrite

## Current State (as of 2026-03-02)
```yaml
z2k_metadata_version:     3.00
z2k_metadata_variant:     "barebones"
z2k_metadata_copyright:   "Z2K Metadata structure is © 2025 Z2K Studios, LLC"
z2k_metadata_reference:   "https://z2ksystem.com/specs/v3.0"
z2k_creation_creator:     "{{wikilink creator}}"
z2k_creation_date:        "{{wikilink today}}"
z2k_creation_timestamp:   "{{timestamp}}"
z2k_creation_template:    "{{wikilink templateName}}"
z2k_creation_domain:      ".:Z2K/Domain/{{normalizePath destPath}}"  ← REMOVE
z2k_creation_language:    "en"
z2k_card_build_state:     ".:Z2K/BuildState/Uninitialized"           ← REMOVE
z2k_card_status:          ".:Z2K/Status/Ongoing"                     ← REMOVE
z2k_card_source_type:     ".:Z2K/SourceType/Unknown"                 ← KEEP
```

## Changes to Make
- **REMOVE:** `z2k_creation_domain` (uses unsupported `normalizePath` helper)
- **REMOVE:** `z2k_card_build_state`
- **REMOVE:** `z2k_card_status` (no default status value in root system-block)
- **ADD:** `z2k_creation_library_version: "3.0.0"` (after `z2k_creation_language`)
- **ADD:** `{{fieldInfo me value="me"}}` in the template body section (below the YAML block)
- **RETAIN:** All other fields unchanged

## Acceptance Criteria
Root `.system-block.md`:
- No `z2k_creation_domain`, no `z2k_card_build_state`, no `z2k_card_status`
- Has `z2k_creation_library_version: "3.0.0"`
- Has `{{fieldInfo me value="me"}}` in body
- All retained fields present and unchanged

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| `.system-block.md` exists | File exists |
| YAML: required fields present | `z2k_metadata_version`, `z2k_creation_creator`, `z2k_creation_date`, `z2k_creation_timestamp`, `z2k_creation_template`, `z2k_creation_language`, `z2k_creation_library_version`, `z2k_card_source_type` all present |
| YAML: removed fields absent | `z2k_creation_domain`, `z2k_card_build_state`, `z2k_card_status` not present |
| Body: `{{fieldInfo me}}` present | File body contains `{{fieldInfo me` |
