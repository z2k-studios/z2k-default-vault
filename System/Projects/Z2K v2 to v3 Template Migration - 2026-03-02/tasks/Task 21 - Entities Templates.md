---
task_id: "Task-21"
ip_tasks: ["6.12"]
execution_phase: "Phase 6"
status: "Pending"
domain: "Entities"
parallelizable: true
parallel_group: "Can run with Tasks 10, 11, 15, 16, 17, 20, 22"
---
# Task 21 — Entities Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Build 1 new Entities domain template from scratch (no v2 equivalent — new template for v3).

## Dependencies
- Task 02 — `Entities/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `Entities/.system-block.md` complete
- Task 07 — Root block templates complete

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## Output File
`Data/Vaults/z2k-default-vault/Entities/Templates/Contact (General).md` — **new, build from scratch**

## Template Design
A minimal generic contact card. Fields:
- Name
- Role / Title
- Organization
- Relationship to vault owner
- First Met (date)
- Tags
- Notes

> **Scope note:** This is a minimal placeholder. A full CRM template set (Person, Organization, Named Entity) is explicitly out of scope for this project (see SoW §1.2 Non-Goals). Do not over-engineer.

## Required v3 YAML Fields
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```

## Acceptance Criteria
- `Entities/Templates/Contact (General).md` exists with required v3 YAML fields
- Template has at minimum: Name, Role, Organization, Relationship, First Met, Tags, Notes fields
- Template is minimal — does not attempt to implement full CRM structure

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| Template exists | `Entities/Templates/Contact (General).md` exists |
| Has required YAML fields | Present |
| Instantiates without error | Output created; no error log |
| System-block injection works | Output contains `z2k_creation_domain: ".:Z2K/Domain/Entities"` |
