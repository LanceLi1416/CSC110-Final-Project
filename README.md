# CSC110 Final Project

## Table of Contents

1.   [Phase 1: Project proposal](#1)
     1.   [Logistics for Phase 1](#1.1)
     2.   [Project topic introduction: The Impact of COVID-19](#1.2)
     3.   [Project overview](#1.3) 
     4.   [Project proposal instructions](#1.4)
     6.   [Some example sources for datasets](#1.5)
     6.   [Example Python libraries](#1.6)
     7.   [Submission instructions](#1.7)
2.   [Phase 2: Final Submission](#2)
     1.   [Logistics](#2.1)
     2.   [Project overview](#2.2)
          1.   [1. Your written report](#2.2.1)
          2.   [2. Your complete program](#2.2.2)
               1.   [Code quality: organization, design, documentation, and style](#2.2.2.1)
               2.   [Program requirements and reproducibility](#2.2.2.2)
     3.   [Submission instructions](#2.3)

## Phase 1: Project Proposal <a name="1"></a>

The CSC110 Course Project is an opportunity to use what you have learned in this course and apply it in a creative, open-ended project. The final submission of your project includes a Python program and report. But before that, you must complete Phase 1: a proposal of what you plan on exploring, designing, and implementing. The CSC110 Teaching Team will give you feedback on your proposal to make sure that your idea is both sufficiently complex and can be completed by the final due date.

### Logistics for Phase 1 <a name="1.1"></a>

-   Due date: Friday, November 5th before 9am Eastern Time.
-   This assessment can be done in groups of up to **4** students.
-   You will submit your proposal on MarkUs (see submission instructions at the end of this handout).
-   Please review the the Course Syllabus section on Academic Integrity.

### Project topic introduction: The Impact of COVID-19 <a name="1.2"></a>

The COVID-19 pandemic is not yet over, but its impact on our lives and the globe is definitely being felt. It has impacted our environment, our healthcare systems, small and large businesses, economic markets, our memes, and virtually every facet of our society. This course is not “about” the pandemic. But the skills you’ve developed in this course, and that you will continue to develop in the rest of your computer science career, can be harnessed to (try to) answer questions about it.

And so for your final project, we ask that you investigate some aspect of the impact COVID-19 has had through a *data and computational lens*. You may investigate the effects of the pandemic on the environment, traffic, education, the potential benefits and limitations of proposed or enacted solutions, mental health, or a completely different angle. We are certain that you will be able to find something to study that is engaging and vital to you.

### Project overview <a name="1.3"></a>

Your project will focus on *answering a data-centric question related to the impact of COVID-19*. You are free to use your imagination and be creative here, and choose something that you are truly interested in answering. There are only two constraints in choosing a question to investigate: it must be meaningfully related to the impact COVID-19 has had on the world in some way, and it must be connected to some kind of real-world data.

For your project, you do the following:

-   *Choose* a particular topic within the broad scope of the problem domain and *research* this topic.
-   *Formulate* a specific data-centric question about this topic, informed by the research you’ve done.
-   *Identify* one or more real-world datasets related to this topic that can help you answer this question.
-   *Compute* on the dataset(s) you’ve found (and possibly perform other computations as well).
-   *Report* the results of your computations in a visual and/or interactive way.

You have performed elements of this a number of times throughout the course already: exploring and computing on datasets (e.g., TTC subway delays, course timetables), defining data models (e.g., generative text models), and visualizations using `plotly` and `pygame`. The purpose of the project is to do something similar with a topic within the problem domain, but on a grander scale. The explorations in the assignments were, metaphorically, a small sandbox for you to play in. In the project, you will build your own, bigger sandbox and play games of your own choosing.

#### Example project ideas

Choosing your own topic can be hard to do, especially when given a fairly broad space like “the impact of COVID-19”. Below, we’ve listed some example project ideas and questions to act as sources of inspiration for your own exploration and brainstorming. (Each one would need to be refined to make a good proposal.) You may not copy any of these ideas directly, but you are welcome to modify and expand on them if you find something you’re particular interested in. And if you want to go in a completely different direction, that’s okay too—please be creative!

-   David loves models—mathematical models, that is! His question is, “*How well can simple supply-and-demand models predict real changes to prices caused by COVID-19?*” He plans to learn about some simple supply-and-demand models that estimate price and implement them in Python. Then, he will compare their estimates over the last year or so with the actual real-world data. His program will display side-by-side graphs of the model and real-world data, for different values of the model parameters.
-   Jen has heard that the pandemic is significantly impacting the price of food. Her question is, *“How has the pandemic’s impact on supply chains increased (or decreased) the cost of food around the world?”* (Jen might want to narrow that down to specific regions and/or specific commodities so that she isn’t overwhelmed with data.) Jen plans to explore datasets on price indexes from multiple countries and see if it can be predicted by the increasing global cost of transportation (e.g., ocean freight prices, fuel prices).
-   Jacqueline loves keeping up to date with the news. Her question is, *“Has the pandemic increased the discussion of mental health in the media?”* She plans to to collect articles from popular publication venues and analyse their texts for mentions of keywords relating to mental health. In addition, she wants to create her own dataset that tracks major events that occured during the pandemic. Her goal is to find out if (a) the pandemic resulted in more articles on mental health, and (b) if there are any patterns associated with major events during the pandemic and a corresponding serge surge (or dirth) of articles.

And here are some examples of **bad** ideas for a project:

-   Paul absolutely *loves* cryptography. He wants to design a new cryptographic system. In order to make this relevant to the pandemic, the data he will encrypt will be related to COVID-19. His goal is to encrypt and decrypt COVID-19 data.

    (*Not meaningfully relevant to the problem domain*)

-   Mario found the use of `pygame` in the tutorials fascinating. He wants to design a game using the `pygame`library. His goal is to create a game where the player repeatedly taps the screen so that a bird is able to make it through all the levels. The levels will be made relevant to the pandemic because there will be hazardous diseases to avoid.

    (*Not meaningfully relevant to the problem domain*)

-   Diane is interested in the pandemic’s impact on people eating in restaurants. She finds a dataset showing the average amount of money spent on restaurants each month over the last 3 years and plots it using `plotly`.

    (*Too simple.*)

### Project proposal instructions <a name="1.4"></a>

Your project proposal is designed as a way to get you started working on this project early, and to give your TAs an opportunity to give you some meaningful feedback and suggestions on your ideas to make sure you are on the right track. *We expect everyone to do very well on this proposal*—our goal is to spend most of our grading time giving you feedback. This proposal does not lock you into a particular topic, and your group will be free to change your plans between this proposal and your final project submission.

Your project proposal will be a LaTeX document (using the **template `project_proposal.tex`**; see the MarkUs starter files) consisting of the following components:

1.  Project title (pick something informative and professional, but you can be creative too) and name of *all*group members.

2.  Brief problem description and research question. (300–400 words)

    -   Give an overview of any background knowledge necessary for *the reader* to understand the problem you are studying.
    -   Provide context for the problem and motivate why you have chosen your research question.
    -   Your research question should be in **bold**; it should be fairly concise, but can be more than one sentence.

3.  A description of at least one relevant dataset you have found. (~150 words)

    -   State the source (e.g., government/organization website) and format (e.g., text, csv, json, image) of the dataset, and give some sample data contained inside that dataset.
    -   Don’t be afraid to cobble together your own dataset, such as creating a collection of images that are related. Or to combine two datasets from different sources.
    -   You will also submit a small sample of your dataset to MarkUs along with your project proposal document. (See more below)

4.  A *computational plan* for your project. (300–500 words)

    -   Describe the kinds of computations you plan to perform, such as: data transformation/filtering/aggregation, computational models, and/or algorithms.
    -   Explain how your program will *report* the results of your computation in a visual and/or interactive way. You don’t need to go into a lot of details here, but it should be clear what you plan to do.

    **Technical requirement**: for your project, you **must** use at least one Python library/module that we have not covered in this course, *or* use `plotly` or `pygame` to a much larger extent than what have given you so far in this course. (See examples and note in the next section).

    -   In this part of your proposal, you should also describe one new library you intend to use, how you will use it, and why it is appropriate. Refer to specific functions, data types, and/or capabilities of the library that make it relevant for solving the problem you wish to solve.

5.  A references section that lists the references you used for your proposal. This should include references from your topic research, the reference for where you obtained the dataset, and any online documentation or tutorials for the Python library you plan to use for the project.

    -   You may use any academic reference style you wish, e.g., APA or MLA.

### Some example sources for datasets <a name="1.5"></a>

Finding a dataset for your idea may be difficult, depending on your topic and question. Below are some examples of websites where you can find datasets or search for datasets. But please don’t limit yourselves to data from these sources.

-   Google now has a [Dataset Search](https://datasetsearch.research.google.com/). Learn more about this feature from their [blog post](https://blog.google/products/search/discovering-millions-datasets-web/)
-   Statistics Canada has a page dedicated to [a data perspective on COVID-19](https://www.statcan.gc.ca/en/covid19?HPA=1) – if you are stumped for inspiration, this may also be a good source of ideas.
-   Many governments have an “open data” website where they publish data to the public that they have collected. For example, here is one for [Canada](https://open.canada.ca/en/open-data), [Australia](https://www.opendataaustralia.org/), and the [United Kingdom](https://data.gov.uk/).

#### A note about originality, licensing, and references

As you do research and come across datasets, it is important to note down where a fact or piece of data came from. This is especially true with data: just because you were able to download it online does not mean you have permission to use it. You need to not only make sure that you have permission to use the data, but also must include an attribution to where you found the data. Similarly, when providing context and/or making claims in your proposal, be sure to provide a reference to where that information came from.

### Example Python libraries <a name="1.6"></a>

-   [`scrapy`](https://scrapy.org/): a library for extracting data from websites
-   [`scikit-learn`](https://scikit-learn.org/stable/index.html): a machine learning library that is (relatively) easy to use
-   [`scikit-image`](https://scikit-image.org/): a library that helps process image data
-   [Natural Language Toolkit (nltk)](https://www.nltk.org/): a library that helps with analyzing text written in a language (like English)

Also, for your reference here are links to the websites for documentation for `plotly` and `pygame`:

-   [`plotly`](https://plotly.com/python/)
-   [`pygame`](https://www.pygame.org/docs/)

*Note*: While you may rely on the library you choose to help you with some computations, you cannot use the library to do *all* your computations. That is, simply applying a well-known algorithm to your dataset by calling functions in the library is not a sufficiently complex project.

Similarly, if your library is responsible for visualization and not computation, your project should not simply be to load and visualize the data. The data you load must be transformed or computed upon in some way before visualization.

### Submission instructions <a name="1.7"></a>

Please **proofread** your work carefully before your final submission!

1.  Login to [MarkUs](https://markus.teach.cs.toronto.edu/csc110-2020-09).
2.  Go to *Project Phase 1: Proposal*, and the “Submissions” tab.
3.  Submit the following files: `project_proposal.tex`, `project_proposal.pdf`, and your sample dataset file(s).
    -   You decide how many files are in your dataset (i.e., one or more).
    -   Please don’t submit the full dataset (this will likely be too large for MarkUs). Instead, extract a small part of it (e.g., just the first 100 entries) to submit.
    -   Your TAs *will* be checking your data set file(s) manually, so make sure they are formatted correctly.
4.  Refresh the page, and then *download each file* to make sure you submitted the right version.

Remember, you can submit your files multiple times before the due date. So you can aim to submit your work early, and if you find an error or a place to improve before the due date, you can still make your changes and resubmit your work.

After you’ve submitted your work, please give yourself a well-deserved pat on the back and go take a rest or do something fun or eat some chocolate!

# Phase 2: Final Submission <a name="2"></a>

The CSC110 Course Project is an opportunity to use what you have learned in this course and apply it in a creative, open-ended project. In [Phase 1 of the project](#1), you submitted a proposal describing how you planned to perform a computational exploration on the impact of COVID-19. Now in the second, and final phase, of the project you will submit a project report and the program that you created. While this is the “final” submission of your project for CSC110, we encourage you to continue with the project even after the course is done and you learn new things!

## Logistics <a name="2.1"></a>

*   Due date: Tuesday, December 14th before 9am Eastern Time.
*   This assessment can be done in groups of up to 4 students.
*   You will submit your project on MarkUs (see submission instructions at the end of this handout).
*   Please review the the Course Syllabus section on Academic Integrity.

## Project overview <a name="2.2"></a>

Before continuing to the rest of this handout, we recommend reviewing the [overall project requirements from Phase 1](#1). We have not repeated them here.

Your project submission is divided into two components, a *written report* and the *Python program* you created for this project. The next two sections of this handout describes the required elements for both of these components.

### 1. Your written report <a name="2.2.1"></a>

Your project written report builds on your project proposal from Phase 1, incorporating any changes to your project direction, a more detailed computational plan, and a discussion of the results of your exploration.

You should submit two files for this part: `project_report.pdf` and `project_report.tex`. We haven’t provided a LaTeX template for this part, and instead encourage you to start with your `project_proposal.tex` file from Phase 1 and adapt it for this phase.

Your report must include the following sections:

1.  Project title (pick something informative and professional, but you can be creative too) and name of *all* group members.

2.  An introduction containing your problem description and research question. You can start with the text from your project proposal, but then incorporate TA feedback or changes that your group has decided on. It’s okay if your research question (or entire project direction) has changed from what you originally proposed! Review the original proposal instructions for this section to include necessary background information and motivation.

    As in the project proposal, your research question should be in **bold**.

    *Note*: this section should also use [inline references](https://advice.writing.utoronto.ca/using-sources/documentation/) when citing facts, data, or work that is not your own. You may use any academic reference style you wish for this project.

3.  The name and description of **all** datasets you used for your project. Include the format and source of each dataset.

    Also state which parts of each dataset (e.g., which columns in a csv file) are actually used by your program. (When using large datasets, it is common to use only a subset of the data found within them.)

    Unlike the proposal, you do *not* need to provide samples of each data set.

4.  A **computational overview** for your project.

    This is similar to the computational plan you submitted in the proposal, except now it’s not a plan, but a description of the program you’re actually submitting.

    -   Describe the major the computations your program performs, such as: data transformation/filtering/aggregation, computational models, and/or algorithms.
    -   Explain how your program reports the results of your computation in a visual and/or interactive way.
    -   Explain how your program uses *new libraries* to accomplish its tasks. Refer to specific functions, data types, and/or capabilities of the library that make it relevant for accomplishing these tasks.

    This overview should be more detailed and concrete than the plan you submitted, since you are submitting your actual code as well. Refer to concrete files, data types, and/or functions that you created in your descriptions of this part. However, you do not need to mention every single data type/function you wrote; use your judgment to only refer to the most important data types and functions that you created for each “computational phase” of your program.

5.  Instructions for **obtaining data sets and running your program**. Your TA will expect to be able to run your program starting from just their computer with only Python (version 3.9) installed. You can expect that the TA will do the following:

    1.  Install all Python libraries listed under a `requirements.txt` file that you submit as part of your project.

        -   Your project must be “pure Python”—you may **not** use other programming languages or non-Python software, and your TA will not install these.
        -   If any Python libraries requires special installation instructions, first check with an instructor, and then include those instructions in your final report.

    2.  Download data sets based on *specific URLs that you provide*.

        -   Because your datasets may be quite large, you will be unable to submit them directly on MarkUs. Instead, you should include *every* URL to the datasets you used so that your TA can download them directly.
        -   Alternatively, part of your program may use a Python library (e.g., `requests`) to automate the process of downloading datasets. In this case, the instructions to your TA should be to run a particular Python file or call a particular function.
        -   If you have done any pre-processing of the datasets, you should both (1) provide links to the raw datasets you started with, and (2) include a link for your TA to download the processed versions using https://send.utoronto.ca/. Note that links generated using this service expire after 14 days, so you should only do your final upload a day or two before the submission deadline. If you are doing this, we strongly recommend bundling your data files into ZIP files to reduce the file size.

        Include instructions to your TA on where to save these dataset files relative to your Python files (e.g., in the same folder, in a subfolder called `datasets`, etc.)

    3.  Run a file that you submit called `main.py`. (See next section for expectations for structuring your code.)

        -   Describe what your TA should expect to see as a result of running your program (i.e., what the output looks like, what data is being shown, etc.) Screenshots are helpful here!
        -   If your program produces an interactive visualization or display, describe the different interactive features and how your TA can use them.

6.  A brief description of any changes to your project plan between your proposal and final submission. This can be based on TA feedback you received on your proposal, discussions with instructors during office hours, or discussions with your group members or other ideas you wanted to explore.

7.  A **discussion section** where you discuss, analyse, and interpret the results of your program. Remember that your goal for this project was to answer the *research question* you posed at the start of this report! Consider questions such as:

    -   Do the results of your computational exploration help answer this question?
    -   What limitations did you encounter, with the datasets you found, the algorithms/libraries you used, or other obstacles?
    -   What are some next steps for further exploration?

    You do *not* need a separate “Conclusion” section, so you may also choose to summarize and write a brief concluding paragraph at the end of this section.

8.  A references section that lists the references you used for your project. This should include references from your topic research, references for every dataset you used, and any online documentation or tutorials you consulted for the Python libraries and algorithms you used for this project.

    -   You may use any academic reference style you wish, e.g. APA or MLA.
    -   See https://advice.writing.utoronto.ca/using-sources/documentation/ for example formats for both inline citations and formatting a list of references.

#### Note about word limits

There are no formal word limits or requirements for this report. The expected length for each section is comparable to but slightly longer than the corresponding sections on your proposal, including more details (e.g., more datasets to describe, and a more concrete computational overview).

Your instructions to your TA for running your program should be clear and concise.

Your discussion section should be around 500-800 words.

### 2. Your complete program <a name="2.2.2"></a>

For this project, you have a large amount of freedom in how you organize, design, and implement your code. Because of the open-ended nature of this project, we aren’t running any automated testing on your submissions! Instead, you are submitting your code so that your TAs can assess the overall quality of your code, and their ability to actually run your program and reproduce the results that you report.

#### Code quality: organization, design, documentation, and style <a name="2.2.2.1"></a>

Your program is the largest and most complex body of Python code you’ve written in this course. You should split up your program into multiple files organized into logical groups (e.g., the code responsible for reading data from data sets; the code responsible for computing on the data; the code responsible for displaying the results of the computations). You should also have one separate file called `main.py`, whose main block consists of the code necessary to run your entire program from start to finish (see next section for details).

Within each file, you are responsible for designing and implementing Python classes and functions to organize your data and operations on that data.

All Python files and code you submit must follow good design, documentation, and style principles that we’ve learned throughout this course.

1.  *Modules*. Each module should have a title and description, following a similar format to the ones we’ve provided for you in starter files for preps and assignments. You and your group members should claim copyright on your own work!

    Modules should consist only of import statements, function and data type definitions, and a main block at the bottom of the file. There should not be any top-level statements/function calls outside of the main block.

2.  *Functions and classes*. Every function and class that you define should follow the course standards for naming, headers, docstrings (including preconditions/representation invariants). This includes helper functions.

    Doctest examples are not required, but strongly encouraged where possible to help your TA understand your code. You may, but are not required, to submit other tests you write for your project.

    A convention we encourage, but not require, you to follow is to list your functions in top-down order of importance: the “main” function(s) at the top of the file, and helper functions beneath them.

3.  *Code-checking tools*. In each file except `main.py`, your main block should run `doctest.testmod()` to check any doctests, and use `python_ta.contracts.check_all_contracts` and `python_ta.check_all` to use PythonTA to check your work. Unlike past assessments, you may modify the `config` argument for `python_ta.check_all` to suit the needs of your module, e.g., by adding additional imports or listing function names that call `open` or `print` under the `'allowed-io'` option.

    We aren’t automatically giving a grade based on passing all doctests or counting the number of PythonTA errors. However, your TAs will be reviewing both doctests and your overall code quality, and these tools are designed to help you check both of these—use them!

    Here is a sample call to `python_ta.check_all` that you can base your own configuration on:

    ```python
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],     # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
    ```

#### Program requirements and reproducibility <a name="2.2.2.2"></a>

As we discussed in the “written report” section above, your TA will expect to be able to run your program starting from just their computer starting with only Python (version 3.9) installed. To help your TA with this process, your program files must include:

1.  A `requirements.txt` file that lists every external library your program relies on, such as `python_ta`, `pygame`, `numpy`, etc. There are many resources online for creating a `requirements.txt` file; [this answer](https://stackoverflow.com/a/31684470) may be helpful. Or, you can adapt the `requirements.txt` we provided at the start of the semester for CSC110:

    ```python
    # CSC110 Fall 2020: Python libraries we'll be using this semester.
    
    # Testing and code checking
    hypothesis
    pytest
    python-ta
    
    # Graphics and data visualization
    plotly
    pygame==2.0.0.dev10
    ```

2.   A Python module called `main.py` whose main block contains the code necessary for running your entire program. When run, this module should:

     1.  Load the necessary files from the datasets.
     2.  Perform your computations on the data.
     3.  Produce an output (which may or may not be interactive).

     Your `main.py` file can be quite short, and just import the necessary functions and data types from your other Python modules. To keep things simple, all of your Python modules should be kept in the same folder as `main.py`, and submitted together on MarkUs at the “top level” (no subfolders).

     Running `main.py` may produce an interactive way of interacting with your computational results. In this case, you should include instructions on how to use the interactive components in your written report.

     You may, if you wish, provide a *few* different ways of calling your program’s primary functions that are commented out in your `main.py` and that your TA should try individually. In this case, include clear comments inside your `main.py` file *or* in your written report to describe the different ways your TA can comment/uncomment various function calls to run your program, and the differences they should be looking for in your program’s output/results.

## Submission instructions <a name="2.3"></a>

Please **proofread** and **test** your work carefully before your final submission. This final project is the culmination of a lot of work and learning you’ve done over the entire semester, so take pride in it and check everything over before you submit!

1.  Login to [MarkUs](https://markus.teach.cs.toronto.edu/csc110-2020-09).

2.  Go to Project2, and the “Submissions” tab.

3.  Submit the following files: `project_report.tex`, `project_report.pdf`, `requirements.txt`, `main.py`, and any other Python modules (or other supporting files) that your project requires.

    Please note that MarkUs is picky with filenames, and so you must submit filenames that match these exactly, including using lowercase letters. You can choose the names of the other Python files you submit, but make sure to follow standard Python naming conventions (lowercase letters, with words separated by underscores).

4.  Test your program out on a *fresh computer* to check that everything will work properly for your TA.

    Here are the steps to follow:

    1.  If you don’t have a fresh computer, first *uninstall Python 3.9* and then re-install it. If you have a fresh computer, install Python 3.9 and PyCharm on it. If you are using one of the department’s computers, they should have PyCharm and Python 3.9 already installed.
    2.  Download all of the files you submitted to MarkUs onto the computer, in a new folder.
    3.  Install all of the Python libraries listed under the `requirements.txt` file you submitted.
    4.  Follow any additional installation instructions you wrote in your project report.
    5.  Download all required datasets by following the instructions you wrote in your project report.
    6.  Run your `main.py` file (e.g., in PyCharm). It should “just work”—if you run into any errors, fix them and (if necessary) update your report’s instructions so that your TA doesn’t run into problems!
    7.  Review the output/product of your program, and the descriptions/instructions you wrote in your report for interpreting the results or interacting with your program. Your TA should be able to make sense of them!

    You can also test out your instructions with a family member or friend (not in CSC110)—they should be able to follow all of these required steps even if they don’t have any technical knowledge, except possibly needing help with “running” `main.py`. Plus it’s a good chance to show off your work! :)

Remember, you can submit your files multiple times before the due date. So you can aim to submit your work early, and if you find an error or a place to improve before the due date, you can still make your changes and resubmit your work.

After you’ve submitted your work, please give yourself a well-deserved pat on the back and go take a rest or do something fun or eat some chocolate. **You’ve just completed CSC110!**



![](https://www.teach.cs.toronto.edu/~csc110y/fall/project/phase2/images/pineapple.jpg)
