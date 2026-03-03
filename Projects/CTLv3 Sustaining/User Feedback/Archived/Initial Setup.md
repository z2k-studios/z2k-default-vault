Now, here's what I want you to do. 

# First, import
I want you to go in and look at the Z2K v2 to v3 template migration project that sits right next to this project. I don't need to know anything about all of the migration-related items - Please ignore and explicitly do not include anything that talks about what's necessary to change an old template into a new template. That process is all done and never needs to be returned to. That project will be deleted as soon as you are able to mine it for all of the information you need to know in order to have a sustaining project that keeps this template library in a healthy working condition. 

So, Instead, what I need you to do is to go through and systematically pull out all project requirements that are in that page to describe the actual working system and place them into feature descriptions. I know there should be PRD descriptions for each of the top-level domains in the PRD doc. Each template should have its own corresponding numbered feature, because in this project the features are the template files

**CTLv3** (also **CTL**) | Z2K Core Template Library v3 

There should also be some underlying system knowledge that we need to capture. These aren't features but rather just describe consistent behavior that is in the system. This would be things like "default templates are named this way". There is also a wealth of information and external resources that are critical for understanding how to implement and test a template. For this initial task, I want you to only focus on the project requirements side of things for the features, the features being the templates in the system. Separate task after this. 


## What is a feature
So in essence, a feature here really is a new template in the system. I don't want to limit myself to that, because I believe we will add in some actual content files in addition to templates. There is no strictly code that performs something, but rather a template that's available to be used. Nonetheless, that feature needs to have some basic requirements such that it can be validated as a valid template. Therefore, there are some global template requirements that need to be captured. (Again, you will probably need to modify the structure of our existing PRD document). 


# Global Requirements
Here are some global ideas for requirements: 
- Every template needs to have valid Handlebars and Z2K Templates syntax. 
- Every template needs to have a consistent naming scheme with the existing overall CTL
- The CTL needs to be able to support system blocks. 
- Every field needs to be fillable. Any automatic fields, such as fields within system blocks, need to correctly get filled in. 
- We need to have templates to handle the majority of cases in which someone wants to put information into their second brain. 
- We need to be able to handle variations and thus use block templates for situations where there are variations, like podcasts. 
- We need to ensure that every template, when they're provided with their data, produces the output that is expected. 
- The templates need to have consistent formatting. 
- The templates need to be AI-aware and preferably future-proofed for AI processing, thus having a YAML description inside the root system block would be a good idea. 
- The templates need to be able to handle more advanced data sets and be tested against them. They also need to handle unusual data that is valid but may be unexpected, for instance, unescaped characters. We can't prevent users from providing garbage, but we don't want it to cause unnecessary errors in our rendered pages. 
- We want our templates to be a guide to how to build your own templates. Thus, they need to show at least one level or two up in terms of complexity, so that they can show off the capabilities of Z2K systems and Z2K templates. For instance, they should use multi-select fields when appropriate. Use system blocks smartly. They should use conditionals and advanced built-in helpers and fields to increase the "wow factor" using them. It is worth kicking off a separate Claude interaction to do nothing but mine the reference manual for good examples inside the reference manual for powerful methods for how to make the templates really pop out. 
- The templates should be built so that they can easily receive automated data. The daily log, for instance, will be heavily fed by external data. 
- The templates will need a level of modular structure so that users can turn on and off individual feature blocks by removing or disabling block insertion. 
- The template should be well documented with comments. 
- The template should not make small annoying mistakes like leaving spaces before or after comments to prevent them from clearing their lines. 
- The templates should look pretty even when viewed in their raw state. For instance, consider making comment blocks be cross lines if it makes the output appear more attractive. Consider adding commented break bars to have the templates appear nice and clean. 

These are just the requirements I can think of the top of my head. I'm sure there's a bunch more that you can glean from the previous project. 

# Testing
okay, let's talk about testing. 

