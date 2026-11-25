# Final project · Your FoodBridge system

Your Final project is **your own `my_foodbridge/` folder**: the files you wrote from Week 4 to Week 10, finished, verified and presented. You do not start a new notebook. You keep building what you have, make your own decisions in it, prove that it works, and explain it to the instructor at Demo day.

The [`Final_Project.ipynb`](notebooks/Final_Project.ipynb) notebook only helps you **check, pack and present** your folder. It never changes your files.

*Campus FoodBridge is fictional. All organisations, people and numbers are invented.*

## Four levels

| Level | You pass it when … | |
|---|---|---|
| **L1 · It runs** | `bridge.check("all", folder="my_foodbridge")` shows ✅ for your parts, including `handle_choice`; there is no ⚠️ file problem; `bridge.show("app", script=["1", "2", "3", "q"])` shows your menu working. Running `python app.py` in a terminal is optional. | ⭐ required |
| **L2 · Make it yours** | The 🧭 list in `check("all")` shows **at least three settings you changed** from the defaults (`SYSTEM_NAME` does not count). At least one is about **privacy** (`PUBLIC_FIELDS`) or **input checks** (`REQUIRED_FIELDS`, `CATEGORIES`, `MIN_PORTIONS`, `MAX_PORTIONS`, `REJECT_IF_HOURS_LEFT_BELOW`). **At least one is backed by data**: a number from `semester.csv` or from your own Week 7 `history.jsonl`. All three have a row in your decision log. | ⭐ required |
| **L3 · Extend** | A new rule, field or report (for example a rejection rate, a choice `4` in your menu, one more check at the door), with **at least two tests that can fail** in `tests.py`. The kit's checks stay ✅. | ⭐⭐ optional |
| **L4 · A screen** | Your Week 8 `public_board.html` grows into a file: an AI writes **only** `screen.py` with `make_page(records)`, from your contract. You check it with a **canary test** and write the result in your verification log. | ⭐⭐ optional |

Levels 3 and 4 have no marks of their own. A Level 3 test counts in *your own tests*; a Level 4 canary counts in the *verification log*. Full marks are possible with Levels 1 and 2 and the required parts only.

Parts you did not write are replaced by the kit's model version (📦), so your system always runs. Your marks come from what **you** wrote and decided.

## Where your decisions live

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

Change a setting in the **Files** panel: open `my_foodbridge/`, double-click the file, change the value, save. Do not run an old week's `%%writefile` cell again: it replaces the whole file and your decision is lost.

## The decision log

One row per decision, in your `README.md`. Your decision logs from Weeks 5–9 already hold candidates with evidence: choose three from them.

| Setting (file) | My value (default) | An alternative | Why I chose it | Evidence (data / week) | Who is affected / the tradeoff |
|---|---|---|---|---|---|
| `URGENT_HOURS` (`rules.py`) | 4 (3) | `REJECT_IF_HOURS_LEFT_BELOW` = 2 | volunteers should go sooner to short-notice offers | offers with 3 h or less: 28% cancelled vs 5% (Week 9 `cancel_rate`) | volunteers make more urgent trips; if everything is urgent, nothing is |

