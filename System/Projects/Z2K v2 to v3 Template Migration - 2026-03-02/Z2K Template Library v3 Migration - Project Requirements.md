---
document_type: Project Requirements
status: Locked
---
# Project Requirements — Z2K Template Library v3 Migration

---

## 1. Definitions

- **v2**: Old template system using Obsidian Templater plugin
- **v3**: New template system using Z2K Templates Plugin
- **System Block**: `.system-block.md` — injects YAML frontmatter into all cards created in its folder tree
- **Document Template**: `Template - <Name>.md` — creates content notes; user is prompted for fields at instantiation
- **Block Template**: `<Name>.md` — reusable partial inserted via `{{> BlockName}}`
- **Instantiation**: Creating a content file from a template; prompts user for field values
- **Finalization**: Resolving all remaining fields and stripping template markup
- **WIP**: Work-In-Progress — a content file with unresolved fields awaiting completion
- **The terms Requirements and Features are used interchangeably throughout this document.** Both terms refer to the same underlying items — requirements from a project management perspective, features from a user perspective.

---

## 1.5 Importance Levels

Every requirement in this document carries an importance level:

| Level | Meaning |
|---|---|
| **Critical** | Must be implemented for the project to succeed. Blocking — project is incomplete without it. |
| **High** | Significant value; should be implemented unless truly blocked by tooling or dependency. |
| **Medium** | Meaningful enhancement; implement if priority permits within the IF cycle. |
| **Low** | Nice-to-have; defer to a future IF iteration or successor project if needed. |

> Importance levels are assigned to all requirements in this document. Each REQ-* item carries an explicit level; unnumbered specification sections carry a section-level importance note.

---

## 2. Source and Target

- **Source templates (READ-ONLY):** `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/`
- **Target vault:** `Data/Vaults/z2k-default-vault/`
- **Do NOT modify source templates under any circumstances**

---

## 2.5 Bootstrapping, Dependencies, and Tool Reliability

This project dogfoods tools that are themselves in active development. The following governs how to treat each tool:

### Z2K Templates Plugin (Primary Tooling)
- The Z2K Templates Plugin is in **mid-development**. Errors may exist in both code and documentation.
- **Documentation is the authority** — treat the plugin documentation as the intended behavior spec.
- Any discrepancy between plugin behavior and its documentation is a **code bug**.
- Any ambiguity or conflict within the documentation is a **documentation bug**.
- Notify the user promptly of any **blocking issues** (bugs that prevent task execution).
- All bugs are tracked per §21 (Bug and Issue Tracking).

### Z2K System Documentation
- The Z2K System Documentation (`Docs/z2k-system-docs/`) is **not reliable**. It is a mix of ZSv1 and ZSv2 content and is also incomplete.
- Only the **top-level domain list** has been updated for ZSv3.
- Do not use Z2K System Documentation as an authority for v3 behavior unless explicitly directed.

### All Other Tools and Components
- All other tools (Obsidian, standard plugins, file system, etc.) should be treated as working and reliable.

---

## 3. API Translation (v2 → v3)

Every migrated template must apply all of the following changes:

| v2 Syntax | v3 Syntax |
|---|---|
| `{{creatorLink}}` | `{{wikilink creator}}` |
| `{{todayLink}}` | `{{wikilink today}}` |
| `{{~prompt-info FieldName "type" "prompt" "default"}}` | `{{fieldInfo FieldName "prompt" type=<type> fallback="default"}}` |
| `z2k_metadata_version: 2.1` | `z2k_metadata_version: 3.00` |
| `z2k_metadata_details: "Z2K Card; https://z2k.dev"` | `z2k_metadata_copyright: "Z2K Metadata structure is © 2025 Z2K Studios, LLC"` |
| `z2k_creation_database: ".:Z2K/Database/X"` | Removed from templates; `z2k_creation_domain` set per domain in domain system-block |
| `z2k_creation_template: "[[TemplateName]]"` | `z2k_creation_template: "{{wikilink templateName}}"` |
| `z2k_card_activation: ".:Z2K/Inactive"` | **Removed entirely** |
| `z2k_card_status: ".:Z2K/Status/Template"` (in template files) | **Removed** — covered by `z2k_template_type` |
| `z2k_card_type: ".:Z2K/CardType/..."` | **Removed entirely** — self-evident from folder; causes conflicts if card is moved |
| `z2k_card_build_state: ...` | **Removed from system-blocks** |
| `normalizePath destPath` helper | **Not used** — hard-code domain values per domain instead |
| `%% Title: ... %%` comment | `z2k_template_suggested_title: "..."` in YAML |
| `%% ... %%` comments | Preserve as is, do not use handlebars comments  |
| `G:` personal prefix (multi-line context when at indentation level 0 or 1 ) | `> [!me]` callout block |
| `G:` personal prefix (multi-line context when at indentation level > 1 ) | `Me:` qualifier |
| `G:` personal prefix (inline single-line) | `Me:` inline prefix |

---

## 4. Naming and Metadata Standards

