---
feature_number: "139"
description: "Resolutions document template for capturing personal resolutions and commitments"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/139 - Resolutions/"
---

# Feature 139 — Resolutions

## Description
The Resolutions template is a document template in the Thoughts domain for capturing personal resolutions, commitments, and intentions. It provides structure for documenting what the user resolves to do, the motivation behind the resolution, and any related context or accountability measures.

## Requirements
### 139-001 — Template file exists `[quantitative]`
Template file exists at `Thoughts/Templates/Resolutions.md`.

### 139-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 139-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 139-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.
