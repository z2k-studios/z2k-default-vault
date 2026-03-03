---
feature_number: "105"
description: "Quotation (Root) — blockquote with attribution and optional [!me] perspective section"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/105 - Quotation (Root)/"
---

# Feature 105 — Quotation (Root)

## Description

The Quotation block template renders a blockquote with attribution and an optional `[!me]` perspective section. It is located at the vault root `Templates/` folder as a cross-domain block. The template uses flat field names (`ContentAuthor`, `ContentTitle`, `ContentText`) because dot-notation is unsupported in block templates per BLK-001. These field names MUST be consistent with the Citation block template (Feature 106) — overlapping fields share the same names to ensure a unified content namespace.

## Requirements

### 105-001 — Template file exists at correct path `[quantitative]`
The file `Data/Vaults/z2k-default-vault/Templates/Quotation.md` exists.

### 105-002 — All fields have fieldInfo declarations `[quantitative]`
All user-facing fields (`ContentAuthor`, `ContentTitle`, `ContentText`) have corresponding `{{fieldInfo}}` declarations.

### 105-003 — Renders correctly via Command Queue with standard data `[quantitative]`
The template renders without errors when processed through Command Queue with a standard set of test data values, producing a blockquote with attribution.

### 105-004 — Template quality meets scorecard threshold `[qualitative]`
The template meets the established quality scorecard criteria for structure, naming, documentation, and consistency.

### 105-005 — Uses flat field names (BLK-001 compliance) `[quantitative]`
All field names are flat (no dots): `ContentAuthor`, `ContentTitle`, `ContentText`. No dot-notation field names are present.

### 105-006 — Field names consistent with Citation block `[quantitative]`
Overlapping fields between Quotation and Citation use identical names: `ContentAuthor` and `ContentTitle` appear in both templates with the same semantics.

### 105-007 — Optional perspective section renders correctly `[quantitative]`
When perspective data is provided, the template renders a valid `[!me]` callout section following the blockquote.
