---
title: Template Library - System Architecture - Open Questions
created: 2026-03-01
status: in-progress
---

# Template Library — System Architecture — Open Questions

This document captures unresolved architectural decisions about the Z2K v3 template system — independent of the v2→v3 migration. These define how the library should be designed going forward.

---

## YAML Schema

### Q1 — Card Fabric: Direction for v3

In v2, every template ended with a markdown "Card Fabric" section listing typed relationship fibers (Contextual, Mental Model, Destination, Reference, Instigation, GeoContext). The maximalist YAML template also had corresponding YAML array fields (`z2k_contextual_tags`, `z2k_destination_links`, `z2k_mentalmodels_tags`, etc.). In v3, neither the system-block nor any existing template includes this structure.

Options:
- **a)** Keep as markdown — move the Card Fabric section into a shared block partial (`{{> "Block - Card Fabric - Standard"}}`) inserted at the bottom of templates that need it
- **b)** Move to YAML only — express fabric as YAML array properties in the system-block or domain system-blocks, dropping the markdown section
- **c)** Drop entirely — Obsidian's native properties panel + graph view have made this redundant
- **d)** Hybrid — YAML arrays for machine-readable fibers, optional markdown section for human annotation

If kept, which fiber types remain relevant? (Some v2 templates had Destination + Reference + Instigation; others only Contextual + GeoContext.)

**Answer:**
The card fabric section was a major portion of the version to design. It is going to the wayside. Now that Obsidian allows you to have tags and wiki links inside your YAML code, it is much easier now to store away information about a card without it being within the body of the text of the card. That was one of the larger motivations for the card fabric.

That said, I think that adding in a block template at the root system level for card fabric would be still a good idea, as there are some items inside the card fabric that are more specific. The question is, should these go in as YAML fields or as information in the body of the text? I'd like to at least initially build out both versions 

The block template should be smart in being able to not display a section if there is no actual data provided. The header preambles for each section should be outputted conditionally. One way to do that is by using the built-in helper function, formatStringBulletize, see `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatStringBulletize.md`. Thus something like

```
{{fieldInfo Fabric.MentalModel prompt="What mental models are used for this card? (One per line)"}}
# Fabrics
{{formatStringBulletize Fabric.MentalModel 0 "#### Mental Models\n"}}
```

Claude: 
`Fabric.MentalModel` as a prompted field name (dot-notation) is likely unsupported for user-defined fields — the plugin would need to create a nested object structure on prompt. The user has acknowledged this as speculative and wants to test it. If it fails, the fallback would be a flat name like `FabricMentalModel`. No decision needed here — proceed as specified.

---

### Q2 — Ratings Fields

The v2 maximalist template included three subjective rating fields:
- `z2k_rating_depth` — depth of the card's content
- `z2k_rating_surprisal` — how surprising or novel
- `z2k_rating_passion` — personal passion/relevance level

Are these still a v3 concept? If yes:
- Should they be in the root system-block (universal), domain system-blocks (selective), or individual templates (opt-in)?
- Are the names/definitions still correct?
- Is "0 - Unknown" still the right default value format?

**Answer:**
they should be used for information, thoughts, memories, and beliefs.   normally, I would have them exist as a block template, but unfortunately, block templates cannot be loaded in side YAML code. so unless you have any better ideas, I think they have to be just inside the system block code for each of those domains 

---

### Q3 — `z2k_card_activation` — Retired or Renamed?

v2 templates included `z2k_card_activation: ".:Z2K/Inactive"`. The v3 system-block drops this field entirely without replacement. v3 introduces `z2k_card_build_state: ".:Z2K/BuildState/Uninitialized"` which may cover similar ground.

Questions:
1. Is `z2k_card_activation` fully retired in v3?
2. What is `z2k_card_build_state` intended to track — is it the card's completion state (Uninitialized → Active → Retired)?
3. Should `z2k_card_build_state` be in the root system-block (applying to all cards universally) or only in specific templates?

