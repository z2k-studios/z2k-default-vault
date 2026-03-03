---
feature_number: "042"
description: "Beliefs domain — simplest domain with 1 document template (domain default only)"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/042 - Beliefs Domain/"
---

# Feature 042 — Beliefs Domain

## Description
The Beliefs domain captures core beliefs and convictions. It is the simplest domain in the vault, containing only 1 document template (the domain default) located at `Beliefs/Templates/`. The system block includes ratings fields (depth, surprisal, passion).

## Requirements
### 042-001 — Domain folder structure exists `[quantitative]`
The `Beliefs/` domain folder exists with a `Templates/` subfolder containing the template file.

### 042-002 — System block exists with ratings fields `[quantitative]`
The Beliefs domain system block exists and includes domain identity fields plus ratings fields (depth, surprisal, passion).

### 042-003 — Domain default template is present `[quantitative]`
The 1 expected document template (domain default) exists in `Beliefs/Templates/`.

### 042-004 — Templates conform to Beliefs domain conventions `[qualitative]`
The domain default template follows consistent naming, frontmatter structure, and content organization patterns appropriate for the Beliefs domain.
