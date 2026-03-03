---
task_id: "Task-14"
ip_tasks: ["6.5"]
execution_phase: "Phase 6"
status: "Done"
domain: "Memories"
parallelizable: true
parallel_group: "Can run with Tasks 12, 13, 18, 19, 20, 21, 22 (all after Task 09 is complete)"
---
# Task 14 — Memories Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 5 Memories domain templates from v2 to v3.

## Dependencies
- Task 02 — `Memories/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `Memories/.system-block.md` complete
- Task 07 — Root block templates complete
- Task 09 — `Memories/Templates/When Where Who.md` block complete (included by all memory templates)

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## Source → Target Mapping

All targets in `Data/Vaults/z2k-default-vault/Memories/Templates/`

| Source (v2) | Target (v3) |
|---|---|
| `Memories - ~Generic` | `Memories (General).md` |
| `Memories - Family Vacation Trip` | `Family Vacation Trip.md` |
| `Memories - Ontology` | `Ontology.md` |
| `Memories - PCT Trail Day` | `PCT Trail Day.md` |
| `Memories - Solo Trip Summary` | `Solo Trip Summary.md` |

> **Drop:** `Memories - Quote an Email` — excluded per Requirements Q8 decision. Do not migrate.

## Special Requirements

### All Templates — Include When Where Who Block
Every memory template must include `{{> "When Where Who"}}`.

### PCT Trail Day — Personal Template
- Add `z2k_template_author: "Geoff (z2k-gwp)"`
- **Preserve all hardcoded personal specifics:** start mileage, trip context, personal notes — these are intentionally personal

## Required v3 YAML Fields (on every template)
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
# PCT Trail Day only:
z2k_template_author: "Geoff (z2k-gwp)"
```

## Acceptance Criteria
- All 5 files exist in `Memories/Templates/`
- All include `{{> "When Where Who"}}`
- `PCT Trail Day.md` has `z2k_template_author: "Geoff (z2k-gwp)"` and preserved personal content
- `Memories - Quote an Email` NOT migrated

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All templates exist | All 5 paths in `Memories/Templates/` |
| Each has required YAML fields | Present |
| Each instantiates without error | Output created; no error log |
| System-block injection works | Output contains `z2k_creation_domain: ".:Z2K/Domain/Memories"` |
| Personal templates have correct `z2k_template_author` | `Geoff (z2k-gwp)` in PCT Trail Day |
