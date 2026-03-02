# Project Phase Tracker - Z2K Template Library v3 Migration

---

## Phase 1 — Statement of Work ✅ LOCKED
**Status:** Locked — 2026-03-02
**Rollback note:** SOW was rolled back for changes; downstream phases (PRD, IP) re-validated and confirmed clean against final SOW on 2026-03-02.

### Completed:
- Loaded z2k-user/init workflow context; read master migration plan + both Q&A docs
- Confirmed all Phase 0 open questions are answered in Q&A docs
- Drafted, rolled back, revised, and locked Statement of Work
- Created Project Metadata file at `ai-context/shared/library/project/known-projects/Z2K Template Library v3 Migration.md`
- PRD and IP re-validated against final SOW — no changes required

---

## Phase 2 — Project Requirements ✅ LOCKED
**Status:** Locked — 2026-03-02

### Completed:
- Wrote comprehensive Requirements document consolidating all decisions from master migration plan + both Q&A docs
- All 24 Architecture Q&A answers + 8 Migration Q&A answers encoded into requirements
- Full domain mapping table, API translation, privacy canonical values, block reqs, template reqs per domain, deferred items, sidebar tasks, and open issues documented
- Q&A source docs archived to `User Feedback Documentation/Archived/`
- RSB-001 resolved: `z2k_card_status` removed entirely from root system-block (no default status value)
- CTLv3 successor post-project items captured in `Post Project/CTLv3 Project/CTLv3 Project - Index.md` (CTLP-001 through CTLP-008)

### Remaining Open Issues (tracked in Requirements doc §19):
- **DSB-005**: System Block Stop behavior for Projects — read System Block Stops doc first; blocking only for Projects system-block
- **ST-001**: Source type taxonomy — read Metadata Specification v3.0 before Information templates (Phase 6)
- **BLK-001/004/005**: Dot-notation for prompted user fields (Fabric.*, Content.*) — test at Phase 4 start
- **LOC-001**: Locations.template vs ~Generic — verify before Phase 6 (Locations)

---

## Phase 3 — Implementation Plan ✅ LOCKED
**Status:** Locked — 2026-03-02

### Initial Draft (prior session):
- Wrote full Implementation Plan with 8 execution phases (Vault Structure → Cleanup)
- Per-phase task breakdown with source files, target files, reference doc IDs per task, dependencies, acceptance criteria
- Reference docs index (REF-A through REF-K) for sub-agent consumption
- All open issues logged in Implementation Plan §Open Issues Summary
- Sidebar tasks documented in Implementation Plan §Sidebar Tasks
- Root system-block current state documented in Phase 2 task
- Added REQ-NM-009, root Ontology template (§11.16 + Task 6.14), root `Templates/` folder description
- Archived 3 source Q&A documents to `User Feedback Documentation/Archived/`

### Key decisions embedded in Implementation Plan:
- Execution order for templates: Thoughts → Beliefs → Information → Interactions → Memories → Locations → Journals → Logs → Projects → Body → System → Entities
- Information domain is blocked on reading REF-I (Metadata Specification v3.0) for source types
- Projects system-block is blocked on reading REF-E (System Block Stops doc)
- Dot-notation test (Content.*, Fabric.*) to be run at Phase 4 start before committing to field names

### Open issues tracked in IP:
- **AI-PERSP**: AI domain system-block — field name/structure for AI authorship perspective not yet designed
- **PROJ-YAML**: Projects template YAML structure (no z2k_* fields) — needs design before Phase 6.9

### Phase 3 Re-Entry Audit (2026-03-02) — COMPLETE:
- PRD block template naming corrected: `Block - <Name>.block` → `<Name>.md` across all §10 file paths and `{{> ...}}` references
- IP structural fixes: removed temp comment block; updated Task 2.1 (z2k_card_status → REMOVE); cleared RSB-001 open issue; updated Tasks 8.2 (done) and 8.4 (PRD locked)
- IP block naming: all Phase 4/5 target filenames updated to `<Name>.md` (no prefix, no `.block`)
- IP document template naming: all Phase 6 targets updated to no-prefix `<Name>.md`; domain defaults use `<Domain> (General).md`; `My Writings (General).md` replacing `(Default)`
- IP locked: `status: Draft` → `status: Locked`

## Phase 4 — Testing Plan ✅ LOCKED
**Status:** Locked — 2026-03-02

### Completed:
- Read user guidance doc: `User Feedback Documentation/Setting up a Testing Plan - Initial Guidance.md`
- Researched Command Queue and URI automation docs (REF-L/M/N)
- Identified existing `z2k-testing-vaults/scripts/run-tests.py` (URI-based, maintained by another developer — read-only reference; not to be modified)
- Updated IP: added REF-L/M/N to Reference Docs Index; updated Feature Prioritization table (Command Queue row now Phase 0); added Phase 0 — Testing Infrastructure Validation (TP-0.1–TP-0.4)
- Drafted and locked Testing Plan: `Z2K Template Library v3 Migration - Testing Plan.md`
- Added `[!WARNING]` audit callout to top of Testing Plan: any change to SoW/PRD/IP triggers a full-scale coverage audit
- Amended SoW: added §4.2 Testing Plan Audit Protocol — documents rollback implications and re-lock requirement
- Filed PWI-006 in CI log: embed traceability requirements + rollback audit instructions in default Testing Plan template

### Key decisions:
- Command Queue is preferred testing method (over URI); to be validated in TP-0.2
- CTL v3 testing vault: `z2k-testing-vaults/Z2K System Vault Testing/` (new, separate from plugin dev's vault)
- CTL v3 test scripts stored in project `Testing/` subfolder
- Golden file model: first successful instantiation saves `expected.md`; all future runs diff against it
- Phase 0 in IP is the pre-execution testing infrastructure gate — must complete before execution begins

### Amendment completed — 2026-03-02:
- **Testing Plan traceability table update:** Added "IP Task" column to all coverage table rows (Phase 0–7). Added Phase 7 (Supporting Docs) rows. Added Coverage Completeness Check section with fully covered list, excluded tasks table, and known gaps (3.11 AI-PERSP, 3.13 block stop).

---

## Phases 5–8 — Not Yet Started

**Phase 5:** Task Breakout
**Phase 6:** Task Execution (Vault Structure → System Blocks → Blocks → Templates → Docs)
**Phase 7:** Iteration (if needed)
**Phase 8:** Celebration
