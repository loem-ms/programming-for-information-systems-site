# Final project · Your FoodBridge system

Your Final project is **your own `my_foodbridge/` folder**: the system you built from Week 4 to Week 10. At Demo day you show and explain it **as a whole**: who uses it, how its files work together, the decisions you made in it, and one extension of your own. You also hand in a short report. You do not start a new notebook. You keep building what you have.

The [`Final_Project.ipynb`](notebooks/Final_Project.ipynb) notebook helps you **check, write up, pack and present** your folder. It never changes a file you wrote.

*Campus FoodBridge is fictional. All organisations, people and numbers are invented.*

## The five parts

All five parts are required. Each one is small.

| Part | You show … | Where |
|---|---|---|
| **1 · It runs** | your menu works, and `bridge.check("all", folder="my_foodbridge")` shows ✅ for the parts you wrote | `app.py` and your Week 4–9 files |
| **2 · Make it yours** | three settings you changed from the defaults: one about **privacy or input checks**, one **backed by data**; each has a row in your decision log, with Evidence | the 🧭 lines of `check("all")` and your decision log |
| **3 · My extension** | one extension from the menu below, with **at least two tests in `tests.py` that can fail** | your files, `tests.py` |
| **4 · The report** | `README.md` in your folder, about two pages, with eight headings | `my_foodbridge/README.md` |
| **5 · Demo day** | 3 minutes with your system poster, then a live change the instructor asks for, then one question | Week 10, Session 3 |

Parts you did not write are replaced by the kit's model version (📦), so your system always runs. Your marks come from what **you** wrote, decided and can explain. A small system with strong, well-explained decisions and one well-tested extension scores higher than a big one with weak reasons.

## From Week 5 to Demo day

The Final starts long before Week 10. Every step below gives you material for the next one, so you never start the report from a blank page.

| When | What you do | In class or at home |
|---|---|---|
| Weeks 5–9, end of Session 3 | 📓 **Project journal**: three lines. *What my system does now* · *One decision I made (and why)* · *One idea for my Final*. | class |
| Week 8, Session 3 | **Choose your extension** from the menu below. | class |
| Week 9, Session 3 | **Project charter** (half a page, below). | class |
| Week 9 → Week 10 (about 3 hours) | Build your extension and its two tests. Draft the report, including the reflection, from your journal and your charter. | home |
| Week 10, Session 1 | `tests.py` and the verification lab (a sanity check, the canary, a clean run): rows for your verification log. | class |
| Week 10, Session 2 | Finish the report and its reflection, do a last clean run, and **submit your zip by minute 45 (code freeze)**: this is your one submission. Then rehearse your demo. In a large class, Demo-day turns at the instructor's desk may start now. | class |
| Week 10, Session 3 | **Demo day**, then a short spoken look back (nothing to write or hand in). | class |

### The project charter (Week 9)

Half a page, written in class. It is your plan, and the first draft of your report.

1. **Who uses my system, and what each person needs.** For example the coordinator, a volunteer, a partner, a donor, anyone in the canteen.
2. **My three decisions so far.** The setting, my value, and the evidence I have (or still need).
3. **My extension, and how I will test it.** Two tests: the input, and the answer I expect.
4. **A first drawing of my system.** The people, the files, and how the data flows between them. Pencil and paper is fine.

## Part 1 · It runs

- `bridge.check("all", folder="my_foodbridge")` shows ✅ for the parts you wrote, and no ⚠️ file problem.
- `bridge.show("app", script=["1", "2", "3", "q"])` shows your menu working (add `"4"` if your extension added a choice).
- Running `python app.py` in a terminal is a good extra row in your verification log (the Week 9 Go further), but it is not required.

## Part 2 · Make it yours

The 🧭 lines of `check("all")` list the settings in your files that differ from the defaults (`SYSTEM_NAME` does not count). You need **at least three**:

- at least one about **privacy** (`PUBLIC_FIELDS`) or **input checks** (`REQUIRED_FIELDS`, `CATEGORIES`, `MIN_PORTIONS`, `MAX_PORTIONS`, `REJECT_IF_HOURS_LEFT_BELOW`);
- at least one **backed by data**: a number from `semester.csv` or from your own history, and the week it came from;
- every one with a row in your decision log.

Your decision logs and your journal from Weeks 5–9 already hold candidates with evidence: choose three of them.

### Where your decisions live

