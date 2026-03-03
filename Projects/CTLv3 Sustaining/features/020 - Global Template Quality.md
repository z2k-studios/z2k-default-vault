---
feature_number: "020"
description: "Cross-cutting quantitative quality requirements that apply to every template in the CTL"
status: "Complete"
date_added: "2026-03-02"
test_folder: "tests/020 - Global Template Quality/"
---

# Feature 020 — Global Template Quality

## Description

This feature defines the quantitative quality requirements that every template in the CTL must satisfy. These are script-testable, deterministic checks that can be run against every template file without rendering. They enforce naming conventions, metadata standards, syntax validity, and structural consistency.

The test suite for this feature iterates over ALL template files in the vault and runs each check. A single failure in any template fails the corresponding requirement. **No exclusions are made for personal templates** — personal templates are prohibited in the CTL system vault entirely (see 020-013). If a personal template exists, it will fail both 020-005 (wrong author) and 020-013 (existence violation).

This is a cross-cutting feature — it does not test any individual template's behavior, but rather the baseline quality bar that all templates must meet.


## Requirements

### 020-001 — Valid Handlebars syntax `[quantitative]`

Every template file contains valid Handlebars syntax: all `{{` have matching `}}`, all `{{#if}}` have `{{/if}}`, all `{{#each}}` have `{{/each}}`, no orphaned tags.

### 020-002 — No v2 Templater syntax remaining `[quantitative]`

No template file contains `<% ... %>` Templater syntax unless wrapped in a `{{! FLAGGED: ... }}` comment.

### 020-003 — Document templates have required YAML metadata `[quantitative]`

Every document template (files with `z2k_template_type: document-template`) contains:
- `z2k_template_type: document-template`
- `z2k_template_version: "v3.0.0 2026-03-02"`
- `z2k_template_suggested_title`

### 020-004 — Block templates have required YAML metadata `[quantitative]`

Every block template (files with `z2k_template_type: block-template`) contains:
- `z2k_template_type: block-template`

### 020-005 — Template author field correct `[quantitative]`

Every template in the vault has `z2k_template_author` set to `"Z2K Studios, LLC"`. No other values. This check applies to all templates without exclusion — personal author values are themselves a violation (see 020-013).

### 020-006 — Field naming conventions followed `[quantitative]`

All custom field names in `{{fieldInfo ...}}` declarations use PascalCase (first letter uppercase). Built-in fields (`today`, `creator`, `timestamp`, `templateName`, `me`) are excluded from this check.

### 020-007 — Comment syntax correct `[quantitative]`

Comments containing `{{` or `}}` use double-dash syntax `{{!-- ... --}}`, not single-form `{{! ... }}`.

### 020-008 — No trailing spaces from comments `[quantitative]`

Comment lines (`{{! ... }}` or `{{!-- ... --}}`) do not leave trailing whitespace on the line when they are the only content on that line. Comments intended to clear their line should be flush (no leading spaces unless at an indentation level).

### 020-009 — All fieldInfo declarations are well-formed `[quantitative]`

Every `{{fieldInfo ...}}` declaration has at minimum a field name. Declarations with prompts have quoted prompt strings. No malformed or incomplete fieldInfo tags.

### 020-010 — Block partial references point to existing files `[quantitative]`

Every `{{> "BlockName"}}` reference in a template corresponds to an existing block template file in the vault. No references to nonexistent blocks.

### 020-011 — Source type values are canonical `[quantitative]`

Every `z2k_card_source_type` value in a template matches one of the canonical values from the registry: `AI/ChatGPT`, `Book`, `ClassLecture`, `Conference`, `Conversation`, `Email`, `InternalMemories`, `InternalMemory`, `InternalThought`, `Interview`, `Lecture`, `LifeLessons`, `Meeting`, `OtherCards`, `Person`, `Podcast`, `Quotation`, `Unknown`, `WebArticle`.

Note: `InternalMemory` (singular) is in the original spec but no current template uses it — all Memories templates use `InternalMemories` (plural). See z2k-default-vault issue #2.

### 020-012 — No duplicate template filenames across domains `[quantitative]`

Where templates share the same name across domains (e.g., `Ontology.md` in Thoughts, Information, Memories, and Root), this is intentional. But no two templates in the SAME `Templates/` folder should have the same filename.

### 020-013 — No personal templates in the CTL vault `[quantitative]`

No template in the CTL system vault carries a personal author value. Specifically: `z2k_template_author` must not be `"Geoff (z2k-gwp)"` or any other non-Z2K Studios value. Personal templates are not permitted in `z2k-default-vault` — they belong in a separate personal vault. A template with a personal author fails this requirement regardless of any other correct properties it may have.
