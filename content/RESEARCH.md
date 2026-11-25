# Research tasks

Six short tasks, **5% each** (30% in total). R1 and R2 take a week's idea out of the notebook and into a real system you know. R3–R6 each teach you one **programming concept** that the next week needs: you **read** about it first, then **ask** an AI about what stayed unclear, **check** one thing by running code, and **decide**: you give your own view on a question that has no single right answer.

This page is the reference for every research task: keep it open whenever you start one. The marking criteria are in [assessment](ASSESSMENT.md).

| Task | Topic | Set in | Share in the class warm-up | Debate question |
|---|---|---|---|---|
| R1 | A real information system | Week 1 | Week 2 | — |
| R2 | Rules and edge cases | Week 2 | Week 3 | — |
| R3 | Errors and exceptions | Week 4 (after the midterm) | Week 5 | Should a program crash, or keep going with a guess? |
| R4 | How real apps keep records: lists, dictionaries and objects | Week 5 | Week 6 | Should a status be free text or one of a fixed list? |
| R5 | What happens to data when the power goes off | Week 6 | Week 7 | Should a system ever really delete data? |
| R6 | Code written by AI | Week 7 | Week 8 | Who is responsible when AI-written code harms someone? |

R3 is the only research task set in the midterm week, and it is set after the midterm itself. There is no research task in Weeks 9–10, so you can focus on the final project.

**Warm-up:** the first 10 minutes of Session 1. Bring one finding to share in a group of three. **Submit** by email to [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com); deadlines and file names are announced in class. Marking criteria are in [assessment](ASSESSMENT.md).

The six tasks follow the course journey. R1 and R2 test the ideas of the first weeks against a real system. R3–R6 come one week early: you meet the concept in your research, and then you use it in the next week's notebook.

## R1 · A real information system

*From [Week 1 · What is an information system?](notebooks/Week_01.ipynb).*

Choose a system you have used: school registration, a bus or ticket app, a library, a hospital queue, a mobile-money app. Who uses it (at least two roles)? What data does it keep? Name one rule it follows, and one thing that could go wrong and who would be hurt.

## R2 · Rules and edge cases

*From [Week 2 · Rules and decisions](notebooks/Week_02.ipynb).*

Choose a rule from real life: a bus fare for children, a library late fee, a data bundle, an exam pass mark. Write it exactly, the way a program would need it. Give a normal case, an edge case (exactly at the limit) and an odd case (missing, negative or unusual). Who decides the rule, and who is affected when the boundary is wrong?

## R3–R6 · Five steps: read, ask, check, decide

R3, R4, R5 and R6 all follow the same five steps. Your submission is about one page.

1. **Read and organise.** Read the [Python Basics](notebooks/Python_Basics.ipynb) section(s) named for your task, and **one** chapter from the list for your task (the books are free online; see [course links](COURSE_LINKS.md)). Then write a summary in your own words, 5–8 sentences: what it is, why it exists, how it works, and one common mistake. Add one tiny example that you ran, with its output.
2. **Ask an AI about what stayed unclear.** Ask an AI assistant about the parts you did not fully understand. Ask **at least two follow-up questions**: one asks for an everyday example from Cambodia, and one asks *"What can go wrong?"* Copy **6–10 key lines** of the conversation into your submission: your questions and the most useful parts of the answers.
3. **Compare and check.** Find one place where the book and the AI say the same thing in different ways, or say different things, or where the AI was vague or wrong. Then test one claim by running a tiny example in Colab. Show the code and the result. Was the claim right?
4. **Your view.** Write **150–250 words** on the debate question. Take a side and give a reason. Use an example from Campus FoodBridge.
5. **Sources and honesty.** Name the sections and chapters you read, and the AI tool you used.

Use invented examples only: never put real personal data (names, phone numbers, ID numbers, marks, account numbers) into an AI or into your submission.

