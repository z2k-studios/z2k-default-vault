---
z2k_metadata_version: 3.0
z2k_creation_date: "2026-03-02"
z2k_card_status: "Placeholder"
---
# Z2K Tags Taxonomy

This document will eventually contain the full Z2K tag taxonomy — a structured registry of all tag prefixes, their meanings, and usage guidelines.

## Status

Full taxonomy authorship is **deferred**. This placeholder documents known tag prefixes from the v2 system for future reference. A comprehensive taxonomy will be authored in a future project iteration.

## Known Tag Prefixes (from v2)

| Prefix | Domain / Usage |
|---|---|
| `#Media/` | Media type classification (Book, Podcast, Film, etc.) |
| `#Location/` | Geographic location tags |
| `#WriterTags/` | Tags for writing-related content |
| `#Questions/` | Question-type tags |
| `#Card/` | Card metadata tags (legacy v1/v2 fabric system) |
| `#YPO-Forum/` | YPO Forum-specific tags (e.g., Icebreakers) |
| `#Synthesis/` | Synthesis/writing metadata (PublishingMethod, Audience) |
| `#Z2K/` | Core Z2K system tags |

## Notes

- The v2 tag system mixed inline tags with YAML metadata. In v3, most metadata has moved to YAML frontmatter via system blocks.
- Tags that remain as inline tags (e.g., `#Media/Book`) serve a contextual linking function distinct from YAML metadata.
- A future project should define clear boundaries between YAML metadata fields and inline tags.
