Now the question is what to do. 

And the question that I really want to ask is, if you were to encounter this error, then where would you look to find out what to do? Where should we have given you instructions on how to handle a failure, and then what is the process that we should have written out for handling a critical failure in the testing scripts or regression test? 

Can you:
1. Make sure that we haven't actually already written out a procedure for handling this.
2. Propose a process or procedure for handling it.
3. Document to hold that process.

I think a critical question will be whether or not we will allow you to make a modification on the template file yourself to fix it. That should be a configurable part of the process that we use to kick you off in the first place.
When we started the testing, you should have engaged me with:
1. Is this a one-script-only test, or two AI and script test?
2. Is this a one-test-only test or two test and fix test?
That needs to be part of the process.

And then finally, we need to be very careful about any fixes that we do, because we simply can't just make a fix and then call it good, because we may have Caused an underlying change in the PRD. If you made a fix that requires a new requirement to be made, or an existing one to be removed, or an existing one to be modified, that should all go into a human review state. The process that we have that I want you to build out, if we don't have it already, should talk about this and force that to occur with the human user. 

Now, I know we should also have the human user validate any fixes that you do, but that I feel more comfortable on because they will appear in the GitHub change list And will be reviewed before the change is committed, assuming, of course, that you do not handle the check-in yourself, which would be bad.

---

## AI Questions

**Q1 — Where should this procedure live?**
The SoW §4.3 Stage 5 and Testing Plan §10 both touch on failure handling but neither has the depth you're describing. My instinct is: the kick-off mode questions belong in the SoW §4.3 (pre-Stage-5), and the full failure + fix procedure belongs in a new named process in SoW §4.4 (alongside Test Suite Refresh). The Testing Plan §10 would then reference the named process rather than re-document it. Does that structure work, or do you want a separate standalone document?

**A1:** I would agree. At first guess, it would have been in the testing plan, but because it has a fix capability, it up levels it to be across multiple documents. That means it must go up to the top level statement of work. 

**Q2 — Kick-off scope**
The two mode questions (script-only vs AI+script, test-only vs test+fix) — should these be asked once per session (when starting any testing work), or once per feature (at the start of each Stage 5)? And should the answers be recorded somewhere (e.g., in the Phase Tracker or in a test session log) so the mode is explicit and reviewable?

**A2:** I'm assuming that we are accumulating a set of commands that we can give that we can describe in the state of work. These would be commands like:
- process the drop folder
- perform regression test

I believe we originally proposed for these to be added as workflow items inside the projects workflow folder. That seems to have dropped off along the way. Now, assuming that we do get them built out as workflow commands, then both of them should be very lightweight, and then consult the statement of work to get guidance on how to perform that for the particular project that is being worked on. For our personal project, that response in the statement of work should immediately cause it to kick back to the user and ask these two mode questions. I think they should be asked every single time the workflow is triggered, which is different than either of the two suggestions you made. If the regression test is automatically triggered when, say, a new feature(template) has been added to the drop folder, then it should default to be a AI+script and test-only - but not performed across all feature tests (so I guess that is a third question to ask when going into testing mode - Do you want to perform a test against a very specific feature, and thus what feature number, or do you want to perform a regression test against all features).

Does this answer your question? 

**Q3 — PRD impact definition**
You said: "if you made a fix that requires a new requirement to be made, or an existing one to be removed, or an existing one to be modified." For 020-005 specifically — adding `z2k_template_author: "Z2K Studios, LLC"` to CTL templates — the requirement already exists (020-005 says exactly this). The templates just don't comply. Is that PRD impact (because it was missed in the migration and reveals a process gap) or a routine fix (requirement exists, template is wrong, fix the template)?

**A3:** In this specific case, the PRD stands strong. It was an implementation error, and therefore the testing and the PRD both did exactly as they were supposed to be done. There is no PRD impact. There is only the need to fix the underlying problem. This will either:
1. require the user to perform the fix
2. have you perform the fix for them

Now let's also talk for a moment about performing that fix. Unless you're in an automation mode, it is important that you propose the fix that you want to make before you actually perform it so that the user can review it. This needs to be part of the process. 

**Q4 — Scale threshold for autonomous fixes**
020-005 affects 71 templates. Even if it's a mechanical one-liner addition, 71 files is a lot of surface area. Should fix authorization have a file count threshold — e.g., AI can fix up to N files autonomously, above that it flags for human batching? Or is file count irrelevant and it's purely about PRD impact?

**A4:** If you are working along in an interactive chat, then it would be worth notifying the user if there is an impact to a PRD change that impacts more than 10 files. If you're in automatic mode, then simply continue forward and rely on the user to discover the issue at the point of GitHub commit. 

**Q5 — My current understanding of the 020-005 state**
You said you removed 8 of 9 files and "we really only have one file that's failing." I want to make sure I understand: the 9 files were the personal templates (`z2k_template_author: "Geoff (z2k-gwp)"`). After removing 8, one personal template remains as a smoke test. But the 71 CTL templates that lack the author field entirely are still failing 020-005 — those are unrelated to the personal templates. Is your "one file failing" referring only to the personal smoke test (and the 71 CTL failures are the expected work to be done), or did something else change that I'm missing?

**A5:** Yes, that's correct. The one file that is failing is the personal template that we left in as a smoke test. The 71 CTL templates that lack the author field are still failing 020-005. Both the 1 and the 71 need to be fixed.