**Weak:** "`URGENT_HOURS` = 4, because the data said so." **Strong:** the row above. A strong row names a specific value, a real alternative, a reason tied to people or data, the evidence (a number, your 🔐 matrix or a person's request, and the week it came from), and who gains and who loses. "It is better" is not a reason, and "the data said so" is not evidence.

## The verification log

| Date | What I checked | How | Result | What I changed |
|---|---|---|---|---|
| 5 Dec | every part and my tests | `bridge.check("all")` | ✅ 15 parts, 4 tests, 3 decisions | my urgency test still used 3 and 4; I changed it to my value |

Required rows:

1. `bridge.check("all", folder="my_foodbridge")`: what it showed, and what you fixed.
2. A **clean run** (Runtime → Restart session and run all).
3. A **review of AI code**: the Week 10 Version A tests, or code an AI wrote for you. What did you find, and what did you change?
4. The **canary drill** (Week 10, Lab 2): change one constant, watch it reach the screens, change it back. If you did Level 4, also the canary test of `screen.py`.

A good log also has the **sanity checks** from Week 10 (the statuses add up to the 404 offers, every rate is between 0 and 100 %, an empty group gives 0.0).

## What you hand in

1. **Your `my_foodbridge/` folder as a zip**, with your `.py` files (`rules`, `records`, `data_model`, `lifecycle`, `storage`, `report`, `app`), `tests.py`, `README.md`, `saved/offers.json`, and `screen.py` if you did Level 4. No slides are needed.
2. Your **`README.md`** has five sections: *What it does* · *How to run it* (steps, each with what you should see) · *My decisions* (the decision log) · *How I verified it* (the verification log) · *Known limits*.

**Deadline: Week 10, Session 2, minute 45 (code freeze).** Email the zip to [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com). The file name and subject line are announced in class (for example `Final_<StudentID>.zip`). After the freeze you present the folder you submitted.

## Schedule

| When | What | In class or at home |
|---|---|---|
| Week 9, Session 3 | `app.py` passes its check (L1); one decision from the semester data; the Final explained; a plan for your three decisions | class |
| Week 9 → Week 10 (one week) | Make your three decisions in the files; draft the decision log (6 columns) and the README; optional L3 or L4 (about 2.5–3 hours) | home |
| Week 10, Session 1 | `tests.py`, `check("all")`, tests that pin your decisions, the verification lab (sanity checks, canary, clean run) | class |
| Week 10, Session 2, first half (45 min) | Review AI tests, finish the README, a last clean run, **submit the zip: code freeze at minute 45** | class |
| Week 10, Session 2 second half and Session 3 | **Demo day:** pod demos, the instructor's booth, the showcase, the final reflection | class |

## Demo day

**Pod demo (3 minutes, to your pod of about four classmates):**

| Part | Time | What to say and show |
|---|---|---|
| 1 · The people and the problem | 0:30 | Who uses your system? What goes wrong for them without it? |
| 2 · My decisions | 0:45 | Two or three settings: the value, the alternative, who is affected. One came from the data. |
| 3 · Live demo | 0:45 | `bridge.show("gallery")` or your menu, plus one chart from your Week 9 analysis. Show one thing your decisions changed. |
| 4 · How I verified it | 0:30 | One test and the bug it catches; your clean run; one thing you found in AI code. |
| 5 · One limit | 0:30 | What your system does not do, and the next step. |

Then one minute of questions, and each listener fills in a peer card (one strength, one question).

**The booth (3 minutes, with the instructor):**

1. **Show and explain (0:45):** one output that your decisions changed (`show("app")`, `show("sheet")` or `show("board")`), and one row of your decision log in your own words.
2. **Live change (1:45):** the instructor picks a card with a setting you did **not** change. You say which file and setting, **predict** what will change (and what will not), edit the file in the Files panel, save, run, and explain any difference from your prediction.
3. **Undo (0:30):** you change it back.

**Before you go to the booth:** the setup cell of your Week 10 or Final notebook has run; the **Files** panel is open at `my_foodbridge/`; this cell is ready to run:

```python
bridge.check("all", folder="my_foodbridge")
bridge.show("app", script=["1", "3", "q"])
```

**Two example cards:**

- *"Hide the category from the public."* → `PUBLIC_FIELDS` in `report.py`: the category column disappears from the public board (choice 3).
- *"Urgent means one hour more than now."* → `URGENT_HOURS` in `rules.py`: from 3 to 4, F004 turns from soon to urgent, and a test that pins 3 hours now fails. Can you say why that failing test is good news?

## Marks (proposed)

The Final project is **30% of the course**. The weights are proposed and await university confirmation.

| What is assessed | Points (of 100) | Full marks look like |
|---|---:|---|
| **A · It runs (Level 1)** | 25 | Every part you wrote is ✅, your menu works, your zip has `README.md`, `tests.py` and `saved/offers.json`, no ⚠️ |
| **B · Your decisions (Level 2)** | 25 | Three changed settings (🧭), one on privacy or input checks, at least one backed by a number, and each log row specific: value, real alternative, reason, evidence, who is affected |
| **C · Your own tests** | 15 | Four or more passing tests in `tests.py`; at least two pin **your** values; normal, both sides of an edge and an odd case; expected values from the contract |
| **D · Verification log and README** | 15 | Dated rows for the check, the clean run, the AI review and the canary; a stranger can run your system from the README; honest known limits |
| **E · Demo day: the booth** | 20 | You explain a decision (6), find where a change lives (4), predict its effect (4), make it and explain the result (6) |

**Minimum to pass the Final:** Levels 1 and 2, a README with both logs, and a visit to the booth. A short system with strong, well-explained decisions scores higher than a long one with weak reasons.

## Ideas for Level 3

- An analysis function such as `rejection_rate(records, category)`, built on your Week 9 `rate`, with tests: a normal case, the whole group (100 %), an empty group (0.0).
- A choice `4` in your menu: portions by status, from your own `portions_by_status`.
- One more check at the door in `clean_offer`, with a clear message (for example, a donor name that is only spaces).
- A volunteer view: `VOLUNTEER_FIELDS` and `volunteer_row(record)` in `report.py`. What does a volunteer need that the public must not see?

Every idea needs at least two tests that can fail, and the kit's checks must stay ✅.

## Level 4 · a screen

Give the AI a contract, not a wish:

> Write a Python file `screen.py` with one function, `make_page(records)`. It returns an HTML page as one string (a `str`). Show one row per open offer (new, approved or picked_up), most urgent first. Import `urgency` from `rules.py` and `most_urgent_first` from `report.py`, and use them. Put all imports at the top of the file. Do not write any of their numbers again. Use only the Python standard library. Never show the contact field.

Read the code before you run it: you wrote the same loop and the same `html.escape` in Week 8. Then do the **canary test**: change `URGENT_HOURS` in `rules.py` (to 10 if it is below 5, to 1 if it is 5 or more), run `bridge.show("screen")` again and see whether the page changes. If it does not, the AI copied the rule instead of importing it: ask again. Change the value back, and write what you found in your verification log.

## AI and integrity

- You may use an AI assistant in the Final project. Write in your verification log what it wrote and how you checked it.
- You must be able to explain **every line** you hand in. At the booth, the instructor may ask about any test, setting or extension. Work you cannot explain is marked only as far as you can explain it.
- Share ideas and help classmates; do not share files or complete answers.
- See [assessment](ASSESSMENT.md) for the course rules on AI tools and fairness.
