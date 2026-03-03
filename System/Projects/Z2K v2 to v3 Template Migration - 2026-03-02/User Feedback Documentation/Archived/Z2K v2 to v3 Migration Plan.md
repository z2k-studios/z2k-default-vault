---
title: Z2K v2 to v3 Migration Plan
created: 2026-03-01
status: completed
completed: 2026-03-02
---

# Z2K v2 to v3 Migration Plan

> [!NOTE] Superseded
> This document has been superseded by the formal project documents created during the Z2K Template Library v3 Migration project. It served as the initial planning artifact and has been archived for historical reference.
>
> **Project Documents (source of truth):**
> - Statement of Work: `Z2K Template Library v3 Migration - Statement of Work.md`
> - Project Requirements: `Z2K Template Library v3 Migration - Project Requirements.md`
> - Implementation Plan: `Z2K Template Library v3 Migration - Implementation Plan.md`
> - Testing Plan: `Z2K Template Library v3 Migration - Testing Plan.md`
> - Task List and Progress Tracker: `Z2K Template Library v3 Migration - Task List and Progress Tracker.md`
>
> All located in: `Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/`

This document is the master reference for migrating the Z2K template library from v2 (Obsidian Templater) to v3 (Z2K Templates Plugin). It is designed to fully reconstruct context in a new chat session — read this file first, then follow the "Session Startup" instructions below.

---

## Session Startup Instructions (for new chat sessions)

1. Load `/wf z2k-user/init` and `/wf z2k-user/template-builder` to establish system context.
2. Read **this file** completely.
3. Read the Q&A documents (see References) to get the latest answered/unanswered questions.
4. Check the Q&A docs for any ==highlighted== clarification questions that still need answers.
5. Delegate heavy reference reading to sub-agents (see "Sub-Agent vs. Root Agent" section below).
6. Resume implementation from the task list at the bottom of this file.

---

## What We Are Doing

Migrating the Z2K template library from v2 to v3 inside `Data/Vaults/z2k-default-vault`. This includes:

1. Updating top-level domain folders to match the current domain list
2. Rewriting all `.system-block.md` files for v3
3. Migrating all old templates (read-only source) into the new per-domain Templates/ structure
4. Building new blocks for shared content patterns
5. Adding full `{{fieldInfo}}` prompting, `z2k_template_suggested_title`, author/version metadata
6. Generating AI recommendations document in the AI domain folder
7. Writing a Tags Taxonomy placeholder in System docs

---

## Source and Target

- **Old templates (read-only):** `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/`
- **Target vault:** `Data/Vaults/z2k-default-vault/`
- **Do NOT modify source templates**

---

## API Translation (v2 → v3)

| v2 | v3 |
|---|---|
| `{{creatorLink}}` | `{{wikilink creator}}` |
| `{{todayLink}}` | `{{wikilink today}}` |
| `{{~prompt-info FieldName "type" "prompt" "default"}}` | `{{fieldInfo FieldName "prompt" type="text" fallback="default"}}` |
| `z2k_metadata_version: 2.1` | `z2k_metadata_version: 3.00` |
| `z2k_metadata_details: "Z2K Card; https://z2k.dev"` | `z2k_metadata_copyright: "Z2K Metadata structure is © 2025 Z2K Studios, LLC"` |
| `z2k_creation_database: ".:Z2K/Database/X"` | `z2k_creation_domain:` (hard-coded per domain system-block) |
| `z2k_creation_template: "[[TemplateName]]"` | `z2k_creation_template: "{{wikilink templateName}}"` |
| `z2k_card_activation: ".:Z2K/Inactive"` | **Removed** |
| `z2k_card_status: ".:Z2K/Status/Template"` | **Removed** (covered by `z2k_template_type`) |
| `z2k_card_type: ".:Z2K/CardType/Atom"` | **Removed** |
| `%% Title: ... %%` | `z2k_template_suggested_title: "..."` in YAML |
| `%% ... %%` comments | `{{! ... }}` template comments |
| `G:` personal prefix | `> [!me]` callout block (see open question on this) |