**Answer:**
this can be removed.  

---

### Q4 — `z2k_card_status` in Template Files

v2 templates set `z2k_card_status: ".:Z2K/Status/Template"` — distinguishing the template file itself from instantiated content. v3's system-block sets it to `".:Z2K/Status/Ongoing"` for content files.

For template *files* stored in Templates/ folders:
- Should template files carry `z2k_card_status: ".:Z2K/Status/Template"` in their own YAML, overriding the system-block value?
- Or is the `z2k_template_type: document-template` property sufficient to identify them, making a status override unnecessary?

**Answer:**
 this can be removed. This is also covered by the Z2K Templates property

---

### Q5 — Maximalist vs. Minimalist YAML Schema

v2 had two YAML partial templates — Minimalist (essential fields only) and Maximalist (adds privacy, projects, structures, ratings, and fabric YAML arrays).

For v3, should there be:
- **a)** One unified schema (everything in the root system-block, with domain-level blocks overriding where needed)
- **b)** Two tiers preserved — a "standard" system-block and an "extended" one for power users
- **c)** Per-domain tuning only — each domain's system-block adds what's relevant, no global maximalist/minimalist distinction

**Answer:**
 without a doubt, the minimalist set of fields needs to be inside the appropriate system blocks 
 then inside the root templates folder, provide an extended YAML block template that users can include whenever they want to have extra data to be stored.  including the extended data will be solely up to the user to manually insert them 

---

### Q6 — Privacy Field

`z2k_card_privacy` appeared in several v2 templates (Daily Log, Daily Journal, YPO templates, Doug/personal interaction templates). Values like `.:Z2K/Privacy/Private/Log`, `.:Z2K/Privacy/Uber-Private/YPO`, `.:Z2K/Privacy/Private/Professional`.

Is this field still a v3 concept? If yes:
- Should it live in domain-level system-blocks (e.g., Journals/ and Logs/ default to Private)?
- Should privacy be a prompt field or a silent preset?
- Is "Uber-Private" still a valid tier?

**Answer:**
-  We definitely need a privacy field and have it stored in every file. It would be nice to have a standardized list of options. Unfortunately,  there is no way to construct that list. We could use a field info with a multi-select, but then we would be entering that in every single time. Obsidian would not have knowledge of what those options are because it would not be able to interpret the template code.
- I think the better solution is to have enough templates with hard coded values for the privacy field to cover all potential values. Then we will document what the potential values are inside the Z2K system documentation.  this way, all potential values will be visible to Obsidian. When a user needs to change it, it will have its own preordained drop-down list of potential values
-

To hard-code all potential values across templates, we need the complete canonical list. From the v2 templates the following tiers were observed, here are the options:
- `.:Z2K/Privacy/Default` — general default (no specific privacy designation)
- `.:Z2K/Privacy/Public` — explicitly public 
- `.:Z2K/Privacy/Private/General` — generally private
- `.:Z2K/Privacy/Private/Professional` — professional context
- `.:Z2K/Privacy/Private/Implied` — implicitly private by context
- `.:Z2K/Privacy/Private/Log` — daily logs
- `.:Z2K/Privacy/Private/Journal` — daily journals
- `.:Z2K/Privacy/Uber-Private/Confidential` — Confidential Conversation
- `.:Z2K/Privacy/Uber-Private/SafePlace` — safe place conversations

---

### Q7 — `z2k_creation_domain` and `normalizePath`

The v3 system-block uses `{{normalizePath destPath}}` to populate `z2k_creation_domain`. This helper does not appear in the Z2K Templates plugin Reference Manual — it may be a Z2K Core plugin feature, a planned feature, or a placeholder.

Questions:
1. Does `normalizePath` exist and work in the current Z2K Core or Templates plugin?
2. What is the intended output format? (e.g., `.:Z2K/Domain/Information`, `.:Z2K/Domain/Thoughts/Quotes`?)
3. If `normalizePath` isn't available yet, should the system-block leave `z2k_creation_domain` as an empty string, a static placeholder, or be omitted entirely until the helper is implemented?

