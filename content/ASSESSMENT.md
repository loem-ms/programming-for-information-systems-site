# Proposed assessment and final project

The course assesses what you can **build, test, explain and hand over**. Both team work and individual understanding matter. The weighting below is the **proposed assessment plan**; the instructor will confirm it with the university before assessment begins. Send private submissions and personal course questions to [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com). Calendar deadlines and the exact file-naming rule will be announced before the work is due.

## Proposed assessment structure

| Component | Weight | Evidence |
|---|---:|---|
| Participation and attendance | 10% | Announced attendance evidence, active participation and short weekly reflection |
| Six individual research assignments | 30% | Six submissions worth 5% each, with sources, a concrete example and the student's reasoning |
| Individual midterm | 30% | Week 4 planning function, four independently expected tests and an explanation |
| Final project | 30% | Baseline reproduction, completed notes, verification, handoff and individual understanding |
| **Total** | **100%** | |

The exact attendance calculation, assessment dates, permitted resources, and final-project rubric split still require confirmation. They will be announced before they apply.

## Six research assignments: 30%

Each assignment is worth 5%. See the [research assignment guide](RESEARCH_ASSIGNMENTS.md) for the six topics, schedule, evidence and proposed rubric. Normal full marks do not require a presentation.

Research Assignment 2 is shared in Week 3. No research submission or presentation is due during the Week 4 midterm week; Research Assignment 3 is released after the midterm. Research Assignment 6 closes at the start of Week 8 before the project-proposal work. Weeks 9–10 have no research obligation.

AI is encouraged as an optional research aid. When AI is used, the student investigates the topic, discusses it with the tool through follow-up questions or challenges, and then submits their own understanding and reasoning. Evidence may be an accessible conversation link, screenshots or relevant excerpts, together with cited sources. A non-user can earn the same full marks by citing sources and providing the required reasoning. No paid tool is required.

Volunteers may later receive a small capped bonus for sharing useful research, but the exact bonus has not been decided. It will only be announced with an equitable opportunity plan.

### Common criteria for each Research task

The following proposed criteria apply to all six tasks. They do not prescribe a response template or page count.

| Criterion | Points |
|---|---:|
| Relevant topic and sources | 1 |
| Accurate explanation in your own words | 1 |
| Concrete example | 1 |
| Reasoning and a limitation or remaining question | 1 |
| Clear sources and evidence, including AI discussion evidence if used | 1 |
| Total | 5 |

## Individual midterm: 30%

Status: **detailed proposal, not yet a final calendar announcement**. The midterm focuses on basic Python from Weeks 1–4.

Complete `summarize_request(lines, reviewed)` using valid supplied dictionaries. Use a loop to return total containers, planned portions and one label. An unreviewed request returns `hold`. A reviewed request below 20 planned portions returns `standard`. A reviewed request at or above 20 returns `team`.

Each input line has this shape:

```python
{"batch_id": "DEMO", "containers": 2, "portions_per_container": 3}
```

Return exactly the fields `total_containers`, `planned_portions` and `coordination_label`. For the single reviewed example above, the expected result is `2`, `6`, `standard`. Inputs are supplied valid; parsing, databases and a web interface are outside this task.

### Do this in order

1. Open `Week_04.ipynb` and read **Midterm begins** in Session 2.
2. Fill in `summarize_request(lines, reviewed)` in the marked code cell. Use a loop to calculate both totals, then choose the label using the review-first rule.
3. Run cases A–D below. For every case, compare all three returned fields with the expected values. Fix the first difference you find.
4. Save the function in `midterm.py`, the four checks in `test_midterm.py`, and the run instructions/disclosure in `README.md`.
5. Put the three files in one ZIP. Extract it into a fresh folder and follow only your README to verify it works.
6. Keep the ZIP and backup, email [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com), and prepare to explain one case in your individual slot.

### Common minimum tests

| Case | Input | Expected result |
|---|---|---|
| A: review gate | `4 × 5`, not reviewed | 4 containers, 20 portions, `hold` |
| B: below threshold | `3 × 3`, reviewed | 3 containers, 9 portions, `standard` |
| C: equality | `4 × 5`, reviewed | 4 containers, 20 portions, `team` |
| D: multi-line | `2 × 3` and `4 × 4`, reviewed | 6 containers, 22 portions, `team` |

Assert all three returned fields for every case.

### ZIP and README

Submit one ZIP containing:

```text
student-id_midterm.zip
├── README.md
├── midterm.py
└── test_midterm.py
```