---

## Domain Structure (v3)

### Vault Folder Changes Required

The following folders are **missing** from `Data/Vaults/z2k-default-vault/` and must be created with `Templates/` subfolders and `.system-block.md` files:
- `Body/` + `Body/Templates/`
- `AI/` + `AI/Templates/`
- `System/` ✅ (created)

Existing domains already present: Beliefs, Entities, Information, Interactions, Journals, Locations, Logs, Memories, Projects, Thoughts

### My Writings Subfolder
Create `Projects/My Writings/` + `Projects/My Writings/Templates/` for Syntheses-derived templates.

---

## Domain Mapping — Old Templates → New Locations

| Old Template | New Location | Notes |
|---|---|---|
| `Beliefs - ~Generic` | `Beliefs/Templates/Template - ~Generic.md` | |
| `Body - ~Generic` | `Body/Templates/Template - ~Generic.md` | |
| `Information - Academic Paper` | `Information/Templates/Template - Academic Paper.md` | |
| `Information - Adam Grant Interview` | `Information/Templates/Template - Podcast Interview - Adam Grant.md` | Option 3 architecture (see Q4) |
| `Information - Blinkist` | `Information/Templates/Template - Blinkist.md` | |
| `Information - Book` | `Information/Templates/Template - Book.md` | |
| `Information - ChatGPT` | `AI/Templates/Template - AI Interaction - ChatGPT.md` | Moved to AI domain |
| `Information - Conference` | `Information/Templates/Template - Conference.md` | |
| `Information - Dwarkesh Interview` | `Information/Templates/Template - Podcast Interview - Dwarkesh Patel.md` | Option 3 |
| `Information - Huberman Lab Podcast` | `Information/Templates/Template - Podcast Interview - Huberman Lab.md` | Option 3 |
| `Information - Interview` | `Information/Templates/Template - Interview.md` | |
| `Information - Kindle Notes` | `Information/Templates/Template - Kindle Notes.md` | |
| `Information - Knowledge Project Interview` | `Information/Templates/Template - Podcast Interview - Knowledge Project.md` | Option 3 |
| `Information - Lecture` | `Information/Templates/Template - Lecture.md` | |
| `Information - Lex Fridman Interview` | `Information/Templates/Template - Podcast Interview - Lex Fridman.md` | Option 3 |
| `Information - Ontology` | `Information/Templates/Template - Ontology.md` | |
| `Information - Podcast Interview` | `Information/Templates/Template - Podcast Interview.md` | Generic document template |
| `Information - Quotation` | `Information/Templates/Template - Quotation.md` | Standalone quote card |
| `Information - Quote a Source` | `Information/Templates/Template - Quote a Source.md` | |
| `Information - Quote an Email` | `Information/Templates/Template - Quote an Email.md` | One email-quote template (per Q8 decision) |
| `Information - Tim Ferriss Interview` | `Information/Templates/Template - Podcast Interview - Tim Ferriss.md` | Option 3 |
| `Information - Web Article` | `Information/Templates/Template - Web Article.md` | |
| `Information - Wikipedia Entry` | `Information/Templates/Template - Wikipedia Entry.md` | |
| `Information - ~Generic` | `Information/Templates/Template - ~Generic.md` | |
| `Interactions - Amateur Hour` | `Interactions/Templates/Template - Amateur Hour.md` | Personal — migrate as-is |
| `Interactions - Business Meeting` | `Interactions/Templates/Template - Business Meeting.md` | |
| `Interactions - Class Lecture` | `Interactions/Templates/Template - Class Lecture.md` | |
| `Interactions - Class Overview` | `Interactions/Templates/Template - Class Overview.md` | |
| `Interactions - Conversation` | `Interactions/Templates/Template - Conversation.md` | |
| `Interactions - Conversation with John Kashiwabara` | `Interactions/Templates/Template - Conversation with John Kashiwabara.md` | Personal — migrate as-is |
| `Interactions - Doug` | `Interactions/Templates/Template - Conversation with Doug.md` | Personal — migrate as-is |
| `Interactions - Email` | `Interactions/Templates/Template - Email.md` | |
| `Interactions - PoND Conversation with Bryn` | `Interactions/Templates/Template - PoND Conversation with Bryn.md` | Personal — migrate as-is |
| `Interactions - YPO Event` | `Interactions/Templates/Template - YPO Event.md` | Personal — migrate as-is |
| `Interactions - YPO Forum` | `Interactions/Templates/Template - YPO Forum.md` | Personal — migrate as-is |
| `Interactions - ~Generic` | `Interactions/Templates/Template - ~Generic.md` | |
| `Locations - ~Generic` | `Locations/Templates/Template - ~Generic.md` | |
| `Locations.template` | Review — likely same as ~Generic | |
| `Memories - Family Vacation Trip` | `Memories/Templates/Template - Family Vacation Trip.md` | |
| `Memories - Ontology` | `Memories/Templates/Template - Ontology.md` | |
| `Memories - PCT Trail Day` | `Memories/Templates/Template - PCT Trail Day.md` | Personal — migrate as-is |
| `Memories - Quote an Email` | **DROP** — absorbed by Information domain email template | Per Q8 |
| `Memories - Solo Trip Summary` | `Memories/Templates/Template - Solo Trip Summary.md` | |
| `Memories - ~Generic` | `Memories/Templates/Template - ~Generic.md` | |
| `Project - Code Poetry - Poem` | `Projects/My Writings/Templates/Template - Code Poem.md` | Personal |
| `Syntheses - ~Generic` | `Projects/My Writings/Templates/My Writings (Default).md` | Per Q2 decision |
| `Syntheses - Extended Journal Writing` | `Projects/My Writings/Templates/Template - Personal Writing.md` | Renamed |
| `Syntheses - Quote an Email` | **DELETE** | Per Q2 decision |
| `Syntheses - Treatise` | `Projects/My Writings/Templates/Template - Treatise.md` | |
| `Thoughts - Book - Quote` | `Thoughts/Templates/Template - Book Quote.md` | |
| `Thoughts - Concept - Book` | `Thoughts/Templates/Template - Book Concept.md` | |
| `Thoughts - General - Quote` | `Thoughts/Templates/Template - General Quote.md` | |
| `Thoughts - Ontology` | `Thoughts/Templates/Template - Ontology.md` | |
| `Thoughts - Quote a Source` | `Thoughts/Templates/Template - Quote a Source.md` | |
| `Thoughts - Quote an Email` | **DROP** — use Information domain email template | Per Q8 |
| `Thoughts - Resolutions` | `Thoughts/Templates/Template - Resolutions.md` | |
| `Thoughts - ~Generic` | `Thoughts/Templates/Template - ~Generic.md` | |
| `~Generic Card Template` | Root `Templates/Template - ~Generic Card.md` | Cross-domain generic |
| `~Journals - Daily` | `Journals/Templates/Template - Daily Journal.md` | |
| `~Journals - Yearly Summaries` | `Journals/Templates/Template - Yearly Summary.md` | |
| `~Logs - Daily` | `Logs/Templates/Template - Daily Log.md` | Migrate Flame fields as-is |
| `~Logs - Monthly` | `Logs/Templates/Template - Monthly Log.md` | |
| `~Logs - Quarterly Focus List` | `Logs/Templates/Template - Quarterly Focus List.md` | |
| `~Logs - Weekly` | `Logs/Templates/Template - Weekly Log.md` | |
| `~Logs - Yearly` | `Logs/Templates/Template - Yearly Log.md` | |
| `~Logs - Yearly Strategic Plan` | `Logs/Templates/Template - Yearly Strategic Plan.md` | |
| `~System - ~Generic` | `System/Templates/Template - ~Generic.md` | |
| `Ideas - *` | **DROP ALL** — Ideas domain retired | Passing thoughts → Daily Journal |
| `~System - Testing` | **DROP** — testing artifact, not a real template | |
| `~Partial - Health Log` | `Body/Templates/Block - Health Log.block` | Moved to Body as block |
| `~Partial - Card Fabric - *` | `Templates/Block - Card Fabric.block` (root) | Optional block |
| `~Partial - YAML Metadata - *` | `Templates/Block - Extended YAML.block` (root) | Extended YAML opt-in block |

