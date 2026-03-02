---
document_type: Statement of Work
status: Locked
---
# Statement of Work (SoW) - Z2K Template Library v3 Migration

## 1. Project Overview
**Project Name:** Z2K Template Library v3 Migration
**Owner:** Geoff (z2k-gwp)
**Primary Project Folder:** `Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/`
**GitHub Repository:** z2k-studios/z2k-default-vault
**Date Created:** 2026-03-02
**Status:** Locked

### 1.1 Objective

Migrate the complete Z2K template library from v2 (Obsidian Templater-based) to v3 (Z2K Templates Plugin) inside `Data/Vaults/z2k-default-vault`. This includes:

- Updating the vault's top-level domain folder structure to match the current v3 domain list
- Rewriting all `.system-block.md` files (root + per-domain) for v3 schema
- Migrating all ~60 old templates to their new domain locations using v3 syntax
- Building shared root-level and domain-level block partials
- Creating a small set of new templates not present in v2
- Producing a Tags Taxonomy placeholder document and an AI Recommendations document

The result is a fully functional v3 template library that can be used directly in the vault and later published as the default Z2K template library.

### 1.2 Non-Goals

- **Personal vault migration** — personal-specific templates will be placed in z2k-default-vault for now but are not migrated to a separate personal vault in this project.
- **Full Entities CRM** — only a `~Generic Contact.md` is in scope; the full CRM template set is a separate future project.
- **AI domain templates** — AI domain gets a folder and system-block only; content templates are out of scope.
- **Tags taxonomy authorship** — only a placeholder document; full taxonomy definition is deferred.
- **Z2K Core plugin** or **Z2K Templates plugin code changes** — this project operates at the vault/template level only. Plugin bugs discovered may be filed but are not resolved here.
- **Export pipeline or publication tooling** for the My Writings domain.

---

## 1.5 Terms and Acronyms

| Term | Full Form | Definition |
|---|---|---|
| **CTLv3** (also **CTL**) | Z2K Core Template Library v3 | The final deliverable of this project — the output of this SoW. A fully functional v3 template library built using the Z2K Templates Plugin. "CTL" unqualified always refers to CTLv3 (the new version). |
| **CTLv2** | Z2K Template Library v2 | The previous version of the template library, built on Obsidian Templater. The primary input for this SoW — what is being transformed into CTLv3. |
| **ZS / ZSv3** | Z2K System / Z2K System v3 | The overall approach of using structured Markdown files to build a digital identity and knowledge system. ZSv3 is the version of ZS that uses CTLv3. |
| **SoW** | Statement of Work | This document. Defines the project boundaries, goals, and process framework. |
| **IF** | Iterative Framework | The meta-level execution model defined in §4 of this SoW. |
| **IF Model** | Iterative Framework Model | The meta-level approach of the IF — a highly iterative, punch-through execution cycle applied to features in priority and dependency order. |
| **PRD** | Project Requirements Document | Defines WHAT must be built. One of the core project documents. |
| **IP** | Implementation Plan | Defines HOW it will be built. One of the core project documents. |
| **TP** | Testing Plan | Defines HOW deliverables will be validated. One of the core project documents. |
| **PDL** | Project Document Library | The folder containing all project documents for this project. |
| **CI** | Continuous Improvement Document | A document tracking changes to consider making to the overall project workflow, to be considered after project completion |
| **Requirements / Features** | — | Used interchangeably in the PRD. Requirements are described from a project management perspective; Features from a user perspective. Both refer to the same underlying items. |

---

## 1.6 Document Highlighting Conventions

The following highlighting conventions are used across all project documents:

- `==highlighted text==` — **Open question** — an unresolved decision or ambiguity that must be addressed before the section can be finalized, typically with the user.
- `===triple-highlighted text===` — **AI directive** — an instruction specifically addressed to an AI agent executing tasks in this project.

These follow the Z2K documentation library highlighting nomenclature.

---

## 2. Success Criteria