### REQ-NM-001 — Document Template Naming
**Importance:** Critical
- All document templates: `<Name>.md` — no `Template -` prefix.
- Files reside in dedicated `Templates/` subfolders, which serve as the type indicator.
- The folder location is sufficient to identify them as templates.
- Avoid name collision with other templates (and what would be envisioned for a fully populated second brain vault)
- **Default domain templates** (the general-purpose fallback for a domain) use the pattern `<Name> (General).md`. The name is typically the domain name or primary card type for that domain (e.g., `Thoughts (General).md`, `Contact (General).md`). This postfix acts as the domain's default template workaround until GH issue #182 (Default Template feature) is implemented in the Z2K Templates Plugin.

### REQ-NM-002 — Block Template Naming
**Importance:** Critical
All block templates: `<Name>.md` — no `Block -` prefix. Same rationale as REQ-NM-001.

> **Note:** Template and block names in §10 and §11 mapping tables reflect this convention (no prefix). All IP task target filenames will be updated to match during Phase 3 re-entry.

### REQ-NM-003 — System Block Naming
**Importance:** Critical
All system blocks: `.system-block.md` (dot-prefixed, hidden file in domain or vault root)

### REQ-NM-004 — Template Version
**Importance:** Critical
All migrated and new templates: `z2k_template_version: "v3.0.0 2026-03-02"`

### REQ-NM-005 — Template Author
**Importance:** Critical
- Official library templates: `z2k_template_author: "Z2K Studios, LLC"`
- Personal-specific templates (hardcoded names, personal orgs): `z2k_template_author: "Geoff (z2k-gwp)"`

### REQ-NM-006 — Metadata Version
**Importance:** Critical
All content templates: `z2k_metadata_version: 3.00`

### REQ-NM-007 — Template Type in YAML
**Importance:** Critical
- Document templates: `z2k_template_type: document-template`
- Block templates: `z2k_template_type: block-template`

