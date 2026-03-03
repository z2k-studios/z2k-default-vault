---
task_id: "Task-04"
ip_tasks: ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10", "3.12"]
execution_phase: "Phase 3"
status: "Done"
domain: "All except AI and Projects"
parallelizable: true
parallel_group: "Can run with Tasks 03, 05, 06, 07, 08, 09 after Task 02 is complete"
---
# Task 04 — Domain System Blocks: Core Domains

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Write `.system-block.md` for all 11 standard domains (excludes AI and Projects, which have open issues and are handled in Tasks 05 and 06).

## Dependencies
- Task 02 (vault structure) must be complete — domain folders must exist

## References to Read First
- REF-C: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Intro to System Blocks.md`
- REF-D: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Using System Blocks and fieldInfo.md`

## Output Files — Create Each

Place each file at `Data/Vaults/z2k-default-vault/<Domain>/.system-block.md`

### Ratings Domains (Information, Thoughts, Beliefs, Memories) — 3.1–3.4
Each has: `z2k_creation_domain` + three ratings fields.

```yaml
z2k_creation_domain: ".:Z2K/Domain/<DomainName>"
z2k_rating_depth:
z2k_rating_surprisal:
z2k_rating_passion:
```

| Domain | IP Task | Target Path |
|---|---|---|
| Information | 3.1 | `Information/.system-block.md` |
| Thoughts | 3.2 | `Thoughts/.system-block.md` |
| Beliefs | 3.3 | `Beliefs/.system-block.md` |
| Memories | 3.4 | `Memories/.system-block.md` |

### Privacy Domains (Journals, Logs) — 3.6, 3.7

```yaml
# Journals
z2k_creation_domain: ".:Z2K/Domain/Journals"
z2k_card_privacy: ".:Z2K/Privacy/Private/Journal"

# Logs
z2k_creation_domain: ".:Z2K/Domain/Logs"
z2k_card_privacy: ".:Z2K/Privacy/Private/Log"
```

### Domain-Identity-Only Domains (Interactions, Locations, Entities, Body, System) — 3.5, 3.8, 3.9, 3.10, 3.12

Each contains only:
```yaml
z2k_creation_domain: ".:Z2K/Domain/<DomainName>"
```

| Domain | IP Task | Target Path |
|---|---|---|
| Interactions | 3.5 | `Interactions/.system-block.md` |
| Locations | 3.8 | `Locations/.system-block.md` |
| Entities | 3.9 | `Entities/.system-block.md` |
| Body | 3.10 | `Body/.system-block.md` |
| System | 3.12 | `System/.system-block.md` |

## Domain Name Values
Use exactly these canonical strings in `z2k_creation_domain`:
`Beliefs`, `Body`, `Entities`, `Information`, `Interactions`, `Journals`, `Locations`, `Logs`, `Memories`, `System`, `Thoughts`
Format: `".:Z2K/Domain/<Name>"`

## Acceptance Criteria
- All 11 `.system-block.md` files exist at the correct paths
- Each has `z2k_creation_domain` with the correct canonical value
- Ratings domains (Information, Thoughts, Beliefs, Memories) have `z2k_rating_depth`, `z2k_rating_surprisal`, `z2k_rating_passion`
- Journals has `z2k_card_privacy: ".:Z2K/Privacy/Private/Journal"`
- Logs has `z2k_card_privacy: ".:Z2K/Privacy/Private/Log"`
- No extra fields present (these are minimal system-blocks)

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All 13 domain `.system-block.md` files exist | All 13 paths exist (includes AI + Projects from Tasks 05/06) |
| Each has correct `z2k_creation_domain` value | YAML field matches expected string per domain |
| Ratings domains have ratings fields | All 3 rating fields present in Information, Thoughts, Beliefs, Memories |
| Journals has `z2k_card_privacy` | `.:Z2K/Privacy/Private/Journal` |
| Logs has `z2k_card_privacy` | `.:Z2K/Privacy/Private/Log` |
