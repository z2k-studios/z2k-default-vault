---
task_id: "Task-02"
ip_tasks: ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"]
execution_phase: "Phase 1"
status: "Done"
domain: "Global"
parallelizable: false
---
# Task 02 — Vault Structure

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Create all missing domain folders and `Templates/` subfolders so subsequent phases have valid target locations.

## Dependencies
None — this task must run first. All other tasks (03–24) depend on it.

## References to Read First
- REF-K: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Template Folders/Template Organization.md`

## Pre-Check
Before creating, run `ls Data/Vaults/z2k-default-vault/` to confirm which domains and subfolders already exist. Only create what is missing.

## Output Files (create if missing)

### New domains (1.1, 1.2)
- `Data/Vaults/z2k-default-vault/Body/`
- `Data/Vaults/z2k-default-vault/Body/Templates/`
- `Data/Vaults/z2k-default-vault/AI/`
- `Data/Vaults/z2k-default-vault/AI/Templates/`

### New subfolder in existing domain (1.3)
- `Data/Vaults/z2k-default-vault/System/Templates/`

### New project subfolder (1.4)
- `Data/Vaults/z2k-default-vault/Projects/My Writings/`
- `Data/Vaults/z2k-default-vault/Projects/My Writings/Templates/`

### Root Templates folder (1.5)
- `Data/Vaults/z2k-default-vault/Templates/`

### Audit existing domain Templates/ subfolders (1.6)
For each of these 10 existing domains, confirm `Templates/` subfolder exists; create if missing:
- `Beliefs/Templates/`
- `Entities/Templates/`
- `Information/Templates/`
- `Interactions/Templates/`
- `Journals/Templates/`
- `Locations/Templates/`
- `Logs/Templates/`
- `Memories/Templates/`
- `Projects/Templates/`
- `Thoughts/Templates/`

## Acceptance Criteria
- `ls Data/Vaults/z2k-default-vault/` shows all 13 domain folders: Beliefs, Entities, Information, Interactions, Journals, Locations, Logs, Memories, Projects, Thoughts, Body, AI, System
- `Templates/` exists at vault root
- All 13 domains have a `Templates/` subfolder
- `Projects/My Writings/Templates/` exists

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All 13 domain folders exist | All domain roots exist |
| All domain `Templates/` subfolders exist | 13 × `Templates/` exist |
| `Templates/` root folder exists | `Templates/` at vault root |
| `Projects/My Writings/Templates/` exists | Path exists |
| `Body/`, `AI/`, `System/Templates/` exist | All 3 paths exist |
