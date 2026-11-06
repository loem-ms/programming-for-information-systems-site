# Programming for Information Systems — Course overview

**Campus Food Rescue · A project-based learning course**

[Open the illustrated PDF overview](/slides/Course_Overview.pdf)

![Three scenes at a fictional Cambodian university: a donor asks how many portions each box contains; volunteers ask whether another team reserved a pickup; a community partner checks what was offered, collected and delivered.](/assets/illustrations/campus_food_rescue_story.png)

*One coordination project, three questions: what is being offered, who is collecting it, and what actually happened?*

## The situation we will work on

A volunteer team at a fictional Cambodian university helps nearby food businesses coordinate surplus-food collections with community partners. A bakery messages “four boxes available”, but the team needs to know what a box contains. Two volunteers may try to reserve the same pickup. At the end of the day, the coordinator needs to distinguish a promising offer from a completed delivery.

**You are the team building the information system behind this work.** Start with a declared container count and portions per container. Build a clear pickup plan, record a coordinator's review decision, reserve availability reliably and make reports traceable to actual recorded events. Later, propose an improvement that another volunteer can operate and verify.

All organizations, messages, quantities and approvals are invented for learning. Human coordinators decide food suitability, collection arrangements and partner allocation. The code records those decisions; a Boolean flag or successful calculation does not certify food safety. A “portion” is a declared planning estimate, not a nutritional measure or a count of unique people served.

The pictured ready-to-collect arrangement assumes that human review has already happened. The course also examines offers that are incomplete, unreviewed, cancelled or never collected.

![The course progresses from planning a pickup, through reliable records and reservations, to stage reports, an improvement and handoff. Each week repeats ask, predict, code, check and revise.](/assets/diagrams/course_overview.svg)

## The system we are designing and developing

**A pickup coordination application for the university coordinator**, implemented with Python and SQLite. Its operations are accessible through the supplied notebooks or scripts. The conceptual interface in the PDF makes those operations visible; a browser interface is not a required deliverable.

The PDF first shows a dashboard-style concept view: stage totals at the top, available offers on the left, a pickup draft in the center, and status/follow-up on the right. Week labels connect each capability to the lessons that develop it. Weeks 9–10 improve and verify a selected capability. The displayed snapshot and an unsubmitted draft are kept distinct.

The coordinator can inspect reviewed offers, select batch quantities for a pickup, calculate the plan, reserve all its lines together, record collection and delivery, and inspect reports or pending work. A donor-import/review queue preserves uncertain source information before it can become reviewed availability. Batch IDs and pickup IDs connect these operations to the same saved records.

For a miniature example, start with five bread containers at two declared portions each and two rice containers at five portions each. A reviewed request for three bread containers and one rice container totals four containers and eleven planned portions. Reserving it leaves two bread containers and one rice container available. Later collection and delivery events update the pickup status without subtracting those quantities again. The coordinator can answer “Which accepted pickups still lack a collection record?” from those same records.

| Inside the application | Supplied by people or the physical world |
|---|---|
| Calculations, validation and coordination labels | Meaning of a container and the donor's declaration |
| Atomic reservation and saved records | Coordinator approval of suitability and arrangements |
| Collection/delivery event records and reports | Actual collection, transport and partner handoff |

## The story's essential distinctions

| Record or measure | What it means | What it does not establish |
|---|---|---|
| Donor proposal | A message or imported row to clarify and review | Reservable availability |
| Reviewed offer batch | Declared containers available under a human-reviewed arrangement | A collection or delivery |
| Pickup plan | Proposed batch lines and calculated planned portions | An operational reservation |
| Reservation | A complete accepted commitment that reduces reservable availability | Physical movement of food |
| Collection event | The accepted pickup was recorded as collected | Delivery to the partner |
| Delivery event | Delivery was explicitly recorded after collection | Unique people served or nutritional benefit |

These stages overlap. Do not add offered, reserved, collected and delivered totals together as if they were different food. Explain the unit, source and stage behind each number.

## What you will learn

By the end, you should be able to:

- Use variables, types, operators, conditions, collections, loops and functions to solve small programming problems.
- Turn a stakeholder request into an explicit rule and independently expected test cases.
- Run `.py` files, explain `main()` and imports, accept command arguments and run tests outside a notebook.
- Distinguish classes, instances, attributes and methods, and choose when a dictionary or function is sufficient.
- Validate input, read errors and handle expected failures without concealing partial changes.
- Store and query linked SQLite records, preserve historical facts and explain transaction boundaries.
- Reconcile stage reports and distinguish authored service output from verified workflow evidence.
- Implement a scoped improvement, respond to peer testing and hand it over with clear instructions.

