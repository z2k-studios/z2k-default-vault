---
feature_number: "052"
description: "System domain — 1 document template with domain identity only system block"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/052 - System Domain/"
---

# Feature 052 — System Domain

## Description
The System domain captures vault infrastructure and system-level content. It contains 1 document template located at `System/Templates/`. The system block includes domain identity only (no extra fields beyond the standard domain identity).

## Requirements
### 052-001 — Domain folder structure exists `[quantitative]`
The `System/` domain folder exists with a `Templates/` subfolder containing the template file.

### 052-002 — System block exists with domain identity only `[quantitative]`
The System domain system block exists and includes domain identity fields only. It does not include ratings, privacy, or other additional fields.

### 052-003 — Document template is present `[quantitative]`
The 1 expected document template exists in `System/Templates/`.

### 052-004 — Templates conform to System domain conventions `[qualitative]`
The template follows consistent naming, frontmatter structure, and content organization patterns appropriate for the System domain.
