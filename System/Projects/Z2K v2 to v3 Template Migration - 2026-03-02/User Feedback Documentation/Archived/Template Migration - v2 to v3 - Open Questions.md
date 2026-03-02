---
title: Template Migration - v2 to v3 - Open Questions
created: 2026-03-01
status: in-progress
---

# Template Migration — v2 to v3 — Open Questions

This document captures unresolved decisions required to complete the migration of the Z2K template library from v2 (Obsidian Templater-based) to v3 (Z2K Templates Plugin). Answer blocks are provided for each question.

---

## Q1 — "Ideas" Domain

The old system had an "Ideas" domain with four templates: Quick Capture, ~Generic, Quote a Source, and Quote an Email. The "Ideas" domain has been removed from Z2K v3. Passing thoughts are now captured directly inside the Daily Journal under `## Passing Thoughts` (alongside Passing Memories, Passing Information, etc.).

**Decision:** Ideas domain is fully retired. No Ideas templates will be migrated. Their function is absorbed into the Daily Journal. Quick idea capture = Passing Thoughts section. Developed thoughts = promoted to Thoughts domain using Thoughts templates.

**Answer:**
> Confirmed 

---

## Q2 — "Syntheses" Domain

The Syntheses domain is explicitly retired in v3. Four templates need to be mapped to current domains:

- *Syntheses - ~Generic* — general published writing
- *Syntheses - Treatise* — long-form structured essay or argument
- *Syntheses - Extended Journal Writing* — long-form personal reflective writing
- *Syntheses - Quote an Email* — capturing an email quote as a synthesis artifact

Proposed mapping:
- Syntheses - ~Generic → **Projects** (goal-directed publishable work)
- Syntheses - Treatise → **Projects**
- Syntheses - Extended Journal Writing → **Journals**
- Syntheses - Quote an Email → **Thoughts**

**Answer:**

First some context:

Geoff:
> In version 2, I had a top level domain called **syntheses** and this domain was focused on storing larger scale writings: an extended journal entry, a "treatise", something that could be used for a blog post, an essay to publish.
> 
> In practice, I found that these started as `thoughts`, and then I just continued to build out the thoughts, so that I never really needed these. But then, when I would want to make something more formal, I would end up making it in a `project`. 
> 
> As soon as you start making it be published, then you have to deal with the fact that 
> - a) Its formatting becomes constrained. For instance, making Wiki links is not able to be supported because it will be published outside the Vault, 
> - b) I struggled with versioning control when something became published, 
> - c) adding extra comments - For instance, some background material that I did not want to include in the main writing but otherwise had as additional material.
> 

