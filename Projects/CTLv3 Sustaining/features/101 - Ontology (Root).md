---
feature_number: "101"
description: "Ontology (Root) — cross-domain Map of Content / Ontology card template"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/101 - Ontology (Root)/"
---

# Feature 101 — Ontology (Root)

## Description

The Ontology template at the vault root `Templates/` folder provides a cross-domain Map of Content (MOC) / Ontology card. It is used to create structural index cards that organize and link related cards across the vault. Domain-specific Ontology templates also exist in Thoughts, Information, and Memories — this is the cross-domain version that lives at the root level and can be used in any domain context.

## Requirements

### 101-001 — Template file exists at correct path `[quantitative]`
The file `Data/Vaults/z2k-default-vault/Templates/Ontology.md` exists.

### 101-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-facing field in the template has a corresponding `{{fieldInfo}}` declaration.

### 101-003 — Renders correctly via Command Queue with standard data `[quantitative]`
The template renders without errors when processed through Command Queue with a standard set of test data values.

### 101-004 — Template quality meets scorecard threshold `[qualitative]`
The template meets the established quality scorecard criteria for structure, naming, documentation, and consistency.

### 101-005 — Template is cross-domain compatible `[qualitative]`
The root Ontology template is usable across all domains without domain-specific assumptions, while domain-specific Ontology variants exist separately in Thoughts, Information, and Memories.
