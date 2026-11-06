# Proposed assessment and final project

The course assesses what you can **build, test, explain and hand over**. Both team work and individual understanding matter. The weighting below is the **proposed assessment plan**; the instructor will confirm it with the university before assessment begins. Calendar deadlines, the approved private submission route and the exact file-naming rule will be announced before the work is due.

## Proposed assessment structure

| Component | Weight | Evidence |
|---|---:|---|
| Participation and attendance | 10% | Announced attendance evidence, active participation and short weekly reflection |
| Six individual research assignments | 30% | Six submissions worth 5% each, with sources, a concrete example and the student's reasoning |
| Individual midterm | 30% | Week 4 planning function, four independently expected tests and an explanation |
| Final project | 30% | Scoped improvement, verification, peer evidence, handoff and individual understanding |
| **Total** | **100%** | |

The exact attendance calculation, assessment dates, permitted resources, final-project rubric split and approved private submission route still require confirmation. They will be announced before they apply.

## Six research assignments: 30%

Each assignment is worth 5%. See the [research assignment guide](RESEARCH_ASSIGNMENTS.md) for the six topics, schedule, evidence and proposed rubric. Normal full marks do not require a presentation.

Research Assignment 2 is shared in Week 3. No research submission or presentation is due during the Week 4 midterm week; Research Assignment 3 is released after the midterm. Research Assignment 6 closes at the start of Week 8 before the project-proposal work. Weeks 9–10 have no research obligation.

AI is encouraged as an optional research aid. When AI is used, the student investigates the topic, discusses it with the tool through follow-up questions or challenges, and then submits their own understanding and reasoning. Evidence may be an accessible conversation link, screenshots or relevant excerpts, together with cited sources. A non-user can earn the same full marks by citing sources and providing the required reasoning. No paid tool is required.

Volunteers may later receive a small capped bonus for sharing useful research, but the exact bonus has not been decided. It will only be announced with an equitable opportunity plan.

## Individual midterm: 30%

Status: **detailed proposal, not yet a final calendar announcement**. The midterm focuses on basic Python from Weeks 1–4.

Complete `summarize_request(lines, reviewed)` using valid supplied dictionaries. Use a loop to return total containers, planned portions and one label. An unreviewed request returns `hold`. A reviewed request below 20 planned portions returns `standard`. A reviewed request at or above 20 returns `team`.

Each input line has this shape:

```python
{"batch_id": "DEMO", "containers": 2, "portions_per_container": 3}
```

Return exactly the fields `total_containers`, `planned_portions` and `coordination_label`. For the single reviewed example above, the expected result is `2`, `6`, `standard`. Inputs are supplied valid; parsing, databases and a web interface are outside this task.

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

Week 4 protects its final **135 minutes** for the Midterm: the last 45 minutes of Session 2 and all of Session 3. Budget **90 minutes implementation + 30 minutes tests/README/ZIP + 15 minutes review and hand-in**. The first 135 minutes are for functions and guided practice. Detailed main/import work and the 16-boundary exercise are optional rehearsal. The five-minute individual explanation is scheduled according to cohort size and examiner capacity; the final 15 minutes do not guarantee an oral slot for every student. Calendar dates and the private submission route remain to be announced. Outside class, Week 4 requires only the 15–20-minute Research 3 preparation after the Midterm and keeping a backup.

## Final project: 30%

### One useful improvement

Improve the supplied Campus Food Rescue Python/SQLite system for a concrete stakeholder need. Keep the change small enough to test convincingly. Examples include a clearer pending-collection report, better handling of incomplete donor proposals, or a more useful handoff step. The team chooses and justifies its own approved scope.

A complete web app, polished UI, paid AI integration or live food-rescue operation is **not required**. A reliable Python or SQL improvement with clear evidence is a valid project. Preserve the course rules: human review, explicit units, atomic reservation and distinct collection/delivery records.

| When | What you do | What you keep |
|---|---|---|
| Week 8 | Each student pitches a stakeholder need in a small group; the team selects a feasible improvement | Need, scope and at least two acceptance cases |
| Week 9 | Freeze expected outcomes, implement the change, exchange a peer test and revise | Code, acceptance/regression evidence, peer finding and retest |
| Week 10, Session 1 | Rehearse from clean inputs and exchange run instructions | A guide another person can follow |
| Week 10, Session 2 | Present the baseline and improvement; a peer operator tries an unseen input and asks a coordinator question | Demonstration and acceptance evidence |
| Week 10, Session 3 | Independently trace a result or make a small approved change | Your own explanation of a judgment, test and revision |

For larger classes, the timetable uses parallel demonstration stations with role reversal. The instructor will announce the calendar date and each team's allocation; the 50-minute station block is not a promised presentation length for every team.

## What to show in the final demonstration

Use this sequence as a guide; explain the work in your own words.

1. **Need:** who needs the improvement, and what decision is difficult now?
2. **Scope:** what did you change, and what remains outside scope?
3. **Working result:** start from known data and run the actual program or notebook.
4. **Evidence:** show the acceptance cases, one unaffected regression case and a boundary or failure case. Compare expected and observed results.
5. **Revision:** explain a peer finding, the resulting change and the retest.
6. **Handoff:** give the next operator the files, run instructions, expected observations and an honest limitation or recovery step.

Every member should understand the team's result and be ready to explain their own contribution. A successful demonstration is not enough if another person cannot reproduce it. Slides can support the explanation; the course does not require a particular slide count or presentation software.

## Submission and questions

Keep a notebook/program copy, required fictional inputs, run instructions, tests and review evidence, plus a separate backup. The instructor will announce the private submission route and file-naming rule before work is due. Use that route for your completed work. The class repository's Issues are for questions and small reproducible examples, not complete assessment solutions or individual grades.

Research Assignment 6 is discussed at the start of Week 8 before the project-proposal work. There is no new research assignment in Week 8 and no research obligation in Weeks 9 or 10, so those weeks can focus on project scope, implementation, peer verification and handoff.

If you use a code suggestion from another person or a tool, inspect it, test it and be able to explain it. Optional AI use is not required for assessment. Ask about an unclear rule early through [GitHub Issues](CONTRIBUTING.md) or the private course contact route when the question concerns your own assessed work.
