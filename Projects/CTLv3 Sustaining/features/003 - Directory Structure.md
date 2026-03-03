---
feature_number: "003"
description: "Validates that the CTL vault folder structure is complete and correct"
status: "Complete"
date_added: "2026-03-02"
test_folder: "tests/003 - Directory Structure/"
---

# Feature 003 — Directory Structure

## Description

The CTLv3 template library depends on a specific vault folder structure: 13 domain folders each with a `Templates/` subfolder, a root `Templates/` folder for cross-domain artifacts, and special substructures for Projects/My Writings. This feature validates that the expected directory tree exists.

This is a pure structure test (Category A) — no Obsidian or Command Queue needed.


## Requirements

### 003-001 — All 13 domain root folders exist `[quantitative]`

The following folders exist in `Data/Vaults/z2k-default-vault/`:
Information, Thoughts, Beliefs, Memories, Interactions, Journals, Logs, Locations, Projects, Entities, Body, AI, System.

### 003-002 — All domains have Templates/ subfolders `[quantitative]`

Each of the 13 domain folders contains a `Templates/` subfolder.

### 003-003 — Root Templates/ folder exists `[quantitative]`

`Data/Vaults/z2k-default-vault/Templates/` exists at vault root.

### 003-004 — Projects/My Writings structure exists `[quantitative]`

`Projects/My Writings/` and `Projects/My Writings/Templates/` both exist.

### 003-005 — System/Templates/ exists `[quantitative]`

`System/Templates/` exists (required for system domain templates).

### 003-006 — Body and AI domains exist `[quantitative]`

`Body/`, `Body/Templates/`, `AI/`, `AI/Templates/` all exist (these were created during migration — verify they persist).
