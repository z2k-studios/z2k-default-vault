---
z2k_metadata_version: 3.0
z2k_creation_date: "2026-03-02"
z2k_card_type: ".:Z2K/CardType/System/LibraryVersion"
---
# Z2K Template Library — Version 3.0.0

## Library Metadata

| Field | Value |
|---|---|
| Library Version | 3.0.0 |
| Creation Date | 2026-03-02 |
| Template Engine | Z2K Templates Plugin (Handlebars-based) |
| Previous Version | v2 (Obsidian Templater-based) |

## Domain Inventory

| Domain | Document Templates | Block Templates | Total |
|---|---|---|---|
| AI | 0 | 0 | 0 |
| Beliefs | 1 | 0 | 1 |
| Body | 1 | 1 | 2 |
| Entities | 1 | 0 | 1 |
| Information | 21 | 5 | 26 |
| Interactions | 12 | 1 | 13 |
| Journals | 2 | 0 | 2 |
| Locations | 1 | 0 | 1 |
| Logs | 6 | 0 | 6 |
| Memories | 5 | 1 | 6 |
| Projects | 3 | 0 | 3 |
| Projects/My Writings | 4 | 0 | 4 |
| System | 1 | 0 | 1 |
| Thoughts | 7 | 0 | 7 |
| Templates/ (root) | 2 | 5 | 7 |
| **Total** | **67** | **13** | **80** |

## Changelog

### v3.0.0 (2026-03-02)

First v3 release. Complete migration from v2 (Obsidian Templater) to v3 (Z2K Templates Plugin, Handlebars-based).

- **Migration scope:** 67 document templates + 13 block templates across 13 domains + root
- **Key architectural changes:**
  - System blocks replace per-template YAML boilerplate — domain identity, privacy, ratings injected at instantiation
  - System block stops isolate subdomains (e.g., Projects/My Writings) from parent domain inheritance
  - Block templates (`{{> "BlockName"}}`) enable reusable content partials (Logistics, When Where Who, Quotation, etc.)
  - `{{fieldInfo}}` declarations provide typed, prompted fields with validation directives
  - Card Fabric moved to opt-in partial: `{{> "Card Fabric"}}`
- **Templates dropped from v2:** `Memories - Quote an Email`, `Syntheses - Quote an Email` (per design decision)
- **New templates (no v2 equivalent):** 6 podcast host-specific templates, 3 Projects root templates, Contact (General), root Ontology, root Card (General)
- **Design decisions documented:** AI-PERSP, DSB-005, LOC-001, PROJ-YAML, ST-001

## Project Reference

Migration project folder: `System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/`