> Claude's Response:
> **The real problem you're describing isn't storage — it's lifecycle.**
> Formal writings have a distinct lifecycle that none of your current domains model well:
> 
> `Thought (atomic) → extended draft → polished artifact → published artifact`
> 
> Each stage has different constraints:
> - **Wikilinks** are valid in vault-internal stages, invalid once published
> - **Versioning** matters only once something is "released" — before that, it's just a file
> - **Background material** is a draft-time concept (your annotations, cut sections, sources) that shouldn't pollute the final artifact
> 
> The failure of Syntheses in v2 was probably that it tried to capture the _draft_ stage, but you were already doing that naturally in Thoughts. The problem isn't the draft — it's what happens _after_.
> 
> **The options, honestly evaluated:**
> 
> 1. **Leave it in Projects** — you're already doing this, and it works until publication. The friction you described (formatting constraints, versioning, background material) is real and won't resolve itself. Projects conflate _process_ with _artifact_.
>     
> 2. **Resurrect a Writings/Publications domain** — but with a different charter than Syntheses. Not "a place to write longer things" (that's just extended Thoughts) but a _destination for finalized artifacts_. Things arrive here by promotion from a Project or Thought, not by creation. This cleanly separates the made thing from the making. Wikilink stripping, versioning, and background material all become tractable because you've isolated the artifact.
>     
> 3. **Publications subfolder inside Projects** — keeps artifact tied to its production context. Good for traceability, bad for discoverability. You can't easily browse your body of work; everything is buried inside individual project folders.
>     
> 4. **Handle it in templates, not domains** — a "Formal Writing" template inside Projects with frontmatter fields like `status: draft | published`, a sibling `_background.md` file convention, and an export script that strips wikilinks. No new domain, but imposes discipline through structure.
> 
> **My instinct:** option 2, but only if the charter is narrow and strict.
> 
> The failure mode of Syntheses was that it had no entry criteria — you could dump anything there. A Publications domain works if the rule is: _nothing lives here until it's ready to leave the vault_. It becomes a staging area for the external world, not a writing space.
> 
> That framing also solves your three pain points directly:
> 
> - **Wikilinks**: an export pipeline targets this domain specifically
> - **Versioning**: frontmatter `status` + a `published/` subfolder or git tag at publish time
> - **Background material**: a sibling `_notes.md` convention in the same artifact folder
> 

**Geoff's Response and conclusion:**
> Let's follow #3 approach. Create a subfolder called "My Writings" under Projects. Thus, 
> 
> - *Syntheses - ~Generic* —> becomes the default template for `/Projects/My Writings`
> - *Syntheses - Treatise* —> another template for `/Projects/My Writings`
> - *Syntheses - Extended Journal Writing* —> `/Projects/My Writings` but rename to "Personal Writing" so that we do not confuse them with `Journals` entries 
> - *Syntheses - Quote an Email* --> Just delete
> 
> (Note: the term "Default Template"  applies to a feature that is not yet fully implemented. See GitHub issue number [182](https://github.com/z2k-studios/z2k-plugin-templates/issues/182).  Until it gets implemented, simply follow the naming approach with " (Default)" postfix, such as for the first bullet above: `/Projects/My Writings/Templates/My Writings (Default).md`

---



---

## Q3 — Personal-Only Interaction Templates

The following templates contain hardcoded personal specifics (real names, private organizations, personal locations):

- *Interactions - YPO Forum* (hardcoded: specific forum members' names)
- *Interactions - YPO Event* (YPO-specific privacy setting)
- *Interactions - Doug* (hardcoded: specific people, Uber-Private/SafePlace tag)
- *Interactions - PoND Conversation with Bryn* (personal relationship context)
- *Interactions - Conversation with John Kashiwabara* (hardcoded person + location)
- *Interactions - Amateur Hour* (personal group)
- *Memories - PCT Trail Day* (hardcoded start mileage, personal trip data)

All are to be built in `z2k-default-vault` for now (with personal→personal vault migration deferred). Question: should personal specifics (hardcoded names, locations, privacy levels) be:

- **a)** Preserved with full fidelity — these are personal-use templates and the specifics are the point
- **b)** Parameterized — strip hardcoded values and replace with `{{fieldInfo}}` prompts, making them reusable templates with personal defaults

**Answer:**
*Geoff: yes, please put them all inside the system vault, as I will just manually move them out into my personal vault before it becomes published. I would like to have an existing solution with all of the templates that I already use, just to make it feel like a full vault. I appreciate you looking in on my personal privacy* 

---

## Q4 — Specific Podcast-Host Templates

Six templates exist for individual podcast hosts, each a variant of "Podcast Interview" with show-specific hashtags and names preset:

- Information - Adam Grant Interview
- Information - Dwarkesh Interview
- Information - Huberman Lab Podcast
- Information - Knowledge Project Interview
- Information - Lex Fridman Interview
- Information - Tim Ferriss Interview

Options:
- **a)** Migrate all as full templates with show-specific values preset via `fieldInfo fallback=` or `value=`
- **b)** Drop all in favor of a single parameterized "Podcast Interview" template that prompts for show name/host at instantiation
- **c)** Keep one generic "Podcast Interview" template plus migrate the specific-host ones as personal-vault templates

**Answer:**
This is a classic example of resuable template writing. There should definitely be a generic podcast template for the information folder, but then it would be nice to have the additional information filled in for the other specific types of podcasts that I listen to more frequently.  so I want some form of option A, but it needs to be smartly done 

There are a couple of ways I could see how to do this:
1. Just a copy and paste of the core template and then fill in the information manually, that's what I have now. This really sucks architecturally and design-wise because any mods to the structure have to be replicated across all variations.  I have specifically been trying to get away from this 
2.  another solution is to blockify the whole template, then have each  variation: include the blocks that they need  and then just have it manually specify the blocks that are different for each podcast.  this is useful if I need to specify additional fields for one particular podcast  
3. another solution is to use an insert partial command to insert the full generic podcast into a file. Have a bunch of set values at the beginning, before the partial inclusion, to pre-fill out a number of the fields for a specific podcast 
4.  a super advanced solution would be to get tricky and provide a field that allows the user to  select what type of podcast it is. This goes into a multi-select field. Then, based on the value of that multi-select field, we can conditionally make different responses into the template.  in theory, this gets down to just a single template file that can be modified to be any of the flavors with a single selection 
5. There may be other ideas of how to do it -  if you see one that's better than the above four, please suggest it 
  
I think the best solution to try out at least initially is to use  option three.

Note: You can perform an insert block  of a document template when using partial notation. Its only the command interface that limits you to picking from a list of block templates. 


---

## Q5 — "G:" Personal Commentary Prefix

Several templates use `G:` as a personal initials marker for commentary sections (e.g., `G: {{Synthesis}}`, `G:` in Background sections of podcast templates). This is a personal convention.

