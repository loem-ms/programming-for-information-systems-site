# From notebook cells to runnable rescue-planning programs

These small examples support the fictional Cambodian university **Campus Food Rescue** course. They calculate declared planning quantities; they do not approve food, reserve offers or establish collection/delivery. The weekly notebooks teach those distinct records and decisions.

Jupyter executes cells through a persistent kernel. A saved `.py` file is plain Python text that an interpreter can execute from top to bottom in a fresh process. `main` is a conventional name, not a keyword or an automatic call.

Run these commands in a **terminal**, with `learning_materials/` as the working directory unless a step explicitly changes it. They are not Python statements for a notebook cell.

## Choose the course interpreter

The examples below use `python` as shorthand for your course interpreter. If setup created a `.venv` folder beside `learning_materials/`, substitute the appropriate path throughout; no activation is required.

| Terminal working directory | macOS / Linux | Windows PowerShell / Command Prompt |
|---|---|---|
| `learning_materials/` | `../.venv/bin/python` | `..\.venv\Scripts\python.exe` |
| `learning_materials/programs/` | `../../.venv/bin/python` | `..\..\.venv\Scripts\python.exe` |

For example, from `learning_materials/`, run `../.venv/bin/python programs/first_pickup.py` on macOS/Linux, or `..\.venv\Scripts\python.exe programs/first_pickup.py` on Windows. The second table row matters for the Week 4 import exercise, which changes into `programs/`.

If you use another installed environment, choose its Python 3 interpreter consistently (`python3` or Windows `py -3` may select a different installation). In a notebook, `import sys; print(sys.executable)` shows its interpreter. Check your chosen terminal command with `--version`. If using Colab or a notebook without a terminal, use the subprocess examples in Python Basics sections 14–17; `sys.executable` launches the notebook's interpreter.

## Program map

| When | Practice file | Purpose |
|---|---|---|
| Week 1 | [first_pickup.py](/learning_materials/programs/first_pickup.py) | Save, execute and rerun a whole file |
| Week 4 | [pickup_app.py](/learning_materials/programs/pickup_app.py) | Reuse `planned_portions`; explain `main()` and the import guard |
| Week 5 | [rescue_cli.py](/learning_materials/programs/rescue_cli.py) | Parse arguments, reject invalid counts and report status |
| Week 6 | [rescue_models.py](/learning_materials/programs/rescue_models.py) | Inspect `OfferLine`, attributes, instances and `total_portions()` |
| Week 7 onward | [test_pickup_app.py](/learning_materials/programs/test_pickup_app.py), [test_rescue_models.py](/learning_materials/programs/test_rescue_models.py) | Reproduce checks in a fresh interpreter |
| Weeks 9–10 | [project starter](project_starter/README.md) | Separate a policy, entry point and tests |

## Week 1: run a saved file

```sh
python programs/first_pickup.py
```

Expected output:

```text
Bread boxes: 4 containers
Planned portions: 12
```

Make a copy, change the count to 3, predict 9 planned portions, save and rerun. Editing changes the file; execution reads the saved version. An old notebook variable cannot supply a missing input in this new process.

## Week 4: run directly or import

```sh
python programs/pickup_app.py
```

The same output now comes from `main()` calling a reusable arithmetic function. The guard `if __name__ == "__main__":` controls that explicit call. Import still executes top-level definitions, but skips the guarded workflow.

To explore import, start Python from `programs/`:

```sh
cd programs
python
```

At Python's `>>>` prompt:

```python
import pickup_app
pickup_app.planned_portions(3, 2)
```

Import prints nothing; the interactive expression shows `6`. Leave with `exit()` and use `cd ..` to return to learning_materials/. A bare module import depends on the invocation and module search path; it is not guaranteed from every directory.

## Week 5: change inputs through arguments

From learning_materials/:

```sh
python programs/rescue_cli.py --help
python programs/rescue_cli.py --containers 3
python programs/rescue_cli.py --portions-per-container 5 --containers 2
python programs/rescue_cli.py --containers 0
python programs/rescue_cli.py --containers many
```

The valid commands report 9 and 10 planned portions. Zero parses but violates this command's positive-count rule; `many` fails integer parsing. Both failures print an explanation to standard error and exit with status 2. Success prints to standard output and exits with status 0. Returning 2 from main alone does not set process status; `raise SystemExit(main())` does.

The arithmetic helper assumes nonnegative integer arguments and allows a zero planning result. The CLI requires positive counts. Neither rule substitutes for coordinator approval or database reservation checks.

## Paths are part of the run instructions

`programs/rescue_cli.py` is a relative path from learning_materials/. A different working directory changes its meaning; quote paths containing spaces. Running the script by absolute path also works.

Ordinary `Path("data.csv")` operations use the process working directory. In a saved script, `Path(__file__).resolve().parent` identifies the script directory and can anchor a deliberately bundled resource. `__file__` is normally absent in notebook cells. Document which convention an input file uses.

## Week 6: inspect an object

```sh
python programs/rescue_models.py
```

Expected: `DEMO-B1 4 12` — batch ID, containers and planned portions. `OfferLine` is a class; `line` is one instance; `containers` is an attribute; `total_portions()` is a method using that instance through `self`.

The constructor checks initial values. Public attributes remain mutable; changing a count does not rerun those checks, save a database row or reserve a pickup. Compare classes with dictionaries and functions before choosing a representation. A whole-system object-oriented rewrite is optional.

## Week 7: run independent tests

```sh
python -m unittest discover -s programs -p "test_*.py"
```

Double quotes work in common Unix shells and Windows Command Prompt. `-s programs` selects the discovery directory; it does not change the working directory. Check that tests were found. The supplied suite has 13 tests, covering arithmetic, objects, invalid input, process status, quiet imports and invocation from another directory.

Start with `PlanningTests`, then inspect command/process tests when those concepts are familiar. These tests do not automatically test your weekly policy, importer, reservation transaction or project. Add independently expected cases for your implementation.

## If there is no terminal UI

Python Basics sections 14–17 use `subprocess.run`, `sys.executable` and temporary files to launch a separate interpreter from a notebook. This is an execution bridge, not another dependency. The classroom environment should be pretested for process and local HTTP support.
