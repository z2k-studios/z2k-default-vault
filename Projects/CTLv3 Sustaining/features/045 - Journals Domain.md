---
feature_number: "045"
description: "Journals domain — 2 document templates with privacy system block; Daily Journal absorbs retired Ideas domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/045 - Journals Domain/"
---

# Feature 045 — Journals Domain

## Description
The Journals domain captures journal entries. It contains 2 document templates located at `Journals/Templates/`. The system block includes a privacy field set to `.:Z2K/Privacy/Private/Journal`. The Daily Journal template absorbs the retired Ideas domain by including sections for Passing Thoughts, Memories, and Information.

## Requirements
### 045-001 — Domain folder structure exists `[quantitative]`
The `Journals/` domain folder exists with a `Templates/` subfolder containing all template files.

### 045-002 — System block exists with privacy field `[quantitative]`
The Journals domain system block exists and includes the privacy field set to `.:Z2K/Privacy/Private/Journal`.

### 045-003 — All 2 document templates are present `[quantitative]`
All 2 expected document templates exist in `Journals/Templates/`, including the Daily Journal.

### 045-004 — Daily Journal includes retired Ideas domain sections `[quantitative]`
The Daily Journal template includes sections for Passing Thoughts, Memories, and Information, absorbing the retired Ideas domain functionality.

### 045-005 — Templates conform to Journals domain conventions `[qualitative]`
Templates follow consistent naming, frontmatter structure, and content organization patterns appropriate for the Journals domain.