**Answer:**
-  for now, just simply hard code them to the domain in which the template is residing. This could be something for the system block that exists at each individual domain level 

---

### Q8 — Card Type and Source Type Taxonomies

v2 used typed enumerations for both `z2k_card_type` and `z2k_card_source_type`:

**Card types used:** `Atom`, `Daily/Log`, `Daily/Journal`, `Log/Weekly`, `Log/Monthly`, `Log/Yearly`, `Log/QuarterlyFocus`, `Structure/Ontology`

**Source types used:** `Book`, `Podcast`, `WebArticle`, `Conversation`, `Meeting`, `InternalThought`, `InternalMemories`, `Quotation`, `Person`, `AI/ChatGPT`, `LifeLessons`, `OtherCards`, `Unknown`

Are these taxonomies documented and stable in v3? Are there additions or removals? Where is the canonical list maintained?

**Answer:**
I've decided that the Z2K card type should no longer exist.  The card type is self-evident from whatever folder is containing the card. Mapping it in the card itself causes it to be potentially out of date if a card gets moved from one domain to another. We still want to capture what it was created as, hence the item in Q7.  this, at least, allows the card to have some information as to how it was intended to be interpreted,  domain-wise. Thus, if a card is sent to somewhere else or uploaded to the marketplace, we can make a best guess as to what type of card it is. Storing it directly in  a card type dedicated YAML field is problematic because if the card is moved, the card type YAML field will not be updated and cause a conflict.

`z2k_card_source_type` (the content type: Book, Podcast, InternalThought, Conversation, etc.). describe what kind of real-world content it represents. Many templates set this per-template (e.g., `.:Z2K/SourceType/Book` in the Book template). Please continue to support this source type. The documentation can be found at: `Docs/z2k-design-notes/Z2K System - Design Notes/Z2K Data Architecture/Z2K Metadata/Z2K Metadata Specification - Version 3.0.md`

---

### Q9 — Inline `::` Property Syntax vs. YAML Frontmatter

v2 templates mixed two property styles:
- **YAML frontmatter** for system metadata (`z2k_*` fields, template settings)
- **Inline Obsidian dataview syntax** in the card body (`- Author:: {{Author}}`, `- Date:: {{date}}`)

In v3, Obsidian natively supports properties in frontmatter via the Properties panel. Should inline `::` properties:
- **a)** Be preserved — they're human-readable and work with Dataview
- **b)** Be moved to YAML frontmatter where possible for better Obsidian integration
- **c)** Remain as-is in the card body but also be mirrored in YAML (dual representation)

**Answer:**
 that will unfortunately need to be a judgment call 
 any item that is using the `::` and is inside the body of the text, should continue to do so 
 and lastly, a good number of them are likely candidates for being set up as  a YAML to field value storage system. See `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/Storing Field Values in YAML.md`

---

## Domain Structure

### Q10 — Missing Vault Domains

Three domains from the current domain list are absent from `z2k-default-vault`:
- **Body** — physical self, health, fitness, biometrics
- **AI** — AI interactions, prompts, retained AI-generated artifacts
- **System** — Z2K infrastructure, configuration, templates, vault machinery

These folders (with Templates/ subfolders) need to be created. Confirm this is in scope, and clarify whether each should also get a domain-level `.system-block.md`.

**Answer:**
 yes, they should all get their own system block.  we can generate out some templates in the future.

---

### Q11 — Entities Domain Templates

Zero entity templates exist in the old system. The Entities domain covers people, organizations, and named real-world actors. Should entity templates be:
- **a)** Built from scratch in this migration (Person, Organization, ~Generic Entity)
- **b)** Left empty for now — Entities are created ad hoc without templates
- **c)** Stubbed with a minimal ~Generic Entity template only

If building, what are the essential fields for a Person card? (Name, role, organization, relationship to you, first met, tags, etc.)

