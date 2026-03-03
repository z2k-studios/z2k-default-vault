---
feature_number: "040"
description: "Information domain — largest domain with 26 templates including podcast interview architecture"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/040 - Information Domain/"
---

# Feature 040 — Information Domain

## Description
The Information domain captures external knowledge sources — books, podcasts, web articles, quotations, and other reference material. It is the largest domain in the vault with 21 document templates and 5 block templates (26 total), located at `Information/Templates/`. The system block includes ratings fields (depth, surprisal, passion). The domain features a podcast interview architecture with a generic template plus 6 host-specific presets that leverage a block partial. Source types include Book, Podcast, WebArticle, Quotation, and Unknown.

## Requirements
### 040-001 — Domain folder structure exists `[quantitative]`
The `Information/` domain folder exists with a `Templates/` subfolder containing all template files.

### 040-002 — System block exists with ratings fields `[quantitative]`
The Information domain system block exists and includes domain identity fields plus ratings fields (depth, surprisal, passion).

### 040-003 — All 21 document templates are present `[quantitative]`
All 21 expected document templates exist in `Information/Templates/`. This includes templates for source types: Book, Podcast (generic + host-specific presets), WebArticle, Quotation, Unknown, and the domain default.

### 040-004 — All 5 block templates are present `[quantitative]`
All 5 expected block templates exist in `Information/Templates/`, including the podcast interview block partial used by host-specific presets.

### 040-005 — Podcast interview architecture uses block partial `[quantitative]`
The 6 host-specific podcast presets reference the podcast interview block partial rather than duplicating interview structure inline.

### 040-006 — Source type field values are correct `[quantitative]`
Each template that specifies a source type uses one of the valid values: Book, Podcast, WebArticle, Quotation, Unknown.

### 040-007 — Templates conform to Information domain conventions `[qualitative]`
Templates follow consistent naming, frontmatter structure, and content organization patterns appropriate for the Information domain.