Should this convention:
- **a)** Be preserved in the migrated templates (it's intentional and meaningful to you)
- **b)** Be replaced with a more neutral convention (e.g., `> *Personal Commentary:*` or a `{{creator}}:` expression)
- **c)** Be removed from the official library templates but preserved in personal-vault templates

**Answer:**
- This is a fundamental design decision we are debating
- See 
	- `Docs/z2k-design-notes/Z2K Plugins - Design Notes/Z2K Core Plugin/Design Decisions/A method for determining author.md` and 
	- `Docs/z2k-design-notes/Z2K Plugins - Design Notes/Z2K Core Plugin/Features/Z2K Tags - Author Tag.md`
- For now, we are going to try using the `[!me]` callouts and `Me:` tag for very short additions (e.g. inline)
- As such, we need to have a system root level block template for "Perspective - Me"

Note: in the future I will try making it be a field `{{me}}` to capture the name, e.g. 
```
> [!{{me}}]
> (text goes here)
```

and then define {{me}} inside the root system block and have it be set value'd to `value="Geoff"`. Ultimately the core plugin we'll implement this and probably do so using a built-in helper, or if the field structure is too difficult, then it will just implement it with  a more direct method. That all said, for now just use a non-field version (`[!me]` and `Me:`)

==**Clarification needed (AI):** There is a conflict between your answer here and the recommendation in `Z2K Tags - Author Tag.md`. The design doc recommends `[!me]` as a **fixed callout type** — where `me` is always the literal string used as the callout type, regardless of user name. Your answer proposes `{{me}}` = `"Geoff"`, which would render as `[!Geoff]` — a person-specific callout type, not a standardized one.==

==These are two different architectures:==
- ==**Fixed type** `[!me]`: One standardized callout type for all vault owners. Requires a single CSS snippet to style. Clean and portable across Z2K users.==
- ==**Name-specific** `[!Geoff]`: Each user's callout type is their name. Requires a personalized CSS snippet. More identity-expressive, but not portable.==

==The Author Tag doc explicitly recommends the fixed `[!me]` type with `Me:` as the inline variant. Given that, should `{{me}}` resolve to `"me"` (the literal callout type string, same for everyone) rather than `"Geoff"` (the user's name)? Or is the name-specific approach intentional?==

---

## Q6 — Flame Automation Fields

The Daily Log and Daily Journal templates are densely populated with `{{Flame-...}}` fields (e.g., `{{Flame-OneWordTheme}}`, `{{Flame-Location}}`, `{{Flame-ImportanceToPosterity}}`, `{{Flame-WeatherRanking}}`, `{{Flame-DailyQuotes}}`, etc.). These appear to be integrations with an external automation system (Apple Shortcuts or similar).

Questions:
1. Is "Flame" still the active automation system for daily log population in v3?
2. Should Flame fields be preserved exactly as-is in the official library template?
3. If Flame is personal infrastructure, should these fields be kept in the official library template (since it's also your personal template for now) or commented out with `{{! ... }}` blocks?
4. Should the official `Template - Daily Log.md` contain Flame fields, or should there be a separate personal-vault layer that adds them?

**Answer:**

Geoff:
>  This is related to an optional plug-in (z2k-sheet-importer) that brings in data from a CSV which was filled out by a Google Forms implementation.
>  Please go ahead and just leave these all to be the same. The current daily log template is highly particular to me, but I want you to still migrate it as is. I will go back and make a more generic daily log  template for the general system

---

## Q7 — Template Version Numbering (Clean Break vs. Continuity)

For templates being migrated from v2, should version numbers:

- **a)** Start fresh at `v3.0.0 YYYY-MM-DD` — a clean break acknowledging the v3 migration regardless of prior version history
- **b)** Carry forward from v2 version numbers (e.g., `v2.1 → v3.0`) — preserving version lineage
- **c)** Something else (e.g., bump the minor version: `v2.1 → v2.2`, treating this as an update rather than a new version)

Also: what date should be used in the version string — today's migration date, or the last substantive edit date of the template?

**Answer:**
-  definitely move to the version 3.0 
- Also, every template should be moved to Today's date.

---

## Q8 — "Quote an Email" Template Type

"Quote an Email" appears as a template in four domains in v2: Information, Thoughts, Memories, and (the now-retired) Syntheses and Ideas. These templates are functionally identical with only minor domain-specific differences.

Is email quoting still a first-class capture pattern in v3, or has this been superseded by the Daily Journal's Passing Quotations section? If still valid as a standalone template, should there be:

- **a)** One cross-domain "Quote an Email" template (root-level or Thoughts-level)
- **b)** Per-domain variants as before
- **c)** Retired entirely — email quotes now go in the journal

**Answer:**
-  just implement a quote and email template into the information domain 

---