### REQ-NM-008 — Suggested Title
**Importance:** High
Every document template includes `z2k_template_suggested_title`. 
- Use v2 `%% Title: %%` comments as source
- Derive sensibly from primary fields if no prior title comment exists.
- For templates with dates, have the date be preceeding (e.g. `{{today}} - Meeting with {{Person}})

### REQ-NM-009 — Field Name Consistency
**Importance:** High
During migration, review and rationalize user-defined field names for consistency across templates. Fields representing the same concept across different templates must use the same name. Favor the most common existing v2 name as the canonical form; where v2 is inconsistent, choose the clearest name and apply it uniformly. Significant renames should be noted in the relevant task. Examples of cross-template fields requiring consistent naming: `Author`, `Location`, `Title`, `Source`, `URL`, `Tags`.
- Use `{{today}}`to access the current date instead of `{{Date}}` as it is an obsidian defined field (see Z2K Templates `reference-manual/Built-In Fields/Built-In Fields - Date and Time/today`)
- Use `{{EventDate}}` to specify a user specified date. Provide a fieldInfo with a `suggest` of `{{now}}` if appropriate.
- Follow the naming conventions from Z2K Templates: see `reference-manual/Naming Conventions/Naming Fields`

---

## 5. Vault Structure Requirements

### REQ-VS-001 — Missing Domain Folders
**Importance:** Critical
Create: `Body/`, `Body/Templates/`, `AI/`, `AI/Templates/`

### REQ-VS-002 — System Templates Subfolder
**Importance:** Critical
`System/` exists; `System/Templates/` is missing. Create it.

### REQ-VS-003 — My Writings Subfolder
**Importance:** Critical
Create `Projects/My Writings/` and `Projects/My Writings/Templates/`.

### REQ-VS-004 — Root Templates Folder
**Importance:** Critical
Create `Templates/` at vault root for cross-domain block partials and the generic card template.

### REQ-VS-005 — Existing Domain Subfolders
**Importance:** High
Audit all existing domains. Create `Templates/` subfolder in any domain missing it.

---

## 6. Root System Block Requirements

File: `Data/Vaults/z2k-default-vault/.system-block.md`

**Current state (as of 2026-03-02):** Partially v3. Already has `z2k_metadata_copyright`, `z2k_metadata_reference`, `z2k_creation_creator`, `z2k_creation_date`, `z2k_creation_timestamp`, `z2k_creation_template`, `z2k_creation_language`. Still has `z2k_card_build_state`, `z2k_card_status`, and `normalizePath` usage that must be corrected. Do not assume the existing file is reflective of what it should be.

### REQ-RSB-001 — Remove Deprecated Fields
**Importance:** Critical
Remove: `z2k_card_build_state`, `z2k_card_status` (from root system-block)

### REQ-RSB-002 — Fix z2k_creation_domain
**Importance:** Critical
Remove `z2k_creation_domain` from the root system-block entirely (it uses the unsupported `normalizePath` helper). The field will be set per-domain in each domain's system-block. The root system-block should not set a domain value.

### REQ-RSB-003 — Library Version Field
**Importance:** High
Add: `z2k_creation_library_version: "3.0.0"`
- Field name follows `z2k_creation_*` prefix pattern: captures library version AT TIME OF CARD CREATION (static, like `z2k_creation_domain`)
- This is not the current library version — it is a snapshot of what version the library was when this card was created

### REQ-RSB-004 — Me Field
**Importance:** High
Add: `{{fieldInfo me value="me"}}`
- Sets the `me` field to the fixed literal string `"me"` for use in `[!me]` callout types
- This is version 3's pragmatic resolution: `[!me]` as a standardized, portable callout type
- Future: Core Plugin will expose `{{me}}` as a built-in that resolves to user's configured display name

### REQ-RSB-005 — Fields to Retain (unchanged)
**Importance:** Critical
- `z2k_metadata_version: 3.00`
- `z2k_metadata_variant: "barebones"`
- `z2k_metadata_copyright: "Z2K Metadata structure is © 2025 Z2K Studios, LLC"`
- `z2k_metadata_reference: "https://z2ksystem.com/specs/v3.0"`
- `z2k_creation_creator: "{{wikilink creator}}"`
- `z2k_creation_date: "{{wikilink today}}"`
- `z2k_creation_timestamp: "{{timestamp}}"`
- `z2k_creation_template: "{{wikilink templateName}}"`
- `z2k_creation_language: "en"`
- `z2k_card_source_type: ".:Z2K/SourceType/Unknown"` (root default; overridden per template)

---

## 7. Domain System Block Requirements

One `.system-block.md` per domain, one in the domain root folder.

### REQ-DSB-001 — z2k_creation_domain (all domains)
**Importance:** Critical
Every domain system-block sets `z2k_creation_domain` to the domain's canonical path:

| Domain | Value |
|---|---|
| Information | `.:Z2K/Domain/Information` |
| Thoughts | `.:Z2K/Domain/Thoughts` |
| Beliefs | `.:Z2K/Domain/Beliefs` |
| Memories | `.:Z2K/Domain/Memories` |
| Interactions | `.:Z2K/Domain/Interactions` |
| Journals | `.:Z2K/Domain/Journals` |
| Logs | `.:Z2K/Domain/Logs` |
| Locations | `.:Z2K/Domain/Locations` |
| Projects | `.:Z2K/Domain/Projects` |
| Entities | `.:Z2K/Domain/Entities` |
| Body | `.:Z2K/Domain/Body` |
| AI | `.:Z2K/Domain/AI` |
| System | `.:Z2K/Domain/System` |

### REQ-DSB-002 — Ratings Fields (selective domains)
**Importance:** High
Include in system-blocks for: **Information, Thoughts, Memories, Beliefs**

Fields (cannot be in block templates — blocks cannot be injected into YAML):
```yaml
z2k_rating_depth:        ""
z2k_rating_surprisal:    ""
z2k_rating_passion:      ""
```

### REQ-DSB-003 — Privacy Fields (Journals, Logs)
**Importance:** High
- Journals system-block: `z2k_card_privacy: ".:Z2K/Privacy/Private/Journal"`
- Logs system-block: `z2k_card_privacy: ".:Z2K/Privacy/Private/Log"`

### REQ-DSB-004 — AI Domain Authorship
**Importance:** Medium
AI domain system-block must express that the default authorship perspective is AI, not the vault owner. Implement as a field comment or dedicated field indicating AI-originated content.

### REQ-DSB-005 — Projects System Block Stop
**Importance:** High
- Goal: project cards in `Projects/` subfolders should not inherit `z2k_*` fields from root system-block
- Mechanism: System Block Stop files in project subdirectories
- Project cards use a completely different YAML structure without `z2k_*` fields
- Reference required: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/System Block Stops.md`

> ⚠️ OPEN ISSUE (DSB-005): The goal of completely suppressing `z2k_*` fields in project subfolder cards may not be fully achievable via system-block stops alone. Blocking `z2k_*` fields while injecting project-specific YAML may require templates to carry their own override YAML. Confirm behavior after reading System Block Stops doc before Phase 3 (Projects system-block) execution. Other domain system-blocks are not blocked.

---

## 8. Privacy Canonical Values
**Importance:** Critical

The following is the complete canonical set of `z2k_card_privacy` values. All values must appear in at least one template so Obsidian Properties panel can discover them for dropdown auto-complete:

| Value | Intended Usage |
|---|---|
| `.:Z2K/Privacy/Default` | General default — no specific privacy designation |
| `.:Z2K/Privacy/Public` | Explicitly public content |
| `.:Z2K/Privacy/Private/General` | Generally private |
| `.:Z2K/Privacy/Private/Professional` | Professional context, not for public |
| `.:Z2K/Privacy/Private/Implied` | Implicitly private by context |
| `.:Z2K/Privacy/Private/Log` | Daily logs (Logs domain default) |
| `.:Z2K/Privacy/Private/Journal` | Daily journals (Journals domain default) |
| `.:Z2K/Privacy/Uber-Private/Confidential` | Confidential conversations |
| `.:Z2K/Privacy/Uber-Private/SafePlace` | Safe place conversations |

**Per-template overrides from v2:**
- YPO Forum, YPO Event: `.:Z2K/Privacy/Uber-Private/SafePlace`
- Conversation with Doug: `.:Z2K/Privacy/Uber-Private/SafePlace`
- PoND Conversation with Bryn: `.:Z2K/Privacy/Uber-Private/Confidential`
- Personal interactions (default): `.:Z2K/Privacy/Private/General`

---

## 9. Source Type (z2k_card_source_type)
**Importance:** High

`z2k_card_source_type` is hard-coded per-template. Root system-block provides `.:Z2K/SourceType/Unknown` as the default fallback.

Known v2 values (to be confirmed against Metadata Specification v3.0):
- `.:Z2K/SourceType/Book`
- `.:Z2K/SourceType/Podcast`
- `.:Z2K/SourceType/WebArticle`
- `.:Z2K/SourceType/Conversation`
- `.:Z2K/SourceType/Meeting`
- `.:Z2K/SourceType/InternalThought`
- `.:Z2K/SourceType/InternalMemory`
- `.:Z2K/SourceType/Quotation`
- `.:Z2K/SourceType/Person`
- `.:Z2K/SourceType/AI/ChatGPT`
- `.:Z2K/SourceType/LifeLessons`
- `.:Z2K/SourceType/OtherCards`
- `.:Z2K/SourceType/Unknown`

> ⚠️ OPEN ISSUE (ST-001): Read `Docs/z2k-design-notes/Z2K System - Design Notes/Z2K Data Architecture/Z2K Metadata/Z2K Metadata Specification - Version 3.0.md` before implementing any Information domain templates. The canonical v3 source type taxonomy may differ from the v2 list above. This is blocking for Phase 6 (Information templates).

---

## 10. Block Template Requirements

### 10.1 Root-Level Blocks (in `Templates/`)

#### REQ-BLK-001 — Block - Card Fabric
**Importance:** High
- File: `Templates/Card Fabric.md`
- Fields: `Fabric.MentalModel`, `Fabric.Contextual`, `Fabric.Reference`, `Fabric.GeoContext`
  - Dot-notation is speculative for prompted user fields. If unsupported: use `FabricMentalModel`, `FabricContextual`, etc.
- Use `{{formatStringBulletize}}` so section headers only appear when field has content
- Build both a YAML array version and a markdown body version
- Card Fabric is an **opt-in partial** (explicit `{{> "Card Fabric"}}` insertion) — never system-block injected

> ⚠️ OPEN ISSUE (BLK-001): `Fabric.MentalModel` dot-notation for prompted fields is untested. Test at the start of Phase 4. If unsupported, use flat names and file a plugin bug report.

#### REQ-BLK-002 — Block - Extended YAML
**Importance:** Medium
- File: `Templates/Extended YAML.md`
- Optional maximalist YAML fields: privacy, projects, structures, ratings, fabric arrays
- User manually inserts this block; never auto-injected

#### REQ-BLK-003 — Block - Perspective - Me
**Importance:** High
- File: `Templates/Perspective - Me.md`
- Standard `[!me]` callout block template for vault-owner perspective sections
- Uses fixed literal `me` as callout type (not `{{me}}` field in v3)

#### REQ-BLK-004 — Block - Quotation
**Importance:** High
- File: `Templates/Quotation.md`
- Fields: `Content.Author`, `Content.Title`, `Content.Text`
- Namespace `Content.*` distinguishes from the card's own `Author` and `Title` fields
- Fallback flat names: `ContentAuthor`, `ContentTitle`, `ContentText`
- Field names must be **consistent** between Quotation and Citation blocks so YAML pre-fill works when inserting either block into a card that already has `Content.*` data

#### REQ-BLK-005 — Block - Citation
**Importance:** High
- File: `Templates/Citation.md`
- Fields: `Content.Author`, `Content.Title`, `Content.Source`, `Content.URL`, `Content.Date`
- Same `Content.*` namespace as Quotation block (identical field names where they overlap)

> ⚠️ OPEN ISSUE (BLK-004/005): Same dot-notation uncertainty as Card Fabric. Test with Quotation block first; if dot-notation works for prompted fields, apply to Citation. If not, fall back to flat names.

### 10.2 Domain-Level Blocks

#### REQ-BLK-010 — Block - Podcast Interview Content (Information)
**Importance:** High
- File: `Information/Templates/Podcast Interview Content.md`
- Core content structure for all podcast interview cards (Key Quotes, Key Takeaways, Summary, Background, etc.)
- Architecture (Option 3): host-specific document templates preset host/show field values BEFORE the block inclusion via `{{> "Podcast Interview Content"}}`. The block contains generic structure only.
- Example: `Template - Podcast Interview - Lex Fridman.md` sets `{{fieldInfo Host value="Lex Fridman"}}`, `{{fieldInfo ShowName value="Lex Fridman Podcast"}}`, then includes the block

#### REQ-BLK-011 — Block - Information - Summary (Information)
**Importance:** Medium
File: `Information/Templates/Information - Summary.md`

#### REQ-BLK-012 — Block - Information - Overview (Information)
**Importance:** Medium
File: `Information/Templates/Information - Overview.md`

#### REQ-BLK-013 — Block - Information - Synthesis (Information)
**Importance:** Medium
File: `Information/Templates/Information - Synthesis.md`

#### REQ-BLK-014 — Block - Information - Details (Information)
**Importance:** Medium
File: `Information/Templates/Information - Details.md`

#### REQ-BLK-015 — Block - Logistics (Interactions)
**Importance:** High
- File: `Interactions/Templates/Logistics.md`
- When/Where/Who/Recorded section common across interaction cards

#### REQ-BLK-016 — Block - When Where Who (Memories)
**Importance:** High
- File: `Memories/Templates/When Where Who.md`
- Context anchor section (date, location, who was present) common across memory cards

#### REQ-BLK-017 — Block - Health Log (Body)
**Importance:** High
- File: `Body/Templates/Health Log.md`
- Migrated from `~Partial - Health Log.md` (v2)
- All Flame-style automation fields preserved exactly as-is
- Future plan: split into individual sub-blocks composed by a parent block (out of scope for this project)

---

## 11. Document Template Requirements
**Section Importance:** Critical — these are the primary deliverable of the project.

### 11.1 Universal Standards (all document templates)
- `z2k_template_type: document-template`
- `z2k_template_version: "v3.0.0 2026-03-02"`
- `z2k_template_author` set per REQ-NM-005
- `z2k_template_suggested_title` expression present
- `{{fieldInfo}}` declarations for all user-defined fields
- `%% ... %%` comments converted to `{{! ... }}`
- Card Fabric section replaced with: `{{! To include Card Fabric: {{> "Card Fabric"}} }}`
- `G:` prefix converted: multi-line → `> [!me]`, inline → `Me:`
- **Templater syntax handling:** Templater code (`<% ... %>`) must only be replaced when a clear v3 equivalent exists. Code that cannot be cleanly converted must be **preserved verbatim** and **flagged** with a `{{! FLAGGED: ... }}` comment explaining what it does. Do not guess — preserve-and-flag is always preferred over an incorrect conversion.

### 11.2 Thoughts Domain (`Thoughts/Templates/`)
| v2 Source | v3 Target |
|---|---|
| `Thoughts - ~Generic` | `Thoughts (General).md` |
| `Thoughts - Book - Quote` | `Template - Book Quote.md` |
| `Thoughts - Concept - Book` | `Template - Book Concept.md` |
| `Thoughts - General - Quote` | `Template - General Quote.md` |
| `Thoughts - Ontology` | `Template - Ontology.md` |
| `Thoughts - Quote a Source` | `Template - Quote a Source.md` |
| `Thoughts - Resolutions` | `Template - Resolutions.md` |

### 11.3 Beliefs Domain (`Beliefs/Templates/`)
| v2 Source | v3 Target |
|---|---|
| `Beliefs - ~Generic` | `Beliefs (General).md` |

### 11.4 Information Domain (`Information/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| `Information - ~Generic` | `Information (General).md` | |
| `Information - Academic Paper` | `Template - Academic Paper.md` | |
| `Information - Blinkist` | `Template - Blinkist.md` | |
| `Information - Book` | `Template - Book.md` | `source_type: Book` |
| `Information - Conference` | `Template - Conference.md` | |
| `Information - Interview` | `Template - Interview.md` | Generic, non-podcast |
| `Information - Kindle Notes` | `Template - Kindle Notes.md` | |
| `Information - Lecture` | `Template - Lecture.md` | |
| `Information - Ontology` | `Template - Ontology.md` | |
| `Information - Podcast Interview` | `Template - Podcast Interview.md` | Generic; `source_type: Podcast` |
| `Information - Adam Grant Interview` | `Template - Podcast Interview - Adam Grant.md` | Option 3: presets + block |
| `Information - Dwarkesh Interview` | `Template - Podcast Interview - Dwarkesh Patel.md` | Option 3 |
| `Information - Huberman Lab Podcast` | `Template - Podcast Interview - Huberman Lab.md` | Option 3 |
| `Information - Knowledge Project Interview` | `Template - Podcast Interview - Knowledge Project.md` | Option 3; host: Shane Parrish |
| `Information - Lex Fridman Interview` | `Template - Podcast Interview - Lex Fridman.md` | Option 3 |
| `Information - Tim Ferriss Interview` | `Template - Podcast Interview - Tim Ferriss.md` | Option 3 |
| `Information - Quotation` | `Template - Quotation.md` | `source_type: Quotation` |
| `Information - Quote a Source` | `Template - Quote a Source.md` | |
| `Information - Quote an Email` | `Template - Quote an Email.md` | Single template (consolidates all v2 email-quote variants from Information, Thoughts, Memories domains) |
| `Information - Web Article` | `Template - Web Article.md` | `source_type: WebArticle` |
| `Information - Wikipedia Entry` | `Template - Wikipedia Entry.md` | |

**Dropped (v2 → not migrated):**
- `Information - Quote an Email` from Thoughts and Memories domains → consolidated into Information version
- `Memories - Quote an Email` → dropped per Q8 decision

### 11.5 Interactions Domain (`Interactions/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| `Interactions - ~Generic` | `Interactions (General).md` | |
| `Interactions - Amateur Hour` | `Template - Amateur Hour.md` | Personal; author: Geoff |
| `Interactions - Business Meeting` | `Template - Business Meeting.md` | |
| `Interactions - Class Lecture` | `Template - Class Lecture.md` | |
| `Interactions - Class Overview` | `Template - Class Overview.md` | |
| `Interactions - Conversation` | `Template - Conversation.md` | |
| `Interactions - Doug` | `Template - Conversation with Doug.md` | Personal; privacy: Uber-Private/SafePlace |
| `Interactions - Conversation with John Kashiwabara` | `Template - Conversation with John Kashiwabara.md` | Personal |
| `Interactions - Email` | `Template - Email.md` | |
| `Interactions - PoND Conversation with Bryn` | `Template - PoND Conversation with Bryn.md` | Personal; privacy: Uber-Private/Confidential |
| `Interactions - YPO Event` | `Template - YPO Event.md` | Personal; privacy: Uber-Private/SafePlace |
| `Interactions - YPO Forum` | `Template - YPO Forum.md` | Personal; privacy: Uber-Private/SafePlace |

### 11.6 Memories Domain (`Memories/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| `Memories - ~Generic` | `Memories (General).md` | |
| `Memories - Family Vacation Trip` | `Template - Family Vacation Trip.md` | |
| `Memories - Ontology` | `Template - Ontology.md` | |
| `Memories - PCT Trail Day` | `Template - PCT Trail Day.md` | Personal |
| `Memories - Solo Trip Summary` | `Template - Solo Trip Summary.md` | |
| `Memories - Quote an Email` | **DROPPED** | Per Q8 — use Information domain email template |

### 11.7 Locations Domain (`Locations/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| `Locations - ~Generic` | `Locations (General).md` | |
| `Locations.template` | Review — likely same as ~Generic; merge if identical |

> ⚠️ OPEN ISSUE (LOC-001): Confirm whether `Locations.template` is functionally identical to `Locations - ~Generic`. If yes, merge into single `Locations (General).md`. If different, create a separate named template.

### 11.8 Journals Domain (`Journals/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| `~Journals - Daily` | `Template - Daily Journal.md` | Must include `## Passing Thoughts`, `## Passing Memories`, `## Passing Information` sections — absorbs retired Ideas domain |
| `~Journals - Yearly Summaries` | `Template - Yearly Summary.md` | |

### 11.9 Logs Domain (`Logs/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| `~Logs - Daily` | `Template - Daily Log.md` | All Flame fields preserved as-is (personal/specific) |
| `~Logs - Monthly` | `Template - Monthly Log.md` | |
| `~Logs - Quarterly Focus List` | `Template - Quarterly Focus List.md` | |
| `~Logs - Weekly` | `Template - Weekly Log.md` | |
| `~Logs - Yearly` | `Template - Yearly Log.md` | |
| `~Logs - Yearly Strategic Plan` | `Template - Yearly Strategic Plan.md` | |

### 11.10 Projects Domain (`Projects/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| *(none — new)* | `Project (General).md` | New template |
| *(none — new)* | `Template - Active Project.md` | New template |
| *(none — new)* | `Template - Completed Project.md` | New template |

**Projects YAML:** project cards use a different YAML structure with no `z2k_*` fields. See REQ-DSB-005 and OPEN ISSUE DSB-005.

### 11.11 Projects/My Writings Domain (`Projects/My Writings/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| `Syntheses - ~Generic` | `My Writings (General).md` | "(General)" postfix is workaround for GH issue #182 |
| `Syntheses - Extended Journal Writing` | `Template - Personal Writing.md` | Renamed to avoid confusion with Journals |
| `Syntheses - Treatise` | `Template - Treatise.md` | |
| `Project - Code Poetry - Poem` | `Template - Code Poem.md` | Personal |
| `Syntheses - Quote an Email` | **DELETED** | Per Q2 decision |

> Note: "Default Template" as a plugin feature is not yet implemented (GH issue #182). The `(General)` postfix naming convention is the current workaround across all domains. Once #182 is implemented, the `(General)` postfix can be dropped and templates renamed to plain domain names.

### 11.12 Entities Domain (`Entities/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| *(none — new)* | `Contact (General).md` | Minimal starting point; full CRM deferred |

### 11.13 Body Domain (`Body/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| `Body - ~Generic` | `Body (General).md` | General body/health topic card |
| `~Partial - Health Log` | `Health Log.md` | Block template (see REQ-BLK-017) |

### 11.14 AI Domain (`AI/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| `Information - ChatGPT` | *Deferred* | AI domain templates not in scope for this project |

> Note: The `Information - ChatGPT` template moves to the AI domain conceptually but AI domain template content is deferred to a future project. AI domain gets a system-block only.

### 11.15 System Domain (`System/Templates/`)
| v2 Source | v3 Target | Notes |
|---|---|---|
| `~System - ~Generic` | `System (General).md` | |
| `~System - Testing` | **DROPPED** | Testing artifact, not a real template |

### 11.16 Root Templates (`Templates/`)

The root `Templates/` folder is the home for all **cross-domain document templates** — templates that are meaningfully applicable across multiple domains. It will expand as additional cross-domain patterns are identified.

**Current scope:**

| v2 Source | v3 Target | Notes |
|---|---|---|
| `~Generic Card Template` | `Card (General).md` | Cross-domain generic card |
| *(domain-specific variants exist in Thoughts, Information, Memories)* | `Template - Ontology.md` | Cross-domain generic Ontology / Map of Content card |

Additional cross-domain templates will be added to this folder as the library evolves. Candidates to evaluate during Phase 6:
- `Template - Quotation.md` — generic cross-domain quote capture (evaluate whether domain-specific variants are sufficient or a root-level version adds value)
- Others as identified during implementation

### 11.17 Dropped Templates (Ideas domain — fully retired)
All `Ideas - *` templates are dropped. Quick idea capture → Daily Journal `## Passing Thoughts` section.

---

## 12. Inline `::` Properties and YAML Mirroring
**Importance:** Medium

- **Preserve in place** — do not remove `::` properties from card bodies
- **Mirror to YAML** where the field is a likely Dataview or Properties panel query candidate
- Judgment-based per template; consult: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/Storing Field Values in YAML.md`

---

## 13. Perspective and Authorship
**Importance:** High

- **Multi-line vault-owner voice**: `> [!me]` callout block
- **Inline single-line annotation**: `Me:` prefix
- **Fixed callout type**: `me` is always the literal string used as callout type (not the user's name)
  - Standardized across all Z2K users; requires a single CSS snippet to style
  - Future: Core Plugin will implement `{{me}}` as a built-in field configurable per user
- **Root block**: `Templates/Perspective - Me.md` — reusable callout block template
- **Design note**: The long-term debate between `[!me]` (portable) and `[!Geoff]` (identity-expressive) remains a conceptual open question. For v3 implementation: always use `[!me]`.

---

## 14. fieldInfo Prompting Strategy
**Importance:** Critical

- All user-defined fields must have a `{{fieldInfo}}` declaration
- Declarations may live in domain system-blocks (for shared cross-template fields) or in individual templates
- A `fieldInfo` in a system-block has no effect if that field is not used in the template — no unintended prompts
- Fields pre-populated by automation (e.g., Flame fields in Daily Log): use `directives="no-prompt"` or leave as plain field references
- Required fields: `directives="required"`
- Optional with default: `fallback="value"`

---

## 15. Library Version and System Card
**Importance:** High

- `z2k_creation_library_version: "3.0.0"` in root system-block
- System card: `System/Z2K Template Library - v3.md` — documents current library release and changelog
- Semantics: both are snapshots; the field in cards is creation-time only and does not update when the library is upgraded

---

## 16. Supporting Documentation

### REQ-SUPP-001 — AI Recommendations Document
**Importance:** Medium
- File: `AI/Z2K Template Library - AI Recommendations.md`
- Content: architectural improvement suggestions, patterns observed during migration, future enhancement ideas
- Created after all templates are complete (Phase 7)

### REQ-SUPP-002 — Tags Taxonomy Placeholder
**Importance:** Low
- Location: `System/` or `Docs/z2k-system-docs/` (determine best location during Phase 7)
- A placeholder document describing the intent of the taxonomy; actual taxonomy authorship deferred

### REQ-SUPP-003 — Library Version System Card
**Importance:** High
- File: `System/Z2K Template Library - v3.md`
- Documents library version, creation date, changelog, domain inventory

---

## 17. Deferred and Future Items

Explicitly out of scope for this project. Tracked here for archival from Q&A docs:

| Item | Q&A Source | Future Action |
|---|---|---|
| Full Entities CRM templates (Person, Org, Named Entity) | Arch Q11 | Separate future project; start with `Contact (General)` only |
| AI domain content templates | Arch Q13 | Separate project; AI domain gets system-block only |
| Tags taxonomy content authorship | Arch Q23 | Only a placeholder in scope |
| `{{me}}` built-in field | Mig Q5 | Core Plugin feature; for now literal `[!me]` |
| "Default Template" plugin feature | Mig Q2 | GH issue #182; `(General)` postfix workaround until implemented; drop postfix once feature ships |
| Health Log sub-block decomposition | Arch Q14 | Migrate as single block for now; decompose in subsequent session |
| Generic Daily Log template | Mig Q6 | Current Flame-specific log migrated as-is; generic version created separately by user |
| My Writings export/publication pipeline | Mig Q2 discussion | Wikilink stripping, versioning, background material — future project |
| Personal template migration to personal vault | Mig Q3 | Manual move required before this library is published publicly |
| Option 4 podcast template (conditional multi-select) | Mig Q4 | Interesting future enhancement; Option 3 chosen for v3 |
| Publications / Writings domain as a first-class domain | Mig Q2 discussion | Option 2 discussed; chose Projects/My Writings for v3 |
| `[!me]` vs `[!Geoff]` design resolution | Mig Q5 | Long-term open; v3 decision: `[!me]` |
| Fabric.MentalModel dot-notation (if fails) | Arch Q1 | File plugin bug if unsupported; use flat names as fallback |

---

## 18. Sidebar Tasks (non-blocking, execute opportunistically)

- **Verify dot-notation for prompted fields** — test `Fabric.MentalModel` as a `{{fieldInfo}}` target at start of Phase 4 (blocks); file plugin bug if unsupported
- **Review Locations.template** — confirm whether it is identical to `Locations - ~Generic` before Phase 6; merge into `Locations (General).md` or keep separate accordingly
- **Mark personal templates** — ensure all personal-specific templates have `z2k_template_author: "Geoff (z2k-gwp)"` so they are easily identifiable for personal vault migration
- **Create System library version card** — `System/Z2K Template Library - v3.md` during Phase 7

---

## 19. Open Issues

| ID | Description | Blocking |
|---|---|---|
| DSB-005 | System Block Stop behavior for Projects — may not fully suppress `z2k_*` fields; read System Block Stops doc before implementing Projects system-block | Phase 3 (Projects only) |
| ST-001 | Source type taxonomy — read Metadata Specification v3.0 before Information domain templates | Phase 6 (Information) |
| BLK-001 | Fabric.MentalModel dot-notation for prompted fields — untested; test at start of Phase 4; file bug if fails | Phase 4 |
| BLK-004/005 | Quotation/Citation Content.* dot-notation — same uncertainty; test with Quotation first | Phase 4 |
| LOC-001 | Locations.template vs. ~Generic — verify before Phase 6 (Locations) | Phase 6 (Locations) |

---

## 20. Outputs and Deliverables

### 20.1 Primary Output — CTLv3
A fully working Z2K Core Template Library v3 implementation in `Data/Vaults/z2k-default-vault/`, meeting all success criteria in the SoW §2.

### 20.2 Continuous Improvement Output
As learnings accumulate during IF execution, improvements to the project workflow are logged in:
`Post Project/Continuous Improvement/Project Workflow Improvements.md`

Each entry includes a description, rationale, and proposed implementation approach.

**Seeded items (from pre-draft feedback):**
- Rename the "Workflow" section in the default SoW template to "Iterative Framework" to deconflict with the `ai-context` workflow term.
- Add a Terms and Acronyms section to the default SoW template.
- Create multiple IF variants for different project types (highly iterative vs. linear).

### 20.3 Post-CTLv3 Outputs
The following outputs are produced only **after CTLv3 work is complete and validated**. Notes and requirements for each are collected in `Post Project/` during execution.

**CTLv3 Project (Successor)**
- A new ongoing project (with its own SoW, PRD, IP, TP) for iteratively adding new templates to the CTLv3 library.
- Input: new template requests from discussion, not CTLv2.
- First run: validate that existing CTLv3 passes all tests.
- Only begins after CTLv3 is fully validated.

**ZSv3 Project (Successor)**
- A new project for building out the Z2K System Architecture documentation.
- Primary output: Z2K System Documentation (authoritative, v3-complete).
- Key input items collected in `Post Project/ZSv3 Project/` during this project.

**Template Best Practices Document**
- A best practices document for template hierarchy and system development, drawn from lessons learned during CTLv3 migration.
- Intended destination: Z2K Templates Plugin documentation website.
- Notes and observations collected in `Post Project/Template Best Practices/` during execution.

---

## 21. Bug and Issue Tracking

Bugs and issues discovered during this project (particularly in the Z2K Templates Plugin) are tracked in:
`Issues/Z2K Templates Plugin/<Bug Title>.md`

An index file at `Issues/Z2K Templates Plugin/Issues - Index.md` tracks all items.

### Bug File Structure

Each bug file must contain:
- **Title** — short descriptive name
- **Status** — `Observed` → `Repeatable` → `Identified (Ready to Submit)`
- **Urgency** — `Low (minor)` / `Normal` / `High` / `High-Blocking`
- **Component** — `Documentation` / `Code`
- **Scope** — `Bug` / `Enhancement`
- **Description** — what the bug is
- **Steps to Reproduce** — minimal reproducible steps
- **Example** — concrete example demonstrating the issue
- **Notes** — additional context, workarounds, related issues

### Workflow
A bug progresses through states: `Observed` → `Repeatable` → `Identified (Ready to Submit)`.

A bug is **only acted upon** (GitHub issue submitted, fix requested) when it reaches `Identified (Ready to Submit)`. Submission and fixing are the responsibility of the Z2K Templates Plugin project, not this project.

`High-Blocking` bugs must be flagged to the user immediately and may pause IF execution for the affected task.
