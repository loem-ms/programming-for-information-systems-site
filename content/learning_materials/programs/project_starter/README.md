# Optional pickup-policy scaffold

Use this unfinished structure to separate a coordination rule, command entry point and tests. It is practice, not a completed assessed project.

| File | Responsibility |
|---|---|
| [policy.py](/learning_materials/programs/project_starter/policy.py) | `pickup_label(total_portions, reviewed)` implements the agreed rule |
| [app.py](/learning_materials/programs/project_starter/app.py) | Parse arguments, call the policy, display result or failure |
| [test_policy.py](/learning_materials/programs/project_starter/test_policy.py) | Preserve independent expected cases |

From learning_materials/:

```sh
python programs/project_starter/app.py 20 --reviewed
python -m unittest discover -s programs/project_starter -p "test_*.py"
```

Initially the app reports the unfinished policy and exits with status 2. The test runner reports **two skipped tests**. Neither is proof of a working feature.

For the course's default rule, an unreviewed request is held; a reviewed request with at least 20 planned portions uses team coordination, otherwise standard coordination. Twenty is a fictional workload threshold, not a rule about suitability or recipient priority. Agree on invalid-input handling, replace the placeholder tests, remove the skip decorators and implement the function. Predict outcomes before implementation.

Only if you choose an optional improvement, make a separate folder matching your stakeholder need. The minimum final project uses the supplied complete baseline, not this unfinished scaffold; reproduce it and complete the requested notes. This toy policy is not a reservation or delivery system. Document the working directory, run command, inputs, expected result, test command and limits. Completed instructor notebooks stay separately under examples/ and are not released student scaffolds.
