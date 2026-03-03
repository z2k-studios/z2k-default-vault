---
feature_number: "049"
description: "Entities domain — 1 document template (Contact General); full CRM deferred"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/049 - Entities Domain/"
---

# Feature 049 — Entities Domain

## Description
The Entities domain captures information about people, organizations, and other entities. It contains 1 document template (Contact (General)) located at `Entities/Templates/`. The system block includes domain identity only (no extra fields beyond the standard domain identity). The template is minimal, with full CRM functionality deferred to a future effort.

## Requirements
### 049-001 — Domain folder structure exists `[quantitative]`
The `Entities/` domain folder exists with a `Templates/` subfolder containing the template file.

### 049-002 — System block exists with domain identity only `[quantitative]`
The Entities domain system block exists and includes domain identity fields only. It does not include ratings, privacy, or other additional fields.

### 049-003 — Contact (General) document template is present `[quantitative]`
The 1 expected document template — Contact (General) — exists in `Entities/Templates/`.

### 049-004 — Contact (General) is minimal `[quantitative]`
The Contact (General) template provides a minimal contact structure, as full CRM functionality is deferred.

### 049-005 — Templates conform to Entities domain conventions `[qualitative]`
The template follows consistent naming, frontmatter structure, and content organization patterns appropriate for the Entities domain.