## The weekly route

| Week | Team's question | Programming and systems skills | Evidence |
|---|---|---|---|
| 1: A first plan | How many portions do these declared containers represent? | Notebook and `.py` execution, variables, types, arithmetic, strings and output | A labelled planning result and a question about an unclear unit |
| 2: Review and dispatch | Which requests need review, standard coordination or a team pickup? | Comparisons, Boolean logic, conditions and boundary cases | A decision table and checked outputs |
| 3: Multi-batch pickups | How do we combine several offer lines without losing their meaning? | Lists, dictionaries, loops and accumulators | Line/container/portion totals and a hand trace |
| 4: Functions and Midterm | Can you calculate, return, test and explain a result? | Functions, arguments, return values, loops, assertions and debugging | Canonical Midterm function, four tests and a reproducible ZIP |
| 5: Donor data | How do we validate rows and explain their outcomes? | CSV, conversion, validation and audit; supplied duplicate grouping | Every source record has a justified disposition |
| 6: Saved plans | Can the next volunteer retrieve the same plan tomorrow? | Objects and methods; SQLite, identifiers, relationships, parameters and persistence | A saved plan with historical line facts |
| 7: Reliable reservations | What if availability runs out halfway through a pickup request? | Transactions, guarded updates, exception boundaries, snapshots and test discovery | Complete success or unchanged state after failure |
| 8: Reports and intake | What was offered, reserved, collected and delivered—and what still needs review? | SQL aggregation, reconciliation, HTTP, JSON, validation and review queues | Stage evidence, six intake outcomes and a project proposal |
| 9: Your improvement | Which small change helps a volunteer or partner make a decision? | Acceptance criteria, scoped implementation, regression tests and peer review | A working change and a justified revision |
| 10: Handoff | Can another volunteer run the system and explain its records? | Clean starts, commands, operating instructions and independent verification | A reproducible handoff and individual evidence |

For the initial classroom policy, an unreviewed request is held. A reviewed request with at least 20 planned portions uses team coordination; smaller reviewed requests use standard coordination. The number 20 is an invented workload threshold. It does not decide food suitability or recipient priority. Students test both sides of the threshold and the equality case.

## How a Saturday works

Each Saturday has three 90-minute sessions. Breaks sit outside the 45 contact hours.

| Session | Typical activities | Purpose |
|---|---|---|
| 1: Python foundations | Explain the week's Python concept, syntax and execution behavior; trace short examples | Understand programming before applying it to the project |
| 2: Hands-on practice | Use the exercises in the same weekly notebook; predict, run, change and explain | Consolidate the same Python skills |
| 3: Project studio | Brief design discussion, then implementation, peer checks and reflection | Build and verify a component of the final system |

An ordinary Session 3 reserves about 10 minutes for design, 55 for implementation/thinking, 15 for peer checks and 10 for reflection. Week 4 reserves its final 135 minutes for the Midterm (90 implementation, 30 tests/package, 15 review/hand-in); Week 10 preserves individual verification time; Week 8 includes actual local HTTP evidence and project proposals. Weekly notebooks and slides follow the same three-session route.

## Programming foundations alongside the case

The companion [Python Basics](learning_materials/Python_Basics.ipynb) notebook is an optional quick lookup: 19 short topics with syntax, a small example and common cautions. It covers execution, values, conditions, collections, loops, functions, errors, tests, files, JSON, SQLite, saved programs, imports, command arguments and objects.

All required explanations, demonstrations and Python exercises are in the weekly notebook. Students follow Start → Session 1 → Session 2 → Session 3 → Finish without changing notebooks for the core lesson. Python Basics has no separate weekly task stream or long solution section.

The execution route begins with a saved planning file in Week 1, introduces reusable functions in Week 4 (main/import detail is optional rehearsal), optional command-argument exploration in Week 5, objects and persistence in Week 6, and independent tests from Week 7. Classes are one representation choice; students are not required to redesign the entire system around inheritance or a large object hierarchy.

## Reading and learning independently

First read the [weekly learning path](LEARNING_PATH.md). It identifies the required evidence, supplied infrastructure, optional extensions and a realistic outside-class time. The stop point is simple: save the required evidence and make sure you can explain it. You do not need to finish every reference example.

1. Start in the weekly notebook with the Python topic, syntax and local examples; use Python Basics only for optional lookup.
2. Read the explanation and diagram, then predict the small example before running it. In the project studio, identify whose decision the result supports.
3. Trace the result, change one input and explain what changes and what remains true.
4. Complete the marked student task using the supplied starter and reference sections.
5. Check a normal case, boundary case and relevant invalid or failure case. Compare state as well as output.
6. Record your decision, observed evidence and revision; prepare the next research assignment when one is scheduled.

