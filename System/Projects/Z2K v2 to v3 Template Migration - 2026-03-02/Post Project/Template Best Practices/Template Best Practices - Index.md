---
document_type: Post-Project Deliverable Index
status: Active
---
# Template Best Practices — Index

Best practices for template hierarchy and system development, collected during the CTLv3 migration project. Intended destination: **Z2K Templates Plugin documentation website**.

Notes and observations are collected here during execution. The full document will be drafted after all CTLv3 work is complete and validated.

---

## Purpose

This document will capture reusable guidance for anyone building a template library using the Z2K Templates Plugin — covering folder structure, system block design, block partial strategy, naming conventions, and migration patterns.

---

## Observations Log

| # | Observation | Phase/Task | Notes |
|---|---|---|---|
| 1 | `Templates/` subfolders make filename prefixes (`Template -`, `Block -`) unnecessary and harmful — prefixed files coexist with unprefixed v3 files, creating duplicates and confusion | Phase 6, Task 12 | Old prefixed files had to be cleaned up in Phase 8 |
| 2 | System block YAML delimiters (`---`) are mandatory — without them, fields inject as body text instead of frontmatter | Phase 2, Task 03 | Easy to miss; causes silent failures |
| 3 | Handlebars comment syntax matters: `{{!-- --}}` (double-dash) is required when the comment body contains `{{` or `}}` | Phase 6, Tasks 10–22 | Single-form `{{! }}` closes at first `}}`, producing stray text |
| 4 | Domain system blocks should only contain fields universal to that domain — ratings fields belong in domains that rate content (Information, Thoughts, Memories, Beliefs), not everywhere | Phase 3, Tasks 04–05 | Minimalist approach prevents unnecessary field noise |
| 5 | `.system-block-stop` files are the correct mechanism for preventing system block inheritance into project-scoped subfolders | Phase 3, Task 06 | Used for Projects domain (My Writings) and per-project isolation |
| 6 | Block partials (`{{> "Block Name"}}`) are powerful for shared content sections but should be opt-in via template comments, not injected automatically | Phase 4, Task 07 | Card Fabric pattern: `{{!-- To include: {{> "Card Fabric"}} --}}` |
| 7 | Date navigation helpers (`dateAdd`, `formatDate`, `formatString`, `wikilink` with nested subexpressions) can compose complex inter-note navigation links | Phase 6, Tasks 16–17 | Daily/Weekly/Monthly/Yearly Log navigation links |
| 8 | Command Queue testing is reliable for `prompt: "none"` templates; 8-second wait after queue drop is sufficient for auto-processing | Phase 0, Task 01 | Eliminated the need for user-assisted testing in most cases |
| 9 | Personal templates should use `z2k_template_author` to distinguish from library templates — enables future separation into personal vaults | Phase 6, Tasks 13–14 | 6 Interactions + PCT Trail Day marked personal |
| 10 | Dot-notation for prompted field names (e.g., `Content.Author`) is unsupported in the plugin — use flat names (`ContentAuthor`) instead | Phase 4, BLK-001 | Filed as plugin issue; workaround in place |

---

## Draft Best Practices

The following best practices are drawn from the CTLv3 migration (80 templates across 13 domains). They apply to anyone building a template library with the Z2K Templates Plugin.

### Folder Structure

Use `Templates/` subfolders within each domain folder. This structure provides natural namespacing and eliminates the need for filename prefixes like `Template -` or `Block -`. A file named `Book.md` inside `Information/Templates/` is unambiguous. Prefixed names create confusion when v3 files coexist with legacy files.

### System Block Design

- **Root system block**: Universal metadata only — `z2k_metadata_version`, `z2k_metadata_copyright`, `z2k_creation_template`, `z2k_creation_date`, `z2k_creation_library_version`, and the `me` fieldInfo declaration.
- **Domain system blocks**: Domain identity (`z2k_creation_domain`) plus domain-specific fields. Only add ratings fields to domains that genuinely rate content. Keep system blocks minimal — every field here appears on every card in the domain.
- **YAML delimiters are mandatory**: System block files must use `---` frontmatter delimiters or their fields inject as body text.

### Block Partial Strategy

Use block templates for reusable structural sections (Card Fabric, Quotation, content section scaffolds). Make blocks opt-in rather than automatic — include them as commented-out references in document templates so users can activate them when needed.

Pattern: `{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}`

### Naming Conventions

- Document templates: `<Descriptive Name>.md` (e.g., `Academic Paper.md`)
- Domain defaults: `<Domain> (General).md` (e.g., `Information (General).md`)
- Block templates: `<Descriptive Name>.md` (e.g., `Card Fabric.md`, `Podcast Interview Content.md`)
- System blocks: `.system-block.md` (dot-prefixed, one per folder)

### Testing Approach

Command Queue is the preferred testing method. Write JSON command files to the plugin's queue folder, wait 8 seconds for auto-processing, then read and verify the output file directly from the filesystem. Use `templatePath` (not `templateContents`) to test the full system-block → template → output chain.

Golden file model: save the first successful output as `expected.md`; subsequent runs diff against it to catch regressions.

### Bootstrapping with an Active Plugin

When building a template library against a plugin under active development, validate each plugin feature before committing to it. Maintain a Feature Prioritization table tracking which features have been tested and confirmed working. File plugin issues immediately when discovered — they affect template design decisions downstream.
