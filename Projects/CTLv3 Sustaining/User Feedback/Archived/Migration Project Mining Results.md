# Migration Project Mining Results

Extracted from `Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/` on 2026-03-02.

**Source documents mined:** PRD, Implementation Plan, Testing Plan, Task List and Progress Tracker, Agent Brief, Post Project (CTLv3 Project Index, Template Best Practices Index).

**Excluded:** Iterative framework process (SoW §4), v2→v3 conversion procedures, old template migration steps, Templater syntax mapping.

---

## 1. Complete Template Inventory

80 templates total (67 document + 13 block) across 13 domains + vault root.

### 1.1 Root-Level Templates (`Templates/`)

#### Document Templates (2)
| Template File | Description |
|---|---|
| `Card (General).md` | Cross-domain generic card — minimal, domain-agnostic |
| `Ontology.md` | Cross-domain Map of Content / Ontology card |

#### Block Templates (5)
| Template File | Description | Key Fields |
|---|---|---|
| `Card Fabric.md` | Opt-in cognitive fabric section (mental models, contextual, reference, geo) | `FabricMentalModel`, `FabricContextual`, `FabricReference`, `FabricGeoContext` (flat names — dot-notation unsupported per BLK-001) |
| `Extended YAML.md` | Maximalist optional YAML fields (privacy, projects, structures, ratings, fabric arrays) | User manually inserts; never auto-injected |
| `Perspective - Me.md` | Standard `[!me]` callout block for vault-owner perspective | `PerspectiveText` |
| `Quotation.md` | Blockquote + attribution + optional `[!me]` perspective | `ContentAuthor`, `ContentTitle`, `ContentText` (flat names — dot-notation unsupported) |
| `Citation.md` | Formal citation block — consistent field names with Quotation | `ContentAuthor`, `ContentTitle`, `ContentSource`, `ContentURL`, `ContentDate` |


### 1.2 Information Domain (`Information/Templates/`)

#### Document Templates (21)
| Template File | Source Type | Notes |
|---|---|---|
| `Information (General).md` | — | Domain default |
| `Academic Paper.md` | — | |
| `Blinkist.md` | — | |
| `Book.md` | `.:Z2K/SourceType/Book` | |
| `Conference.md` | — | |
| `Interview.md` | — | Generic, non-podcast |
| `Kindle Notes.md` | — | |
| `Lecture.md` | — | |
| `Ontology.md` | — | |
| `Podcast Interview.md` | `.:Z2K/SourceType/Podcast` | Generic; uses `{{> "Podcast Interview Content"}}` block |
| `Podcast Interview - Adam Grant.md` | `.:Z2K/SourceType/Podcast` | Host-specific preset (Option 3 architecture) |
| `Podcast Interview - Dwarkesh Patel.md` | `.:Z2K/SourceType/Podcast` | Host-specific preset |
| `Podcast Interview - Huberman Lab.md` | `.:Z2K/SourceType/Podcast` | Host-specific preset |
| `Podcast Interview - Knowledge Project.md` | `.:Z2K/SourceType/Podcast` | Host-specific preset (host: Shane Parrish) |
| `Podcast Interview - Lex Fridman.md` | `.:Z2K/SourceType/Podcast` | Host-specific preset |
| `Podcast Interview - Tim Ferriss.md` | `.:Z2K/SourceType/Podcast` | Host-specific preset |
| `Quotation.md` | `.:Z2K/SourceType/Quotation` | |
| `Quote a Source.md` | — | |
| `Quote an Email.md` | — | Consolidated from multiple v2 domains |
| `Web Article.md` | `.:Z2K/SourceType/WebArticle` | |
| `Wikipedia Entry.md` | — | |

#### Block Templates (5)
| Template File | Description |
|---|---|
| `Podcast Interview Content.md` | Core podcast interview structure — generic, included by host-specific templates |
| `Information - Summary.md` | One-paragraph abstract of source content |
| `Information - Overview.md` | Structured breakdown of main points |
| `Information - Synthesis.md` | Vault-owner's analysis (uses `[!me]` callout) |
| `Information - Details.md` | Granular notes, highlights, direct quotes |