**New templates to build from scratch:**
- `Entities/Templates/Template - ~Generic Contact.md` (start here; full CRM in separate session)
- `Projects/Templates/Template - ~Generic Project.md`
- `Projects/Templates/Template - Active Project.md`
- `Projects/Templates/Template - Completed Project.md`

---

## Architectural Decisions Made

### YAML Schema
- **`z2k_card_type`** — REMOVED. Self-evident from folder location.
- **`z2k_card_source_type`** — ⚠️ PENDING CORRECTION (user flagged their answer was wrong; awaiting revised answer — see Q8 in Architecture Q&A doc)
- **`z2k_card_activation`** — REMOVED.
- **`z2k_card_status`** in templates — REMOVED (use `z2k_template_type` instead).
- **`z2k_card_build_state`** — REMOVED from root system-block per user clarification.
- **`z2k_creation_domain`** — hard-coded per domain in each domain's `.system-block.md`. Format: `.:Z2K/Domain/DomainName`
- **`z2k_creation_library_version`** — new field, added to root system-block. Captures library version at time of card creation. ⚠️ Confirm field name and initial version number (proposed: `3.0.0`).
- **Ratings fields** (`z2k_rating_depth`, `z2k_rating_surprisal`, `z2k_rating_passion`) — kept, but in domain-level system-blocks only for: Information, Thoughts, Memories, Beliefs.
- **Privacy field** (`z2k_card_privacy`) — kept; hard-coded per template. ⚠️ Need complete privacy tier list (see Q6 clarification in Architecture Q&A).
- **Inline `::` property syntax** — preserve in card bodies; candidates for YAML mirroring per `Storing Field Values in YAML.md` pattern.
- **Maximalist/minimalist schema** — minimalist fields in system-blocks; extended YAML as opt-in root-level block template.