| Setting | File | Week | The question it answers |
|---|---|---|---|
| `TEAM_PICKUP_MIN_PORTIONS` | `rules.py` | 4 (from 2) | When does an offer need a team instead of one volunteer? |
| `URGENT_HOURS` | `rules.py` | 4 (from 2) | How few hours left make an offer urgent? |
| `SOON_HOURS` | `rules.py` | 4 (from 2) | Up to how many hours left is an offer "soon"? |
| `REQUIRED_FIELDS` | `data_model.py` | 5 | Which fields must every offer have? |
| `CATEGORIES` | `data_model.py` | 5 | Which kinds of food do we accept? |
| `MIN_PORTIONS` | `data_model.py` | 5 | What is the smallest offer worth a trip? |
| `MAX_PORTIONS` | `data_model.py` | 5 | What is the largest offer we can carry and store? |
| `REJECT_IF_HOURS_LEFT_BELOW` | `data_model.py` | 5 | How late is too late to accept an offer? |
| `REQUIRE_APPROVAL` | `lifecycle.py` | 6 | Must a coordinator approve before pickup? |
| `LOG_EVENTS` | `storage.py` | 7 | What does the history keep (accountability against noise)? |
| `PUBLIC_FIELDS` | `report.py` | 8 | What may anyone in the canteen see (the privacy decision)? |

Change a setting in the **Files** panel: open `my_foodbridge/`, double-click the file, change the value, and save (**Ctrl+S** / **Cmd+S**).

### The decision log

One row per decision, in your `README.md`. These are the columns of your weekly decision log (*My choice · An alternative · Why I chose it · Evidence · Who is affected / the tradeoff*), with *My choice* split into the setting and its value.

| Setting (file) | My value (default) | An alternative | Why I chose it | Evidence (data / week) | Who is affected / the tradeoff |
|---|---|---|---|---|---|
| `URGENT_HOURS` (`rules.py`) | 4 (3) | `REJECT_IF_HOURS_LEFT_BELOW` = 2 | volunteers should go sooner to short-notice offers | offers with 3 h or less: 28% cancelled vs 5% (Week 9 rates) | volunteers make more urgent trips; if everything is urgent, nothing is |