The README must let a third party understand and run the work. Include the purpose, Python version, exact run and test commands, expected output for one case, the loop and review-first rule, one limitation, and the AI-use disclosure. Extract the ZIP into a fresh folder and test it before submission.

### Midterm AI policy

AI may help with planning, implementation choices, code ideas, review, test design, debugging, fixes and README wording. In the README, either state **“I did not use AI for this assignment”** or list the stages where it helped, the tool name, one help request and one suggestion you accepted, changed or rejected with your reason.

AI use or non-use does not itself change the mark. Every student must run and explain their own program, trace a required case and answer a question about a choice or small change.

### Proposed 30-point rubric

| Criterion | Points |
|---|---:|
| Python totals and units | 6 |
| Review-first coordination rule | 6 |
| Four common tests | 6 |
| Program structure and readability | 4 |
| README and ZIP reproducibility | 4 |
| Individual explanation | 3 |
| Honest AI-use disclosure | 1 |
| **Total** | **30** |

Full standard marks do not require AI or optional refactoring. A small capped bonus may later be offered for identifying and improving a visible, working-but-improvable design while preserving the tests. The bonus value and fairness rule are **not decided**.

Week 4 includes functions and guided practice followed by the Midterm. Detailed main/import work and the 16-boundary exercise are optional rehearsal. Individual explanations and calendar dates will be announced. Send submissions to [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com). Prepare Research 3 after the Midterm and keep a backup.

## Final project: 30%

### Required minimum: reproduce and explain

You may complete the final project **without changing any program code**. Reproduce the supplied Food Rescue system, compare the observed results with the supplied expectations, and complete every requested response/note in your own words. Keep your predictions, observations, explanations, peer/run evidence and handoff instructions. Running all cells without completing the notes is not the full submission.

Use the small planning example first: input counts → `plan_pickup(...)` → returned portions and label → printed output. Bread has 2 declared portions/container; rice has 5. Then run the supplied full baseline and its tests. Do not rebuild the database engine or the interface.

### Where to work

| When | Required minimum | Optional if you have time |
|---|---|---|
| Week 8 | Identify the baseline input, processing and output; predict two results | Suggest one coordinator improvement |
| Week 9 | Reproduce the supplied system, compare results and fill the notes; ask a peer to follow the run steps | Propose or implement an approved small change |
| Week 10, Session 1 | Rehearse from clean inputs and check the run guide | Refine an optional change |
| Week 10, Session 2 | Demonstrate the baseline and let a peer reproduce it | Show the optional improvement separately |
| Week 10, Session 3 | Explain or trace a result independently and finish the requested writing | Explain an optional code change |

### Optional improvements and notebook form

If you have time, you may propose an improvement, rewrite a small part or implement an approved change. Explain what you changed, why, and its expected/observed results. Keep the unchanged baseline for comparison. Proposing an idea does not oblige you to implement it. No extra feature or UI is required for standard completion, and no bonus points are promised.

Week 5 introduces libraries and a supplied `ipywidgets` form. The final notebook can use the same form pattern to call the same planning function. The form is off by default. If it is absent, blank, displayed as text or unresponsive, use ordinary input cells and printed output. No server, package installation, paid AI, key or GPU is needed for the required route. UI appearance and callback code are not assessed.

### What to show and submit

1. **Reproduction:** start from known data and follow the supplied run order. Show the real outputs and test results.
2. **Understanding:** identify an input, the processing step and the output. Explain units, human review and one failure/boundary case.
3. **Written responses:** complete every requested response/note. Record predictions, observations and an honest explanation of any mismatch or limitation.
4. **Peer and handoff evidence:** give another learner the run guide, record what happened and clarify confusing instructions if needed. A successful repeat with no code revision is valid evidence.
5. **Optional work:** clearly separate any improvement proposal or changed code from the reproduced baseline. If none, say “No code change” where the notebook asks.

The canonical full fixture has 94 offered, 60 reserved, 42 collected and 29 delivered planned portions. These are overlapping lifecycle measures, not values to add together or counts of distinct people served. Preserve human review, declared units, atomic reservations and event evidence.

The proposed final weight remains 30%. The numeric split, calendar dates, team arrangements and exact file-naming rule will be announced before they apply. The minimum does not require an implemented improvement. Each student must understand and explain the submitted results.

Send the notebook/program copy, required fictional inputs, completed notes, run guide and evidence to [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com). Keep a separate backup. Do not post completed assessment work in GitHub Issues. A separate slide deck is not required.

Research 6 closes at the start of Week 8. Weeks 9–10 have no new research obligation. Optional AI suggestions must be inspected, tested and understood; no AI tool is required.
