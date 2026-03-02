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
