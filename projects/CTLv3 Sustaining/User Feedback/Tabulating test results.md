The the pass/fail/skip response to standard out is just whether or not it was successful at performing the evaluation, not the evaluation response itself, correct? Yes, I would like to have the ability to have the results of the last run be stored inside the testing folders. I only need the last run. In the case of the qualitative evaluation, it should be storing not just the final score card but also the results of its evaluation and why it gave a score. You have a table up above in which you gave a sample scoring evaluation where you had item, weight, score, and notes. Then a final evaluation afterwards. That's perfect, except I wish there was a little bit more detail in the notes for each one as to how it calculated that score. 

On a larger level, all tests should be storing their latest execution results inside the test folder structure. That's why every single feature has a folder. The results need to be both human readable, so that a human can pull up the results of the last test and quickly understand what failed and why. It also needs to be machine readable in a consistent way. This is so that you can have a script that will look at the analysis of the last run and be able to provide the current score. 

These two files may be separate from each other, or if you think you can make the human and computer results be in the same file, I'm also fine with that. Your call. 

For qualitative metrics, the whole process, including creating the human-readable form, should be fully automated via script and not require an AI agent. 

For the computer readable File it not only needs a result, but it's the date of the execution period, because there may be a mixture of old executions and more recent executions. 

I would then like to have a script created inside a new "scripts" Folder in the project that will then go through and tabulate all of the latest results across all of the tests and identify places where features are failing. It should output a resultant table with columns for | Date Run | Feature | Score | Pass/fail/skip |. Any individual feature deemed as failing should be highlighted ==FAILED== for visual emphasis. The file will be a markdown file inside the the folder "test-result-summaries" and is named something like "Test Result Summary - 2026-03-01 - 11 36 AM.md". These can accumulate no problem. 

Performing a regression test causes all tests to be updated and will also run the script to tabulate the results into a new test result summary. 
 