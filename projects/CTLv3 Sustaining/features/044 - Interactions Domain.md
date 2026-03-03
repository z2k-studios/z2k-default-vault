---
feature_number: "044"
description: "Interactions domain — 6 document templates and 1 block template"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/044 - Interactions Domain/"
---

# Feature 044 — Interactions Domain

## Description
The Interactions domain captures records of interactions with people and groups. It contains 6 document templates and 1 block template (Logistics) located at `Interactions/Templates/`. The system block includes domain identity only (no extra fields beyond the standard domain identity). The Logistics block template provides When/Where/Who/Recorded fields.

## Requirements
### 044-001 — Domain folder structure exists `[quantitative]`
The `Interactions/` domain folder exists with a `Templates/` subfolder containing all template files.

### 044-002 — System block exists with domain identity only `[quantitative]`
The Interactions domain system block exists and includes domain identity fields. It does not include ratings or privacy fields beyond the standard domain identity.

### 044-003 — All 6 document templates are present `[quantitative]`
All 6 expected document templates exist in `Interactions/Templates/`.

### 044-004 — Logistics block template is present `[quantitative]`
The 1 expected block template (Logistics) exists in `Interactions/Templates/`, providing When, Where, Who, and Recorded fields.

### 044-005 — Logistics block contains expected fields `[quantitative]`
The Logistics block template includes fields for When, Where, Who, and Recorded.

### 044-006 — Templates conform to Interactions domain conventions `[qualitative]`
Templates follow consistent naming, frontmatter structure, and content organization patterns appropriate for the Interactions domain.
