---
task_id: "Task-16"
ip_tasks: ["6.7"]
execution_phase: "Phase 6"
status: "Pending"
domain: "Journals"
parallelizable: true
parallel_group: "Can run with Tasks 10, 11, 15, 17, 20, 21, 22"
---
# Task 16 — Journals Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 2 Journals domain templates from v2 to v3.

## Dependencies
- Task 02 — `Journals/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `Journals/.system-block.md` complete (includes `z2k_card_privacy: ".:Z2K/Privacy/Private/Journal"`)
- Task 07 — Root block templates complete

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## Source → Target Mapping

| Source (v2) | Target (v3) |
|---|---|
| `~Journals - Daily` | `Journals/Templates/Daily Journal.md` |
| `~Journals - Yearly Summaries` | `Journals/Templates/Yearly Summary.md` |

## Special Requirements

### Daily Journal — Required Sections
The Daily Journal template must include three "passing capture" sections. These absorb the retired Ideas domain — passing thoughts/memories/information that don't warrant a full card go here:
```markdown
## Passing Thoughts

## Passing Memories

## Passing Information
```

### Privacy
Privacy is set at the domain level (`Journals/.system-block.md`) — no per-template privacy override needed. Both templates inherit `z2k_card_privacy: ".:Z2K/Privacy/Private/Journal"` from the system-block.

## Required v3 YAML Fields
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```

## Acceptance Criteria
- Both files exist in `Journals/Templates/`
- `Daily Journal.md` includes `## Passing Thoughts`, `## Passing Memories`, `## Passing Information` sections
- Both have required v3 YAML fields

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All templates exist | Both paths in `Journals/Templates/` |
| Each has required YAML fields | Present |
| Each instantiates without error | Output created; no error log |
| System-block injection works | Output contains `z2k_creation_domain: ".:Z2K/Domain/Journals"` |
| Privacy inherited correctly | Output YAML contains `z2k_card_privacy: ".:Z2K/Privacy/Private/Journal"` |
