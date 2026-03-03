---
feature_number: "048"
description: "Projects domain — 6 document templates across two subfolder paths with non-z2k YAML and .system-block-stop"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/048 - Projects Domain/"
---

# Feature 048 — Projects Domain

## Description
The Projects domain captures project management and creative writing content. It spans two template paths: `Projects/Templates/` (3 document templates) and `Projects/My Writings/Templates/` (3 document templates), totaling 6 document templates. The system block includes domain identity plus `.system-block-stop` in subfolders. Project templates use a NON-z2k YAML frontmatter structure. The My Writings subfolder has its own `.system-block-stop` file.

## Requirements
### 048-001 — Domain folder structure exists `[quantitative]`
The `Projects/` domain folder exists with both `Templates/` and `My Writings/Templates/` subfolders containing all template files.

### 048-002 — System block exists with domain identity and system-block-stop `[quantitative]`
The Projects domain system block exists and includes domain identity fields. Subfolders contain `.system-block-stop` files to control system block inheritance.

### 048-003 — All 3 document templates in Projects/Templates/ are present `[quantitative]`
All 3 expected document templates exist in `Projects/Templates/`.

### 048-004 — All 3 document templates in My Writings/Templates/ are present `[quantitative]`
All 3 expected document templates exist in `Projects/My Writings/Templates/`.

### 048-005 — Project templates use non-z2k YAML structure `[quantitative]`
Project templates in `Projects/Templates/` use a NON-z2k YAML frontmatter structure that differs from the standard z2k template format.

### 048-006 — My Writings has its own system-block-stop `[quantitative]`
The `Projects/My Writings/` path contains its own `.system-block-stop` file to prevent system block inheritance from the parent Projects domain.

### 048-007 — Templates conform to Projects domain conventions `[qualitative]`
Templates follow consistent naming, frontmatter structure, and content organization patterns appropriate for the Projects domain, respecting the distinction between project management and creative writing templates.
