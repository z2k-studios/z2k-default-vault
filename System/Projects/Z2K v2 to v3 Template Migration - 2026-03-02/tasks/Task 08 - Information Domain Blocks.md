---
task_id: "Task-08"
ip_tasks: ["5.1", "5.2", "5.3", "5.4", "5.5"]
execution_phase: "Phase 5"
status: "Done"
domain: "Information"
parallelizable: true
parallel_group: "Can run with Tasks 03–07, 09 after Task 02 is complete"
---
# Task 08 — Information Domain Blocks

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Build 5 Information domain block partials used by Information document templates.

## Dependencies
- Task 02 (vault structure) — `Information/Templates/` must exist
- **Task 07 should be complete first** — dot-notation test result from Task 07 governs field naming here

## References to Read First
- REF-A: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md`

## Source Reference (v2)
`/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/Information - Podcast Interview*.md`
(for field names and section structure in block 5.1)

## Output Files
All targets in `Data/Vaults/z2k-default-vault/Information/Templates/`

### 5.1 — `Podcast Interview Content.md`
Generic podcast interview content block — included by host-specific podcast templates.

**Architecture:** Host-specific templates set fixed values (host name, show name, default tags) BEFORE including this block via `{{> "Podcast Interview Content"}}`. The block itself is generic.

**Sections:** Key Quotes, Key Takeaways, Personal Synthesis, Background/Context, Episode Details
**Fields:** Interviewer, Interviewee, Episode Title, Date, URL

### 5.2 — `Information - Summary.md`
Summary section block — one-paragraph abstract of source content.

### 5.3 — `Information - Overview.md`
Overview section block — structured breakdown of main points or chapters.

### 5.4 — `Information - Synthesis.md`
Personal synthesis section — vault-owner's analysis and takeaways. Uses `[!me]` callout from Perspective - Me block pattern.

### 5.5 — `Information - Details.md`
Details section — granular notes, highlights, or direct quotes from the source.

## All Blocks Must Have
```yaml
---
z2k_template_type: block-template
---
```

## Acceptance Criteria
- All 5 files exist in `Information/Templates/`
- Each has `z2k_template_type: block-template`
- Podcast Interview Content block is generic (no hardcoded host names)
- All 5 blocks instantiate without error (Category B test)

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| All 8 domain block files exist | Includes these 5 |
| Each has `z2k_template_type: block-template` | YAML field present |
| Each block instantiates without error | Output created; no error log |
