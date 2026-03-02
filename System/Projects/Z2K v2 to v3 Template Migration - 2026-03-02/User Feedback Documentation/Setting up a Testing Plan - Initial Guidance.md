So we now need to build the testing plan. I need to lean on you to do that as much as possible, but I can give you some general guidance. 

In general, all testing should be performed via scripts so that it is repeatable and executable in regression testing. Minimize the amount of AI-level intelligence of interpreting Text, context, or situation in which the AI is assessing whether an implementation task was completed successfully Against its requirements. 

For the scripts, No need to build one script per task, but rather group them together in their larger phases or task chunks. 

Store the scripts into a testing subfolder of the PLD. 

For many of the early tasks, you're just focused on creating directories and files. This can be tested just by a simple file existence script. 

Later, as you create new templates and the templates reach a point where they are working, then begin to use one of the automated methods with the Z2K Templates plug-in to validate that the template was successfully instantiated. 

You can provide a number of different calls with JSON packages to control how it handles different situations. Do as much testing in an automated fashion as you possibly can before engaging with user-level testing. 

All user level, as in Requiring a user to assist with the process should be put to the very end. Therefore, you should do as much testing as possible with an automated solution. 

I am fine with putting off all tasks that require a user-assisted testing method at this point. We can revisit after we have exhausted our automated processes. 

You can use URIs or command queues to perform the testing. Both likely will have some bugs that we do not know about just yet, so we will need to do some exploratory work to figure out which testing method will work the best. 

As such, that may need to be an early task to perform, and therefore we need to spec out an implementation plan task that will help determine which method to use. 

You will likely want to update your reference docs index in the implementation plan to cover how to do the JSON-based testing. 

So stepping back, here's what I think you need to do: 
Inside your implementation plan, make a task Or set of tasks to establish a working path for having an automated testing method in place. This should basically make that decision on command queues versus URI, with a preference to command queues because I believe it is more powerful. 

Then, after buy-in, return to the testing document and Draft an initial testing plan. This should reference the need for automation and emphasize the prioritization of fully automated tests first. 

The testing plan can leave details on the approach for user-assisted testing for a future revision period. 

I recognize that you will need a fair amount of user assistance here at the beginning as well in order to set up the Vault for automated testing. 

Do you have any questions that I can answer? If so add them below.
