---
feature_number: "050"
description: "Body domain — 1 document template and 1 block template (Health Log with Flame fields)"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/050 - Body Domain/"
---

# Feature 050 — Body Domain

## Description
The Body domain captures health and physical well-being information. It contains 1 document template and 1 block template located at `Body/Templates/`. The system block includes domain identity only (no extra fields beyond the standard domain identity). The block template is a Health Log that includes Flame automation fields.

## Requirements
### 050-001 — Domain folder structure exists `[quantitative]`
The `Body/` domain folder exists with a `Templates/` subfolder containing all template files.

### 050-002 — System block exists with domain identity only `[quantitative]`
The Body domain system block exists and includes domain identity fields only. It does not include ratings, privacy, or other additional fields.

### 050-003 — Document template is present `[quantitative]`
The 1 expected document template exists in `Body/Templates/`.

### 050-004 — Health Log block template is present `[quantitative]`
The 1 expected block template (Health Log) exists in `Body/Templates/`.

### 050-005 — Health Log block includes Flame automation fields `[quantitative]`
The Health Log block template includes fields specific to the Flame automation integration.

### 050-006 — Templates conform to Body domain conventions `[qualitative]`
Templates follow consistent naming, frontmatter structure, and content organization patterns appropriate for the Body domain.