- [ ] All v3 domain folders present: Information, Thoughts, Beliefs, Memories, Interactions, Journals, Logs, Locations, Projects, Entities, Body, AI, System — each with a `Templates/` subfolder
- [ ] `Projects/My Writings/` and `Projects/My Writings/Templates/` created
- [ ] Root `Templates/` folder created for cross-domain blocks and generic templates
- [ ] Root `.system-block.md` rewritten for v3 schema (correct fields, removed deprecated fields, v3 API)
- [ ] All 13 domain `.system-block.md` files written with correct `z2k_creation_domain` values and domain-appropriate field sets
- [ ] All root-level block partials created (Card Fabric, Extended YAML, Perspective - Me, Quotation, Citation)
- [ ] All domain-level blocks created (Podcast Interview Content, Information summary/overview/synthesis/details, Logistics, When-Where-Who, Health Log)
- [ ] All ~60 templates from the domain mapping table migrated to v3 syntax
- [ ] All new templates built (Generic Contact, Generic Project, Active Project, Completed Project)
- [ ] Every template has `z2k_template_suggested_title`, `z2k_template_version: "v3.0.0 2026-03-02"`, `z2k_template_author`, and `{{fieldInfo}}` declarations
- [ ] No v2 Templater syntax remaining in any migrated template
- [ ] `AI/Z2K Template Library - AI Recommendations.md` written
- [ ] Tags taxonomy placeholder created in System docs
- [ ] `Post Project/Continuous Improvement/Project Workflow Improvements.md` reviewed and finalized
- [ ] `Post Project/CTLv3 Project/` populated with requirements for the CTLv3 successor project
- [ ] `Post Project/ZSv3 Project/` populated with requirements for the ZSv3 successor project
- [ ] `Post Project/Template Best Practices/` contains a draft best practices document for template hierarchy development

---

## 3. Project Documentation

Note: all project documents reside in the Primary Project Folder listed above.

Core Project Documents, in authority order:

1. **Statement of Work** — Defines overall project (boundaries, goals, process). This is the meta of all meta documents for the project.
   - `Z2K Template Library v3 Migration - Statement of Work.md`

2. **Project Requirements Document** — Defines WHAT must be built.
   - `Z2K Template Library v3 Migration - Project Requirements.md`
   - Note: Much of the requirements detail has already been resolved in the master migration plan and Q&A documents. The Requirements doc will consolidate those decisions into a single authoritative reference.

3. **Implementation Plan** — Defines HOW it will be built.
   - `Z2K Template Library v3 Migration - Implementation Plan.md`
   - Note: The master migration plan's phase/task list is the starting point.

4. **Testing Plan** — Defines HOW it will be validated.
   - `Z2K Template Library v3 Migration - Testing Plan.md`
   - Note: Validation will primarily be **automated** using Z2K Templates Plugin URI commands and the Command Queue feature. Manual inspection in Obsidian is a fallback. See Testing Plan for details.

5. **Task Documents** — Atomic executable units per domain or phase.
   - `tasks/Task #n - <task name>.md`

> **Large document note:** If the PRD or IP becomes excessively large, sub-documents may be created to hold groupings of requirements or implementation plans. Sub-documents are linked from the parent document and treated with equal authority.

### AI-Maintained Project Files

1. **Project Metadata File** — `ai-context/shared/library/project/known-projects/Z2K Template Library v3 Migration.md`
2. **Project Phase Tracker** — `Z2K Template Library v3 Migration - Project Phase Tracker.md`
3. **Task List and Progress Tracker** — `Z2K Template Library v3 Migration - Task List and Progress Tracker.md`

### Pre-Existing Reference Documents (authoritative inputs, read-only)
> Note: the Q&A source docs below were archived into the PDL after their decisions were consolidated into the PRD. Paths are relative to the Primary Project Folder.

- `User Feedback Documentation/Archived/Z2K v2 to v3 Migration Plan.md` — master migration plan; domain mapping table; architectural decisions
- `User Feedback Documentation/Archived/Template Migration - v2 to v3 - Open Questions.md`
- `User Feedback Documentation/Archived/Template Library - System Architecture - Open Questions.md`
- v2 source templates (READ-ONLY): `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/`

If documents conflict, higher authority overrides lower. Notify user of any significant conflicts.

---

## 4. Iterative Framework (IF)

### Critical Imperatives

- **Project Phase Tracker**: keep current state up to date at the end of each phase (minimum) and ideally per session.
- **Phase Transitions**: every phase shift must follow the **Phase Transition Protocol** defined in §4.1 below.
- **Progression**: obtain explicit user agreement before transitioning to the next phase.
- **Request Feedback**: engage with the user during planning phases to solicit feedback. Do not assume plans are sufficient.
- **Locked Documents are Read-Only**: once a document is marked "Locked", treat it as read-only. Changes require a formal phase rollback.
- **Phase Rollback Triggers**: if a locked document must change, declare a rollback explicitly. All downstream phases must be re-validated.

### 4.1 Phase Transition Protocol

