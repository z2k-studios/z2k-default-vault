---
task_id: "Task-11"
ip_tasks: ["6.2"]
execution_phase: "Phase 6"
status: "Done"
domain: "Beliefs"
parallelizable: true
parallel_group: "Can run with Tasks 10, 15, 16, 17, 20, 21, 22"
---
# Task 11 — Beliefs Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Migrate 1 Beliefs domain template from v2 to v3. This is the recommended **first punch-through task** — simplest domain; no extra fields; validates the full system-block + fieldInfo + template instantiation chain.

## Dependencies
- Task 02 — `Beliefs/Templates/` exists
- Task 03 — Root system-block complete
- Task 04 — `Beliefs/.system-block.md` complete
- Task 07 — Root block templates complete

## ⚠️ Recommended First Punch-Through
The IP recommends executing this task first (along with Task 03 and Task 04 Beliefs system-block) as the minimal viable chain to validate end-to-end: system-block injection + `{{fieldInfo}}` prompting + template instantiation. Complete this before scaling to larger domain tasks.

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-H: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

## Source → Target Mapping

| Source (v2) | Target (v3) | Source Type |
|---|---|---|
| `Beliefs - ~Generic` | `Beliefs/Templates/Beliefs (General).md` | `.:Z2K/SourceType/InternalThought` |

## Conversion Approach
See Task 10 for full conversion steps (same process applies).

## Required v3 YAML Fields
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```

## Acceptance Criteria
- `Beliefs/Templates/Beliefs (General).md` exists
- Has all required v3 YAML fields
- No v2 syntax remaining (or FLAGGED)
- Template instantiates; output YAML contains `z2k_creation_domain: ".:Z2K/Domain/Beliefs"`

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| Template exists | `Beliefs/Templates/Beliefs (General).md` exists |
| Has `z2k_template_type: document-template` | YAML field present |
| Has `z2k_template_version` | YAML field present |
| Has `z2k_template_suggested_title` | YAML field present |
| Instantiates without error | Output created; no error log |
| System-block YAML injection works | Output YAML contains `z2k_creation_domain: ".:Z2K/Domain/Beliefs"` |