### Blocks and Partials
- **Card Fabric** — retired from templates body; exists as an optional root-level block template (`Block - Card Fabric.block`)
- **Block for Card Fabric** — explicit opt-in partial (not system-block injection)
- **Podcast host templates** — Option 3: block template for content + document templates preset values per show (⚠️ see Q4 clarification in Migration Q&A about block vs document template architecture)
- **Citation / Quotation blocks** — at root Templates/ level; use `Content.Author`, `Content.Title` dot-notation fields (speculative — may need to fall back to `ContentAuthor`, `ContentTitle` if dot-notation unsupported for prompted fields)
- **Health Log** — `Body/Templates/Block - Health Log.block`
- **Ontology** — both a root-level generic AND domain-specific variants

### Perspective / Authorship
- **`[!me]` callout** — the standard perspective block for vault-owner voice. ⚠️ Open question: should `{{me}}` resolve to `"me"` (fixed callout type, portable) or `"Geoff"` (name-specific callout type)? See Q5 in Migration Q&A.
- **`Me:` inline prefix** — retained as informal shorthand for single-line inline annotations
- A root-level `Block - Perspective - Me.block` should be created

### Template Metadata
- **Version numbering** — all migrated templates start at `v3.0.0 2026-03-01`
- **`z2k_template_suggested_title`** — included in all templates; use existing v2 `%% Title: %%` comments as source
- **`z2k_template_author`** — "Z2K Studios" for official library templates; user name for personal templates
- **`z2k_template_version`** — per-template version number

