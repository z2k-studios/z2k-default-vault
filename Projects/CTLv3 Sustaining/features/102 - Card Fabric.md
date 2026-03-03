---
feature_number: "102"
description: "Card Fabric — opt-in cognitive fabric block template for mental models, contextual, reference, and geo sections"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/102 - Card Fabric/"
---

# Feature 102 — Card Fabric

## Description

Card Fabric is an opt-in block template that provides a cognitive fabric section for cards. It builds both YAML array fields and markdown body sections covering mental models, contextual links, reference material, and geographic context. The template uses flat field names (`FabricMentalModel`, `FabricContextual`, `FabricReference`, `FabricGeoContext`) because dot-notation is unsupported in block templates per BLK-001. Section rendering is conditional via `{{formatStringBulletize}}`. Cards opt in by including `{{> "Card Fabric"}}` — the block is never auto-injected.

## Requirements

### 102-001 — Template file exists at correct path `[quantitative]`
The file `Data/Vaults/z2k-default-vault/Templates/Card Fabric.md` exists.

### 102-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-facing field (`FabricMentalModel`, `FabricContextual`, `FabricReference`, `FabricGeoContext`) has a corresponding `{{fieldInfo}}` declaration.

### 102-003 — Renders correctly via Command Queue with standard data `[quantitative]`
The template renders without errors when processed through Command Queue with a standard set of test data values, producing both YAML and markdown body output.

### 102-004 — Template quality meets scorecard threshold `[qualitative]`
The template meets the established quality scorecard criteria for structure, naming, documentation, and consistency.

### 102-005 — Uses flat field names (BLK-001 compliance) `[quantitative]`
All field names are flat (no dots): `FabricMentalModel`, `FabricContextual`, `FabricReference`, `FabricGeoContext`. No dot-notation field names are present.

### 102-006 — Uses formatStringBulletize for conditional rendering `[quantitative]`
The template uses `{{formatStringBulletize}}` to conditionally render each fabric section only when the user provides data.

### 102-007 — Template is opt-in only `[qualitative]`
The block is designed for explicit inclusion via `{{> "Card Fabric"}}` and is never auto-injected into cards by the system.
