---
task_id: "Task-12"
ip_tasks: ["6.3"]
execution_phase: "Phase 6"
status: "Done"
domain: "Information"
parallelizable: true
parallel_group: "Can run with Tasks 13, 14, 18, 19, 20, 21, 22 (all after Task 08 is complete)"
---
# Task 12 — Information Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 21 Information domain templates from v2 to v3.

## Dependencies
- Task 02 — `Information/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `Information/.system-block.md` complete
- Task 07 — Root block templates complete
- Task 08 — Information domain blocks complete (Podcast Interview Content block required)

## ⚠️ PREREQUISITE: Read REF-I Before Executing
Before writing any Information templates, read REF-I to confirm canonical `z2k_card_source_type` values.
> REF-I: `Docs/z2k-design-notes/Z2K System - Design Notes/Z2K Data Architecture/Z2K Metadata/Z2K Metadata Specification - Version 3.0.md`

The source type values in Requirements §9 are placeholders. The canonical values from the Metadata Specification v3.0 take precedence.

Open issue **ST-001**: document the source type taxonomy decisions made here for future reference.

## References to Read First
- **REF-I (required, see above)**
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`
- REF-J: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatString.md` (as needed)

## Source → Target Mapping

All targets in `Data/Vaults/z2k-default-vault/Information/Templates/`

### Generic + Academic (5)
| Source (v2) | Target (v3) |
|---|---|
| `Information - ~Generic` | `Information (General).md` |
| `Information - Academic Paper` | `Academic Paper.md` |
| `Information - Blinkist` | `Blinkist.md` |
| `Information - Book` | `Book.md` |
| `Information - Kindle Notes` | `Kindle Notes.md` |

### Lecture / Conference / Interview (3)
| Source (v2) | Target (v3) |
|---|---|
| `Information - Conference` | `Conference.md` |
| `Information - Lecture` | `Lecture.md` |
| `Information - Interview` | `Interview.md` |

### Web + Wikipedia (2)
| Source (v2) | Target (v3) |
|---|---|
| `Information - Web Article` | `Web Article.md` |
| `Information - Wikipedia Entry` | `Wikipedia Entry.md` |

### Quotation / Email (3)
| Source (v2) | Target (v3) |
|---|---|
| `Information - Quotation` | `Quotation.md` |
| `Information - Quote a Source` | `Quote a Source.md` |
| `Information - Quote an Email` | `Quote an Email.md` |

### Ontology (1)
| Source (v2) | Target (v3) |
|---|---|
| `Information - Ontology` | `Ontology.md` |

### Podcast — Generic (1)
| Source (v2) | Target (v3) | Note |
|---|---|---|
| `Information - Podcast Interview` | `Podcast Interview.md` | Uses `{{> "Podcast Interview Content"}}` block |

### Podcast — Host-Specific (6) — NEW (no v2 source)
Build from scratch. Each template:
1. Sets fixed fields: `{{fieldInfo Host value="<HostName"}}`, `{{fieldInfo ShowName value="<ShowName>"}}`
2. Sets default tags for the show
3. Includes: `{{> "Podcast Interview Content"}}`

| Target (v3) | Host | Show Name |
|---|---|---|
| `Podcast Interview - Adam Grant.md` | Adam Grant | Think Again / WorkLife |
| `Podcast Interview - Dwarkesh Patel.md` | Dwarkesh Patel | Dwarkesh Podcast |
| `Podcast Interview - Huberman Lab.md` | Andrew Huberman | Huberman Lab |
| `Podcast Interview - Knowledge Project.md` | Shane Parrish | The Knowledge Project |
| `Podcast Interview - Lex Fridman.md` | Lex Fridman | Lex Fridman Podcast |
| `Podcast Interview - Tim Ferriss.md` | Tim Ferriss | The Tim Ferriss Show |

## Conversion Approach
See Task 10 for full conversion steps. Note: verify source type values against REF-I for each template.

## Required v3 YAML Fields (on every template)
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```

## Acceptance Criteria
- All 21 files exist in `Information/Templates/`
- All have required v3 YAML fields
- Source type values confirmed against REF-I (not placeholder values)
- Podcast templates include `{{> "Podcast Interview Content"}}`
- Host-specific templates preset Host and ShowName via `{{fieldInfo ... value="..."}}`
- ST-001 resolved and documented

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All templates exist | All 21 paths in `Information/Templates/` |
| Each has required YAML fields | `z2k_template_type`, `z2k_template_version`, `z2k_template_suggested_title` present |
| Each instantiates without error | Output created; no error log |
| System-block YAML injection works | Output YAML contains `z2k_creation_domain: ".:Z2K/Domain/Information"` |