Some of these requirements can be automated with testing. For instance, you can have a whole series of JSON packets, some shared across all templates and some designed just for an individual template or domain of templates. You can then have a testing framework that uses Obsidian's correction Z2K Templates plug-in command q feature to process those JSON packets into templates to create new files. Your testing script can check that generated file from template against an expected output. These can all be stored inside of the folder that maps to that containing feature (template). You can generate a whole series of expected outputs for different JSON packets in any structure that is consistent and easy to use for your scripts that you will generate. 

I am assuming you will make a shared folder to heavily reuse on scripts and JSON packets. If you look at the agent brief of the sister project, you may get some additional ideas of what is needed. If the tester is going to do actual changes on the template to improve it (see below), it will likely need to know more about how templates work and thus have some knowledge of the reference manual. 

## Qaulitative Requirements Testing
Okay, but there are a lot of requirements up there. In fact, the majority of them that are not directly automatable. Instead, they sound like subjective guidelines. How do we deal with that? I still think it's important for us to do.

I'll leave it up to you as to how to implement a system, but let me give you an idea to get you started. I was wondering if you can have an AI agent be effectively your script for assessing these qualitative requirements. In this instance, imagine you have a python script that makes a command line call to Claude to perform a "template quality assessment" with a specialized agent. That agent should have knowledge of the overall system, and should be working against a checklist. This checklist becomes effectively a scorecard. After it's completed applying the scorecard against the template, then it generates out a score and a list of suggestions of how to make the template better. 

That same agent, when executed with a command line option to fix things (or a separate one) can then use that information to go back and make improvements to the template. This can be an iterative process where you keep running the assessment and improvement agent until you get a score that is above a certain threshold.

If the testing script is running in a strictly analysis mode where the agents are not allowed to make modifications to the template, then it will output that score card with suggestions and that number. That number must pass some threshold in order for the test to be considered a success. 


# Drop folder 
Once your system is set up, I am hoping to run a complete audit of the template library with an AI agent to identify what other templates need to be included with the system. I will then have that agent draw up feature requests to implement that template. I will likely have the actual template text be included as part of the text of the feature request. Then I will put these in the drop folder and run the implement command. 

# New Testing Plan
Please note that I may also go in and change the requirements for a template by modifying its feature requirements document. In this case, for instance, I might simply add in a new field or a new block. I will need a tool or a methodology to handle this that will go through and update the test folder to incorporate this new change. This needs to be a named process inside the statement of work so that I can ask an AI agent to go off and do it. This should be the equivalent of what you yourself would do when you create your initial versions of the test folders. So that process of creating a new test folder or updating it to reflect changes needs to be something extremely well documented in the testing plan as a known process. It should be able to be executed by an AI agent, hopefully completely standalone without input.


---

## Clarifying Questions

### Import from Migration Project

#### Q1 — Source documents to mine
The migration project is at `Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/`. Which documents should I focus on? I assume the PRD is the primary source, but should I also mine the Implementation Plan, Task files, or Agent Brief for requirements that describe the working system?

**Answer:**  I think it's easier for me to tell you what not to focus on. Do not focus on the iterative framework process that is within the statement of work. It has nothing to do with our approach. Also, do not focus on anything to do with the old templates that are being migrated in. Instead, I would focus in on the two areas where you will be building out  information and can heavily reuse work already done by this project. They are:

1. project requirements and what they would look like as individual requirements per template or per domain.  the project also has done a great job at identifying global requirements for the overall system that need to be captured, in addition to the individual features (i.e., template files) 
2.  how to build a testing script that uses JSON and command queues in order to test if a template is working 
3. some great general knowledge - what reference manual pages to know, and always load. What does every individual agent working on individual requirements validation need to know? - The agent brief file, for instance, should have great work in it. Having a good list of documents that you should know is also a great thing to have in your statement of work or project requirements 


