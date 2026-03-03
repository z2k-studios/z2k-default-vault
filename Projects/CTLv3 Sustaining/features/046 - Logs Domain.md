---
feature_number: "046"
description: "Logs domain — 5 document templates with privacy system block"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/046 - Logs Domain/"
---

# Feature 046 — Logs Domain

## Description
The Logs domain captures daily logs and structured tracking entries. It contains 5 document templates located at `Logs/Templates/`. The system block includes a privacy field set to `.:Z2K/Privacy/Private/Log`.

## Requirements
### 046-001 — Domain folder structure exists `[quantitative]`
The `Logs/` domain folder exists with a `Templates/` subfolder containing all template files.

### 046-002 — System block exists with privacy field `[quantitative]`
The Logs domain system block exists and includes the privacy field set to `.:Z2K/Privacy/Private/Log`.

### 046-003 — All 5 document templates are present `[quantitative]`
All 5 expected document templates exist in `Logs/Templates/`.

### 046-004 — Templates conform to Logs domain conventions `[qualitative]`
Templates follow consistent naming, frontmatter structure, and content organization patterns appropriate for the Logs domain.
