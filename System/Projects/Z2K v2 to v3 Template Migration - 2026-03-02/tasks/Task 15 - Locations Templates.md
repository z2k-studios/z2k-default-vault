---
task_id: "Task-15"
ip_tasks: ["6.6"]
execution_phase: "Phase 6"
status: "Pending"
domain: "Locations"
parallelizable: true
parallel_group: "Can run with Tasks 10, 11, 16, 17, 20, 21, 22"
---
# Task 15 — Locations Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 1–2 Locations domain templates from v2 to v3, after resolving LOC-001.

## Dependencies
- Task 02 — `Locations/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `Locations/.system-block.md` complete
- Task 07 — Root block templates complete

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## ⚠️ PREREQUISITE: Resolve LOC-001 Before Writing

Before writing any templates, read **both** v2 source files:
- `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/Locations - ~Generic`
- `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/Locations.template` (if it exists)

**Decision:**
- If the files are functionally identical → create one `Locations (General).md`
- If they are substantively different → create appropriately named templates for each distinct use case

### LOC-001 Resolution (to be filled in when executing)
> Files compared: ___
> Decision: ___
> Templates to create: ___

## Output Files (minimum)

`Data/Vaults/z2k-default-vault/Locations/Templates/Locations (General).md`

Additional templates as determined by LOC-001 resolution.

## Required v3 YAML Fields
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```

## Acceptance Criteria
- LOC-001 resolved and documented in this task file
- At least `Locations (General).md` exists
- All created files have required v3 YAML fields

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All templates exist | All created paths in `Locations/Templates/` |
| Each has required YAML fields | Present |
| Each instantiates without error | Output created; no error log |
| System-block injection works | Output contains `z2k_creation_domain: ".:Z2K/Domain/Locations"` |
