---
document_type: Continuous Improvement Log
status: Active
---
# Project Workflow Improvements

Running list of proposed improvements to the Z2K project workflow, collected during the CTLv3 migration project. These are universal improvements (not project-specific) intended to improve the IF and project document templates for future projects.

Each entry: **Description** / **Rationale** / **Proposed Implementation**

---

## PWI-001 — Rename SoW "Workflow" Section to "Iterative Framework"

**Description:** The default SoW template uses "Workflow" as the section heading for the phased execution model. This should be renamed to "Iterative Framework (IF)" to match the terminology used in this project and to deconflict with the `ai-context` workflow term (which refers to Claude Code workflow files).

**Rationale:** The term "Workflow" is overloaded — it conflicts with the `ai-context/shared/workflows/` system used by Claude Code. "Iterative Framework" is more precise and descriptive of what the section actually defines.

**Proposed Implementation:** Update the default SoW template file (wherever it lives in ai-context). Replace `## Workflow` with `## Iterative Framework (IF)`. Update any references to "Workflow" in associated project template files accordingly.

---

## PWI-002 — Add Terms and Acronyms Section to Default SoW Template

**Description:** Add a standard Terms and Acronyms section to the default SoW template. Include the standard IF terminology as a starting scaffold; project-specific terms are added per project.

**Rationale:** Projects accumulate acronyms quickly (SoW, PRD, IP, TP, IF, PDL, etc.). Having a dedicated section from the start ensures consistent vocabulary within and across project documents.

**Proposed Implementation:** Add `## 1.5 Terms and Acronyms` to the SoW template with a table scaffold pre-populated with the standard IF terms. Project teams fill in project-specific terms.

---

## PWI-003 — Create Multiple IF Variants for Different Project Types

**Description:** The current IF is designed for highly iterative projects (punch-through model). Create at least two IF variants: (1) Highly Iterative — punch-through cycle, features sequenced by priority/dependency; (2) Linear — full phase completion before advancing, suited to well-defined projects with stable requirements.

**Rationale:** Not all projects benefit from the iterative punch-through model. A simpler, more linear project would be over-engineered by the current IF. Having named variants lets teams select the right model upfront.

**Proposed Implementation:** Create two SoW template variants in ai-context (e.g., `sow-iterative.md` and `sow-linear.md`). Document the trade-offs. Update the `project/create` workflow to ask which IF variant to use.

---

## PWI-004 — Encode Document Requirements for Highly Iterative Projects into Reusable Templates

**Description:** The CTLv3 SoW originally contained a "Document Requirements" section specifying what a highly iterative PRD and IP must contain (importance levels, bootstrapping section, outputs section, bug tracking, prioritization and dependencies, feature prioritization artifact, etc.). These requirements have been fulfilled in this project's PRD and IP. They should be encoded into reusable templates for future projects rather than living in each individual SoW.

**Rationale:** Document requirements captured in a SoW are project-specific and get removed once fulfilled. The same requirements will apply to every highly iterative project. Encoding them in reusable templates (a "highly iterative" PRD template and IP template) means future projects inherit these structural requirements automatically without needing to re-discover or re-specify them.

**Proposed Implementation:**
1. Create a `prд-iterative-template.md` in ai-context (or equivalent location) pre-seeded with the sections added to this project's PRD: §1.5 Importance Levels schema, §2.5 Bootstrapping, §20 Outputs and Deliverables, §21 Bug and Issue Tracking.
2. Create an `ip-iterative-template.md` pre-seeded with the Prioritization and Dependencies section (Tooling Priority, Requirements Priority, Z2K Templates Feature Prioritization table, Draft tasks note).
3. Create a `sow-iterative.md` that references these templates in its Document Requirements section (rather than inlining the requirements).
4. Update the `project/create` workflow to use these templates when the "Highly Iterative" IF variant is selected (see PWI-003).

---

## PWI-005 — Add Phase Buyoff Table to SoW; Flag Automation Potential per Phase

**Description:** The SoW's Workflow Phases section should include a table listing every IF phase with two additional columns: (1) **Buyoff Giver** — who must approve the phase deliverable (e.g., User, AI, Joint); and (2) **Automation Potential** — whether the phase can be fully executed and validated without user interaction.

The execution and validation phases (Task Execution, Iteration) are candidates for full automation — they could potentially be run end-to-end by an autonomous "Chief" agent without user interaction after the planning phases are approved. The planning and document-review phases (SoW, PRD, IP, TP) require user buyoff and cannot be skipped.

A minimal draft table would look like:

| Phase | Deliverable | Buyoff Giver | Automation Potential |
|---|---|---|---|
| Phase 1 — Statement of Work | SoW (Locked) | User | None — human approval required |
| Phase 2 — Project Requirements | PRD (Locked) | User | None — human approval required |
| Phase 3 — Implementation Plan | IP (Locked) | User | None — human approval required |
| Phase 4 — Testing Plan | TP (Locked) | User | None — human approval required |
| Phase 5 — Task Breakout | Task files + Tracker | Joint | Partial — AI drafts, user reviews |
| Phase 6 — Task Execution | Completed tasks | AI | High — fully automatable per-task |
| Phase 7 — Iteration | Revised tasks | AI | High — automatable if criteria are clear |
| Phase 8 — Celebration | Project closure | User | None — human milestone |

