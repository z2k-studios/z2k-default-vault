---
feature_number: "106"
description: "Citation — formal citation block template with author, title, source, URL, and date fields"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/106 - Citation/"
---

# Feature 106 — Citation

## Description

The Citation block template provides a formal citation block for referencing sources. It is located at the vault root `Templates/` folder as a cross-domain block. The template uses flat field names (`ContentAuthor`, `ContentTitle`, `ContentSource`, `ContentURL`, `ContentDate`) because dot-notation is unsupported in block templates per BLK-001. Field names MUST be consistent with the Quotation block template (Feature 105) — overlapping fields (`ContentAuthor`, `ContentTitle`) share the same names to ensure a unified content namespace.

## Requirements

### 106-001 — Template file exists at correct path `[quantitative]`
The file `Data/Vaults/z2k-default-vault/Templates/Citation.md` exists.

### 106-002 — All fields have fieldInfo declarations `[quantitative]`
All user-facing fields (`ContentAuthor`, `ContentTitle`, `ContentSource`, `ContentURL`, `ContentDate`) have corresponding `{{fieldInfo}}` declarations.

### 106-003 — Renders correctly via Command Queue with standard data `[quantitative]`
The template renders without errors when processed through Command Queue with a standard set of test data values, producing a properly formatted citation block.

### 106-004 — Template quality meets scorecard threshold `[qualitative]`
The template meets the established quality scorecard criteria for structure, naming, documentation, and consistency.

### 106-005 — Uses flat field names (BLK-001 compliance) `[quantitative]`
All field names are flat (no dots): `ContentAuthor`, `ContentTitle`, `ContentSource`, `ContentURL`, `ContentDate`. No dot-notation field names are present.

### 106-006 — Field names consistent with Quotation block `[quantitative]`
Overlapping fields between Citation and Quotation use identical names: `ContentAuthor` and `ContentTitle` appear in both templates with the same semantics.
