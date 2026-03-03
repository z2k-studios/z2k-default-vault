---
task_id: "Task-20"
ip_tasks: ["6.11"]
execution_phase: "Phase 6"
status: "Pending"
domain: "System"
parallelizable: true
parallel_group: "Can run with Tasks 10, 11, 15, 16, 17, 21, 22"
---
# Task 20 — System Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 1 System domain template from v2 to v3.

## Dependencies
- Task 02 — `System/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `System/.system-block.md` complete
- Task 07 — Root block templates complete

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## Source → Target Mapping

| Source (v2) | Target (v3) | Note |
|---|---|---|
| `~System - ~Generic` | `System/Templates/System (General).md` | |
| `~System - Testing` | *DROP* | Testing artifact — do not migrate |

## Required v3 YAML Fields
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```

## Acceptance Criteria
- `System/Templates/System (General).md` exists with required v3 YAML fields
- `~System - Testing` not migrated

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| Template exists | `System/Templates/System (General).md` exists |
| Has required YAML fields | Present |
| Instantiates without error | Output created; no error log |
| System-block injection works | Output contains `z2k_creation_domain: ".:Z2K/Domain/System"` |
