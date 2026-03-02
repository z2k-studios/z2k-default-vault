Z2K Core Template Library

## SoW Modifications
- Rename the SOW Workflow to be the “Iterative Framework” 
- Some Terms and Acronyms to add to the SOW (Make a dedicated section)
    - Z2K Core Template Library v3 - CTLv3, or just CTL (assume CTL means the new version) - This is the final product of this SoW, the output
    - Z2K v2 Template Library - CTLv2 - this is the previous version of the templates library (location already given). This is the input for this SoW - what we are taking in to transform into CTLv3
    - ZS - Z2K System - this is the name of the overall approach of storing markdown files to build a digital identity. “Version 3” (ZSv3) is the version of the system that uses CTLv3.
    - Sow - Statement of Work 
    - IF - the interactive Framework inside the SOW. 
    - The “IF Model” is the meta of IF - the overall phased and iterative  approach
    - PRD - Project Requirements Doc. 
    - IP - Implementation Plan
    - TP - Testing Plan
    - PDL - Project Document Library
    - Requirements and Features - the PRD will use both terms but they effectively mean the same thing. Be flexible in using both terms. Features are from a user perspective, requirement is from a project manager perspective.
- The Phased IF model will be highly iterative. We will first begin with the most basic of tasks, and tasks that are most upstream in a dependency list and run them through the Phased model first.  The goal is to punch through the iterative nature of the IF from start to finish on the most basic of tasks first. Then, using prioritization and dependency graphs, build out from there with new features, pushing it through the entire IF model, and repeating again and again with the next feature in the requirements document
    - Some features will need to be grouped together for implementation together
    - We will have initially far more features than we will have implementation plan details for. That’s fine. Just list those features that we do not yet have plans (or only rough plans) for as draft.
- The PDL needs an area for out-of-scope tasks discovered during iterating the IF. 
    - Create a PDL SubFolder called “Out of Scope Tasks”
    - Create a template file as an index file. Each task should get its own file.
    - Review the Q&A for any out of scope tasks (e.g. I remember making a note of an implementation i want to potentially try in the future).

### Document Feedback
When I had you draft PR and IP documents for this project, you were given largely empty templates. Having had some timme to think (and not yet having read your actual first draft output), I want you to incorporate some feedback into the structure of the various docs. Here is how to incorporate it:
- Some feedback for the specifications of what needs to go into each document are below. Please use that feedback directly to modify the generated Project Requirements and Implementation Plan documents for this project. (It's ok to skip forward during this session and ignore the lock requirements). This feedback should only be additive - do not remove any existing sections or content from the generated documents. 
- Some if this feedback is more general and pertains to the overall project workflow and approach, rather than specific requirements for the PRD and IP documents. Please use that feedback to modify the Statement of Work document for this project, particularly in the section where we describe the project workflow and approach. 
    - Note that we are listing the PRD and IP Docs feedback here in the statement of work because we want to capture this as part of this project’s IF. By capturing these requirements for the documents themselves at the statement of work level, we will then be able to reuse these concepts for future projects by using this statement of work as a template for future iterative projects.
        - When we go to improve our project workflow, these would be good things to add to sample template files (for SOW, IP, PRD) for each of these documents. I can imagine having multiple variations of templates depending on the type of project. For instance, this is a highly iterative project. I can see a different template be needed for a more sequential project. This should be noted in the "continuous improvement" (details discussed below)
    - More direct feedback that pertain to this particular projects situation will follow in the next header. 




#### Document Requirements Feedback for the SOW, PRD and IP Docs
- Feedback for the SOW Doc:
    - Identify elements from the feedback for the PRD and IP docs that should be elevated to the SOW as requirements for those documents. 

- Feedback and Doc Requirements for the PR doc: 
    - We have already, through Q&A, developed a fairly large scope for the over all project using the preexisting templates. None of that should be lost and all of must be captured in the Requirements document
    - Every requirement should have an importance level attached. 
- Feedback and Doc Requirements for the IP Doc.
    - Prioritization and Dependencies
        - The implementation plan needs to be driven by prioritization and dependencies. Reminder - the IF is highly iterative, with the first implementations to be done to “punch through” to the end.
        - There needs to be a dedication prioritization and dependencies section to the document. It contains two sets of priorities and dependencies:
            - Tooling Priority (Z2K Templates Plugin):
                - Knowing that we are bootstrapping, it is important to also prioritize the importance and dependencies of the Tooling (Z2K Templates Plugin)’s features.
                - For instance, we will need to know that system blocks work early on. Further we will need the ability to perform Command Queue processing early on to enable automated testing.
            - Requirements Priority
                - The general requirements priority precedence should be laid out. For instance, getting the root level templates should be the first concern. Then system blocks. Then default templates for each domain, etc.
        - Every implementation task (mapping to requirements) should have:
            - A List of Dependencies:
                - The implement plan should have a “Z2K Templates Features” section within it that a) lists out all features in the Z2K Templates Plug-in that are required to implement the task
            - An implementation priority/order assigned to it. 
            - 
        - Implementation Order
            - With that, then the IP document should generate a dependency graph on its is own of the features in the Z2K Templates plugin required in order to implement and test a feature, and successively, all features
            - This will generate an order of implementation tasks to perform 
            - The priority/order will be a combination of the requirement’s importance, its tools requirements priority and dependence (i.e. what features in Z2K Templates does it require in order for it to be implemented and tested), its testing automation level (prioritize tasks that are automated in testing) and the requirements own position in the dependency list
                - This will require judgment calls. Given that the IF is iterative, it will be easy to make adjustments to task ordering if needed.
            - Some implementation tasks will be contained in “implementation task groups” of interrelated requirements-implementation mappings. If things can be linear, however, always try to sequentialize. These will be performed at the same priority level. 
            - Every Implementation task/task group should have a list of dependencies, to include: other implementation tasks, tooling requirements (e.g. z2k templates plugin features). 
        - Z2K Templates Feature Prioritization
            - With the Implementation Order in place, Construct a priority and dependency graph of features within the Z2K templates plugin that are required for the Z2K Template Library to work. For instance, to perform automated testing, it is important that the Command Queue capabilities be tested and validated very early on. 
            - This will be given to the Z2K templates plug-in developer to help him prioritize. What items to work on.

