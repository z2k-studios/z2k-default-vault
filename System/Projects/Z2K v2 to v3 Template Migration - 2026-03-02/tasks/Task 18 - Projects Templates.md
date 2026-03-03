---
task_id: "Task-18"
ip_tasks: ["6.9"]
execution_phase: "Phase 6"
status: "Pending"
domain: "Projects"
parallelizable: true
parallel_group: "Can run with Tasks 12–17, 19–22 (after Task 06 is complete)"
---
# Task 18 — Projects Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Build 3 new Projects root templates and migrate 4 My Writings templates from v2 to v3.

## Dependencies
- Task 02 — `Projects/Templates/` and `Projects/My Writings/Templates/` exist
- Task 03 — Root system-block complete
- Task 04 — `Projects/.system-block.md` not from Task 04; see Task 06
- **Task 06 — Projects system-block + block stop must be complete** (DSB-005 resolution affects this task)
- Task 07 — Root block templates complete

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`
- **REF-E:** `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/System Block Stops.md` (for block stop behavior — check Task 06 resolution first)

## Open Issue — PROJ-YAML (Design Decision Required Before Executing)

Projects root templates use a **different YAML structure** — no `z2k_*` fields. Design project-specific YAML before writing the templates.

**Fields to design:** `goal`, `status`, `start_date`, `stakeholders`, `outcomes` + any others appropriate for project cards.

**Context from Task 06 (DSB-005):** After Task 06, review the DSB-005 resolution. If block stop does NOT fully prevent `z2k_*` injection, these templates need explicit YAML that overrides the injected fields. Note this in both Task 06 and here.

### PROJ-YAML Decision (to be filled in when executing)
> Project YAML fields designed: ___
> DSB-005 impact on these templates: ___

## Source → Target Mapping

### Projects Root Templates (3 — NEW, no v2 source)
Build from scratch. All in `Data/Vaults/z2k-default-vault/Projects/Templates/`

| Target (v3) | Description |
|---|---|
| `Project (General).md` | Generic project card — minimal structure |
| `Active Project.md` | Active project card — includes goal, status, milestones |
| `Completed Project.md` | Completed project card — includes outcomes, learnings |

**Note on YAML:** These use project-specific YAML (no `z2k_*` fields). Use the PROJ-YAML design from above.

### My Writings Templates (4 — migrated from Syntheses domain)
All in `Data/Vaults/z2k-default-vault/Projects/My Writings/Templates/`

| Source (v2) | Target (v3) | Note |
|---|---|---|
| `Syntheses - ~Generic` | `My Writings (General).md` | GH issue #182 workaround — `(General)` suffix until Default Template feature ships |
| `Syntheses - Extended Journal Writing` | `Personal Writing.md` | |
| `Syntheses - Treatise` | `Treatise.md` | |
| `Project - Code Poetry - Poem (personal)` | `Code Poem.md` | Personal template |

> **Drop:** `Syntheses - Quote an Email` — excluded per Requirements Q2 decision.

### My Writings Personal Templates
- `Code Poem.md` → add `z2k_template_author: "Geoff (z2k-gwp)"`

## Required v3 YAML Fields
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
# Projects root templates: project-specific YAML instead of z2k_* fields
# My Writings personal templates:
z2k_template_author: "Geoff (z2k-gwp)"
```

## Acceptance Criteria
- All 7 files exist at correct paths
- Projects root templates use project-specific YAML (no `z2k_*` fields per PROJ-YAML design)
- My Writings templates have standard v3 metadata
- `Code Poem.md` has `z2k_template_author: "Geoff (z2k-gwp)"`
- `Syntheses - Quote an Email` NOT migrated
- DSB-005 impact addressed per Task 06 resolution

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All templates exist | All 7 paths exist |
| Each has required YAML fields | Present |
| Each instantiates without error | Output created; no error log |
| System-block injection works | Output handled per DSB-005 resolution |
| Personal templates have correct `z2k_template_author` | `Geoff (z2k-gwp)` in Code Poem |
