---
feature_number: "047"
description: "Locations domain — 1 document template with domain identity only system block"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/047 - Locations Domain/"
---

# Feature 047 — Locations Domain

## Description
The Locations domain captures place-based information. It contains 1 document template located at `Locations/Templates/`. The system block includes domain identity only (no extra fields beyond the standard domain identity).

## Requirements
### 047-001 — Domain folder structure exists `[quantitative]`
The `Locations/` domain folder exists with a `Templates/` subfolder containing the template file.

### 047-002 — System block exists with domain identity only `[quantitative]`
The Locations domain system block exists and includes domain identity fields only. It does not include ratings, privacy, or other additional fields.

### 047-003 — Document template is present `[quantitative]`
The 1 expected document template exists in `Locations/Templates/`.

### 047-004 — Templates conform to Locations domain conventions `[qualitative]`
The template follows consistent naming, frontmatter structure, and content organization patterns appropriate for the Locations domain.
