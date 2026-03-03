---
document_type: Implementation Plan
status: Locked
---
# Implementation Plan — Z2K Template Library v3 Migration


## Overview

This plan breaks the Project Requirements into sequenced implementation phases. Each phase produces specific artifacts, requires specific reference documentation to be read first, and has explicit acceptance criteria. Phases are ordered by dependency — Phase N output is input to Phase N+1.

**Execution order:**
1. Vault Structure → 2. Root System Block → 3. Domain System Blocks → 4. Root Blocks → 5. Domain Blocks → 6. Templates (by domain) → 7. Supporting Docs → 8. Cleanup

**Draft tasks:** Some implementation tasks do not yet have detailed plans. These are marked `(Draft)` and will be fleshed out as they become next in the priority queue per the IF Model (see Prioritization and Dependencies section below).

**Template conversion approach (applies to all Phase 6 tasks):**
For each v2 template:
1. Read the source file from `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/<filename>`
2. Apply API Translation table (Requirements §3)
3. Add v3 YAML metadata (`z2k_template_type`, `z2k_template_version`, `z2k_template_author`, `z2k_template_suggested_title`)
4. Add `{{fieldInfo}}` declarations for all user-defined fields
5. Convert `%% ... %%` comments to `{{! ... }}`
6. Convert `G:` prefixes to `[!me]` / `Me:`
7. Replace Card Fabric section with opt-in block comment: `{{! To include Card Fabric: {{> "Card Fabric"}} }}`
8. **Templater code:** Only replace `<% ... %>` syntax when a clear v3 equivalent exists. Preserve verbatim any code that cannot be cleanly converted; wrap with `{{! FLAGGED: <explanation> }}` and notify the user.
9. Write to target path in `Data/Vaults/z2k-default-vault/`

> **Note:** Task target filenames follow the no-prefix convention per REQ-NM-001/002. Block templates: `<Name>.md` (no `Block -` prefix). Document templates: `<Name>.md` (no `Template -` prefix). Domain defaults use `<DomainName> (General).md`.

---

## Reference Docs Index

The following reference documents are called out per task. AI agents should read these on demand when executing the relevant task, not all upfront.

| Ref ID | Document | Used in |
|---|---|---|
| REF-A | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md` | All phases (already loaded at session start) |
| REF-B | `Docs/z2k-system-docs/4 - Z2K Reference Docs/4b - Data Formats/Z2K Card Metadata - YAML.md` | Phase 2 (root system-block) |
| REF-C | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Intro to System Blocks.md` | Phase 2, 3 |
| REF-D | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Using System Blocks and fieldInfo.md` | Phase 2, 3 |
| REF-E | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/System Block Stops.md` | Phase 3 (Projects domain only) |
| REF-F | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatStringBulletize.md` | Phase 4 (Card Fabric block) |
| REF-G | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/Storing Field Values in YAML.md` | Phase 4 (blocks), Phase 6 (inline :: templates) |
| REF-H | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md` | Phase 6 |
| REF-I | `Docs/z2k-design-notes/Z2K System - Design Notes/Z2K Data Architecture/Z2K Metadata/Z2K Metadata Specification - Version 3.0.md` | Phase 6 (Information templates — source types) |
| REF-J | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatString.md` | Phase 6 (as needed) |
| REF-K | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Template Folders/Template Organization.md` | Phase 1 (verify structure) |
| REF-L | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/Command Queues/Command Queues Overview.md` | Phase 0 (Testing Infrastructure) |
| REF-M | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/JSON Packages/JSON Packages Overview.md` | Phase 0 (Testing Infrastructure) |
| REF-N | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/URI Actions/URI Actions.md` | Phase 0 (Testing Infrastructure, URI fallback) |

---

## Prioritization and Dependencies

This section defines the priority and dependency ordering for IF execution. It governs which tasks to run first (the "punch-through" order) and which Z2K Templates Plugin features are required at each phase.

### Tooling Priority (Z2K Templates Plugin)

The following plugin capabilities are required for this project, listed in the order they must be validated — each gates subsequent implementation:

| Priority | Plugin Capability | Required By | Notes |
|---|---|---|---|
| P1 | System block YAML injection (merge into card) | Phase 2, 3 | Most foundational; all templates depend on this |
| P1 | `{{fieldInfo}}` basic prompting | Phase 4, 6 | Required for any template with user-prompted fields |
| P1 | `{{wikilink creator}}` / `{{wikilink today}}` / `{{timestamp}}` | Phase 2 | Core system-block built-ins |
| P2 | Block partial inclusion (`{{> BlockName}}`) | Phases 4, 5, 6 | Required for block templates |
| P2 | `{{formatStringBulletize}}` | Phase 4 (Card Fabric) | Required for Card Fabric block |
| P2 | Dot-notation for prompted fields (`Fabric.MentalModel`) | Phase 4+ | Untested; fallback ready; see BLK-001 |
| P3 | System Block Stops | Phase 3 (Projects only) | Required for Projects domain suppression |
| P3 | `z2k_template_suggested_title` YAML expression | Phase 6 | Required for all document templates |
| P4 | Command Queue / automated testing | Phase 0 (TP-0.1) | Needed for test automation; validate in Phase 0 |

### Requirements Priority

General priority ordering for requirements — drives punch-through sequencing:

1. Vault structure (all domain folders, root `Templates/`) — blocks everything else
2. Root system block — blocks all domain work
3. Domain system blocks — blocks all template work per domain
4. Root block templates (Perspective, Quotation, Citation, Card Fabric, Extended YAML) — blocks any template using these blocks
5. Domain block templates — blocks templates that include domain blocks
6. Document templates — the primary deliverable; execute by domain in dependency order (simplest/fewest dependencies first)
7. Supporting docs — after all templates complete