**Rationale:** As AI tooling matures (specifically a "Chief" orchestration tool), Phases 6–7 could be executed autonomously without the user sitting in the loop for each task. Making automation potential explicit in the SoW creates a clear target for future automation investment and signals to the AI which phases require human gatekeeping.

**Proposed Implementation:**
1. Add the phase buyoff table to the default SoW template under the Workflow Phases section.
2. Create a "Chief" tool or workflow that can execute a Task Breakout + Task Execution loop autonomously given a locked Testing Plan and Task List.
3. Update the `project/create` workflow to include guidance on when to engage the Chief tool.

---

## PWI-006 — Embed Traceability Requirements and Rollback Audit Instructions in the Default Testing Plan Template

**Description:** The default Testing Plan template should embed two structural requirements that future projects inherit automatically:
1. A prominent audit warning at the top of the document stating that any change to the SoW, PRD, or IP requires a full-scale Testing Plan audit before execution resumes — including verification that every PRD requirement and IP task has at least one test assertion mapped to it.
2. A traceability mechanism in the coverage table: each test row explicitly references the IP task ID(s) and PRD requirement(s) it validates, enabling a simple completeness check (every task ID should appear in at least one row).

**Rationale:** Discovered during CTLv3 Phase 4 (Testing Plan). The initial Testing Plan was organized by test type rather than by task, making coverage impossible to audit without manual cross-referencing. Traceability and rollback audit requirements were added after the fact — they should be structural defaults, not retrofits. The corresponding rollback protocol is captured in the SoW (§4.2 Testing Plan Audit Protocol), which was also added after the fact for the same reason.

**Proposed Implementation:**
1. Add an `[!WARNING]` callout block at the top of the default Testing Plan template (after the title, before the Overview section) with the audit requirement verbatim.
2. Add an "IP Task" column and a "PRD Req" column to the coverage table scaffold in the template.
3. Add a "Coverage Completeness Check" section to the template: a short checklist instructing the author to confirm every IP task ID appears in at least one table row before locking the document.
4. Add §4.2 (Testing Plan Audit Protocol) to the default SoW template to anchor the cross-document obligation at the framework level.

---

## PWI-007 — Add Agent Context Brief to Default Task Breakout Phase

**Description:** Every project using a Task Breakout phase should produce an **Agent Context Brief** alongside the individual task files and master tracker. The brief (`tasks/Agent Brief.md`) contains project-wide constants that task files assume but do not repeat: key paths, critical constraints, naming conventions, conversion rules, reference doc index, issue logging, and status update protocol. Each task file should open with a callout directing the agent to read the brief first.

**Rationale:** Discovered during CTLv3 Phase 5. Individual task files are scoped to one task and do not carry global context. A fresh agent lacks: the v2 source path, target vault path, template version string, naming conventions, conversion approach, and the READ-ONLY constraint on source files. Without this, agents must search for context (slow and error-prone) or hallucinate it (dangerous). A co-located brief ensures every execution agent is fully oriented with one additional read before starting any task.

**Proposed Implementation:**
1. Add an `Agent Brief` template to the project/task-breakout library in ai-context, pre-seeded with sections: Project Summary, Key Paths, Critical Constraints, Naming Conventions, Metadata Requirements, Conversion Approach (if applicable), Reference Docs Index, Issue Logging, Status Update Protocol.
2. Each task file template includes a callout immediately after the title: `> Before executing this task, read \`tasks/Agent Brief.md\` — project-wide paths, constraints, naming conventions, and conversion rules.`
3. The `project/save` and Phase 5 workflows reference the Agent Brief as a required Phase 5 deliverable alongside the master task tracker.

---

## PWI-008 — Task Acceptance Criteria Should Include Cleanup of Superseded Files

**Description:** When a task produces files that replace existing files (e.g., renaming `Template - Book.md` to `Book.md`), the task's acceptance criteria should explicitly require deletion of the superseded files. Cleanup should not be deferred to a later phase.

**Rationale:** During CTLv3 Phase 6, v3 templates were created alongside old prefixed files in `Information/Templates/`. The old files (`Block - ...`, `Template - ...`) were not deleted during the task that replaced them, leaving 9 stale duplicates that had to be cleaned up in Phase 8. This creates confusion (which file is canonical?) and risks using the wrong version.

**Proposed Implementation:** Add a standard step to the task file template for migration/replacement tasks: "Delete any superseded files that this task's output replaces. Verify no stale duplicates remain in the target folder." The Agent Brief should also include a note: "When a task replaces an existing file with a renamed version, delete the old file as part of the same task."
