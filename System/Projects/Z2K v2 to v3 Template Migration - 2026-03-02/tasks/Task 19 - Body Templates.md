---
task_id: "Task-19"
ip_tasks: ["6.10"]
execution_phase: "Phase 6"
status: "Done"
domain: "Body"
parallelizable: true
parallel_group: "Can run with Tasks 12, 13, 14, 18, 20, 21, 22 (after Task 09 is complete)"
---
# Task 19 — Body Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 1 Body domain template from v2 to v3. (Health Log block was handled in Task 09.)

## Dependencies
- Task 02 — `Body/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `Body/.system-block.md` complete
- Task 07 — Root block templates complete
- Task 09 — `Body/Templates/Health Log.md` block complete (block already done — no action needed here)

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## Source → Target Mapping

| Source (v2) | Target (v3) |
|---|---|
| `Body - ~Generic` | `Body/Templates/Body (General).md` |

> The Health Log block (`Body/Templates/Health Log.md`) was created in Task 09. No action needed for it here.

## Required v3 YAML Fields
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```

## Acceptance Criteria
- `Body/Templates/Body (General).md` exists with required v3 YAML fields

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| Template exists | `Body/Templates/Body (General).md` exists |
| Has required YAML fields | Present |
| Instantiates without error | Output created; no error log |
| System-block injection works | Output contains `z2k_creation_domain: ".:Z2K/Domain/Body"` |