**Recommended first punch-through (minimal viable chain):**
Execute this sequence first to validate the full IF end-to-end before scaling:
- Task 1.5 (Root Templates/ folder) + Task 1.3 (System/Templates/) + Task 1.6 partial (Beliefs/Templates/)
- Task 2.1 (Root system block)
- Task 3.3 (Beliefs system block) — simplest domain; no extra fields
- Task 6.2 (Beliefs templates — 1 template, minimal complexity)
- Validate in Obsidian: confirm system block + `{{fieldInfo}}` prompting + template instantiation all work

Subsequent iterations expand outward using the dependency graph and importance levels from the PRD.

### Z2K Templates Feature Prioritization

> **Living artifact.** Populated and refined as tasks are executed and plugin feature requirements are confirmed. When sufficiently complete, this list will be shared with the Z2K Templates Plugin developer to guide plugin development priorities.

| Plugin Feature | Tasks Requiring It | Validated? | Notes |
|---|---|---|---|
| System block YAML injection | Phases 2, 3, all Phase 6 | ✅ | Confirmed Task 03; used in all 13 domain system blocks and 67 document templates |
| `{{fieldInfo}}` prompting | Phases 4, 5, 6 | ✅ | Confirmed Task 07; used across all block and document templates |
| `{{wikilink creator/today}}` | Phase 2 | ✅ | Confirmed Task 03; works in root system block |
| `{{timestamp}}` | Phase 2 | ✅ | Confirmed Task 03; works in root system block |
| Block partials (`{{> ...}}`) | Phases 4, 5, 6 (blocks) | ✅ | Confirmed Tasks 07–09; 13 block templates created and referenced |
| `{{formatStringBulletize}}` | Phase 4 (Card Fabric) | ✅ | Confirmed Task 07; Card Fabric block working |
| Dot-notation for prompted fields | Phase 4+ | ❌ | **Unsupported.** BLK-001 filed. Handlebars interprets dots as property access. Workaround: flat field names (`ContentAuthor` instead of `Content.Author`) |
| System Block Stops | Phase 3 (Projects) | ✅ | Confirmed Task 06; `.system-block-stop` files work for Projects/My Writings isolation |
| `z2k_template_suggested_title` | Phase 6 | ✅ | Confirmed across all 67 document templates |
| Command Queue / automated testing | Phase 0 (TP-0.1) | ✅ | Confirmed Task 01; 74 automated tests passing via Command Queue |
| `{{dateAdd}}` / `{{formatDate}}` | Phase 6 (Journals, Logs) | ✅ | Confirmed Tasks 16–17; date navigation links working with nested subexpressions |

### Feature Prioritization — Handoff Summary

**For the Z2K Templates Plugin developer:**

9 of 10 originally tracked plugin features are validated and working correctly in the CTLv3 template library (80 templates, 74 automated tests). The one failure — **dot-notation for prompted field names** (BLK-001) — is a Handlebars limitation rather than a plugin bug, but supporting escaped or quoted field names (e.g., `{{fieldInfo "Content.Author" "prompt"}}`) would enable cleaner namespacing for complex templates. A workaround (flat names) is in place and does not block any functionality.

One additional feature was discovered and validated during execution: `{{dateAdd}}` and `{{formatDate}}` for date arithmetic in navigation links.

**No blocking bugs were discovered.** The plugin is production-ready for the CTLv3 template library as built. See `Issues/Z2K Templates Plugin/` for the full issue log (1 issue, BLK-001, with workaround).

---

## Phase 0 — Testing Infrastructure Validation

**Goal:** Establish a confirmed, working path for automated template testing before execution begins. Determine whether Command Queues or URIs will serve as the primary mechanism, create the CTL v3 testing vault, and produce a minimal passing end-to-end test.

**Reference docs to read first:** REF-L (Command Queues Overview), REF-M (JSON Packages Overview), REF-N (URI Actions)

**Dependency:** None — can be executed independently; does not require vault structure changes.

**Testing vault:** A new dedicated vault will be created for CTL v3 testing: `Data/Vaults/z2k-testing-vaults/Z2K System Vault Testing/`. This vault is separate from the existing `Templates Test Vault - Primary/` (maintained by another developer — do not modify).

**Testing scripts:** All CTL v3 test scripts live in the project's `Testing/` subfolder:
`Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/Testing/`

**Two automation mechanisms to evaluate:**
- **Command Queues** (preferred): Drop `.json`/`.jsonl` files into a watched folder; plugin processes automatically. Enables batch testing.
- **URI Actions** (fallback): Fire Obsidian URIs from shell scripts; Obsidian must be running. The existing `scripts/run-tests.py` in `z2k-testing-vaults/` uses this approach (read-only reference — do not modify).

### Task TP-0.1 — Create CTL v3 Testing Vault

