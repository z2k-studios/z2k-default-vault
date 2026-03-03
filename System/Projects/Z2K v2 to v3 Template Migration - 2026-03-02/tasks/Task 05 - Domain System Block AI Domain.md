---
task_id: "Task-05"
ip_tasks: ["3.11"]
execution_phase: "Phase 3"
status: "Pending"
domain: "AI"
parallelizable: true
parallel_group: "Can run with Tasks 03, 04, 06, 07, 08, 09 after Task 02 is complete"
---
# Task 05 — Domain System Block: AI Domain

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Write `AI/.system-block.md` with domain identity and an AI authorship/perspective field.

## Dependencies
- Task 02 (vault structure) must be complete — `AI/` folder must exist

## References to Read First
- REF-C: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Intro to System Blocks.md`
- REF-D: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Using System Blocks and fieldInfo.md`

## Target File
`Data/Vaults/z2k-default-vault/AI/.system-block.md`

## Open Issue — AI-PERSP (Design Decision Required Before Executing)

The field name/structure for AI authorship perspective is not yet designed. Before writing this file, decide:

**Candidates:**
- A field `z2k_creation_perspective: "AI"` (simplest; signals AI-originated content)
- A comment `{{! AI-authored content — perspective: AI agent }}` (metadata in template body only, no YAML field)
- A custom field `z2k_ai_author: "Claude"` (specific to AI tool used)

**Decision factors:**
- Does the Z2K Metadata Specification v3.0 define a perspective or AI-authorship field? (Check REF-I if available)
- Is this field needed by any downstream queries or templates?
- Should it be standardized across ZSv3, or specific to this vault?

**Action:** Make a design decision, document the rationale below, then write the file. If the decision requires broader ZSv3 input, file it as an open item in `Post Project/ZSv3 Project/` and proceed with the simplest reasonable choice.

### AI-PERSP Decision (to be filled in when executing)
> Decision made: ___
> Rationale: ___
> Field chosen: ___

## Minimum Content
```yaml
z2k_creation_domain: ".:Z2K/Domain/AI"
<ai_authorship_field>: <value>
```

## Acceptance Criteria
- `AI/.system-block.md` exists
- Has `z2k_creation_domain: ".:Z2K/Domain/AI"`
- Has an AI authorship/perspective field (design decision above resolved)
- AI-PERSP design decision documented in this task file

## Note on Phase 6
Task 6.13 (AI domain templates) is no-action — no document templates are built for the AI domain in this project. This system-block is the only AI domain artifact.

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All 13 domain `.system-block.md` files exist | Includes this file |
| Each has correct `z2k_creation_domain` value | `.:Z2K/Domain/AI` |
| (AI-PERSP) AI authorship field | Add test row when design is finalized — see Testing Plan §Coverage Completeness Check |
