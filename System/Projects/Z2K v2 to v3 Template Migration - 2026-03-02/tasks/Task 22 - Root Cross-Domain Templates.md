---
task_id: "Task-22"
ip_tasks: ["6.14"]
execution_phase: "Phase 6"
status: "Done"
domain: "Global (root Templates/)"
parallelizable: true
parallel_group: "Can run with Tasks 10, 11, 15, 16, 17, 20, 21"
---
# Task 22 — Root Cross-Domain Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 1 cross-domain template and build 1 new cross-domain template in the root `Templates/` folder. Evaluate whether an additional Quotation template is needed.

## Dependencies
- Task 02 — root `Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — All domain system-blocks complete (templates span any domain)
- Task 07 — Root block templates complete (these templates and blocks share the same folder)

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## Source → Target Mapping

### Confirmed (2 templates)

| Source (v2) | Target (v3) | Note |
|---|---|---|
| `~Generic Card Template` | `Templates/Card (General).md` | Generic cross-domain card |
| *(new)* | `Templates/Ontology.md` | Cross-domain MOC/index card — domain-specific variants exist in Thoughts, Information, Memories; this is the root-level generic |

### Evaluate (1 template)
**`Templates/Quotation.md`** — Determine whether the Information domain `Quotation.md` (Task 12) is sufficient for cross-domain use, or whether a root-level generic quotation template adds distinct value.
- If yes → build `Templates/Quotation.md`
- If no → skip; note the decision in this task file

### Additional cross-domain patterns
If other cross-domain patterns emerge during Phase 6 execution, they may be added here. Check back during or after Task execution and add any that qualify.

### Evaluation Decision
> Root Quotation needed: No
> Rationale: Thoughts domain already has Book Quote, General Quote, and Quote a Source templates covering primary quotation use cases. The root `Templates/Quotation.md` block template provides reusable quotation structure via `{{> "Quotation"}}` for any domain. A root-level quotation document template adds marginal value.
> Additional patterns identified: None — the Card (General) + Ontology pair covers cross-domain needs adequately.

## Required v3 YAML Fields
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```

## Acceptance Criteria
- `Templates/Card (General).md` exists
- `Templates/Ontology.md` exists
- Quotation evaluation completed and decision documented
- All created templates have required v3 YAML fields

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All templates exist | `Card (General).md`, `Ontology.md` (+ Quotation if created) exist in `Templates/` |
| Each has required YAML fields | Present |
| Each instantiates without error | Output created; no error log |
| System-block injection works | Output reflects whichever domain system-block applies to the instantiation location |