#### Q2 — Feature granularity
You say "each template should have its own corresponding numbered feature." So Feature 002 might be `002 - Daily Log.md`, Feature 003 might be `003 - Book Note.md`, etc.? And the "top-level domains" in the migration PRD (e.g., a domain like "Media" or "Daily") would just be an organizational grouping, not a feature themselves?

**Answer:** yes, that looks right. I suspect there may also be an initial set of features for each of the top-level domains-  "000 - Body".  finally, there will be some basic infrastructure and bare minimum requirements that should be in the very first initial set of features. This ranges from things like  "000 - System Blocks" and "000 - Directory Structure" to "000 - Working System" (does command queues actually work? Can I run hello world and confirm the creation of the file? - see the example in the sister project)

#### Q3 — Scope of import
You mention "underlying system knowledge" like naming conventions, but say that's a "separate task after this." So for the initial import, I should extract only per-template feature descriptions and their requirements — no system-level documentation yet?

**Answer:**  in general, I really want to maintain a linkage between a feature with an assigned number and a testing strategy for that feature with the same exact assigned number. As a result, some  a test may be a simple return true, but preferably at least something like "verify the existence of these folders." They still need to be a test that is returning a value that the regression script can call and get a true value for.  now, underlying system knowledge, like naming conventions - some of that needs to be tested for, like having a baseline script that looks at the fields and verifies that there are no fields being used with the first letter being lower case unless they are built-ins. That script is an important one to build, and that requirement needs to be tested against. The naming conventions should be in the requirements for the features.

There is some other general knowledge, like having a knowledge of what the underlying domains actually are for. This system knowledge can just be included in the PRD if it is of value

### Global Requirements & PRD Structure

#### Q4 — Where do global requirements live?
The current sustaining PRD describes structural conventions (how features and requirements are organized). The global requirements you listed (valid Handlebars syntax, consistent naming, AI-aware YAML, etc.) are a different animal — they're cross-cutting quality requirements that apply to every template. Options:
- Add them to the PRD as a new section (expanding its role beyond structural conventions)
- Create a dedicated feature for them (e.g., `002 - Global Template Requirements.md`) so they get their own test suite
- Both — PRD defines them, and a feature + test suite enforces them

Which approach? The second or third option gives us a natural place to hang the qualitative scoring agent.

**Answer:**  well, if you look at the idea that a feature and a requirement are ultimately the same thing, then yes, having a dedicated feature for them seems like a perfectly reasonable thing to do. You can build out their own test suite that automates that test just for that particular requirement or set of requirements.  similarly, I'd prefer to keep the PRD focused on structural conventions, as you say, and not actual requirements 

#### Q5 — Aspirational vs. testable
Some global requirements are concrete and testable ("valid Handlebars syntax", "no spaces before/after comments"). Others are aspirational and subjective ("handle the majority of cases", "show off capabilities", "look pretty in raw state"). Should I capture both but tag them differently (e.g., `automated` vs. `qualitative`)? Or do you want me to sharpen the aspirational ones into testable form?

**Answer:** Yes, please capture both, and I think it would be a good idea to tag them separately between those that are qualitative (it must be AI tested) and those that are quantitative and can be automatically tested via a script. 

### Testing — Automated

#### Q6 — "Command Q" feature
You mention using "Obsidian's Z2K Templates plugin command Q feature to process JSON packets into templates." Can you clarify what this is exactly? Is it an Obsidian command, a CLI tool, a plugin API? I need to understand the mechanism so I can design the test scripts to invoke it correctly.

**Answer:** command Queues are an amazing feature of Z2K Templates that will automate testing.  drop a JSON packet into a folder describing what template you want to use and what data you want to supply the template, and it will automatically create the resultant file. It takes a few seconds for it to perform. You can then clean up the file afterwards and move to the next JSON package. See `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/Command Queues/Command Queues Overview.md`

