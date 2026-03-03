---
feature_number: "147"
description: "Locations (General) document template — domain default for the Locations domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/147 - Locations (General)/"
---

# Feature 147 — Locations (General)

## Description
The Locations (General) template is the domain default document template for the Locations domain. It captures information about places and locations, providing structured fields for recording geographic details, descriptions, significance, and associations with other cards in the vault.

## Requirements
### 147-001 — Template file exists `[quantitative]`
Template file exists at `Locations/Templates/Locations (General).md`.

### 147-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 147-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 147-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.
