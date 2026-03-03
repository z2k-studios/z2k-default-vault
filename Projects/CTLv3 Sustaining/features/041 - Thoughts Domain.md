---
feature_number: "041"
description: "Thoughts domain — 7 document templates for internal thoughts and quotations"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/041 - Thoughts Domain/"
---

# Feature 041 — Thoughts Domain

## Description
The Thoughts domain captures original ideas, reflections, and attributed quotations. It contains 7 document templates located at `Thoughts/Templates/`. The system block includes ratings fields (depth, surprisal, passion). Source types include InternalThought and Quotation.

## Requirements
### 041-001 — Domain folder structure exists `[quantitative]`
The `Thoughts/` domain folder exists with a `Templates/` subfolder containing all template files.

### 041-002 — System block exists with ratings fields `[quantitative]`
The Thoughts domain system block exists and includes domain identity fields plus ratings fields (depth, surprisal, passion).

### 041-003 — All 7 document templates are present `[quantitative]`
All 7 expected document templates exist in `Thoughts/Templates/`, covering the InternalThought and Quotation source types plus the domain default.

### 041-004 — Source type field values are correct `[quantitative]`
Each template that specifies a source type uses one of the valid values: InternalThought, Quotation.

### 041-005 — Templates conform to Thoughts domain conventions `[qualitative]`
Templates follow consistent naming, frontmatter structure, and content organization patterns appropriate for the Thoughts domain.
