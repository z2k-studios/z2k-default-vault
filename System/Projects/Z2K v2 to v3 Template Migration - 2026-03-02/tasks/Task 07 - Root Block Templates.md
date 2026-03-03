---
task_id: "Task-07"
ip_tasks: ["4.1", "4.2", "4.3", "4.4", "4.5"]
execution_phase: "Phase 4"
status: "Done"
domain: "Global (root Templates/)"
parallelizable: true
parallel_group: "Can run with Tasks 03–06, 08, 09 after Task 02 is complete"
---
# Task 07 — Root Block Templates

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Build 5 shared block partial templates in the root `Templates/` folder.

## Dependencies
- Task 02 (vault structure) — root `Templates/` folder must exist

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`
- REF-F: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatStringBulletize.md`
- REF-G: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/Storing Field Values in YAML.md`

## ⚠️ Dot-Notation Test Gate (BLK-001/004/005)
**Execute this test BEFORE writing blocks 4.2, 4.3, 4.4.**

At the start of Task 4.2 (Quotation block), test whether `{{fieldInfo Content.Author "Author?"}}` causes the Obsidian prompt to appear correctly. Use a minimal inline test template:
- If prompt appears correctly → dot-notation is supported; use `Content.*` and `Fabric.*` field names as specified
- If `{{Content.Author}}` appears verbatim (unfilled) in output → dot-notation is unsupported; use flat names (`ContentAuthor`, `ContentTitle`, etc.) and file a plugin bug in `Issues/Z2K Templates Plugin/`

**Document result here before proceeding:**
> Dot-notation result: Bare dot-notation (`Content.Author`) fails in `{{fieldInfo}}` (Handlebars parse error). Bracket notation (`[Content.Author]`) works everywhere — fieldInfo, output, prompting. Both approaches are functionally viable.
> Field names to use: **Flat names** (`ContentAuthor`, `FabricMentalModel`, etc.) — chosen for simplicity and accessibility over bracket dot-notation.

---

## Output Files

All targets in `Data/Vaults/z2k-default-vault/Templates/`

### 4.1 — `Perspective - Me.md`
Block template for vault-owner perspective (callout-based).
```
---
z2k_template_type: block-template
---
{{fieldInfo PerspectiveText "Your perspective or commentary" type="text"}}

> [!me]
> {{PerspectiveText}}
```

### 4.2 — `Quotation.md`
Block template for quotations.
- **Fields:** `Content.Author`, `Content.Title`, `Content.Text` (or flat names if dot-notation fails — see test gate above)
- **Structure:** Blockquote + attribution line + optional perspective section
- **YAML storage:** Use REF-G pattern to store fields in YAML for cross-block pre-fill
- Field names must be consistent with Citation block (Task 4.3) where they overlap

### 4.3 — `Citation.md`
Block template for source citations.
- **Fields:** `Content.Author`, `Content.Title`, `Content.Source`, `Content.URL`, `Content.Date`
- Field names must be identical to Quotation block where they overlap (same namespace for YAML pre-fill)
- Ref: REF-G

### 4.4 — `Card Fabric.md`
Block template for Card Fabric sections (mental models, contexts, references).
- **Fields:** `Fabric.MentalModel`, `Fabric.Contextual`, `Fabric.Reference`, `Fabric.GeoContext` (or flat names if dot-notation fails)
- **Structure:** Use `{{formatStringBulletize}}` for conditional section headers; build both YAML array section and markdown body
- Example pattern from IP: `{{formatStringBulletize Fabric.MentalModel 0 "#### Mental Models\n"}}`
- Ref: REF-F, REF-G

### 4.5 — `Extended YAML.md`
Extended YAML fields block for power users.
- **Fields:** privacy, project links, structures, ratings arrays, fabric YAML arrays
- **Usage:** User manually inserts via `{{> "Extended YAML"}}`; never auto-injected
- Ref: REF-G

## All Blocks Must Have
```yaml
---
z2k_template_type: block-template
---
```

## Acceptance Criteria
- All 5 files exist in `Templates/`
- Each has `z2k_template_type: block-template`
- Quotation and Citation use consistent `Content.*` field names (or flat equivalents)
- Card Fabric uses `{{formatStringBulletize}}` correctly
- Dot-notation test result recorded; flat names applied if needed
- No `.block` prefix in filenames — use `<Name>.md` only

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All 5 block files exist | All 5 paths in `Templates/` exist |
| Each has `z2k_template_type: block-template` | YAML field present |
| Quotation instantiation | Output matches expected; Content.* fields rendered |
| Citation instantiation | Output matches expected; field names consistent with Quotation |
| Card Fabric instantiation | `{{formatStringBulletize}}` renders correctly |
| Perspective - Me instantiation | `[!me]` callout present |
| Extended YAML instantiation | YAML fields rendered |
