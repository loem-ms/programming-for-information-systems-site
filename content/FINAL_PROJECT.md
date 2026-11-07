# Final project · Your Food Rescue system

In Weeks 2–8 you build the parts of an information system. In Weeks 9–10 you put them together into **your own** system. It runs a day of offers, follows **your** decisions, and you can explain and hand over every choice. Everything happens in one notebook: `Final_Project.ipynb`.

## Four levels

| Level | What you do | Required? |
|---|---|---|
| **1 · Run it** | Run the complete system with the default settings; `verify()` shows ✅ for every kit check. | ⭐ Required |
| **2 · Make it yours** | Make at least **3 decisions** in `MY_SETTINGS`, at least one about **privacy** or **input checks**, and explain each one in a decision log. No new code is needed. | ⭐ Required |
| **3 · Extend** | Plug in your own functions (a rule, a check, a report or a new status) and protect them with at least two tests. | ⭐⭐ Optional |
| **4 · Web page** | Open your system as a web page in Colab, and download it as a ZIP that runs at home with `python run_web.py`. | ⭐⭐ Optional |

Levels 1 and 2 are the **minimum** and need settings, not new code, so every student can finish them. Your grade depends mostly on the **quality of your decisions and explanations**.

## Your decisions

These are the settings you met during the course. Each one is a real tradeoff.

| Setting | Week | The question it answers |
|---|---|---|
| `TEAM_PICKUP_MIN_PORTIONS` | 2 | When does an offer need a team instead of one volunteer? |
| `URGENT_HOURS`, `SOON_HOURS` | 2 | What counts as urgent? |
| `CATEGORIES`, `PARTNERS` | 3 | Which food do we accept, and who receives it? |
| `REQUIRED_FIELDS`, `MIN_PORTIONS`, `MAX_PORTIONS`, `REJECT_IF_HOURS_LEFT_BELOW` | 5 | Which offers are refused at the door? |
| `REQUIRE_APPROVAL` | 6 | Must a coordinator approve before pickup? |
| `LOG_EVENTS` | 7 | What does the history keep? |
| `PUBLIC_FIELDS`, `REPORT_SORT` | 8 | What can the public see, and in which order? |
| `LANGUAGE` | — | English (`"en"`) or Khmer (`"km"`) words in reports |

A **strong decision log entry** names a specific value, a real alternative, a reason tied to people, and who is affected. "I changed it to 25 because it is better" is weak: better for whom, and what is lost?

## Timeline

| When | What |
|---|---|
| Week 9, Session 3 | Open `Final_Project.ipynb`; finish Level 1 in class and start Level 2. |
| Week 10, Session 1 | Finish Level 2; optional Levels 3–4; write tests; review your code with the ten principles. |
| Week 10, Session 2 | **Peer test:** a classmate runs your system from your handoff note while you watch silently. |
| Week 10, Session 3 | **Presentation** (3 minutes) and an individual check: explain one decision and one test. |

## What to submit

1. Your `Final_Project.ipynb`, after **Runtime → Restart session and run all**, with:
   - Level 1 and Level 2 complete, including the decision log;
   - Level 3 and 4 work, if you did it;
   - the handoff note and the peer test record.
2. Email it to [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com). The deadline and file name are announced in class.

**Presentation outline (3 minutes):** the people and the problem · your decisions · a short demo · what you tested · what you would improve next.

See [assessment](ASSESSMENT.md) for how the project is graded.

## Ideas for Level 3

- A smarter `pickup_label` or `urgency` that also uses another value you decide (with named constants).
- A stricter `clean_offer` that refuses something new, with a clear message.
- An honest number, such as the share of offers that were rejected or cancelled.
- A new status such as `"reserved"` in your own `ALLOWED_MOVES`, and who would use it.