Each week supplies its own starting data. An unfinished previous notebook does not prevent participation. Complete examples are separate from intentional bugs or unfinished lab operations; running an untouched starter is not completion of the task.

## Questions and research

Ask questions during or after class. Once the course repository is announced, use its **GitHub Issues** for shared technical questions; until then, keep a local note or use the separately announced class route. Search existing questions, then include the week, a small input, your expectation and what happened. Follow the [question guide](CONTRIBUTING.md). Questions about donor messages, coordination rules and setup are all welcome; keep assessed submissions and personal attendance concerns in the private course route.

The course has six individual research assignments, worth a proposed 5% each. They are assigned in Weeks 1, 2, 4, 5, 6 and 7, then discussed in Weeks 2, 3, 5, 6, 7 and 8. Research Assignment 2 is shared in Week 3. Week 4 has no research submission or presentation; Research Assignment 3 is released after the midterm. Research Assignment 6 closes at the start of Week 8, before the project-proposal work. Weeks 9–10 contain no research obligation. The topics are learning goals and real information systems in the generative AI era, functions/testing, input validation, persistence/databases, transactions/failure handling and verification of output including AI. See the [research assignment guide](RESEARCH_ASSIGNMENTS.md).

Each assignment should normally fit within 15–20 minutes of focused preparation. Students cite sources, give a concrete example and explain their own reasoning. Slides, a short report or another clear format are acceptable. Presentation is not required for normal full marks. A small capped volunteer bonus may be considered only after the instructor confirms the amount and an equitable opportunity plan.

## Service integration and suggested code

Week 8's local HTTP endpoint returns authored responses that simulate an extractor. It is real communication with replay data, not live model inference. Students compare each candidate with the original donor message, validate fields and preserve uncertainty in a review queue. An offer or cancellation must not become availability or a delivery automatically.

A live-model demonstration and a coding-assistant comparison remain optional. Assessment does not depend on a paid model or AI subscription. Any suggested implementation must be inspected, tested and explained. The same standard applies to human-written code.

## Your own improvement and final presentation

Each student pitches a stakeholder need in Week 8. Student teams choose one small change that fits the **supplied** Python/SQLite system, such as identifying reservations still awaiting collection, clarifying incomplete offers or improving stage reporting. You do not rebuild the baseline application. Freeze at least two acceptance cases before coding. Week 9 adds peer verification and revision; Week 10 demonstrates the result, a boundary/failure case and a limitation. The final project presentation is announced from orientation: show your team’s working improvement, let another person try it, and provide a reproducible handoff. Individual final verification remains a separate activity. See the [assessment and project guide](ASSESSMENT.md) for the timeline and presentation expectations; the calendar date and team allocations will be announced.

## Proposed assessment

| Component | Weight | Evidence |
|---|---:|---|
| Participation and attendance | 10% | Announced attendance evidence, active participation and short weekly reflection |
| Six individual research assignments | 30% | Six submissions worth 5% each, with sources, application and the student's reasoning |
| Individual midterm | 30% | Week 4 Python function, four common tests, reproducible ZIP and individual explanation |
| Final project | 30% | Scoped improvement, verification, handoff and individual understanding |

These weights remain proposed until confirmed by the instructor and university. The exact attendance calculation, dates, private submission route, examiner plan, optional bonus rules and final-project rubric split still need announcement. AI may support the midterm at several stages with honest self-disclosure, but every student must run and explain their own implementation. Use fictional data in shared questions and keep complete submissions and individual feedback in the designated private route. See the [assignment collection](assignments/README.md) for detailed tasks and current submission status.

## Access and release status

This downloaded course package is the current home for notebooks, student-facing slide PDFs, weekly ZIPs and setup instructions. Use the [course links page](COURSE_LINKS.md) for the repository and reflection form. The instructor will announce live-class access separately.

Choose a local Python 3/Jupyter installation on Windows, macOS or Linux/Ubuntu, or use Google Colab in a browser. Follow the [setup guide](SETUP.md), including the support-file upload when using Colab. Local examples and reading cards work offline after installation and download. Colab needs internet access and its temporary files must be saved deliberately. Actual cloud access and the Week 8 HTTP exercise need a check in the chosen classroom environment.

The [course home](README.md) lists the weeks included in this package. Keep the provided directory structure when downloading files. Instructor notes, completed model notebooks, attendance responses and grading keys are not part of this student package.
