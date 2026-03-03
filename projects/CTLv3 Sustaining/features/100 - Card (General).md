---
feature_number: "100"
description: "Card (General) — cross-domain generic card template with minimal domain-agnostic structure"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/100 - Card (General)/"
---

# Feature 100 — Card (General)

## Description

Card (General) is the cross-domain generic card template located at the vault root `Templates/` folder. It provides a minimal, domain-agnostic card structure suitable for any domain. The "(General)" postfix follows the domain default naming pattern used throughout the CTL. As a document template, it includes a suggested title and standard v3 metadata fields.

## Requirements

### 100-001 — Template file exists at correct path `[quantitative]`
The file `Data/Vaults/z2k-default-vault/Templates/Card (General).md` exists.

### 100-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-facing field in the template has a corresponding `{{fieldInfo}}` declaration.

### 100-003 — Renders correctly via Command Queue with standard data `[quantitative]`
The template renders without errors when processed through Command Queue with a standard set of test data values.

### 100-004 — Template quality meets scorecard threshold `[qualitative]`
The template meets the established quality scorecard criteria for structure, naming, documentation, and consistency.

### 100-005 — Template is domain-agnostic `[qualitative]`
The template contains no domain-specific fields or references, making it suitable for use across all domains.
