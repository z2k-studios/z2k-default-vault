---
feature_number: "104"
description: "Perspective - Me — standard [!me] callout block for vault-owner perspective"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/104 - Perspective - Me/"
---

# Feature 104 — Perspective - Me

## Description

Perspective - Me is a block template that renders a standard `[!me]` callout block for the vault owner's perspective. It provides a structured way to capture the user's personal take, opinion, or reflection on a card's subject. The template uses a fixed literal `me` as the callout type — not `{{me}}`, which is a future Core Plugin feature. The single user-facing field is `PerspectiveText`.

## Requirements

### 104-001 — Template file exists at correct path `[quantitative]`
The file `Data/Vaults/z2k-default-vault/Templates/Perspective - Me.md` exists.

### 104-002 — All fields have fieldInfo declarations `[quantitative]`
The `PerspectiveText` field has a corresponding `{{fieldInfo}}` declaration.

### 104-003 — Renders correctly via Command Queue with standard data `[quantitative]`
The template renders without errors when processed through Command Queue with a standard set of test data values, producing a valid `[!me]` callout block.

### 104-004 — Template quality meets scorecard threshold `[qualitative]`
The template meets the established quality scorecard criteria for structure, naming, documentation, and consistency.

### 104-005 — Uses fixed literal callout type `[quantitative]`
The callout type is the literal string `me`, not a template variable `{{me}}`. The `{{me}}` syntax is reserved for a future Core Plugin feature.

### 104-006 — Produces valid Obsidian callout syntax `[quantitative]`
The rendered output is a valid Obsidian callout block using the `[!me]` syntax.
