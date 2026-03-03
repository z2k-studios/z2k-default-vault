---
task_id: "Task-10"
ip_tasks: ["6.1"]
execution_phase: "Phase 6"
status: "Done"
domain: "Thoughts"
parallelizable: true
parallel_group: "Can run with Tasks 11, 15, 16, 17, 20, 21, 22"
---
# Task 10 — Thoughts Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 7 Thoughts domain templates from v2 to v3.

## Dependencies
- Task 02 — `Thoughts/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `Thoughts/.system-block.md` complete
- Task 07 — Root block templates complete (dot-notation result must be known)

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## Conversion Approach (applies to all Phase 6 tasks)
For each template:
1. Read source from `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/<filename>`
2. Apply API Translation table (Requirements §3)
3. Add v3 YAML: `z2k_template_type: document-template`, `z2k_template_version: "v3.0.0 2026-03-02"`, `z2k_template_author`, `z2k_template_suggested_title`
4. Add `{{fieldInfo}}` declarations for all user-defined fields
5. Convert `%% ... %%` → `{{! ... }}`
6. Convert `G:` / `Geoff:` prefixes → `[!me]` callout with `Me:` label
7. Replace Card Fabric section with: `{{! To include Card Fabric: {{> "Card Fabric"}} }}`
8. Preserve unconvertible Templater code verbatim; wrap with `{{! FLAGGED: <explanation> }}`
9. Write to target path in `Data/Vaults/z2k-default-vault/`

## Source → Target Mapping

| Source (v2) | Target (v3) | Source Type |
|---|---|---|
| `Thoughts - ~Generic` | `Thoughts/Templates/Thoughts (General).md` | `.:Z2K/SourceType/InternalThought` |
| `Thoughts - Book - Quote` | `Thoughts/Templates/Book Quote.md` | `.:Z2K/SourceType/Quotation` |
| `Thoughts - Concept - Book` | `Thoughts/Templates/Book Concept.md` | `.:Z2K/SourceType/InternalThought` |
| `Thoughts - General - Quote` | `Thoughts/Templates/General Quote.md` | `.:Z2K/SourceType/Quotation` |
| `Thoughts - Ontology` | `Thoughts/Templates/Ontology.md` | `.:Z2K/SourceType/InternalThought` |
| `Thoughts - Quote a Source` | `Thoughts/Templates/Quote a Source.md` | `.:Z2K/SourceType/Quotation` |
| `Thoughts - Resolutions` | `Thoughts/Templates/Resolutions.md` | `.:Z2K/SourceType/InternalThought` |

## Required v3 YAML Fields (on every template)
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```
No `z2k_template_author` needed (these are not personal templates).

## Acceptance Criteria
- All 7 files exist in `Thoughts/Templates/`
- Each has `z2k_template_type: document-template`, `z2k_template_version`, `z2k_template_suggested_title`
- No v2 Templater syntax remaining (or FLAGGED if unconvertible)
- Quote templates have `z2k_card_source_type: ".:Z2K/SourceType/Quotation"` (if applicable)
- No `Block -` or `Template -` prefixes in filenames

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All templates exist | All 7 paths in `Thoughts/Templates/` |
| Each has `z2k_template_type: document-template` | YAML field present |
| Each has `z2k_template_version` | YAML field present |
| Each has `z2k_template_suggested_title` | YAML field present |
| Each instantiates without error | Output created; no error log |
| System-block YAML injection works | Output YAML contains `z2k_creation_domain: ".:Z2K/Domain/Thoughts"` |
