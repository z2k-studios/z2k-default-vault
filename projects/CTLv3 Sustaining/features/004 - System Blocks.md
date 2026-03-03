---
feature_number: "004"
description: "Validates that root and domain system blocks exist with correct fields"
status: "Complete"
date_added: "2026-03-02"
test_folder: "tests/004 - System Blocks/"
---

# Feature 004 — System Blocks

## Description

System blocks are the YAML injection layer that gives every card its domain identity, metadata, and domain-specific fields. The CTL has 14 system blocks: 1 root + 13 domain. Each must exist, use YAML frontmatter delimiters (`---`), and contain the correct fields.

This feature validates both structure (files exist, fields present) and correctness (field values match the canonical specification).


## Requirements

### 004-001 — Root system block exists `[quantitative]`

`Data/Vaults/z2k-default-vault/.system-block.md` exists.

### 004-002 — Root system block has YAML delimiters `[quantitative]`

The root system block file starts with `---` and has a closing `---` delimiter. Fields are inside the YAML frontmatter block.

### 004-003 — Root system block required fields present `[quantitative]`

The following fields are present in the root system block YAML:
`z2k_metadata_version`, `z2k_metadata_variant`, `z2k_metadata_copyright`, `z2k_metadata_reference`, `z2k_creation_creator`, `z2k_creation_date`, `z2k_creation_timestamp`, `z2k_creation_template`, `z2k_creation_language`, `z2k_creation_library_version`, `z2k_card_source_type`.

### 004-004 — Root system block deprecated fields absent `[quantitative]`

The root system block does NOT contain: `z2k_creation_domain`, `z2k_card_build_state`, `z2k_card_status`.

### 004-005 — Root system block has me fieldInfo `[quantitative]`

The root system block body contains `{{fieldInfo me value="me"}}`.

### 004-006 — All 13 domain system blocks exist `[quantitative]`

A `.system-block.md` file exists in each of the 13 domain root folders.

### 004-007 — Domain system blocks have correct z2k_creation_domain `[quantitative]`

Each domain system block's `z2k_creation_domain` value matches its canonical value:
- Information → `.:Z2K/Domain/Information`
- Thoughts → `.:Z2K/Domain/Thoughts`
- Beliefs → `.:Z2K/Domain/Beliefs`
- Memories → `.:Z2K/Domain/Memories`
- Interactions → `.:Z2K/Domain/Interactions`
- Journals → `.:Z2K/Domain/Journals`
- Logs → `.:Z2K/Domain/Logs`
- Locations → `.:Z2K/Domain/Locations`
- Projects → `.:Z2K/Domain/Projects`
- Entities → `.:Z2K/Domain/Entities`
- Body → `.:Z2K/Domain/Body`
- AI → `.:Z2K/Domain/AI`
- System → `.:Z2K/Domain/System`

### 004-008 — Ratings domains have ratings fields `[quantitative]`

The system blocks for Information, Thoughts, Beliefs, and Memories contain: `z2k_rating_depth`, `z2k_rating_surprisal`, `z2k_rating_passion`.

### 004-009 — Non-ratings domains lack ratings fields `[quantitative]`

System blocks for domains NOT in {Information, Thoughts, Beliefs, Memories} do NOT contain ratings fields.

### 004-010 — Privacy fields correct `[quantitative]`

- Journals system block: `z2k_card_privacy: ".:Z2K/Privacy/Private/Journal"`
- Logs system block: `z2k_card_privacy: ".:Z2K/Privacy/Private/Log"`

### 004-011 — AI domain has perspective field `[quantitative]`

AI system block contains `z2k_creation_perspective: "AI"`.

### 004-012 — Projects has system block stops `[quantitative]`

`.system-block-stop` files exist in the appropriate Projects subfolders (e.g., `Projects/My Writings/.system-block-stop`).

### 004-013 — Domain system blocks have YAML delimiters `[quantitative]`

All 13 domain system block files use `---` frontmatter delimiters.
