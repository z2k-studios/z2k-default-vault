---
task_id: "Task-13"
ip_tasks: ["6.4"]
execution_phase: "Phase 6"
status: "Pending"
domain: "Interactions"
parallelizable: true
parallel_group: "Can run with Tasks 12, 14, 18, 19, 20, 21, 22 (all after Task 09 is complete)"
---
# Task 13 — Interactions Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 12 Interactions domain templates from v2 to v3.

## Dependencies
- Task 02 — `Interactions/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `Interactions/.system-block.md` complete
- Task 07 — Root block templates complete
- Task 09 — `Interactions/Templates/Logistics.md` block complete (required by all interaction templates)

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## Source → Target Mapping

All targets in `Data/Vaults/z2k-default-vault/Interactions/Templates/`

### Generic + Business (3)
| Source (v2) | Target (v3) |
|---|---|
| `Interactions - ~Generic` | `Interactions (General).md` |
| `Interactions - Business Meeting` | `Business Meeting.md` |
| `Interactions - Email` | `Email.md` |

### Class (2)
| Source (v2) | Target (v3) |
|---|---|
| `Interactions - Class Lecture` | `Class Lecture.md` |
| `Interactions - Class Overview` | `Class Overview.md` |

### Conversation (1)
| Source (v2) | Target (v3) |
|---|---|
| `Interactions - Conversation` | `Conversation.md` |

### Personal (6) — personal templates
| Source (v2) | Target (v3) |
|---|---|
| `Interactions - Amateur Hour` | `Amateur Hour.md` |
| `Interactions - Conversation with Doug` | `Conversation with Doug.md` |
| `Interactions - Conversation with John Kashiwabara` | `Conversation with John Kashiwabara.md` |
| `Interactions - PoND Conversation with Bryn` | `PoND Conversation with Bryn.md` |
| `Interactions - YPO Event` | `YPO Event.md` |
| `Interactions - YPO Forum` | `YPO Forum.md` |

> **Note on v2 source filenames:** Verify exact filenames in `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/` — some names may vary slightly from what's listed here. Match by content if filename differs.

## Special Requirements

### All Templates — Include Logistics Block
Every interaction template must include `{{> "Logistics"}}` to pull in When/Where/Who/Recorded section.

### Personal Templates
- Add `z2k_template_author: "Geoff (z2k-gwp)"`
- **Preserve all hardcoded personal specifics** (names, group details, private tags) — these are intentionally personal
- Apply correct `z2k_card_privacy` values per Requirements §8 for each template

### Privacy Values (check Requirements §8 for exact values per template)
- YPO templates may have specific privacy settings
- Preserve any explicit privacy assignments from v2 source

## Required v3 YAML Fields (on every template)
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
# Personal templates only:
z2k_template_author: "Geoff (z2k-gwp)"
```

## Acceptance Criteria
- All 12 files exist in `Interactions/Templates/`
- All have required v3 YAML fields
- All include `{{> "Logistics"}}` block
- Personal templates have `z2k_template_author: "Geoff (z2k-gwp)"`
- Correct `z2k_card_privacy` values per Requirements §8
- Hardcoded personal specifics preserved verbatim

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All templates exist | All 12 paths in `Interactions/Templates/` |
| Each has required YAML fields | Present |
| Each instantiates without error | Output created; no error log |
| System-block injection works | Output contains `z2k_creation_domain: ".:Z2K/Domain/Interactions"` |
| Personal templates have correct `z2k_template_author` | `Geoff (z2k-gwp)` in personal template YAML |
| Privacy templates have correct `z2k_card_privacy` | Correct value per Requirements §8 |
