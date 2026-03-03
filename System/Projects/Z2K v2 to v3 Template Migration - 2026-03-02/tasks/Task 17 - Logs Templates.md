---
task_id: "Task-17"
ip_tasks: ["6.8"]
execution_phase: "Phase 6"
status: "Done"
domain: "Logs"
parallelizable: true
parallel_group: "Can run with Tasks 10, 11, 15, 16, 20, 21, 22"
---
# Task 17 — Logs Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 6 Logs domain templates from v2 to v3.

## Dependencies
- Task 02 — `Logs/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `Logs/.system-block.md` complete (includes `z2k_card_privacy: ".:Z2K/Privacy/Private/Log"`)
- Task 07 — Root block templates complete

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## Source → Target Mapping

| Source (v2) | Target (v3) |
|---|---|
| `~Logs - Daily` | `Logs/Templates/Daily Log.md` |
| `~Logs - Monthly` | `Logs/Templates/Monthly Log.md` |
| `~Logs - Quarterly Focus List` | `Logs/Templates/Quarterly Focus List.md` |
| `~Logs - Weekly` | `Logs/Templates/Weekly Log.md` |
| `~Logs - Yearly` | `Logs/Templates/Yearly Log.md` |
| `~Logs - Yearly Strategic Plan` | `Logs/Templates/Yearly Strategic Plan.md` |

## Special Requirements

### Daily Log — Preserve Flame Fields
> **⚠️ CRITICAL:** The Daily Log template contains `{{Flame-*}}` field references. These field names correspond to a Google Forms / CSV import automation system (z2k-sheet-importer). **Do NOT rename, simplify, prompt, or modify any Flame field names.**
>
> - Use `directives="no-prompt"` or plain field references for each Flame field
> - Do NOT add `{{fieldInfo}}` declarations for Flame fields
> - Preserve the exact field names verbatim

### Privacy
Privacy is set at the domain level (`Logs/.system-block.md`) — no per-template override needed. All templates inherit `z2k_card_privacy: ".:Z2K/Privacy/Private/Log"` from the system-block.

## Required v3 YAML Fields
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```

## Acceptance Criteria
- All 6 files exist in `Logs/Templates/`
- All have required v3 YAML fields
- `Daily Log.md` has all `{{Flame-*}}` field names preserved verbatim; no prompts for Flame fields

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All templates exist | All 6 paths in `Logs/Templates/` |
| Each has required YAML fields | Present |
| Each instantiates without error | Output created; no error log |
| System-block injection works | Output contains `z2k_creation_domain: ".:Z2K/Domain/Logs"` |
| Privacy inherited correctly | Output YAML contains `z2k_card_privacy: ".:Z2K/Privacy/Private/Log"` |