**Weak:** "`URGENT_HOURS` = 4, because the data said so." **Strong:** the row above. A strong row names a specific value, a real alternative, a reason tied to people or data, the evidence (a number, your privacy table or a person's request, and the week it came from), and who gains and who loses. "It is better" is not a reason, and "the data said so" is not evidence.

## Part 3 · My extension

Choose **one** extension in Week 8 and plan it in your charter in Week 9. You may have started it already in a week's ⭐⭐ **Go further**. The rules:

- It lives in your own files, and you can explain every line.
- The kit's checks stay ✅: an extension adds to your system, it does not break a part.
- `tests.py` has **at least two tests for it that can fail**: each test checks one answer you worked out by hand, and at least one tries a boundary or an odd input.

### The menu

| Extension | Started in | Where the code goes | How you see it |
|---|---|---|---|
| **A new rule or field, with its check** | Week 5 Go further (your own input rule) · Week 6 Go further (a new state such as `returned`) | `data_model.py` (`clean_offer`) or `lifecycle.py` (`ALLOWED_MOVES`) | `bridge.show("sheet")` or `bridge.show("lifecycle")` |
| **A volunteer view** | Week 8 (who may see which field) | `report.py` (`VOLUNTEER_FIELDS`, `volunteer_row(record)`) and choice `"4"` in `app.py` | `bridge.show("app", script=["4", "q"])` |
| **A weekly summary report or chart** | Week 7 Go further (an event summary) | `report.py` (a summary function) and choice `"4"` in `app.py` | `bridge.show("app", script=["4", "q"])` |
| **The public page from Week 8** | Week 8 Go further (the public HTML page) | `screen.py`: `make_page(records)` returns your page as text | `bridge.show("screen")` |
| **A screen written by an AI, checked with a canary test** | Week 10 (reading AI code) | `screen.py`: `make_page(records)`, written by an AI from your contract | `bridge.show("screen")` |

A new choice `"4"` in `handle_choice` also needs your `MENU` line in `app.py` to mention it.

**A new rule or field.** *Example:* a contact, when it is given, must contain `"@"`; the message says *"The contact must be an email address, for example name@example.org."* Or a new state `returned`, for food a partner sends back: `"picked_up": ["delivered", "returned"]`. *How to test it:* one input that your new rule refuses (and that the old rules accepted), and one input just on the other side of the line that is still accepted. For a new state: one move that is now allowed, and one that is still not. *Watch out:* the kit's own test rows do not have your new field, so a new field must be **optional** (a missing value is fine, or gets a default). If you add it to `REQUIRED_FIELDS`, the kit's check of `clean_offer` fails.

**A volunteer view.** *Example:* `VOLUNTEER_FIELDS = ["id", "donor", "food", "portions", "hours_left", "partner"]` and `volunteer_row(record)`, which works like `public_row`. Choice `"4"` lists the open offers, most urgent first, one volunteer row each. What does a volunteer need that the public must not see? What must a volunteer still not see? *How to test it:* `volunteer_row` returns exactly your fields; the contact is not among them (if that is your decision); choice `"4"` shows an open offer and leaves out a delivered one.

**A weekly summary report or chart.** *Example:* choice `"4"` prints *"Offers: 4 · portions offered: 100 · delivered: 18 · rejected: 40 · still open: 42"*, from a function such as `summary_text(records)`; or, from your Week 7 history, how many offers were added, moved and refused. A chart is drawn from a function that returns the numbers: test the numbers, not the picture. *How to test it:* the numbers for the four sample records, worked out by hand **before** you run; and an empty list, which must give zeros, not a crash (a rate of an empty group is 0.0).

**The public page from Week 8.** *Example:* your Week 8 page code moves into `make_page(records)` in `screen.py`. It returns the page as one string, uses `public_row` from `report.py` (import it, do not copy it), uses `html.escape`, and leaves out rejected and cancelled offers. *How to test it:* a page made from a record with a contact never shows the contact; a food name with `<b>` in it shows as plain text (`&lt;b&gt;`); a rejected offer is not on the page. *Canary:* add or remove one field in `PUBLIC_FIELDS`: your page must change too. If it does not, the page copied the fields instead of using `public_row`.

**A screen written by an AI.** Give the AI a contract, not a wish:

> Write a Python file `screen.py` with one function, `make_page(records)`. It returns an HTML page as one string (a `str`). Show one row per open offer (new, approved or picked_up), most urgent first. Import `urgency` from `rules.py` and `most_urgent_first` from `report.py`, and use them. Put all imports at the top of the file. Do not write any of their numbers again. Use only the Python standard library. Never show the contact field.

Read the code before you run it: you wrote the same loop and the same `html.escape` in Week 8. Then do the **canary test**: change `URGENT_HOURS` in `rules.py` (to 10 if it is below 5, to 1 if it is 5 or more), run `bridge.show("screen")` again and see whether the page changes. If it does not, the AI copied the rule instead of importing it: ask again. Change the value back, and write what you found in your verification log. *How to test it:* a delivered offer is not on the page; the contact never appears; the offer with the fewest hours left comes first.

### Prove that a test can fail

"All tests pass" means nothing until you know the tests **can** fail. Break your extension on purpose once: remove your new `if`, add `"contact"` to your fields, or change one number. Save, run `bridge.check("all", folder="my_foodbridge")`, and see ❌. Put it back, save, run again: ✅. Both results go in your verification log.

## Part 4 · The report (`README.md`)

About two pages, in `my_foodbridge/README.md`, with these eight headings in this order. The `Final_Project.ipynb` notebook has a starter you can copy.

| Heading | What you write | Where it comes from |
|---|---|---|
| **A drawing of my system** | the people, your files, and how the data flows between them | your charter's drawing, improved |
| **What each user sees** | for each person: what they need, where they see it (a menu choice, a view, a page), and what they must **not** see; one line on how to run the system | your charter, Weeks 8–9 |
| **My decisions (decision log)** | three rows, six columns (Part 2) | your weekly decision logs and journal |
| **My extension** | what it does, for whom, why you chose it, where the code is, and how its tests work | your charter, Weeks 9–10 |
| **How I verified it (verification log)** | dated rows, five columns (below) | Week 10 labs, your own checks |
| **How I used AI and what I checked** | the tool, what you asked, what you checked and how, what you changed. No AI? Say so, and name one piece of code you checked anyway (for example the Week 10 AI tests). | your notes |
| **Two known limits** | two things your system does not do or does not know, honest and specific | your journal |
| **Reflection** | 150–250 words, written before the code freeze (prompts in the notebook) | your journal and charter |

**The drawing.** Draw on paper and take a photo, or use any drawing tool. Put the picture into your folder (for example `drawing.jpg`): upload it into `My Drive/my_foodbridge` with the Google Drive app, or drag it onto `my_foodbridge` in the **Files** panel. Show it in the report with one line: `![A drawing of my system](drawing.jpg)`. Then it travels in your zip. A drawing in text is fine too.

**The verification log** (five columns):

| Date | What I checked | How | Result | What I changed |
|---|---|---|---|---|
| 5 Dec | every part and my tests | `bridge.check("all")` | ✅ 15 parts, 6 tests, 3 decisions | my urgency test used the numbers 3 and 4; I rewrote it with `URGENT_HOURS`, so it follows my decision |

Required rows:

1. `bridge.check("all", folder="my_foodbridge")`: what it showed, and what you fixed.
2. A **clean run** (Runtime → Restart session and run all).
3. **Your extension's tests can fail**: what you broke on purpose, the ❌ you saw, and the ✅ after you put it back.
4. The **canary** (Week 10): change one constant, watch it reach the screens, change it back. For an AI screen, also the canary test of `screen.py`.
5. A **review of AI code**: the Week 10 AI tests, or code an AI wrote for you. What did you find, and what did you change?

A good log also has the **sanity checks** from Week 10 (the statuses add up to the 404 offers, every rate is between 0 and 100 %, an empty group gives 0.0).

## Part 5 · Demo day

**Your system poster** is one screen and one page: `bridge.show("gallery")` (all your views on one page) next to your drawing.

**The 3 minutes:**

| Time | What to say and show |
|---|---|
| 0:00–0:30 | **The people:** who uses your system, and what each person needs (your drawing). |
| 0:30–1:15 | **The whole system:** follow one offer from the door to the public board, file by file (your drawing and the gallery). |
| 1:15–2:00 | **Your decisions:** two of the three. The value, the alternative, who is affected. One came from the data. |
| 2:00–2:45 | **Your extension:** show it working, and name the test that would catch a bug in it. |
| 2:45–3:00 | **One limit,** and your next step. |

**The live change (about 2 minutes):** the instructor asks for one small change, for example a setting you did **not** change, or a small change to your extension. You say which file and which name, **predict** what will change (and what will not), edit the file in the **Files** panel, save, run, and explain any difference from your prediction. Then you change it back.

**One question (about 1 minute):** about any line, test or decision in your folder.

In a large class you give your 3 minutes to a small group of classmates first. At the instructor's desk you then give a 1-minute tour of your poster before the live change and the question.

**Before your turn:** the setup cell of your Final notebook has run; the **Files** panel is open at `my_foodbridge/`; this cell is ready to run:

```python
bridge.check("all", folder="my_foodbridge")
bridge.show("app", script=["1", "3", "q"])
```

**Two example requests:**

- *"Hide the category from the public."* → `PUBLIC_FIELDS` in `report.py`: the category column disappears from the public board (choice 3), and from your public page if you made one.
- *"Urgent means one hour more than now."* → `URGENT_HOURS` in `rules.py`: from 3 to 4, F004 turns from soon to urgent; your tests, written with the constant, still pass. If one fails, it has a raw number in it (Week 4): which line?

## What you hand in

1. **Your `my_foodbridge/` folder as a zip**, with your `.py` files (`rules`, `records`, `data_model`, `lifecycle`, `storage`, `report`, `app`, and `screen` if your extension made one), `tests.py`, `README.md`, your drawing, and `saved/offers.json`. No slides are needed.
2. Nothing else: the report, with its reflection, is the `README.md` inside the zip. This is your one submission.

**Deadline: Week 10, Session 2, minute 45 (code freeze).** Email the zip to [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com). The file name and the subject line are announced in class (for example `Final_<StudentID>.zip`). After the freeze you present the folder you submitted.

## Marks (proposed)

The Final project is **30% of the course**. The points below are **proposed** and await university confirmation.

| What is assessed | Points (of 100) | Full marks look like |
|---|---:|---|
| **1 · It runs** | 25 | Every part you wrote is ✅, your menu works, your zip has `README.md`, `tests.py` and `saved/offers.json`, no ⚠️ |
| **2 · Make it yours: decisions with evidence** | 20 | Three changed settings (🧭), one on privacy or input checks, one backed by a number; each log row specific: value, real alternative, reason, evidence, who is affected |
| **3 · My extension and its tests** | 20 | The extension works and shows in its view; at least two tests for it that pass and can fail (you proved it); your Week 10 tests use your constants |
| **4 · The report** | 15 | All eight headings; a clear drawing; what each user sees; dated verification rows; honest AI use and limits; a real reflection |
| **5 · Demo day** | 20 | You explain the system as a whole with your poster, make the live change with a prediction and explain the result, and answer the question in your own words |

**Minimum to pass the Final:** all five parts handed in or done: the system runs, three decisions with log rows, an extension with two tests, a report with the eight headings, and your Demo-day turn.

## AI and integrity

- You may use an AI assistant in the Final project. Write in your report what it wrote and how you checked it.
- You must be able to explain **every line** you hand in. At Demo day, the instructor may ask about any test, setting or line of your extension. Work you cannot explain is marked only as far as you can explain it.
- Share ideas and help classmates; do not share files or complete answers. Two students may choose the same extension; each one writes and explains their own.
- See [assessment](ASSESSMENT.md) for the course rules on AI tools and fairness.