## Project Requirements (PR) Contents
- We are bootstrapping / dogfooding. 
    - Z2K Templates Plugin
        - The Z2K Templates plugin project is in the middle of development. There will be errors in both its code and its documentation that we will need to fix. 
        - We will use the documentation as the intended behavior, and treat any discrepancies from the documentation as an issue with the template plugin. 
        - Any ambiguities or conflicts within the documentation is a documentation issue.
        - Notify the user promptly of blocking issues.
    - Z2K System Documentation
        - Please consider the Z2K System Documentation to be non reliable. It is a mixmash of ZSv1 and ZSv2, and even then, incomplete.
        - Only the list of top level domains has been updated for the new version 3 of the Z2K System.
    - All other tools and components should be considered as working tools.
- Outputs:
    - A Working CTLv3 implementation
    - Continuous Improvement: A List of changes to make to the existing project workflow. These changes should be items of a universal appeal, not specific to this SOW
        - To jump early into implementation, this should be a folder in the PDL called "Post Project", then a subfolder for "Continuous Improvement" with a file in there for "Project Workflow Improvements" or something like that. This file should have a list of proposed improvements to the project workflow based on the learnings from this project. Each item should have a description, rationale, and proposed implementation approach.
        - To start:
            - rename the SOW in the default project template to be Interative Framework to deconflict with the ai-context workflow term
            - Add a list of acronyms to the SOW
            - Create multiple IFs that describe different levels of iterativeness. Some projects will be highly linear, proceeding forward with one phase in the IF before continuing with the next phase (the existing template is like that). This project will use a far more iterative approach - see details in the SOW above.
    - Post CTLv3 Outputs:
        - Preface: The following will be outputted only after all work has been done for CTLv3. But it is important to record notes into a filing system to prepare for these outputs once we are done. Many of the items here are only found as we iterate through the IF on specific requirements
        - CTLv3 Project
            - A new project defined (the “CTLv3 Project”) with new SoW, PR, IP, and TP documents that will be the ongoing CTLv3 Project. This Project will be all about implementing new templates within the workflow framework we establish here. The output will remain being a full implemented Core Template Library
            - This will no longer be have CTLv2 as an input. Rather new inputs will come from chat discussions (“I’d like to add a template for xxxx”). 
            - The initial run of this project will simply ensure that the existing CTLv3 passes all tests
            - This work only begins when we have validated the new CTLv3
        - ZSv3 Project
            - A new project defined (like CTLv3) that will capture the project of building out the Z2K System Architecture. The key output for this will be the Z2K System Documentation
    - An ongoing list of bugs within the Z2K Templates plugin and a level of severity and blocking nature of the bug.
        - This list should have everything needed to create a new GitHub issue for each bug. This includes an example and steps to repo. 
        - Each bug should have a status attached (observed, repeatable, identified and ready to submit). A bug should step through those steps. A bug will only be acted upon when it reaches the final state. Submitting of the bug and fixing it is the responsibility of the Z2K Templates plugin project 
        - Each bug will have an urgency (low (minor), normal, high, and high-blocking). 
        - Each bug will have a component label (documentation, code) 
        - Each bug will have a scoping label (bug, enhancement)
        - In the implementation plan to create a subfolder within the PDL to hold Issues/Bugs, and then another subfolder underneath that for each of the Tools this project uses. Each bug should create its own file.

## Implementation Plan
- For post CTLv3 outputs, we will need a Folder in the PL to capture items to be included in the different projects. Each item will have its own file. In general, most items will likely be requirements to add to the PRD of those projects.
-  

## Testing Plan
- 
