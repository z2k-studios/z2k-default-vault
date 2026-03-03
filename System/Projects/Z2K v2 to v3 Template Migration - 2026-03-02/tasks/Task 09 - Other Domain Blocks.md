---
task_id: "Task-09"
ip_tasks: ["5.6", "5.7", "5.8"]
execution_phase: "Phase 5"
status: "Pending"
domain: "Interactions, Memories, Body"
parallelizable: true
parallel_group: "Can run with Tasks 03–08 after Task 02 is complete"
---
# Task 09 — Other Domain Blocks

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Build 3 domain block partials: Logistics (Interactions), When Where Who (Memories), and Health Log (Body).

## Dependencies
- Task 02 (vault structure) — `Interactions/Templates/`, `Memories/Templates/`, `Body/Templates/` must exist
- **Task 07 should be complete first** — dot-notation test result governs field naming

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`

## Source Reference (v2)
- Logistics: `Information - Podcast Interview` or `Interactions - Business Meeting` (v2) for logistics section structure
- Health Log: `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/~Partial - Health Log.md` (migrate as-is)

## Output Files

### 5.6 — `Interactions/Templates/Logistics.md`
Context section for interaction cards: When / Where / Who / Recorded.
- **Source reference:** `Interactions - Business Meeting` (v2) logistics section

### 5.7 — `Memories/Templates/When Where Who.md`
Context anchor for memory cards: Date, Location, Who Was Present.

### 5.8 — `Body/Templates/Health Log.md`
Migrate `~Partial - Health Log.md` from v2.

> **⚠️ CRITICAL:** All `{{Flame-*}}` field names must be preserved exactly as-is. These field names correspond to a Google Forms / CSV import automation system. Do NOT rename, simplify, or normalize them.
>
> Use `directives="no-prompt"` or leave as plain field references for each Flame field — do NOT prompt the user for them.
>
> Convert v2 syntax (`<% ... %>`) to v3 equivalents only where a clean conversion exists. Preserve any unconvertible Templater code verbatim with `{{! FLAGGED: ... }}`.

## All Blocks Must Have
```yaml
---
z2k_template_type: block-template
---
```

## Acceptance Criteria
- All 3 files exist at the correct paths
- Each has `z2k_template_type: block-template`
- Health Log: all `{{Flame-*}}` field names preserved verbatim
- All 3 blocks instantiate without error

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All 8 domain block files exist | Includes these 3 |
| Each has `z2k_template_type: block-template` | YAML field present |
| Each block instantiates without error | Output created; no error log |
| Health Log: Flame fields preserved verbatim | All `{{Flame-*}}` field names appear unfilled in output (no-prompt) |