### Domains
- **Ideas** — RETIRED. No templates. Passing captures → Daily Journal `## Passing Thoughts`.
- **Syntheses** — RETIRED. Content mapped to Projects/My Writings and Journals (see domain mapping table).
- **Projects/My Writings** — new subfolder for formal writing templates
- **AI domain** — folder + system-block only for now; no templates yet
- **System domain** — folder + system-block; migrate existing System templates
- **Body domain** — folder + system-block + Health Log block
- **Entities** — start with `Template - ~Generic Contact.md` only; full CRM deferred

---

## Open Questions Requiring User Input Before Implementation

1. **`z2k_card_source_type`** — user flagged their Q8 answer was wrong. Awaiting correction. Do NOT implement Q8 until answered.
2. **Privacy tier list** — complete list needed before hard-coding privacy values in templates (see ==highlighted== note in Architecture Q&A, Q6).
3. **`z2k_creation_library_version`** — confirm field name and initial version number (Architecture Q&A, Q19).
4. **Projects system-block "prevention"** — clarify mechanism (Architecture Q&A, Q12 clarification).
5. **`[!me]` vs `[!Geoff]`** — confirm which callout type to use (Migration Q&A, Q5 clarification).
6. **Podcast block architecture** — confirm Option 3 block template design (Migration Q&A, Q4 clarification).

---

## Reference Documents

### Q&A Documents (read fully at session start)
- `Docs/z2k-design-notes/Z2K System - Design Notes/Design Decisions/Template Migration - v2 to v3 - Open Questions.md`
- `Docs/z2k-design-notes/Z2K System - Design Notes/Design Decisions/Template Library - System Architecture - Open Questions.md`

### Plugin Documentation (delegate to sub-agent for deep reading)
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md` — **ROOT AGENT** must read at session start (compact reference)
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/best-practices/best-practices.md` — sub-agent or reference as needed
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Template Folders/Template Organization.md` — sub-agent or reference as needed
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Template Folders/Template Folder Hierarchies.md` — already read; key: hierarchical template discovery
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Intro to System Blocks.md` — already read
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Using System Blocks and fieldInfo.md` — already read; key: unused fieldInfo = no prompt
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/Storing Field Values in YAML.md` — already read; key pattern for mirroring fields into YAML
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md` — already read
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatString.md` — already read
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatStringBulletize.md` — already read

### System Design Documents (sub-agent as needed)
- `Docs/z2k-system-docs/4 - Z2K Reference Docs/4a - Data Types/2 - Z2K Domains/Z2K Domains.md` — already read; canonical domain list
- `Docs/z2k-design-notes/Z2K Plugins - Design Notes/Z2K Core Plugin/Z2K Core - Design Spec.md` — already read
- `Docs/z2k-design-notes/Z2K Plugins - Design Notes/Z2K Core Plugin/Design Decisions/A method for determining author.md` — already read; key: default perspective per domain
- `Docs/z2k-design-notes/Z2K Plugins - Design Notes/Z2K Core Plugin/Features/Z2K Tags - Author Tag.md` — already read; key: `[!me]` callout type

### Files to Read Before Specific Tasks (sub-agent)
- `Docs/z2k-system-docs/4 - Z2K Reference Docs/4b - Data Formats/Z2K Card Metadata - YAML.md` — read before building system-blocks (user has this open in IDE)
- `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/Storing Field Values in YAML.md` — read before building block templates that depend on YAML field storage

---

## Implementation Task List

Tasks are ordered by dependency. Do not start a task until its prerequisites are complete.

### Phase 0 — Resolve Open Questions
- [ ] Get corrected answer on `z2k_card_source_type` (Q8)
- [ ] Get complete privacy tier list (Q6)
- [ ] Confirm library version field name and initial version (Q19)
- [ ] Confirm Projects system-block "prevention" intent (Q12)
- [ ] Confirm `[!me]` vs `[!Geoff]` callout type (Q5)
- [ ] Confirm podcast block architecture (Q4)