Every phase shift must complete **all** of the following steps, in order:

1. **Run `/wf project/save`** — updates all project documentation and the Phase Tracker with the session's work. See the `project/save` workflow for full details on what this covers.
2. **GitHub source check-in** — commit and push all changes to the GitHub repository (`z2k-studios/z2k-default-vault`). This step is performed *in addition to* the documentation updates done by `/wf project/save`; it ensures vault files and project documents are version-controlled at every phase boundary.

Both steps are mandatory. A phase boundary is not complete until both are done.

---

### 4.2 Testing Plan Audit Protocol

Any change to the SoW, PRD, or IP — regardless of how minor it appears, and including changes introduced by a phase rollback — triggers a mandatory Testing Plan audit. The audit must be completed before the project re-enters execution.

**Audit requirements:**
1. Every PRD requirement must have at least one test assertion mapped to it in the Testing Plan
2. Every IP task must have at least one test assertion mapped to it in the Testing Plan
3. Any requirement or task added or modified by the upstream change must have a new validation step explicitly assigned before the audit is considered complete

**Phase rollback implications:**
- Rolling back to Phase 2 (PRD) or Phase 3 (IP) creates new or modified requirements and tasks that are, by definition, untested
- The Testing Plan must be revised and re-locked before re-entering Phase 6 (Execution)
- The Testing Plan re-lock is a required gate in the Phase Transition Protocol for any phase following a rollback

**Responsibility:** The Testing Plan is not a one-time artifact. It is a living document that must remain in sync with the PRD and IP at all times. Coverage gaps are project risks, not cosmetic issues.

---

### The IF Model

The IF for this project is **highly iterative**. Rather than completing all requirements before moving to the next phase, execution proceeds as follows:

1. **Identify the most basic and upstream features** — features with the fewest dependencies and simplest implementation, establishing the foundation for everything else.
2. **Punch through the full IF cycle** — take that feature from Requirements → IP task → Testing criteria → Execution → Validation before moving to the next.
3. **Expand outward by priority and dependency** — once the first punch-through succeeds, the next features are selected based on importance level and dependency graph, and the cycle repeats.
4. **Group where necessary** — some features are tightly coupled and must be implemented together as an "implementation task group." Always prefer linear sequencing where possible.

This means the IP will always have more features listed than there are detailed implementation plans for. Features without detailed plans are marked `Draft` in the IP. Plans are fleshed out as each feature becomes next in priority order.

### PDL Structure

The Project Document Library (PDL) for this project is organized as follows:

- **Core project documents** — SoW, PRD, IP, TP, task files (see §3)
- **`Out of Scope Tasks/`** — features and work items discovered during IF execution that are out of scope for this SoW. Each item gets its own file; an index file tracks all items. Initially seeded from Q&A history; expanded during execution.
- **`Post Project/`** — items to carry forward after this project completes:
  - **`Continuous Improvement/`** — contains `Project Workflow Improvements.md`, a running list of improvements to the project workflow itself (universal, not project-specific). Each entry includes a description, rationale, and proposed implementation approach.
  - **`CTLv3 Project/`** — requirements and items feeding into the successor CTLv3 ongoing project.
  - **`ZSv3 Project/`** — requirements and items feeding into the ZSv3 project (Z2K System Architecture and Documentation).
  - **`Template Best Practices/`** — best practices for template hierarchy development; intended for the Z2K Templates Plugin documentation website.
- **`Issues/`** — bug and issue tracking for dogfooded tools:
  - **`Z2K Templates Plugin/`** — one file per discovered bug or issue; governed by PRD §21.
- **`User Feedback Documentation/`** — pre-draft and in-session feedback for reference. All long feedback guidance should go here (if long feedback comes through the chat, then save a copy here to ensure ease of access to the information).

### IF Phases

#### Phase 1 — Iterate and Agree on Statement of Work
- Deliverable: this document, marked Locked
- Exit criteria: requirements complete, ambiguities resolved, user approves

#### Phase 2 — Iterate and Agree on Project Requirements
- Consolidate decisions from master migration plan + Q&A docs into a single authoritative Requirements document
- Define per-domain and per-template requirements
- Deliverable: Project Requirements, marked Locked
- Exit criteria: complete, no ambiguities, user approves

#### Phase 3 — Implementation Plan
- Break requirements into sequenced implementation tasks organized by phase (structure → system-blocks → blocks → templates)
- Map each task to its source template(s) and target file(s)
- Identify dependencies and risks
- Deliverable: Implementation Plan, marked Locked