**Answer:**
In the old system, people were marked via hashtags and not through unresolved Wikilinks.  we have migrated to the WikiLink structure, with the acknowledgement that most contacts will be simply unresolved. This is for both internal families and friends as well as external famous authors and media personnel 

 we will need to create a whole set of templates here.  this will allow the system to become a CRM.  we will need a qualifier to segregate out the public and private based contacts. I'm fine with leaving this question out for a separate chat to preserve the context window. Please, however, begin with a default contact just to get started.


---

### Q12 — Projects Domain Templates
Only one template exists in the old system (Code Poetry - Poem, which is personal). The Projects domain covers active and completed initiatives.

Should project templates be:
- **a)** Built from scratch (Active Project, Completed Project, ~Generic Project)
- **b)** Left with only the migrated personal template
- **c)** Stubbed with a minimal ~Generic Project template

What fields make a good generic project card? (Goal, status, start date, stakeholders, milestones, outcomes, etc.)

**Answer:**
 the projects folder will be very context specific. In fact, we will have a system block stop  in the folder, to prevent it from using the top-level Z2K YAML frontmatter.
  if you can build out the sample project templates that you've listed in a, that would be helpful

Note: that system block stop only works for sub folders - but that is fine here. You can assume the projects folder will have many subfolders for projects. You want system block suppresion to occur each of them.

Projects cards should have a completely **different YAML structure** with no `z2k_*` fields at all — not currently achievable via system-blocks; would require templates to have their own YAML that conflicts with (and overrides) the injected root block==

See `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/System Block Stops.md`

---

### Q13 — AI Domain Template Design

The only AI-adjacent template in v2 was "Information - ChatGPT" (a card for capturing a ChatGPT conversation). In v3, AI is its own domain.

What should the AI domain template library contain?
- A generic "AI Interaction" template?
- Model-specific templates (Claude, ChatGPT, Gemini)?
- AI prompt library cards?
- AI-generated artifact cards (summaries, analyses, code)?
- Something else?

**Answer:**
 this also is a brand new domain and one that has not yet been spec'd out.  I'm fine with just leaving this blank, but be sure to at least set a system block that establishes the perspective to be that of AI 

---

### Q14 — Body Domain Template Design

The Body domain covers physical self: health, fitness, biometrics, and somatic tracking. v2 had only a generic Body ~Generic template (same structure as any generic card). The `~Partial - Health Log.md` (used inside Daily Log) covers detailed daily health tracking.

What templates should the Body domain have?
- A ~Generic Body card (health condition, body metric topic)?
- A Fitness Activity template?
- A Medical Event template?
- Something else?

Should the daily Health Log partial remain a block (inserted into Daily Log) or become its own standalone Body domain template?

**Answer:**
 the Health Log Card is a great template to put into the body domain.  Put it as a block template. In a subsequent task, I'm sure we will split this up into individual blocks and then use the parent block to pull them all together
---

### Q15 — System Domain Content

The System domain covers Z2K infrastructure — configuration notes, template library documentation, vault setup guides, etc. What templates should the System domain have? Examples:

- System - ~Generic (generic system/config card)
- System - Template Library Notes
- System - Vault Setup
- System - Plugin Configuration

**Answer:**
I don't know yet on this, but if you can just convert the ones that exist already, that would be helpful.

---

## Block Design

### Q16 — Block Placement for Shared Content

Several content patterns appear across multiple domains. Tentative placement proposals — please correct or approve:

**Root-level blocks (visible globally):**
- `Block - Citation.md` — standard citation fields (Title, Author, Source, URL, Date)
- `Block - Quotation.md` — blockquote + attribution + personal commentary
- `Block - Card Fabric - Standard.md` — Card Fabric section (if kept)
- `Block - Card Fabric - Maximalist.md` — extended Card Fabric with all fiber types