### 1.3 Thoughts Domain (`Thoughts/Templates/`)

#### Document Templates (7)
| Template File | Source Type | Notes |
|---|---|---|
| `Thoughts (General).md` | `.:Z2K/SourceType/InternalThought` | Domain default |
| `Book Quote.md` | `.:Z2K/SourceType/Quotation` | |
| `Book Concept.md` | `.:Z2K/SourceType/InternalThought` | |
| `General Quote.md` | `.:Z2K/SourceType/Quotation` | |
| `Ontology.md` | — | |
| `Quote a Source.md` | `.:Z2K/SourceType/Quotation` | |
| `Resolutions.md` | — | |


### 1.4 Beliefs Domain (`Beliefs/Templates/`)

#### Document Templates (1)
| Template File | Source Type | Notes |
|---|---|---|
| `Beliefs (General).md` | `.:Z2K/SourceType/InternalThought` | Domain default |


### 1.5 Interactions Domain (`Interactions/Templates/`)

#### Document Templates (12)
| Template File | Privacy | Author | Notes |
|---|---|---|---|
| `Interactions (General).md` | — | Z2K Studios | Domain default |
| `Amateur Hour.md` | — | Geoff (z2k-gwp) | Personal |
| `Business Meeting.md` | — | Z2K Studios | |
| `Class Lecture.md` | — | Z2K Studios | |
| `Class Overview.md` | — | Z2K Studios | |
| `Conversation.md` | — | Z2K Studios | |
| `Conversation with Doug.md` | `.:Z2K/Privacy/Uber-Private/SafePlace` | Geoff (z2k-gwp) | Personal |
| `Conversation with John Kashiwabara.md` | — | Geoff (z2k-gwp) | Personal |
| `Email.md` | — | Z2K Studios | |
| `PoND Conversation with Bryn.md` | `.:Z2K/Privacy/Uber-Private/Confidential` | Geoff (z2k-gwp) | Personal |
| `YPO Event.md` | `.:Z2K/Privacy/Uber-Private/SafePlace` | Geoff (z2k-gwp) | Personal |
| `YPO Forum.md` | `.:Z2K/Privacy/Uber-Private/SafePlace` | Geoff (z2k-gwp) | Personal |

#### Block Templates (1)
| Template File | Description |
|---|---|
| `Logistics.md` | When/Where/Who/Recorded section — standard context for interaction cards |


### 1.6 Memories Domain (`Memories/Templates/`)

#### Document Templates (5)
| Template File | Author | Notes |
|---|---|---|
| `Memories (General).md` | Z2K Studios | Domain default |
| `Family Vacation Trip.md` | Z2K Studios | |
| `Ontology.md` | Z2K Studios | |
| `PCT Trail Day.md` | Geoff (z2k-gwp) | Personal |
| `Solo Trip Summary.md` | Z2K Studios | |

#### Block Templates (1)
| Template File | Description |
|---|---|
| `When Where Who.md` | Date/Location/Who Was Present — context anchor for memory cards |


### 1.7 Locations Domain (`Locations/Templates/`)

#### Document Templates (1)
| Template File | Notes |
|---|---|
| `Locations (General).md` | Domain default (LOC-001 resolved — merged with Locations.template) |


### 1.8 Journals Domain (`Journals/Templates/`)

#### Document Templates (2)
| Template File | Notes |
|---|---|
| `Daily Journal.md` | Includes `## Passing Thoughts`, `## Passing Memories`, `## Passing Information` sections (absorbed retired Ideas domain) |
| `Yearly Summary.md` | |


### 1.9 Logs Domain (`Logs/Templates/`)

#### Document Templates (6)
| Template File | Author | Notes |
|---|---|---|
| `Daily Log.md` | Geoff (z2k-gwp) | All Flame-style automation fields preserved (personal/specific) |
| `Monthly Log.md` | Z2K Studios | |
| `Quarterly Focus List.md` | Z2K Studios | |
| `Weekly Log.md` | Z2K Studios | |
| `Yearly Log.md` | Z2K Studios | |
| `Yearly Strategic Plan.md` | Z2K Studios | |


### 1.10 Projects Domain (`Projects/Templates/`)