#### Phase 4 — Testing Plan
- Define automated and manual validation approach for each implementation phase
- Primary approach: Z2K Templates Plugin URI commands and Command Queue processing
- Define acceptance criteria per task type (system-block, block, template)
- Deliverable: Testing Plan, marked Locked

#### Phase 5 — Task Breakout
- Break implementation + testing plan into individual atomic task files
- Produce master Task List and Progress Tracker
- Tasks organized by domain; parallelizable tasks flagged

#### Phase 6 — Task Execution
- Execute tasks in sequence (or parallel where flagged)
- Validate each task per Testing Plan criteria before marking Done
- Update Task List continuously

#### Phase 7 — Iteration
- Task failure → refine at task level first
- Structural flaws → phase rollback per `/wf project/phase-rollback`

#### Phase 8 — Celebration

---

## 5. Risks

- **Plugin API gaps** — `Fabric.MentalModel` dot-notation for prompted user fields may not be supported. Mitigation: test early; fall back to flat names (`FabricMentalModel`). Signal: prompt dialog fails to appear or produces errors.
- **System Block Stop limitations for Projects** — goal of completely different YAML (no `z2k_*` fields) in Projects subfolders may not be fully achievable via system-blocks alone. Mitigation: templates carry their own YAML overrides; read System Block Stops doc before implementing. Signal: z2k_* fields still appear in instantiated project cards.
- **Personal templates in default vault** — templates with hardcoded personal details (names, private tags) are intentionally included but will need to move to a personal vault before the library is published. Mitigation: mark personal templates clearly in metadata; track them in task list. Signal: templates contain real names or Uber-Private privacy tags.
- **Scope creep** — rich Q&A history reveals many deferred features (full CRM, AI templates, export pipeline). Mitigation: enforce non-goals section strictly; file deferred items as separate future projects.
- **Context window** — this is a large migration with ~60+ files. Mitigation: sub-agents for heavy reading; tasks designed to be executable in isolated sessions.

---

## 6. Constraints

- **Source templates are read-only.** Do not modify `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/`.
- **Target vault only.** All output goes into `Data/Vaults/z2k-default-vault/`.
- **Naming conventions must be followed:**
  - Document templates: `<Name>.md` — no `Template -` prefix; files reside in dedicated `Templates/` subfolders which serve as the type indicator
  - Block templates: `<Name>.block` (or `<Name>.md` where `.block` extension is impractical) — no `Block -` prefix; same rationale
  - System blocks: `.system-block.md` (dot-prefixed, hidden)
- **v3 metadata version:** `z2k_metadata_version: 3.00`
- **Template version string:** `v3.0.0 2026-03-02` for all migrated templates
- **Templater syntax handling:** Templater code (`<% ... %>`) must only be replaced when a clear, equivalent v3 conversion exists. Code that cannot be cleanly converted must be **preserved verbatim** in the output file and **flagged to the user** with a `{{! FLAGGED: ... }}` comment explaining what it does and why it was preserved. Do not guess at Templater behavior — preserve-and-flag is always preferred over an incorrect conversion.

---

## 7. Dependencies

- **Z2K Templates Plugin** (`z2k-studios/z2k-plugin-templates`) — must be installed and active in the vault for templates to function
- **v2 source snapshot** — `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/` (read-only reference)
- **Z2K Metadata Specification v3.0** — `Docs/z2k-design-notes/Z2K System - Design Notes/Z2K Data Architecture/Z2K Metadata/Z2K Metadata Specification - Version 3.0.md` — needed before implementing `z2k_card_source_type` values
- **System Block Stops doc** — `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/System Block Stops.md` — needed before implementing Projects domain
- **Z2K Templates Plugin Reference Manual** — `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/` — comprehensive reference for all plugin features; read relevant sections on demand per task. See also REF-A in the IP for the AI-specific guide.

---

## 8. Acceptance & Closure

The effort is complete when:

- All success criteria in Section 2 are met
- All tasks marked Done (implementation complete + validation passed)
- All project documents reflect final state
- No open critical risks remain
- Master migration plan updated with final decisions
- Memory file updated
- `Post Project/Continuous Improvement/Project Workflow Improvements.md` reviewed and finalized
- `Post Project/CTLv3 Project/` populated with all requirements for the CTLv3 successor project
- `Post Project/ZSv3 Project/` populated with all requirements for the ZSv3 successor project
- `Post Project/Template Best Practices/` contains a draft best practices document

Status must be updated to "Completed".
