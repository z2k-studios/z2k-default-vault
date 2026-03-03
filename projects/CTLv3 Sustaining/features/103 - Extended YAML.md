---
feature_number: "103"
description: "Extended YAML — maximalist optional YAML block template for privacy, projects, structures, ratings, and fabric arrays"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/103 - Extended YAML/"
---

# Feature 103 — Extended YAML

## Description

Extended YAML is a block template providing maximalist optional YAML fields that users can manually insert into any card's frontmatter. It covers extended metadata categories including privacy settings, project associations, structural fields, ratings, and fabric array fields. Like Card Fabric, this block is never auto-injected — the user manually inserts it when a card needs additional metadata beyond what the standard system block and document template provide.

## Requirements

### 103-001 — Template file exists at correct path `[quantitative]`
The file `Data/Vaults/z2k-default-vault/Templates/Extended YAML.md` exists.

### 103-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-facing field in the template has a corresponding `{{fieldInfo}}` declaration.

### 103-003 — Renders correctly via Command Queue with standard data `[quantitative]`
The template renders without errors when processed through Command Queue with a standard set of test data values.

### 103-004 — Template quality meets scorecard threshold `[qualitative]`
The template meets the established quality scorecard criteria for structure, naming, documentation, and consistency.

### 103-005 — Template is manual-insert only `[qualitative]`
The block is designed for explicit manual insertion by the user and is never auto-injected into cards by the system.

### 103-006 — Covers all extended YAML categories `[quantitative]`
The template includes fields for privacy, projects, structures, ratings, and fabric arrays.