#### Document Templates (3)
| Template File | Notes |
|---|---|
| `Project (General).md` | New template (not migrated from v2); uses different YAML structure without `z2k_*` fields |
| `Active Project.md` | New template |
| `Completed Project.md` | New template |


### 1.11 Projects/My Writings Domain (`Projects/My Writings/Templates/`)

#### Document Templates (4)
| Template File | Author | Notes |
|---|---|---|
| `My Writings (General).md` | Z2K Studios | "(General)" postfix = workaround for GH issue #182 |
| `Personal Writing.md` | Z2K Studios | Renamed from "Extended Journal Writing" |
| `Treatise.md` | Z2K Studios | |
| `Code Poem.md` | Geoff (z2k-gwp) | Personal |


### 1.12 Entities Domain (`Entities/Templates/`)

#### Document Templates (1)
| Template File | Notes |
|---|---|
| `Contact (General).md` | Minimal starting point; full CRM deferred |


### 1.13 Body Domain (`Body/Templates/`)

#### Document Templates (1)
| Template File | Notes |
|---|---|
| `Body (General).md` | General body/health topic card |

#### Block Templates (1)
| Template File | Notes |
|---|---|
| `Health Log.md` | All Flame fields preserved exactly as-is; future plan: split into sub-blocks |


### 1.14 AI Domain (`AI/Templates/`)

No templates — system block only. Content templates deferred to future project (CTLP-002).


### 1.15 System Domain (`System/Templates/`)

#### Document Templates (1)
| Template File | Notes |
|---|---|
| `System (General).md` | |


---

## 2. Domain Inventory

13 top-level domains, plus 1 subdomain.

| Domain | Path | System Block Fields | Notes |
|---|---|---|---|
| Information | `Information/` | `z2k_creation_domain`, ratings (depth/surprisal/passion) | Largest domain — 21 document templates, 5 blocks |
| Thoughts | `Thoughts/` | `z2k_creation_domain`, ratings | 7 document templates |
| Beliefs | `Beliefs/` | `z2k_creation_domain`, ratings | 1 document template |
| Memories | `Memories/` | `z2k_creation_domain`, ratings | 5 document + 1 block |
| Interactions | `Interactions/` | `z2k_creation_domain` | 12 document + 1 block |
| Journals | `Journals/` | `z2k_creation_domain`, `z2k_card_privacy: ".:Z2K/Privacy/Private/Journal"` | 2 document templates |
| Logs | `Logs/` | `z2k_creation_domain`, `z2k_card_privacy: ".:Z2K/Privacy/Private/Log"` | 6 document templates |
| Locations | `Locations/` | `z2k_creation_domain` | 1 document template |
| Projects | `Projects/` | `z2k_creation_domain` + `.system-block-stop` in subfolders | 3 document templates; projects use non-z2k YAML |
| Projects/My Writings | `Projects/My Writings/` | Inherits from Projects; has own `.system-block-stop` | 4 document templates (subdomain) |
| Entities | `Entities/` | `z2k_creation_domain` | 1 document template (minimal; full CRM deferred) |
| Body | `Body/` | `z2k_creation_domain` | 1 document + 1 block |
| AI | `AI/` | `z2k_creation_domain`, `z2k_creation_perspective: "AI"` | No templates (system block only) |
| System | `System/` | `z2k_creation_domain` | 1 document template |


---

## 3. Global System Requirements

These are cross-cutting requirements that apply to the CTL as a whole. Sourced from migration PRD §§4–15, Agent Brief, and Template Best Practices.

### 3.1 Naming and Metadata Standards (PRD §4)

| Req ID | Requirement | Tag |
|---|---|---|
| NM-001 | Document templates: `<Name>.md` — no `Template -` prefix. Domain defaults: `<Domain> (General).md` | quantitative |
| NM-002 | Block templates: `<Name>.md` — no `Block -` prefix | quantitative |
| NM-003 | System blocks: `.system-block.md` (dot-prefixed, hidden) | quantitative |
| NM-004 | All templates: `z2k_template_version: "v3.0.0 2026-03-02"` | quantitative |
| NM-005 | Author: `z2k_template_author: "Z2K Studios, LLC"` for library; `"Geoff (z2k-gwp)"` for personal | quantitative |
| NM-006 | All content templates: `z2k_metadata_version: 3.00` | quantitative |
| NM-007 | Document templates: `z2k_template_type: document-template`; Blocks: `z2k_template_type: block-template` | quantitative |
| NM-008 | Every document template includes `z2k_template_suggested_title` | quantitative |
| NM-009 | Consistent field naming across templates (same concept = same name); PascalCase for custom fields unless built-in | quantitative |