#### Q7 — Test execution environment
If tests need to invoke the Z2K Templates plugin to render templates, does that mean tests need a running Obsidian instance? Or is there a headless/CLI path to render a template from a JSON data packet? This affects whether `run_tests.py` can be truly standalone.

**Answer:**  you will need a running Obsidian instance. That's fine. I can guarantee that. I just will leave it up and running while you do your work.  it helps to have a hello world test to first perform in order to make sure the system is up and running correctly.  there is even a hello world example inside the documentation 

#### Q8 — Shared test resources
You mention a shared folder for reusable JSON packets and scripts. Should this be `tests/shared/` (a sibling to the feature test folders), or somewhere else? And should certain "universal" JSON packets (e.g., a packet with edge-case characters, an empty packet) be defined upfront as part of the testing infrastructure?

**Answer:** that sounds reasonable, but I defer to you as to how to actually implement it or what you would prefer to have. Your design, I'm sure, will be fine 

### Testing — Qualitative (AI Agent Scorecard)

#### Q9 — Scorecard as a document
The AI quality assessment agent would work against a checklist/scorecard. Should this scorecard be a maintained project document (e.g., `Template Quality Scorecard.md` in the project folder)? And should it be derived from the global requirements in Q4?

**Answer:**  that seems like the right thing to do, to maintain it as a separate project document. Then, if you need to add new qualitative scores to be included, you can perform a regression test, but with these new  items on the checklist .  it should most definitely be derived from the global requirements

#### Q10 — Analysis vs. fix modes
You describe two modes: analysis-only (outputs score + suggestions) and fix (iteratively improves the template). When in fix mode, the agent would be modifying the actual template files in the template library. Is that intentional? That means a "test" could alter source files — should there be safeguards (e.g., work on a copy, require user approval before committing changes)? 

**Answer:**  there should definitely be safeguards. I have the system inside GitHub, so I will always do a comparison against GitHub to see what the changes are. The other safeguard is that to run the testing scripts in fixed mode, it can only be done with a very explicit command. We should say that you need a user to confirm that you want to run it in fixed mode before you ever use that 

#### Q11 — Integration with regression
Should the qualitative AI assessment be part of the standard `run_all_tests.py` regression run? Or a separate command (since it involves API calls to Claude, has cost implications, and takes longer)? Something like `run_all_tests.py --include-quality` or a separate `run_quality_audit.py`?

**Answer:**  most definitely it should be included. But yes,  it should be configurable as to whether or not you are running a full regression or a script-only regression without AI calls

#### Q12 — Passing threshold
You mention a score threshold for the qualitative test to "pass." Should this threshold be defined in the Testing Plan, or per-feature, or both (a global minimum with per-feature overrides)?

**Answer:**  yes, defined in the testing plan.  having some method to override the qualitative score to force a pass inside the features testing plan would be a smart idea. For instance, we may have a very simple basic template that will fail because of its simplicity. But we should be able to force it to pass through the use of a special flag inside its testing plan 

### Process — Test Folder Updates

#### Q13 — Named process for test updates
You want a well-documented process for updating test folders when feature requirements change, executable by an AI agent standalone. Should this be:
- A new named stage in the SoW's Project Framework (e.g., "Test Suite Refresh")
- A section in the Testing Plan (§ "Updating Test Suites When Requirements Change")
- Both

And should it follow the same structural steps as initial test creation (update test_plan.md → update run_tests.py → update expected outputs → run and verify)?

**Answer:**  this should be its own named process ( let's just call it a process ) inside the Statement of Work. "test suite refresh process "  and yes, it should follow that same structure 

### SoW Modifications

#### Q14 — SoW scope creep
This feedback introduces several things the current SoW doesn't account for: the qualitative testing agent, the test-update process, the eventual audit agent for the drop folder. Should I incorporate all of this into the SoW now during this iteration, or handle some as future enhancements after the core sustaining infrastructure is working?

**Answer:**  yes, incorporate now. It needs to be part of the core foundation of what this project is all about 