**Domain-level blocks:**
- `Information/Templates/Block - Information - Summary.md`
- `Information/Templates/Block - Information - Overview.md`
- `Information/Templates/Block - Information - Synthesis.md`
- `Information/Templates/Block - Information - Details.md`
- `Interactions/Templates/Block - Interaction - Logistics.md` — When/Where/Who/Recorded section
- `Memories/Templates/Block - Memory - WhenWhereWho.md`
- `Logs/Templates/Block - Health Log.md` — the detailed health tracking block

Does this structure feel right? Are there additional shared patterns you want expressed as blocks?

**Answer:**
 for the root citations and quotations, please note that it would be helpful if you use the same nomenclature across all of them. That way we can store the fields in the YAML and have them automatically pre-fill when you are inserting the block. That only works if the fields are consistent inside the blocks and all the places that they may be used. 
 
 Note the subtlety that, for things like title and author, we may need to have these be inside a namespace or  prefixed with a word to distinguish it from the underlying author and title of the card itself 

```
Author: {{creator}} <-- this is the card's author
ContentAuthor: {{ContentAuthor}}
```
 then in the blocks reference `{{ContentAuthor}}`. 
 
 Even better would be:

```
Author: {{creator}} <-- this is the card's author
Content:
	Author: {{Content.Author}}
```
 then in the blocks reference `{{Content.Author}}`. 
But I suspect that Is not supported in the code. 

 But let's try it anyway, so go ahead and put it that way, and then we'll either fix it or file a bug in the code to have it supported. 
 
---

### Q17 — Card Fabric as Block vs. System Block

If Card Fabric is preserved (see Q1), should it be:
- **a)** An explicit partial block — inserted with `{{> "Block - Card Fabric"}}` in each template that wants it. Opt-in, visible in template files.
- **b)** A system block — injected automatically into all cards at the folder level. Universal, invisible in template files.

The tradeoff: system-block injection is automatic and consistent but gives no per-template control. Explicit partial gives templates the ability to choose the minimalist vs. maximalist Card Fabric variant.

**Answer:**
 not preserved as it will be an optional block to be inserted 

---

### Q18 — Ontology Template Type

Ontology cards (index/map-of-content cards organizing related notes) exist in three domains in v2: Thoughts, Information, and Memories. Their structures differ slightly by domain.

Should v3 have:
- **a)** A single cross-domain Ontology template (root-level Templates/ folder)
- **b)** Domain-specific Ontology templates (since field structures differ: e.g., Memory Ontology has When/Where/Who; Thought Ontology has TOC sections)
- **c)** Both — a root-level generic plus domain-specific variants

**Answer:**
 I think we will need both 

---

## Plugin & System Features

### Q19 — Library Version Number — Storage Location

A root-level library version number is desired, tracking the version of the entire template library independently of individual template versions.

Proposed approach:
- Store as a YAML comment in the root `.system-block.md`: `# z2k_template_library_version: 3.0.0`
- Also as a dedicated readable card: `System/Z2K Template Library - v3.md`

Alternatives:
- As a `z2k_template_library_version` YAML field in the root system-block (YAML comments get stripped by Obsidian — this may not survive)
- As a separate `library-version.json` file in the vault root
- Only in the System card

What is your preferred approach? What should the initial version number be?

**Answer:**
both
it needs to be stored in the root system block YAML.  do note that this is a static value that's assigned, so this is more a reflection of the version number of the library at the moment that the card was created. The underlying library itself will get upgraded over time, but all those cards that have been made are ready will still reflect, in their content files, the library version. This is similar to the "source domain" in which you capture the domain that it had at the point of creation, but after that point it could be anything.

I mention all this because the name of the YAML field should reflect this nuance by having a similar naming scheme as the source domain field
would be good to have it stored in a system card for details on the current release of the library.

Following the `z2k_creation_domain` naming pattern (prefix `z2k_creation_` to indicate "captured at creation time"), the proposed field name would be `z2k_creation_library_version`. and use the number to embed `3.0.0`