### Phase 1 — Vault Structure
- [ ] Create `Body/`, `Body/Templates/` folders
- [ ] Create `AI/`, `AI/Templates/` folders
- [ ] Create `System/Templates/` folder
- [ ] Create `Projects/My Writings/`, `Projects/My Writings/Templates/` folders
- [ ] Create `Templates/` at vault root (for cross-domain blocks and generic templates)
- [ ] Add `Templates/` subfolders to any existing domains missing them

### Phase 2 — Root System Block
- [ ] Read `Docs/z2k-system-docs/4 - Z2K Reference Docs/4b - Data Formats/Z2K Card Metadata - YAML.md` first
- [ ] Rewrite `Data/Vaults/z2k-default-vault/.system-block.md` with v3 schema
  - Remove: `z2k_card_activation`, `z2k_card_status`, `z2k_card_type`, `z2k_metadata_details`, `z2k_card_build_state`, `normalizePath`
  - Add: `z2k_metadata_copyright`, `z2k_metadata_reference`, `z2k_creation_language`, `z2k_creation_library_version`
  - Add: `{{fieldInfo me value="me"}}` (or `value="Geoff"` — pending Q5 answer)
  - Add: fieldInfo defaults for shared fields

### Phase 3 — Domain System Blocks
- [ ] Write `.system-block.md` for each domain (Information, Thoughts, Memories, Beliefs, Interactions, Journals, Logs, Locations, Projects, Entities, Body, AI, System)
  - Each sets `z2k_creation_domain` to its domain value
  - Information, Thoughts, Memories, Beliefs: add ratings fields
  - Journals, Logs: add privacy fields
  - AI: add default perspective = AI

### Phase 4 — Root-Level Blocks
- [ ] `Templates/Block - Card Fabric.block`
- [ ] `Templates/Block - Extended YAML.block` (maximalist YAML fields)
- [ ] `Templates/Block - Perspective - Me.block`
- [ ] `Templates/Block - Quotation.block` (using `Content.Author`, `Content.Title`)
- [ ] `Templates/Block - Citation.block`

### Phase 5 — Domain-Level Blocks
- [ ] `Information/Templates/Block - Podcast Interview Content.block` (core of Option 3)
- [ ] `Information/Templates/Block - Information - Summary.block`
- [ ] `Information/Templates/Block - Information - Overview.block`
- [ ] `Information/Templates/Block - Information - Synthesis.block`
- [ ] `Information/Templates/Block - Information - Details.block`
- [ ] `Interactions/Templates/Block - Logistics.block`
- [ ] `Memories/Templates/Block - When Where Who.block`
- [ ] `Body/Templates/Block - Health Log.block`

### Phase 6 — Templates (by domain)
Build in this order: Thoughts → Beliefs → Information → Interactions → Memories → Locations → Journals → Logs → Projects → Body → AI → System → Entities

For each template:
- Convert v2 field syntax to v3
- Add `z2k_template_suggested_title`
- Add `z2k_template_version: "v3.0.0 2026-03-01"`
- Add `z2k_template_author: "Z2K Studios, LLC"`
- Replace `%% comments %%` with `{{! comments }}`
- Add `{{fieldInfo}}` declarations
- Replace Card Fabric section with optional block reference comment

### Phase 7 — Recommendations Document
- [ ] Write `AI/Z2K Template Library - AI Recommendations.md` with architectural improvement suggestions

### Phase 8 — Tags Taxonomy Placeholder
- [ ] Write placeholder at `Docs/z2k-system-docs/` (location TBD) for tags taxonomy

### Phase 9 — Plan Update
- [ ] Update this document with any decisions made during implementation
- [ ] Update memory file at `/Users/gp/.claude/projects/-Users-gp-Vaults-Z2K-Studios-Workspace/memory/MEMORY.md`