### 3.2 Vault Structure Standards (PRD §5)

| Req ID | Requirement | Tag |
|---|---|---|
| VS-001 | All 13 domain folders exist with `Templates/` subfolder | quantitative |
| VS-002 | `System/Templates/` exists | quantitative |
| VS-003 | `Projects/My Writings/` and `Projects/My Writings/Templates/` exist | quantitative |
| VS-004 | Root `Templates/` folder exists at vault root | quantitative |
| VS-005 | Every domain has a `Templates/` subfolder | quantitative |

### 3.3 Root System Block Standards (PRD §6)

| Req ID | Requirement | Tag |
|---|---|---|
| RSB-001 | No deprecated fields: `z2k_card_build_state`, `z2k_card_status` absent | quantitative |
| RSB-002 | No `z2k_creation_domain` in root (domain set per-domain only) | quantitative |
| RSB-003 | `z2k_creation_library_version: "3.0.0"` present | quantitative |
| RSB-004 | `{{fieldInfo me value="me"}}` in template body | quantitative |
| RSB-005 | All retained fields present: `z2k_metadata_version`, `z2k_metadata_variant`, `z2k_metadata_copyright`, `z2k_metadata_reference`, `z2k_creation_creator`, `z2k_creation_date`, `z2k_creation_timestamp`, `z2k_creation_template`, `z2k_creation_language`, `z2k_card_source_type` | quantitative |

### 3.4 Domain System Block Standards (PRD §7)

| Req ID | Requirement | Tag |
|---|---|---|
| DSB-001 | Every domain system-block sets `z2k_creation_domain` to the correct canonical value | quantitative |
| DSB-002 | Ratings fields in: Information, Thoughts, Memories, Beliefs only | quantitative |
| DSB-003 | Privacy fields: Journals = `.:Z2K/Privacy/Private/Journal`; Logs = `.:Z2K/Privacy/Private/Log` | quantitative |
| DSB-004 | AI domain: `z2k_creation_perspective: "AI"` | quantitative |
| DSB-005 | Projects: `.system-block-stop` files in project subfolders | quantitative |

### 3.5 Universal Document Template Standards (PRD §11.1)

| Requirement | Tag |
|---|---|
| `z2k_template_type: document-template` present in YAML | quantitative |
| `z2k_template_version: "v3.0.0 2026-03-02"` present | quantitative |
| `z2k_template_author` set correctly (library vs personal) | quantitative |
| `z2k_template_suggested_title` expression present | quantitative |
| `{{fieldInfo}}` declarations for all user-defined fields | quantitative |
| No v2 Templater syntax (`<% ... %>`) remaining | quantitative |
| Card Fabric replaced with opt-in block comment | qualitative |
| `G:` prefix converted to `[!me]` / `Me:` | quantitative |
| Valid Handlebars syntax (no unmatched tags, correct comment syntax) | quantitative |
| Consistent field naming (PascalCase, no lowercase-initial custom fields) | quantitative |
| Template uses `{{!-- --}}` (double-dash) for comments containing `{{` or `}}` | quantitative |
| Comments don't leave trailing spaces or break line clearing | quantitative |

### 3.6 Qualitative Standards (from User Feedback / Initial Setup Q&A)

| Requirement | Tag |
|---|---|
| Templates are well-documented with comments | qualitative |
| Templates look readable/attractive in raw Markdown state (comment break bars, clean structure) | qualitative |
| Templates showcase Z2K Templates capabilities (conditionals, helpers, multi-select fields, system blocks) | qualitative |
| Templates are AI-aware — YAML is structured for AI processing | qualitative |
| Templates handle edge cases gracefully (special characters, empty fields, unusual but valid data) | qualitative |
| Templates are modular — block insertions can be toggled on/off | qualitative |
| Templates are built to receive automated data (especially Logs) | qualitative |
| Templates serve as guides for how to build your own templates (show advanced complexity) | qualitative |
| Consistent formatting across all templates | qualitative |