- **Action:** Create a new Obsidian vault at `Data/Vaults/z2k-testing-vaults/Z2K System Vault Testing/`
  - Create vault root and `.obsidian/` config directory
  - Install Z2K Templates Plugin (copy from existing vault's `.obsidian/plugins/z2k-plugin-templates/` or install fresh)
  - Configure plugin with minimal settings (creator name, templates folder name)
  - Enable Command Queue: Settings → Z2K Templates → Command Queue Settings
  - Set queue folder (recommended: `.obsidian/plugins/z2k-plugin-templates/command-queue/`)
  - Set scan frequency to 10s for fast test turnaround
- **Acceptance:** Vault opens in Obsidian; Z2K Templates Plugin is active; Command Queue is enabled

> ⚠️ **User assist required at this task:** Opening a new vault in Obsidian and confirming the plugin is active requires user interaction. This is the primary setup gate; all subsequent tasks can be automated.

### Task TP-0.2 — Validate Command Queue with Hello World Test

- **Action:** Write and execute a minimal Command Queue test against a simple inline template
  - Script location: `Testing/scripts/tp-0-hello-world.py`
  - Use `templateContents` directive (inline template, no file needed): a trivial template with one field and `{{fieldInfo}}`
  - JSON package: `{"cmd": "new", "templateContents": "Hello {{Name}}!", "fileTitle": "hello-world-output", "prompt": "none", "finalize": true, "Name": "World"}`
  - Write to queue folder; trigger "Process Command Queue Now" from Obsidian Command Palette (user-assisted first run)
  - Verify: output file `hello-world-output.md` created in vault root; command moved to `done/`
- **Open question:** Determine whether "Process Command Queue Now" can be triggered via URI or external macOS mechanism (AppleScript, `open` command with Obsidian URI) to eliminate manual trigger requirement. Document findings.
- **Failure path:** If Command Queue fails or cannot be triggered non-interactively, evaluate URI fallback per TP-0.3

### Task TP-0.3 — Evaluate URI Fallback (If Needed)

- **Action:** If TP-0.2 reveals blocking issues, test URI-based triggering as fallback
  - Build a minimal Python script in `Testing/scripts/` that fires an Obsidian `obsidian://z2k-templates` URI via `subprocess.run(["open", uri])`
  - Use same hello-world template via `templateContents` + URI `fromJson` command
  - Wait for output file, assert content matches expected
- **Skip condition:** Skip if TP-0.2 fully succeeds and Command Queue is confirmed as viable

### Task TP-0.4 — Select Primary Testing Method and Document Findings

- **Action:** Based on TP-0.2 and TP-0.3 results:
  - Select primary testing method: Command Queue (preferred) or URI (fallback)
  - Document any plugin bugs → log to `Issues/Z2K Templates Plugin/`
  - Update Z2K Templates Feature Prioritization table with validated status
  - Findings feed directly into the Testing Plan (Phase 4 deliverable)

**Phase 0 Acceptance:** New testing vault exists and has Z2K Templates Plugin active with Command Queue enabled. At least one template instantiation test passes end-to-end. Primary testing method confirmed and documented. Testing Plan can now be drafted against a known-working approach.

---

## Phase 1 — Vault Structure

**Goal:** Create all missing folders so subsequent phases have valid target locations.

**Reference docs:** REF-K (verify structure expectations)

**Pre-read:** Confirm current vault folder state with `ls Data/Vaults/z2k-default-vault/` before creating.

### Task 1.1 — Create Body Domain
- **Action:** Create `Body/` and `Body/Templates/`
- **Target:** `Data/Vaults/z2k-default-vault/Body/`, `Data/Vaults/z2k-default-vault/Body/Templates/`
- **Acceptance:** Both folders exist; no content yet

### Task 1.2 — Create AI Domain
- **Action:** Create `AI/` and `AI/Templates/`
- **Target:** `Data/Vaults/z2k-default-vault/AI/`, `Data/Vaults/z2k-default-vault/AI/Templates/`
- **Acceptance:** Both folders exist; no content yet

### Task 1.3 — Create System/Templates/
- **Action:** `System/` exists; create `System/Templates/` subfolder
- **Target:** `Data/Vaults/z2k-default-vault/System/Templates/`
- **Acceptance:** Folder exists

### Task 1.4 — Create Projects/My Writings
- **Action:** Create `Projects/My Writings/` and `Projects/My Writings/Templates/`
- **Target:** `Data/Vaults/z2k-default-vault/Projects/My Writings/`, `.../Templates/`
- **Acceptance:** Both folders exist

### Task 1.5 — Create Root Templates/ Folder
- **Action:** Create `Templates/` at vault root
- **Target:** `Data/Vaults/z2k-default-vault/Templates/`
- **Acceptance:** Folder exists

### Task 1.6 — Audit Existing Domain Templates/ Subfolders
- **Action:** For each existing domain (Beliefs, Entities, Information, Interactions, Journals, Locations, Logs, Memories, Projects, Thoughts), confirm `Templates/` subfolder exists. Create any that are missing.
- **Acceptance:** All 10 existing domains have a `Templates/` subfolder

**Phase 1 Acceptance:** `ls Data/Vaults/z2k-default-vault/` shows all 13 domains + `Templates/` at root; all domains have `Templates/` subfolders; `Projects/My Writings/Templates/` exists.

---

## Phase 2 — Root System Block

**Goal:** Rewrite the root `.system-block.md` to v3 schema.

**Reference docs to read first:** REF-B (Z2K Card Metadata YAML), REF-C (System Block Intro), REF-D (System Blocks + fieldInfo)

**Pre-read:** Current root system-block at `Data/Vaults/z2k-default-vault/.system-block.md` (already read in this session — see current state below).

**Current state of root system-block (read 2026-03-02):**
```yaml
z2k_metadata_version:     3.00
z2k_metadata_variant:     "barebones"
z2k_metadata_copyright:   "Z2K Metadata structure is © 2025 Z2K Studios, LLC"
z2k_metadata_reference:   "https://z2ksystem.com/specs/v3.0"
z2k_creation_creator:     "{{wikilink creator}}"
z2k_creation_date:        "{{wikilink today}}"
z2k_creation_timestamp:   "{{timestamp}}"
z2k_creation_template:    "{{wikilink templateName}}"
z2k_creation_domain:      ".:Z2K/Domain/{{normalizePath destPath}}"  ← REMOVE (unsupported helper)
z2k_creation_language:    "en"
z2k_card_build_state:     ".:Z2K/BuildState/Uninitialized"           ← REMOVE
z2k_card_status:          ".:Z2K/Status/Ongoing"                     ← REMOVE (resolved: no default status value in root system-block)
z2k_card_source_type:     ".:Z2K/SourceType/Unknown"                 ← KEEP (root default)
```

### Task 2.1 — Rewrite Root System Block

- **Source:** Current `Data/Vaults/z2k-default-vault/.system-block.md`
- **Target:** Same file (in-place rewrite)
- **Changes:**
  - **REMOVE:** `z2k_creation_domain` line (uses unsupported `normalizePath` helper; domain moved to per-domain system-blocks)
  - **REMOVE:** `z2k_card_build_state` line
  - **REMOVE:** `z2k_card_status` line (resolved: no default status value in root system-block)
  - **ADD:** `z2k_creation_library_version: "3.0.0"` (after `z2k_creation_language`)
  - **ADD:** `{{fieldInfo me value="me"}}` (below the YAML block, in the template body section)
  - **RETAIN:** All other fields unchanged
- **Reference docs:** REF-B, REF-C, REF-D

**Acceptance:** Root system-block has no `normalizePath`, no `z2k_card_build_state`, no `z2k_card_status`, has `z2k_creation_library_version: "3.0.0"`, has `{{fieldInfo me value="me"}}`, and all retained fields are present.

---

## Phase 3 — Domain System Blocks

**Goal:** Write a `.system-block.md` for each of the 13 domains.

**Reference docs to read first:** REF-C, REF-D; REF-E for Projects domain only.

**Dependency:** Phase 1 must be complete (domain folders must exist).

**Common pattern for all domain system-blocks:**
```yaml
# Z2K Domain Identity
z2k_creation_domain: ".:Z2K/Domain/<DomainName>"
```
Each domain system-block is placed at `Data/Vaults/z2k-default-vault/<Domain>/.system-block.md`.

### Task 3.1 — Information System Block
- **Target:** `Information/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Information"` + ratings fields (`z2k_rating_depth`, `z2k_rating_surprisal`, `z2k_rating_passion`)
- **Ref:** REF-C, REF-D

### Task 3.2 — Thoughts System Block
- **Target:** `Thoughts/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Thoughts"` + ratings fields
- **Ref:** REF-C, REF-D

### Task 3.3 — Beliefs System Block
- **Target:** `Beliefs/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Beliefs"` + ratings fields
- **Ref:** REF-C, REF-D

### Task 3.4 — Memories System Block
- **Target:** `Memories/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Memories"` + ratings fields
- **Ref:** REF-C, REF-D

### Task 3.5 — Interactions System Block
- **Target:** `Interactions/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Interactions"`
- **Ref:** REF-C, REF-D

### Task 3.6 — Journals System Block
- **Target:** `Journals/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Journals"` + `z2k_card_privacy: ".:Z2K/Privacy/Private/Journal"`
- **Ref:** REF-C, REF-D

### Task 3.7 — Logs System Block
- **Target:** `Logs/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Logs"` + `z2k_card_privacy: ".:Z2K/Privacy/Private/Log"`
- **Ref:** REF-C, REF-D

### Task 3.8 — Locations System Block
- **Target:** `Locations/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Locations"`

### Task 3.9 — Entities System Block
- **Target:** `Entities/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Entities"`

### Task 3.10 — Body System Block
- **Target:** `Body/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Body"`

### Task 3.11 — AI System Block
- **Target:** `AI/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/AI"` + authorship/perspective field indicating AI-originated content
- **Note:** Decide appropriate field name/structure for AI authorship. Candidate: a `z2k_creation_perspective: "AI"` field or a YAML comment noting AI default perspective.

### Task 3.12 — System Domain System Block
- **Target:** `System/.system-block.md`
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/System"`

### Task 3.13 — Projects System Block + Block Stop
- **Target:** `Projects/.system-block.md`; System Block Stop files in project subfolders
- **Contents:** `z2k_creation_domain: ".:Z2K/Domain/Projects"` for the Projects-level system-block; System Block Stop files inside project subdirectories to suppress z2k_* fields
- **Reference docs:** REF-C, REF-D, **REF-E (required — read before this task)**

> ⚠️ OPEN ISSUE (DSB-005): The goal of completely suppressing `z2k_*` fields in project subfolder cards may not be fully achievable with current system-block architecture. System Block Stops can prevent system-block injection in subfolders, but project templates may still need to carry their own override YAML. Read REF-E and confirm behavior before executing this task. Document findings here.
>
> **Known constraint from Q&A:** "Note: that system block stop only works for sub folders — but that is fine here. You can assume the projects folder will have many subfolders for projects. You want system block suppression to occur for each of them."

**Phase 3 Acceptance:** All 13 domains have a `.system-block.md` file. Each file has `z2k_creation_domain` correctly set. Ratings domains have ratings fields. Journals/Logs have privacy fields. Projects system-block + block stop strategy documented and implemented per REF-E findings.

---

## Phase 4 — Root-Level Block Templates

**Goal:** Build 5 shared block partials in the root `Templates/` folder.

**Reference docs to read first:** REF-F (formatStringBulletize), REF-G (Storing Field Values in YAML), REF-A (already loaded)

**Dependency:** Phase 1 must be complete (root `Templates/` folder must exist).

### Task 4.1 — Block - Perspective - Me
- **Target:** `Templates/Perspective - Me.md`
- **Contents:** Standard `[!me]` callout block template — the vault owner's perspective marker
  ```
  > [!me]
  > {{PerspectiveText}}
  ```
  With `{{fieldInfo PerspectiveText "Your perspective or commentary" type="text"}}`
- **Ref:** REF-A

### Task 4.2 — Block - Quotation
- **Target:** `Templates/Quotation.md`
- **Fields:** `Content.Author`, `Content.Title`, `Content.Text` (attempt dot-notation; fallback flat names if unsupported)
- **Structure:** Blockquote + attribution line + optional `[!me]` perspective section
- **Ref:** REF-A, REF-G

> ⚠️ TEST POINT (BLK-004): At the start of this task, test whether `{{fieldInfo Content.Author "Author of the content?"}}` causes the prompt to appear correctly in Obsidian. If dot-notation is unsupported for prompted user fields, use `ContentAuthor`, `ContentTitle`, `ContentText` as flat names and log a plugin bug.

### Task 4.3 — Block - Citation
- **Target:** `Templates/Citation.md`
- **Fields:** `Content.Author`, `Content.Title`, `Content.Source`, `Content.URL`, `Content.Date` (same namespace as Quotation block)
- **Note:** Field names must be identical to Quotation block where they overlap, so YAML pre-fill works when inserting either block into the same card
- **Ref:** REF-A, REF-G

### Task 4.4 — Block - Card Fabric
- **Target:** `Templates/Card Fabric.md`
- **Fields:** `Fabric.MentalModel`, `Fabric.Contextual`, `Fabric.Reference`, `Fabric.GeoContext`
- **Structure:** Use `{{formatStringBulletize}}` to conditionally output each section header (section only appears if field has content). Build both a YAML array section and a markdown body section.
- **Ref:** REF-A, REF-F, REF-G
- **Example pattern from Q&A:**
  ```
  {{fieldInfo Fabric.MentalModel "Mental models used? (one per line)"}}
  ## Fabrics
  {{formatStringBulletize Fabric.MentalModel 0 "#### Mental Models\n"}}
  ```

> ⚠️ TEST POINT (BLK-001): Test dot-notation for `Fabric.MentalModel` as a prompted field (same test as BLK-004 — if Quotation block test already ran, apply result here). If flat names are required, use `FabricMentalModel`, `FabricContextual`, `FabricReference`, `FabricGeoContext`.

### Task 4.5 — Block - Extended YAML
- **Target:** `Templates/Extended YAML.md`
- **Contents:** Extended set of YAML fields for power users — includes: privacy, project links, structures, ratings arrays, fabric YAML arrays
- **Usage:** User manually inserts via `{{> "Extended YAML"}}`; never auto-injected
- **Ref:** REF-A, REF-G

**Phase 4 Acceptance:** All 5 block files exist in `Templates/`. Each has `z2k_template_type: block-template`. Quotation and Citation blocks use consistent `Content.*` field names. Card Fabric block uses `{{formatStringBulletize}}` correctly. Dot-notation test result recorded (pass or fail + fallback applied if needed).

---

## Phase 5 — Domain-Level Block Templates

**Goal:** Build 8 domain-specific block partials.

**Reference docs:** REF-A (loaded), REF-F (formatStringBulletize as needed), REF-G (YAML field storage)

**Dependency:** Phase 1 complete (domain `Templates/` folders must exist).

### Task 5.1 — Block - Podcast Interview Content (Information)
- **Target:** `Information/Templates/Podcast Interview Content.md`
- **Contents:** Core structure for podcast interview cards. Sections: Key Quotes, Key Takeaways, Personal Synthesis, Background/Context, Episode Details. Fields for Interviewer, Interviewee, Episode Title, Date, URL.
- **Architecture note (Option 3):** This block is included by host-specific templates via `{{> "Podcast Interview Content"}}`. The host-specific template sets fixed field values (host name, show name, default tags) BEFORE the block inclusion. The block itself is generic.
- **Source reference:** `Information - Podcast Interview` (v2) for field names and section structure
- **Ref:** REF-A

### Task 5.2 — Block - Information - Summary (Information)
- **Target:** `Information/Templates/Information - Summary.md`
- **Contents:** Summary section — one-paragraph abstract of the source content

### Task 5.3 — Block - Information - Overview (Information)
- **Target:** `Information/Templates/Information - Overview.md`
- **Contents:** Overview section — structured breakdown of main points or chapters

### Task 5.4 — Block - Information - Synthesis (Information)
- **Target:** `Information/Templates/Information - Synthesis.md`
- **Contents:** Personal synthesis section — vault-owner's analysis and takeaways (uses `[!me]` callout)

### Task 5.5 — Block - Information - Details (Information)
- **Target:** `Information/Templates/Information - Details.md`
- **Contents:** Details section — granular notes, highlights, or direct quotes from the source

### Task 5.6 — Block - Logistics (Interactions)
- **Target:** `Interactions/Templates/Logistics.md`
- **Contents:** When/Where/Who/Recorded fields — standard context section for all interaction cards
- **Source reference:** `Interactions - Business Meeting` (v2) for logistics section structure

### Task 5.7 — Block - When Where Who (Memories)
- **Target:** `Memories/Templates/When Where Who.md`
- **Contents:** Date, Location, Who Was Present — context anchor for memory cards

### Task 5.8 — Block - Health Log (Body)
- **Target:** `Body/Templates/Health Log.md`
- **Source:** `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/~Partial - Health Log.md`
- **Action:** Migrate as-is; convert v2 syntax to v3; preserve all Flame field names exactly
- **Note:** All `{{Flame-*}}` field names preserved without change — they correspond to a Google Forms / CSV import automation system. A more generic public version is a future task.
- **Ref:** REF-A

**Phase 5 Acceptance:** All 8 block files exist in their domain `Templates/` folders. Each has `z2k_template_type: block-template`. Health Log Flame fields are preserved verbatim.

---

## Phase 6 — Document Templates (by domain)

**Goal:** Migrate all v2 templates to v3 and build new templates.

**Reference docs to read first (for this phase as a whole):**
- REF-A (loaded)
- REF-H (`z2k_template_suggested_title` — confirm YAML expression syntax)
- REF-I (Metadata Specification v3.0 — **required before Information domain tasks; read source type taxonomy**)

**Dependency:** Phases 1–5 complete. For each domain: domain `Templates/` folder and domain system-block must exist.

**Execution order:** Thoughts → Beliefs → Information → Interactions → Memories → Locations → Journals → Logs → Projects → Body → System → Entities

### Task 6.1 — Thoughts Templates (7 templates)
- **Source files:** `Thoughts - ~Generic`, `Thoughts - Book - Quote`, `Thoughts - Concept - Book`, `Thoughts - General - Quote`, `Thoughts - Ontology`, `Thoughts - Quote a Source`, `Thoughts - Resolutions`
- **Targets:** `Thoughts/Templates/` —
  - `Thoughts (General).md` ← from `Thoughts - ~Generic`
  - `Book Quote.md` ← from `Thoughts - Book - Quote`
  - `Book Concept.md` ← from `Thoughts - Concept - Book`
  - `General Quote.md` ← from `Thoughts - General - Quote`
  - `Ontology.md` ← from `Thoughts - Ontology`
  - `Quote a Source.md` ← from `Thoughts - Quote a Source`
  - `Resolutions.md` ← from `Thoughts - Resolutions`
- **Source type:** `.:Z2K/SourceType/InternalThought` for most; `.:Z2K/SourceType/Quotation` for quote templates
- **Ref:** REF-A, REF-H

### Task 6.2 — Beliefs Templates (1 template)
- **Source:** `Beliefs - ~Generic`
- **Target:** `Beliefs/Templates/Beliefs (General).md`
- **Source type:** `.:Z2K/SourceType/InternalThought`
- **Ref:** REF-A, REF-H

### Task 6.3 — Information Templates (21 templates)

> ⚠️ **PREREQUISITE:** Read REF-I (Metadata Specification v3.0) before this task to confirm canonical `z2k_card_source_type` values. The placeholder values in Requirements §9 may not match v3 canonical names.

- **Generic + academic templates (5):** `Information (General).md`, `Academic Paper.md`, `Blinkist.md`, `Book.md`, `Kindle Notes.md`
- **Lecture/Conference/Interview (3):** `Conference.md`, `Lecture.md`, `Interview.md`
- **Web + Wikipedia (2):** `Web Article.md`, `Wikipedia Entry.md`
- **Quotation/Email (3):** `Quotation.md`, `Quote a Source.md`, `Quote an Email.md`
- **Ontology (1):** `Ontology.md`
- **Podcast — generic (1):** `Podcast Interview.md` (generic template; uses Podcast Interview Content block)
- **Podcast — host-specific (6):** `Podcast Interview - Adam Grant.md`, `Podcast Interview - Dwarkesh Patel.md`, `Podcast Interview - Huberman Lab.md`, `Podcast Interview - Knowledge Project.md`, `Podcast Interview - Lex Fridman.md`, `Podcast Interview - Tim Ferriss.md`
  - Each presets: `{{fieldInfo Host value="<HostName"}}`, `{{fieldInfo ShowName value="<ShowName>"}}`, default tags
  - Then includes: `{{> "Podcast Interview Content"}}`
- All targets in: `Information/Templates/`
- **Ref:** REF-A, REF-H, REF-I

### Task 6.4 — Interactions Templates (12 templates)

- **Generic + business (3):** `Interactions (General).md`, `Business Meeting.md`, `Email.md`
- **Class (2):** `Class Lecture.md`, `Class Overview.md`
- **Conversation (2):** `Conversation.md`
- **Personal (6):** `Amateur Hour.md`, `Conversation with Doug.md`, `Conversation with John Kashiwabara.md`, `PoND Conversation with Bryn.md`, `YPO Event.md`, `YPO Forum.md`
- All targets in: `Interactions/Templates/`
  - Personal templates use `z2k_template_author: "Geoff (z2k-gwp)"`
  - Apply correct `z2k_card_privacy` values per Requirements §8
  - Preserve hardcoded personal specifics (names, group details) — these are intentionally personal
- **Include Logistics block:** All interaction templates should include `{{> "Logistics"}}`
- **Ref:** REF-A, REF-H

### Task 6.5 — Memories Templates (5 templates)

- **Source files:** `Memories - ~Generic`, `Memories - Family Vacation Trip`, `Memories - Ontology`, `Memories - PCT Trail Day`, `Memories - Solo Trip Summary`
- **Targets:** `Memories/Templates/` —
  - `Memories (General).md` ← from `Memories - ~Generic`
  - `Family Vacation Trip.md` ← from `Memories - Family Vacation Trip`
  - `Ontology.md` ← from `Memories - Ontology`
  - `PCT Trail Day.md` ← from `Memories - PCT Trail Day`
  - `Solo Trip Summary.md` ← from `Memories - Solo Trip Summary`
- **Drop:** `Memories - Quote an Email` (per Q8 decision)
- **Include When-Where-Who block:** All memory templates include `{{> "When Where Who"}}`
- **PCT Trail Day:** personal template; preserve hardcoded start mileage and trip context
- **Ref:** REF-A, REF-H

### Task 6.6 — Locations Templates (1–2 templates)

> ⚠️ **PREREQUISITE (LOC-001):** Read both `Locations - ~Generic` and `Locations.template` from the v2 source. If they are functionally identical, create one `Locations (General).md`. If different, create appropriately named templates for each.

- **Target:** `Locations/Templates/Locations (General).md` (at minimum; second template named appropriately if LOC-001 confirms distinct content)
- **Ref:** REF-A, REF-H

### Task 6.7 — Journals Templates (2 templates)

- **Source:** `~Journals - Daily`, `~Journals - Yearly Summaries`
- **Targets:** `Journals/Templates/Daily Journal.md`, `Journals/Templates/Yearly Summary.md`
- **Daily Journal special requirement:** Must include `## Passing Thoughts`, `## Passing Memories`, `## Passing Information` sections. These absorb the retired Ideas domain — passing captures that don't warrant a full card go here.
- **Privacy:** Journals domain system-block sets `Private/Journal` — no per-template override needed unless specific journal has different privacy
- **Ref:** REF-A, REF-H

### Task 6.8 — Logs Templates (6 templates)

- **Source files:** `~Logs - Daily`, `~Logs - Monthly`, `~Logs - Quarterly Focus List`, `~Logs - Weekly`, `~Logs - Yearly`, `~Logs - Yearly Strategic Plan`
- **Targets:** `Logs/Templates/` —
  - `Daily Log.md`, `Monthly Log.md`, `Quarterly Focus List.md`, `Weekly Log.md`, `Yearly Log.md`, `Yearly Strategic Plan.md`
- **Daily Log special requirement:** Preserve all `{{Flame-*}}` field references exactly as-is. These are populated by an external Google Forms / CSV import automation (z2k-sheet-importer plugin). Use `directives="no-prompt"` or leave as plain field references for each Flame field — do NOT prompt the user for them.
- **Privacy:** Logs domain system-block sets `Private/Log` — no per-template override needed
- **Ref:** REF-A, REF-H

### Task 6.9 — Projects Templates (3 new + 4 My Writings)

**Projects root templates (3 new templates):**
- `Projects/Templates/Project (General).md`
- `Projects/Templates/Active Project.md`
- `Projects/Templates/Completed Project.md`

These use a **different YAML structure** (no `z2k_*` fields — project-specific metadata only). Design the YAML for project cards: fields like `goal`, `status`, `start_date`, `stakeholders`, `outcomes`. Do not include standard `z2k_metadata_*`, `z2k_creation_*` fields.

> ⚠️ OPEN ISSUE (DSB-005): After executing Task 3.13 (Projects system block + block stop), confirm whether the system-block suppression successfully prevents z2k_* field injection in project subfolder cards. If not, these templates must include YAML that overrides the injected fields. Document findings and implementation approach here.

**My Writings templates (4 templates):**
- `Projects/My Writings/Templates/My Writings (General).md` ← from Syntheses - ~Generic
- `Projects/My Writings/Templates/Personal Writing.md` ← from Syntheses - Extended Journal Writing
- `Projects/My Writings/Templates/Treatise.md` ← from Syntheses - Treatise
- `Projects/My Writings/Templates/Code Poem.md` ← from Project - Code Poetry - Poem (personal)

- **Drop:** `Syntheses - Quote an Email` (per Q2 decision)
- **"(General)" naming note:** `My Writings (General).md` is the workaround for GH issue #182 (Default Template feature). Once that feature ships, the `(General)` postfix can be dropped (tracked as CTLP-004).
- **Ref:** REF-A, REF-H, REF-E (for block stop behavior)

### Task 6.10 — Body Templates (1 template + 1 block)

- **Template:** `Body/Templates/Body (General).md` ← from `Body - ~Generic`
- **Block:** Done in Phase 5, Task 5.8 — no action needed here
- **Ref:** REF-A, REF-H

### Task 6.11 — System Templates (1 template)

- **Source:** `~System - ~Generic`
- **Target:** `System/Templates/System (General).md`
- **Drop:** `~System - Testing` (testing artifact, not a real template)
- **Ref:** REF-A, REF-H

### Task 6.12 — Entities Templates (1 new template)

- **Target:** `Entities/Templates/Contact (General).md` (new — build from scratch)
- **Minimal fields:** Name, Role, Organization, Relationship to vault owner, First Met date, Tags, Notes
- **Note:** Full CRM template set (Person, Organization, Named Entity) is deferred to a future project
- **Ref:** REF-A, REF-H

### Task 6.13 — AI Templates
- **Action:** None — AI domain gets system-block only (Phase 3, Task 3.11). Template content deferred to future project.

### Task 6.14 — Root Cross-Domain Templates

The root `Templates/` folder holds cross-domain document templates usable across any domain. It will expand as patterns are identified during implementation.

**Current in-scope templates:**

- **`Templates/Card (General).md`** — migrated from `~Generic Card Template` (v2); cross-domain generic card
- **`Templates/Ontology.md`** — new; cross-domain generic Map of Content / index card (domain-specific variants exist in Thoughts, Information, and Memories; this is the root-level generic applicable to any domain)

**Evaluate during this phase:**
- `Templates/Quotation.md` — cross-domain generic quote capture. Determine whether the Information domain `Quotation.md` is sufficient, or whether a root-level version adds distinct value. Add if yes; skip if redundant.
- Other cross-domain patterns identified during Phase 6 execution — add to this folder if they emerge

- **Ref:** REF-A, REF-H

**Phase 6 Acceptance:** All templates from the domain mapping table in Requirements §11 exist in their target locations. All have v3 YAML metadata, `{{fieldInfo}}` declarations, `z2k_template_suggested_title`, and no v2 syntax. Personal templates have correct author metadata and privacy values.

---

## Phase 7 — Supporting Documentation

**Goal:** Produce AI Recommendations document, Tags Taxonomy placeholder, and Library Version System card.

**Dependency:** Phase 6 complete (all templates done — AI Recommendations is based on observations made during migration).

### Task 7.1 — AI Recommendations Document
- **Target:** `AI/Z2K Template Library - AI Recommendations.md`
- **Contents:** Observations and improvement suggestions gathered during migration. Potential topics:
  - Patterns that work well in v3 (e.g., `{{fieldInfo}}` in system-blocks for shared fields)
  - Patterns that are suboptimal (e.g., personal templates in default library — need vault separation strategy)
  - Feature gaps discovered (dot-notation for prompted fields, Default Template plugin feature)
  - Structural improvements for future library versions
  - Recommendations for automating library updates
- **Note:** This is an AI-authored document expressing system-level observations; appropriate for the AI domain

### Task 7.2 — Tags Taxonomy Placeholder
- **Target:** `System/Z2K Tags Taxonomy.md` (or determine better location based on System domain structure at time of execution)
- **Contents:** Placeholder explaining the intent of the taxonomy; list known tag prefixes from v2 (`#Media/`, `#Location/`, `#WriterTags/`, `#Questions/`, `#Card/`, `#YPO-Forum/`); note that full authorship is deferred
- **Note:** Confirm placement — may fit better in `Docs/z2k-system-docs/` than in the vault `System/` folder

### Task 7.3 — Library Version System Card
- **Target:** `System/Z2K Template Library - v3.md`
- **Contents:** Library version (3.0.0), creation date (2026-03-02), domain inventory, brief changelog (first v3 release — migrated from v2 Templater-based system), link to project folder

**Phase 7 Acceptance:** All 3 documents exist. AI Recommendations doc has substantive content. Tags Taxonomy placeholder has known prefix list and deferred notice. Library Version card has correct metadata.

---

## Phase 8 — Cleanup and Archival

**Goal:** Update project-level docs, archive source materials, update memory.

### Task 8.1 — Update Master Migration Plan
- **File:** `Data/Vaults/z2k-default-vault/System/Z2K v2 to v3 Migration Plan.md`
- **Action:** Add a note that the plan has been superseded by the formal project documents in the project folder; link to SoW, Requirements, and Implementation Plan. Mark plan status as `completed`.

### Task 8.2 — Archive Q&A Documents ✅ DONE
- **Status:** Completed during Phase 2 re-entry (2026-03-02)
- All 3 Q&A/planning source documents moved to `User Feedback Documentation/Archived/` within the project folder
- No further action needed

### Task 8.3 — Update AI Memory File
- **File:** `/Users/gp/.claude/projects/-Users-gp-Vaults-Z2K-Studios-Workspace/memory/MEMORY.md`
- **Action:** Update the Z2K Template Library Migration section to reflect project formalization: project documents created, Q&A docs can be archived, Phase 0 fully resolved, ready for execution phases.

### Task 8.4 — Mark Requirements and Implementation Plan as Locked
- **Requirements:** ✅ Locked — 2026-03-02
- **Implementation Plan:** Lock pending (Phase 3 re-entry audit in progress — will be locked when audit completes)

### Task 8.5 — Verify Out of Scope Tasks Index
- **Target:** `Out of Scope Tasks/Out of Scope Tasks - Index.md`
- **Action:** Confirm all out-of-scope items discovered during execution are filed; verify each has its own file with sufficient detail for future reference.

### Task 8.6 — Populate Post Project Folders
- **Action:** Review `Post Project/CTLv3 Project/` and `Post Project/ZSv3 Project/` for items collected during execution. Ensure each item has its own file describing it as a requirement for the successor project. Confirm no items are missing.

### Task 8.7 — Finalize Continuous Improvement File
- **Target:** `Post Project/Continuous Improvement/Project Workflow Improvements.md`
- **Action:** Review all entries; ensure each has a description, rationale, and proposed implementation approach. Remove duplicates or stale entries.

### Task 8.8 — Finalize Z2K Templates Feature Prioritization
- **Target:** Prioritization and Dependencies section → Z2K Templates Feature Prioritization table (this document)
- **Action:** Update all rows with final validated status. Ensure all blocking bugs are in `Issues/Z2K Templates Plugin/`. Export or summarize for handoff to plugin developer.

**Phase 8 Acceptance:** Migration plan updated. Q&A docs have archival headers. Memory file updated. All project documents reflect final state. PDL Post Project and Out of Scope Tasks folders are current. Z2K Templates Feature Prioritization table is complete and ready for handoff.

---

## Implementation Open Issues Summary

| ID | Issue | Blocking Phase |
|---|---|---|
| DSB-005 | Projects system-block stop behavior — read REF-E before executing | Phase 3 (Projects) |
| ST-001 | Source type taxonomy — read REF-I before Information templates | Phase 6 (Information) |
| BLK-001/004/005 | Dot-notation for prompted user fields (`Fabric.*`, `Content.*`) — test at Phase 4 start | Phase 4 |
| LOC-001 | Locations.template vs ~Generic — verify before Phase 6 (Locations) | Phase 6 (Locations) |
| AI-PERSP | AI domain system-block — determine field name/structure for AI-perspective authorship | Phase 3 (AI) |
| PROJ-YAML | Projects template YAML structure (no z2k_* fields) — design before Phase 6.9 | Phase 6 (Projects) |

---

## Sidebar Tasks (Log Here)

- **Dot-notation bug report:** If Phase 4 test confirms `Content.Author` dot-notation is unsupported for prompted fields, file a bug against `z2k-studios/z2k-plugin-templates`
- **GH Issue #182 tracking:** "Default Template" plugin feature. Workaround: `My Writings (Default).md` naming. Watch for implementation.
- **Generic Daily Log:** After migration complete, user will create a more generic public-friendly version of the Daily Log template (current version is Flame/personal-specific)
- **Personal vault migration:** All templates with `z2k_template_author: "Geoff (z2k-gwp)"` must be manually moved to personal vault before this library is published publicly
- **Health Log sub-block decomposition:** After v3 migration is complete, revisit `Body/Templates/Health Log.md` and decompose into individual sub-blocks composed by a parent block
