---
task_id: "Task-06"
ip_tasks: ["3.13"]
execution_phase: "Phase 3"
status: "Pending"
domain: "Projects"
parallelizable: true
parallel_group: "Can run with Tasks 03, 04, 05, 07, 08, 09 after Task 02 is complete"
---
# Task 06 — Domain System Block: Projects

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Write `Projects/.system-block.md` and implement a System Block Stop strategy so that project subfolder cards do not inherit z2k_* fields from parent system-blocks.

## Dependencies
- Task 02 (vault structure) must be complete — `Projects/` folder must exist
- **Read REF-E before executing** (required — see open issue below)

## References to Read First (REQUIRED)
- **REF-E (required):** `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/System Block Stops.md`
- REF-C: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Intro to System Blocks.md`
- REF-D: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Using System Blocks and fieldInfo.md`

## Output Files
- `Data/Vaults/z2k-default-vault/Projects/.system-block.md`
- System Block Stop file(s) in project subfolders (strategy determined after reading REF-E)

## Open Issue — DSB-005 (Must Resolve Before Executing)

**Context:** The Projects domain contains many project subfolders (one per project). Each project subfolder should have a different YAML structure — no `z2k_*` fields injected from the parent system-block. The goal is to use System Block Stops to suppress the Projects domain system-block in subfolders.

**Known constraint from Q&A:** "System Block Stop only works for subfolders — but that is fine here. You can assume the Projects folder will have many subfolders for projects. You want system block suppression to occur for each of them."

**Question to resolve by reading REF-E:** Can a single System Block Stop placed at `Projects/` suppress system-block injection for all `Projects/<subfolder>/` paths? Or does each project subfolder need its own stop file?

**Action:**
1. Read REF-E
2. Determine the correct stop file placement
3. Implement the stop strategy
4. If complete suppression is NOT achievable, document the limitation and specify what project templates must do to override YAML (relevant to Task 18)
5. Document findings in this task file under "DSB-005 Resolution"

### DSB-005 Resolution (to be filled in when executing)
> Strategy chosen: ___
> Stop file location(s): ___
> Limitation (if any): ___
> Impact on Task 18: ___

## Projects System-Block Content
```yaml
z2k_creation_domain: ".:Z2K/Domain/Projects"
```
(Minimal — project subfolder cards will use project-specific YAML, not z2k_* fields)

## Acceptance Criteria
- `Projects/.system-block.md` exists with `z2k_creation_domain: ".:Z2K/Domain/Projects"`
- System Block Stop strategy implemented per REF-E findings
- DSB-005 resolution documented in this task file
- Findings communicated to Task 18 (Projects Templates) regarding any YAML override requirements

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All 13 domain `.system-block.md` files exist | Includes this file |
| Each has correct `z2k_creation_domain` value | `.:Z2K/Domain/Projects` |
| (DSB-005) System Block Stop behavior | Manual Obsidian validation required — see Testing Plan §Coverage Completeness Check |