### 3.7 Privacy Canonical Values (PRD §8)

Complete set of `z2k_card_privacy` values that must appear across the library:

| Value | Usage |
|---|---|
| `.:Z2K/Privacy/Default` | General default |
| `.:Z2K/Privacy/Public` | Explicitly public |
| `.:Z2K/Privacy/Private/General` | Generally private |
| `.:Z2K/Privacy/Private/Professional` | Professional context |
| `.:Z2K/Privacy/Private/Implied` | Implicitly private by context |
| `.:Z2K/Privacy/Private/Log` | Logs domain default |
| `.:Z2K/Privacy/Private/Journal` | Journals domain default |
| `.:Z2K/Privacy/Uber-Private/Confidential` | Confidential (e.g., PoND/Bryn) |
| `.:Z2K/Privacy/Uber-Private/SafePlace` | Safe place (e.g., YPO, Doug) |

### 3.8 Source Type Values (PRD §9)

`z2k_card_source_type` is hard-coded per template. Root system-block default: `.:Z2K/SourceType/Unknown`.

Known values: `Book`, `Podcast`, `WebArticle`, `Conversation`, `Meeting`, `InternalThought`, `InternalMemory`, `Quotation`, `Person`, `AI/ChatGPT`, `LifeLessons`, `OtherCards`, `Unknown`.


---

## 4. Reference Document Index

Curated from the migration project's Agent Brief and Implementation Plan. These are the reference manual pages that agents working on CTLv3 templates need.