---

### Q20 — `z2k_template_suggested_title` Strategy

The Z2K Templates plugin supports `z2k_template_suggested_title` in template YAML — a Handlebars expression that pre-fills the output filename. This is a significant UX improvement over the old `%% Title: ... %%` comments.

Should all v3 templates include a `z2k_template_suggested_title`? What are the naming conventions?

Examples from v2 (as comments) to migrate:
- Book: `{{BookTitle}} - {{Author}}`
- Podcast Interview: `{{Interviewer}} Interview - {{Interviewee}}`
- Business Meeting: `Meeting with {{PrimaryParticipant}} - {{date}}`
- Daily Log: `{{date}} - Log`
- Daily Journal: `{{date}}`

Any templates where the filename should be left entirely to the user?

**Answer:**
 most definitely. This is crucial.
 you have two options:

1. Use the YAML tag.
2. Use field info on the file title.

I think the YAML tag is a little easier to use. See
`Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md`

 please follow my existing schema for naming files. 
 Please, in general, update my field names to be more consistent across different templates 

---

### Q21 — `fieldInfo` Prompting Strategy

The new `{{fieldInfo}}` / `{{fi}}` system enables rich, typed prompting for field values. For shared fields that appear across many templates (e.g., `Author`, `Date`, `Location`, `Who`), should their `fieldInfo` declarations live:

- **a)** In each individual template file (maximum per-template customization)
- **b)** In domain-level `.system-block.md` files (shared prompts across a domain)
- **c)** In the root `.system-block.md` (global shared prompts)
- **d)** A mix — root/domain system-blocks for universal fields, templates for domain-specific fields

Note: a `fieldInfo` in a system-block applies to all cards created in that folder tree, which could cause unintended prompts. What is the right balance?

**Answer:**
 actually, if a field info is given on a field that is not used in that template, then it simply will never appear in the prompting interface. Your concern is not valid. Although I appreciate you bringing it up 
 See `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Using System Blocks and fieldInfo.md`
does that address your issue ?

---

### Q22 — Deferred Field Resolution Strategy

The Z2K Templates plugin supports a "WIP" (Work In Progress) state — a card is created with unresolved fields that are filled in later. This enables templates with optional or context-dependent fields.

Should templates be designed primarily for:
- **a)** Immediate full resolution — user fills everything at instantiation (or uses `prompt: none` with automation)
- **b)** Deferred resolution — cards are created in WIP state and completed over time
- **c)** Per-template choice — some templates (Daily Log) are automation-filled, others (Memories) are filled at creation, others (Projects) grow over time

**Answer:**
this will be highly dependent on the type of file. Logs and dailies, for instance, are notoriously WIP and remain so for several days 
 on the other extreme is something like capturing content from an email, you will likely have all the information you need right away 
outside of using directives like `required`, I'm not sure I understand where the ramifications are.

---

### Q23 — Tags Taxonomy — Stability and Location

v2 used an extensive hashtag taxonomy: `#Media/Book`, `#Media/Podcast`, `#Location/Portland`, `#WriterTags/BeautifulLanguage`, `#Questions/ToAsk/Author`, `#Card/Instigation/Book`, `#YPO-Forum/Icebreakers`, etc.

Is this taxonomy documented and stable in v3? Where is the canonical tag taxonomy maintained? Should it be documented inside the System domain?

**Answer:**
 yes, we will need to have a dedicated TAGS taxonomy document that is located in the systems documentation area.  create a placeholder document there, and we can deal with that later 

---

### Q24 — `z2k_creation_language` Field

The v3 system-block introduces `z2k_creation_language: "en"`. Is this always a static value, or should it be a prompt field for multilingual use? Should it be in the root system-block or only for specific domains/templates?

**Answer:**
 I don't really know for sure, but what my best guess is is that we should define it in the root system block, and then the user can override that for any individual file thereafter.  
note that this also suffers from the "capturing the state of things at the moment of instantiation" problem 

