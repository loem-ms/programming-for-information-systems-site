# Questions belong here

You are encouraged to ask questions **during and after class**. Once the course repository is announced, use its **Issues** tab for shared technical questions. Until then, keep a local note with the smallest example or use the separately announced class route. Questions about Python, the food-rescue rules, notebook instructions, setup and unexpected results all help improve the class. You do not need a proposed answer before asking.

## Ask a useful question

1. Search existing Issues for the week, concept or exact error message.
2. Choose **Issues → New issue**, then **Learning question** or **Setup / notebook problem**.
3. Add the teaching week, notebook section, a small fictional input, your expectation, what happened and what you have tried. If you are unsure what to expect, say so.
4. For a setup problem, include Windows/macOS/Linux/Ubuntu/Colab, the Python version and a short traceback as text. Do not include credentials, access tokens or personal file paths from an unedited log.
5. Try a suggested answer and reply with the result. A useful final reply helps the next student. Close the issue when resolved, or explain what is still unclear.

Students with repository read access can create Issues when Issues are enabled. You do not need to commit, push or open a pull request to ask a question. [GitHub's issue guide](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue)

## Example

**Title:** `[W02] Does exactly 20 planned portions need team dispatch?`

> The request has been reviewed. Four containers have five declared portions each, so I calculate 20. The rule says “at least 20.” I expect the team label, but my condition is `portions > 20` and it returns standard. Should the equality case be included?

A helpful answer explains the inclusive boundary, tests 19/20/21 and distinguishes dispatch workload from food suitability or delivery evidence.

Use fenced code blocks for short examples:

```python
portions = 5 * 4
print(portions > 20)  # What does this comparison exclude?
```

## Discuss respectfully

Explain the reasoning, ask clarifying questions and avoid posting a complete answer to someone else's assessed task. Share one small distinguishing input or test. When you discover an error in the course material, report the file and section so it can be corrected for everyone.

Everyone with access to a private repository can read its Issues. In a public repository, anyone can read them. An Issue is not a private message to the instructor. Keep complete submissions, grades, attendance details and sensitive personal concerns in the instructor-designated private route. Use fictional donor/partner data. This question space is not an attendance register or an emergency contact channel.

If you cannot access GitHub or your connection fails, keep a local note with the smallest example and ask during class or through the separately announced private contact route. When useful, a general version of the question can later be added here without identifying personal details. The instructor will announce response expectations; no immediate-response promise is implied.
