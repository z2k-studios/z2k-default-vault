---
task_id: "Task-24"
ip_tasks: ["8.1", "8.3", "8.4", "8.5", "8.6", "8.7", "8.8"]
execution_phase: "Phase 8"
status: "Done"
domain: "Global"
parallelizable: false
---
# Task 24 — Cleanup and Archival

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Update project-level docs, finalize post-project materials, and mark the project complete.

## Dependencies
- Task 23 complete (all Phase 7 documents done)

## Note on IP Task 8.2
Task 8.2 (Archive Q&A Documents) was completed during Phase 2 re-entry on 2026-03-02. No action needed.

## Steps

### 8.0 - ASK USER DO THEY WISH TO PROCEED WITH CLEANUP AND ARCHIVAL
- Before proceeding with cleanup and archival tasks, ask the user if they wish to continue with this final phase of the project. 
- VERY IMPORTANT - DO NOT PROCEED WITH ANY OF THE STEPS BELOW UNLESS THE USER CONFIRMS THEY WISH TO PROCEED.

### 8.1 — Update Master Migration Plan
- **File:** `Data/Vaults/z2k-default-vault/System/Z2K v2 to v3 Migration Plan.md`
- Add a note that this plan has been superseded by the formal project documents
- Link to: SoW, Requirements, and Implementation Plan in the project folder
- Mark plan status as `completed`

### 8.4 — Confirm Locked Status on All Core Project Documents
- SoW: `status: Locked` ✅
- PRD: `status: Locked` ✅
- IP: `status: Locked` ✅
- TP: `status: Locked` ✅
- If any still say Draft, lock them now

### 8.5 — Verify Out of Scope Tasks Index
- **File:** `Out of Scope Tasks/Out of Scope Tasks - Index.md`
- Confirm all out-of-scope items discovered during execution are filed
- Each should have its own file with sufficient detail for future reference
- Add any missing items discovered during execution

### 8.6 — Populate Post Project Folders
- **CTLv3 Project:** `Post Project/CTLv3 Project/` — confirm CTLP-001 through CTLP-008 are current; add any new items discovered during execution
- **ZSv3 Project:** `Post Project/ZSv3 Project/` — confirm all ZSv3-relevant items are filed
- **Template Best Practices:** `Post Project/Template Best Practices/` — confirm a draft best practices document exists; if not, write a brief one based on patterns observed during migration

### 8.7 — Finalize Continuous Improvement Log
- **File:** `Post Project/Continuous Improvement/Project Workflow Improvements.md`
- Review all PWI entries; ensure each has Description, Rationale, and Proposed Implementation
- Remove duplicates or stale entries
- Add any new improvement ideas surfaced during execution

### 8.8 — Finalize Z2K Templates Feature Prioritization Table
- **Location:** IP §Z2K Templates Feature Prioritization
- Update all rows with final validated status (✅ or ❌ + notes)
- Ensure all blocking bugs are in `Issues/Z2K Templates Plugin/`
- Write a brief summary of the table suitable for handoff to the Z2K Templates Plugin developer

## Final Step: Mark Project Complete
Update the Phase Tracker: mark Phase 8 as complete. Update SoW `status` from `Locked` to `Completed`. Run `/wf project/save` to commit final state.

## Acceptance Criteria
- Master migration plan updated and marked completed
- Memory file updated with final project state
- All core documents locked (or completed)
- Out of Scope Tasks Index current
- Post Project folders populated
- CI log finalized
- Feature Prioritization table complete and ready for handoff
- Phase Tracker shows Phase 8 complete

## Validation (from Testing Plan)
Phase 8 tasks are cleanup/archival — no automated tests. All validation is manual review of document state.