The books: [Python for Everybody (PY4E)](https://www.py4e.com/book) · [Think Python (3rd edition)](https://greenteapress.com/wp/think-python-3rd-edition/) · [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) · [The Official Python Tutorial](https://docs.python.org/3/tutorial/) · and, to watch code run line by line, [Python Tutor](https://pythontutor.com/python-compiler.html).

## R3 · Errors and exceptions

*From [Week 4 · Functions you can trust · Your first files · Midterm](notebooks/Week_04.ipynb).*

**The concept:** What is an error (an **exception**) in Python? What happens to a program when one happens, and how can a program **catch** it?

- **Read:** Python Basics "08 · Reading error messages" and "09 · `try`/`except` (and `raise`)". Then one chapter: PY4E "Conditional execution" (the part about catching exceptions) or the official tutorial "Errors and Exceptions".
- **Ask, for example:** *"I read that `except` catches an error. What happens to the rest of the program after that?"* Follow up with an everyday example from Cambodia (a form, a shop, a phone app) and *"What can go wrong if a program catches every error and keeps going?"*
- **Check, for example:** run `int("abc")` and `int("12")`. Does the first one stop with the error the book and the AI described? Then put it inside `try:` and `except ValueError:`. Does the program keep going?
- **Your view:** *Should a program crash, or keep going with a guess?*

## R4 · How real apps keep records

*From [Week 5 · Checking input](notebooks/Week_05.ipynb).*

**The concept:** How do real apps, such as a phone's contact list or a bank account, keep their records? What are **lists**, **dictionaries** and **objects**, and when is each one useful?

- **Read:** Python Basics "05 · Lists, dictionaries, tuples, sets" and "13 · Classes, objects, methods". Then one chapter: PY4E "Dictionaries" or Think Python "Dictionaries".
- **Ask, for example:** *"How would a contact list or a bank account be kept in Python: as a list, a dictionary or an object?"* Follow up with an everyday example from Cambodia and *"What can go wrong with the way these records are kept?"*
- **Check, for example:** make a list of two dictionaries (two invented contacts), find one by its key, and try a key that is not there. Does Python do what the book and the AI said?
- **Your view:** *Should a status (for example "approved" or "delivered") be free text that anyone can type, or one of a fixed list?*

## R5 · What happens to data when the power goes off

*From [Week 6 · Lifecycles](notebooks/Week_06.ipynb).*

**The concept:** Where does a program keep its data while it runs, and what is lost when the power goes off? What do **files**, file formats, **databases** and **backups** add?

- **Read:** Python Basics "11 · Files and CSV" and "12 · JSON and JSON Lines". Then one chapter: PY4E "Files" or Automate the Boring Stuff "Reading and Writing Files". If you are curious about databases, also look at the start of PY4E "Using Databases and SQL".
- **Ask, for example:** *"What is the difference between data in memory and data in a file? Why do systems use databases and backups?"* Follow up with an everyday example from Cambodia and *"What can go wrong when a system saves data?"*
- **Check, for example:** in Colab, give a name a value and run it. Then use **Runtime → Restart session** and print the name again. Is the value still there? Now write the value into a small file (as in Python Basics 11), restart, and read the file. What is different?
- **Your view:** *Should a system ever really delete data?*

## R6 · Code written by AI

*From [Week 7 · Saving and history](notebooks/Week_07.ipynb).*

**The concept:** How far can you trust code that an AI writes? How do you **test** it?

- **Read:** Python Basics "07 · Functions and `return`" and "10 · Tests with `assert`". Then one chapter: the "Debugging" section of a Think Python chapter (for example "Functions"). Use Python Tutor to watch a function run line by line.
- **Ask, for example:** give the AI a small contract, such as *"Write a Python function `average_mark(marks)` that returns the average of a list of marks, and 0 for an empty list. Explain each line."* Follow up with an everyday example from Cambodia where such code is used and *"What can go wrong with this function?"*
- **Check:** test the AI's function with **your own cases**, written as `assert` lines: a normal case, a boundary case and an odd case (for example an empty list). Show each case and its result. Did the function pass every one? If not, which case caught the problem? Paste the function into Python Tutor and follow one case.
- **Your view:** *Who is responsible when AI-written code harms someone?*

## Using AI tools for research

- **R1 and R2:** AI tools are allowed but not needed. If you use one, show one place where you checked or corrected it, and say how. You can earn full marks without using AI.
- **R3–R6:** you read first (step 1). The AI conversation comes **after** the reading (step 2) and is part of the task; comparing and checking what it said is step 3. The AI helps you understand; it does not write your summary or your view. Steps 1 and 4 must be your own words. **No AI access?** Ask a classmate or the instructor instead and keep 6–10 key lines of that conversation in the same way, or write the questions you would ask and answer them from a second book chapter. This earns the same marks.

In every task, your submission must be your own explanation, and you must be able to explain it in class.