| Ref ID | Document | Path | Purpose |
|---|---|---|---|
| REF-A | Reference Manual for AI | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md` | **Always load first** — comprehensive AI-friendly reference for all plugin features |
| REF-B | Z2K Card Metadata - YAML | `Docs/z2k-system-docs/4 - Z2K Reference Docs/4b - Data Formats/Z2K Card Metadata - YAML.md` | YAML field structure for Z2K cards |
| REF-C | Intro to System Blocks | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Intro to System Blocks.md` | How system blocks work |
| REF-D | Using System Blocks and fieldInfo | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Using System Blocks and fieldInfo.md` | fieldInfo in system blocks |
| REF-E | System Block Stops | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/System Block Stops.md` | Suppressing system block inheritance (Projects domain) |
| REF-F | formatStringBulletize | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatStringBulletize.md` | Conditional section rendering (Card Fabric) |
| REF-G | Storing Field Values in YAML | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/Storing Field Values in YAML.md` | YAML mirroring for blocks and templates |
| REF-H | z2k_template_suggested_title | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md` | Title expression syntax |
| REF-I | Z2K Metadata Specification v3.0 | `Docs/z2k-design-notes/Z2K System - Design Notes/Z2K Data Architecture/Z2K Metadata/Z2K Metadata Specification - Version 3.0.md` | Source type taxonomy |
| REF-J | formatString | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatString.md` | String formatting helpers |
| REF-K | Template Organization | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Template Folders/Template Organization.md` | Folder structure conventions |
| REF-L | Command Queues Overview | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/Command Queues/Command Queues Overview.md` | How Command Queues work — rendering mechanism for tests |
| REF-M | JSON Packages Overview | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/JSON Packages/JSON Packages Overview.md` | JSON Package format specification |
| REF-N | URI Actions | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/URI Actions/URI Actions.md` | URI-based triggering (fallback) |
| REF-NF | Naming Fields | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Naming Conventions/Naming Fields` | Field naming conventions |


---

## 5. Testing Patterns (from Migration Project)

### 5.1 Command Queue Testing Mechanism

The migration project's confirmed testing approach:

1. Write a JSON command file to the Command Queue watched directory
2. Wait ~8 seconds for auto-processing (scan interval was set to 5-10s)
3. Read the rendered output file directly from the vault filesystem
4. Compare against expected output (golden file model)
5. Clean up output files after verification

**JSON package for document template tests:**
```json
{
  "cmd": "new",
  "templatePath": "<vault-relative path to template>",
  "destDir": "Testing/Output/<test-name>/",
  "fileTitle": "output",
  "prompt": "none",
  "finalize": true,
  "<FieldName>": "<value>"
}
```

**JSON package for block template tests:**
```json
{
  "cmd": "insertblock",
  "blockPath": "<vault-relative path to block>",
  "existingFilePath": "Testing/Output/<test-name>/target.md",
  "location": "file-bottom",
  "prompt": "none",
  "finalize": true,
  "<FieldName>": "<value>"
}
```

### 5.2 Two Test Categories

- **Category A (Structure):** Pure Python — `os.path.exists()`, YAML parsing. No Obsidian needed. Tests file/folder existence, YAML field presence/values, field naming conventions.
- **Category B (Instantiation):** Command Queue dispatch → output polling → golden file diff. Requires running Obsidian instance.

### 5.3 Golden File Model

- First successful run: save output as `expected.md`
- Subsequent runs: auto-diff against `expected.md`
- Dynamic fields normalized before comparison: `{{wikilink today}}` → `<TODAY_WIKILINK>`, `{{timestamp}}` → `<TIMESTAMP>`, `{{wikilink creator}}` → `<CREATOR_WIKILINK>`, `{{wikilink templateName}}` → `<TEMPLATE_WIKILINK>`

### 5.4 Important `templatePath` vs `templateContents`

- **`templatePath`** — resolves from disk, **applies system blocks**. Correct for testing the full chain.
- **`templateContents`** (inline) — does **NOT** apply system blocks. Only for isolated syntax tests.

### 5.5 Key Findings from Migration Testing

- Command Queue is reliable with `prompt: "none"` and `finalize: true`
- 8-second wait after queue drop is sufficient
- 74 automated tests passed (all Category A structure + existence)
- System block YAML delimiters (`---`) are mandatory — without them, fields inject as body text
- `{{!-- --}}` (double-dash) required for comments containing `{{` or `}}`


---

## 6. Resolved Open Issues

Issues that were open during the migration but have since been resolved. Relevant context for the sustaining project.

| Issue ID | Resolution | Impact |
|---|---|---|
| BLK-001 | Dot-notation for prompted fields **unsupported**. Handlebars interprets dots as property access. Workaround: flat names (`ContentAuthor` not `Content.Author`). Plugin issue filed. | All block templates use flat field names |
| DSB-005 | System Block Stops **work correctly** for project subfolders. Per-project `.system-block-stop` files suppress `z2k_*` field inheritance. `My Writings/.system-block-stop` created. | Projects domain templates use non-z2k YAML |
| AI-PERSP | Resolved as `z2k_creation_perspective: "AI"` in AI domain system block | AI domain system block fully specified |
| LOC-001 | `Locations.template` confirmed functionally identical to `Locations - ~Generic`. Merged into `Locations (General).md`. | Single template for Locations domain |
| ST-001 | Source type taxonomy confirmed from Metadata Specification v3.0 | Source type values are authoritative |
| PROJ-YAML | Project template YAML structure confirmed — uses non-z2k fields | Projects templates fully specified |


---

## 7. Validated Plugin Features

Features confirmed working during the migration project (all 9 of 10 tracked features validated):

| Plugin Feature | Status | Notes |
|---|---|---|
| System block YAML injection | Confirmed | Used across all 13 domains + 67 document templates |
| `{{fieldInfo}}` prompting | Confirmed | Used across all block and document templates |
| `{{wikilink creator/today}}` | Confirmed | Works in root system block |
| `{{timestamp}}` | Confirmed | Works in root system block |
| Block partials (`{{> ...}}`) | Confirmed | 13 block templates created and referenced |
| `{{formatStringBulletize}}` | Confirmed | Card Fabric block working |
| System Block Stops | Confirmed | Projects/My Writings isolation working |
| `z2k_template_suggested_title` | Confirmed | All 67 document templates |
| Command Queue testing | Confirmed | 74 automated tests passing |
| `{{dateAdd}}` / `{{formatDate}}` | Confirmed | Date navigation in Journals/Logs templates |
| Dot-notation for prompted fields | **Unsupported** | BLK-001 — Handlebars limitation; flat names used |


---

## 8. Template Best Practices (from Migration Project)

Key learnings distilled from 80 templates across 13 domains:

1. **Folder structure:** `Templates/` subfolders eliminate the need for filename prefixes
2. **System block YAML delimiters mandatory:** Without `---`, fields inject as body text
3. **Comment syntax:** `{{!-- --}}` (double-dash) required when comment body contains `{{` or `}}`
4. **Minimalist system blocks:** Only include domain-universal fields (ratings only in content-rating domains)
5. **Block partials are opt-in:** Include as commented references, not auto-injected
6. **Date helpers compose:** `dateAdd`, `formatDate`, `formatString`, `wikilink` with nested subexpressions enable complex navigation links
7. **Command Queue testing is reliable:** 8-second wait after drop; `prompt: "none"` for fully automated tests
8. **Personal templates distinguished by `z2k_template_author`:** Enables future separation into personal vaults
9. **Flat field names only:** Dot-notation unsupported for prompted fields
10. **Validate plugin features early:** Test each feature before committing to it in templates


---

## 9. AI Recommendations (from AI/Z2K Template Library - AI Recommendations.md)

Additional qualitative and structural insights written by the migration project's AI agents. Relevant items for the qualitative scorecard and cross-cutting requirements:

### 9.1 Additional Qualitative Criteria

| Recommendation | Tag | Notes |
|---|---|---|
| Block templates include a comment listing which document templates consume them | qualitative | Reverse mapping — enables impact analysis when a block changes |
| External/automation fields (e.g., Flame) declared with `{{fieldInfo ... directives="no-prompt"}}` or equivalent | qualitative | Prevents opaque dependencies on external systems |
| Templates reference only existing block partials (`{{> "BlockName"}}` targets must exist) | quantitative | Script-checkable: parse template for partial references, verify target files exist |
| `z2k_card_source_type` values are from the canonical registry | quantitative | Script-checkable against known values list |
| Consistent source type naming conventions (singular nouns vs compound descriptors flagged as inconsistency) | qualitative | Taxonomy consistency across domains |

### 9.2 Structural Recommendations (Future Enhancement Candidates)

These are not requirements for the current library but are tracked as potential future features:

| Recommendation | Source |
|---|---|
| Add `z2k_template_category` and `z2k_template_tags` to template YAML for UI grouping | AI Recommendations §4 |
| Add `z2k_system_block_version` to system blocks for schema change detection | AI Recommendations §4 |
| Domain-level `.template-index.md` for human and AI navigation | AI Recommendations §4 |
| Date-offset navigation link helpers (`{{dateOffset}}` or similar) for Logs/Journals | AI Recommendations §3 |
| Conditional rendering (`{{#if FieldName}}`) for optional sections | AI Recommendations §3 |

### 9.3 Discrepancy Note

The AI Recommendations document (§3) states dot-notation for prompted fields was "confirmed working." This contradicts the Task List, Agent Brief, and Template Best Practices which all record BLK-001 as **unsupported** with flat name workarounds in place. The Task List is authoritative — dot-notation is unsupported. The AI Recommendations doc appears to contain an error on this point.

---

## 10. Successor Project Items (from Post Project/CTLv3 Project)

Items explicitly deferred to the CTLv3 ongoing project:

| ID | Item | Notes |
|---|---|---|
| CTLP-001 | Full Entities CRM templates (Person, Org, Named Entity) | Start with Contact (General) built |
| CTLP-002 | AI domain content templates | AI domain has system-block only |
| CTLP-003 | `{{me}}` built-in field integration | Currently hard-coded `[!me]` |
| CTLP-004 | "Default Template" feature (GH #182) | Currently using `(General)` postfix workaround |
| CTLP-005 | Health Log sub-block decomposition | Currently migrated as single block |
| CTLP-006 | Generic (non-Flame) Daily Log template | Current log is personal/Flame-specific |
| CTLP-007 | Option 4 podcast template (conditional multi-select) | Currently using Option 3 |
| CTLP-008 | `[!me]` vs `[!Geoff]` callout-type resolution | v3 uses `[!me]` as portable standard |
