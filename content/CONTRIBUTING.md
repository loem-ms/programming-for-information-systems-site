# Questions and help

Questions are welcome **during and after class**. A question that helps you usually helps a classmate too. You do not need to know the answer before you ask.

## Ask a useful question

Good questions are small and concrete. Include:

1. **The week and the section**, for example "Week 3, Session 3, Part 2".
2. **The smallest piece of code** that shows the problem.
3. **What you expected**, and **what happened** (copy the last line of the error as text).
4. **What you already tried.**

For a setup problem, also say whether you use Colab, Windows, macOS or Linux, and your Python version (`import sys; print(sys.version)`).

## Example

**Title:** `[W02] Does exactly 20 portions need a team?`

> The rule says "20 portions or more need a team". My function returns "standard" for 20. My condition is `portions > 20`. I expected "team". Should the boundary be included?

````
```python
def pickup_label(portions, approved):
    if portions > 20:      # is this the problem?
        return "team"
    ...
```
````

A helpful answer explains the boundary, tests 19, 20 and 21, and connects it to Principle 2 (explicit rules).

## Where to ask

- **In class:** any time, especially during Sessions 2 and 3.
- **Issues** in the course repository (when access is announced): **Issues → New issue**. Search first: your question may already have an answer. When you get an answer, reply with what worked and close the issue.
- **Email** [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com) for anything private: submissions, grades, attendance or personal matters.

Issues are visible to everyone with access to the repository. They are not private messages. Do not post complete answers to assessed tasks, passwords or personal data.

## Found a mistake in the course?

Report the file and section (for example "Week 5 notebook, Part 2, the check for portions") so it can be fixed for everyone. Thank you!
