---
feature_number: "043"
description: "Memories domain — 4 document templates and 1 block template (When Where Who)"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/043 - Memories Domain/"
---

# Feature 043 — Memories Domain

## Description
The Memories domain captures personal memories and recollections. It contains 4 document templates and 1 block template located at `Memories/Templates/`. The system block includes ratings fields (depth, surprisal, passion). The block template provides a "When Where Who" structure capturing date, location, and who was present.

## Requirements
### 043-001 — Domain folder structure exists `[quantitative]`
The `Memories/` domain folder exists with a `Templates/` subfolder containing all template files.

### 043-002 — System block exists with ratings fields `[quantitative]`
The Memories domain system block exists and includes domain identity fields plus ratings fields (depth, surprisal, passion).

### 043-003 — All 4 document templates are present `[quantitative]`
All 4 expected document templates exist in `Memories/Templates/`.

### 043-004 — When Where Who block template is present `[quantitative]`
The 1 expected block template exists in `Memories/Templates/`, providing structured fields for date, location, and who was present.

### 043-005 — When Where Who block contains expected fields `[quantitative]`
The When Where Who block template includes fields for date/when, location/where, and who was present.

### 043-006 — Templates conform to Memories domain conventions `[qualitative]`
Templates follow consistent naming, frontmatter structure, and content organization patterns appropriate for the Memories domain.
