# Set up your programming workspace

## First: create a GitHub account and join the private repository

Complete this step before setting up Python so that the instructor can share the private course repository with you. If you already have a personal GitHub account, reuse it and check that its email address is verified.

1. Open [github.com/signup](https://github.com/signup) in your browser. A free personal account is sufficient.
2. Follow the signup prompts using an email you can access, and choose a username. Complete any account verification prompts.
3. Open GitHub’s verification email and verify your email address. Check your spam folder if it does not arrive.
4. Sign in and open your profile. Your profile address is `https://github.com/USERNAME`; record that exact username.
5. Send your name and GitHub username to the instructor at [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com). Never send your password, verification codes or access tokens.
6. After the instructor invites you, open GitHub’s invitation email or the invitation link provided by the instructor. Sign in with the account whose username you shared, then accept the invitation.
7. Open the course repository link supplied by the instructor and confirm that you can read its `README.md`. You can then use **Code → Download ZIP** to obtain the course files.

A private repository requires an invitation and your acceptance. If the link shows **404** or you cannot see the repository, check that you are signed in to the invited account and have accepted the invitation. Ask the instructor privately to check access or resend an expired invitation. You do not need to install Git or create your own repository for this step.

Official help: [creating a GitHub account](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github) and [repository invitations](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository).

## Choose your Python workspace

Choose **Google Colab** for a browser-based start, or **local JupyterLab** for a workspace that can keep running after your internet connection drops. Both use the same course notebooks. A laptop or desktop is recommended for programming; a phone can help you read materials and join discussion.

| Route | What you need | Where your work lives |
|---|---|---|
| Google Colab | A browser, Google account and internet connection | Notebook saved in your Drive or downloaded; runtime files are temporary |
| Windows | A supported stable Python 3 release and JupyterLab | Your course folder on the computer |
| macOS | A supported stable Python 3 release and JupyterLab | Your course folder on the computer |
| Linux / Ubuntu | A supported stable Python 3 release, `venv` and JupyterLab | Your course folder on the computer |

For a new local installation, use **Python 3.12 or newer**, choosing a supported stable release rather than a preview build. Required programming examples use Python's standard library; JupyterLab provides the notebook interface. The setup commands below create a separate environment for that interface. Python's [version-status page](https://devguide.python.org/versions/) identifies supported releases.

## 1. Get the course files

Start with the current week’s package and its root `README.md`. Use the repository link on the [course links page](COURSE_LINKS.md) when available, or the package shared by the instructor.

Download the ZIP linked from the current week's row on the course home. If you have repository access, **Code → Download ZIP** downloads the full repository; the weekly ZIP is enough for the current lesson. For syntax lookup without a weekly notebook, choose the Python Basics ZIP. Required exercises are in the weekly ZIP. If you already extracted a weekly ZIP, Python Basics is included. You do not need to install Git before the first lesson. A weekly ZIP contains that week's notebook and its required support files.

Keep this layout together:

```text
course-folder/
  learning_materials/
    Week_01.ipynb             # the notebook for your week
    Python_Basics.ipynb       # reference companion when included
    programs/                # runnable .py files and tests
    final-data/              # fictional CSV fixtures
    assets/                  # diagrams
```

Do not download only a notebook and assume its neighbouring files will follow. The code uses relative paths, so **the working directory should be `learning_materials/`**. For local work, save a personal notebook copy inside the same `learning_materials/` folder, for example `Week_01_MyWork.ipynb`, so its relative paths still work. These personal-copy names are ignored by the distributed repository. Before replacing course files with a later release, back up your work or extract the new release into a different folder.

## 2A. Run in Google Colab

[![Open Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

Use the **Open in Colab** button beside your notebook. If it opens Colab’s home page, follow the upload route below. For a private repository, direct opening may require authorization with the GitHub account invited to the course.

1. Open the notebook's **Open in Colab** button. If it opens Colab's home page, extract your downloaded ZIP on your computer and use **Colab → File → Open notebook → Upload** to select `learning_materials/Week_XX.ipynb`.
2. Use **File → Save a copy in Drive**, give your copy a recognisable name, and work in that copy. Your changes do not automatically update the course repository.
3. Connect to a normal Python runtime. This course does not require a GPU, TPU, paid Colab plan or API key.
4. Run the first **course workspace setup** code cell. When it asks, upload the complete course or weekly **ZIP** you downloaded. The helper copies only its `learning_materials/` files into a fresh runtime folder and sets the working directory. Loading the notebook alone does **not** bring its CSVs, programs or diagrams into the runtime.
5. Run the short check in Section 3 below, then read and run the notebook one cell at a time from the top. Pause at marked student tasks and intentional bugs; untouched starters may raise an expected error or report that work remains. That does not by itself mean setup failed. If a diagram's Markdown preview is missing in Colab, run its accompanying diagram-display cell; the original asset remains available in GitHub or your downloaded folder.
6. Continue editing the notebook copy you opened and saved in Drive. The `.ipynb` files extracted into the runtime are starting files, not automatically updated copies of that open notebook. Save the open notebook to Drive, and use **File → Download → Download .ipynb** for a backup. Separately download any `.py`, `.csv`, `.sqlite` or other files you created using Colab's Files pane. Saving the notebook does not save those runtime files.

The setup cell reuses a valid course folder when you rerun it in the same runtime. If the instructor updates the package, save your work first, then run `prepare_course_workspace(force_upload=True)` in a new code cell and upload the new ZIP. This creates another folder without deleting the old one. After Colab starts a new runtime, upload the ZIP again.

Use the ZIP upload route for course files. Do not paste a GitHub password or access token into a notebook, a repository URL, or an Issue. The course helper does not mount your entire Google Drive or require a GitHub token.

Colab runtimes can stop or be deleted, so a tab left open is not a backup. The official [Colab FAQ](https://research.google.com/colaboratory/faq.html) explains notebook storage, runtime lifetime and file downloads. Google's [GitHub notebook example](https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb) explains loading and sharing notebooks separately from their runtime files.

## 2B. Run locally on Windows

Install a supported stable Python from the [official Windows downloads](https://www.python.org/downloads/windows/), or use the university's prepared Python installation. Open **PowerShell** and check:

```powershell
py -3 --version
```

If `py` is not recognised but `python --version` reports the intended Python 3 version, use `python` instead of `py -3` in the environment-creation command. Otherwise finish the Python installation and reopen PowerShell.

Extract the course ZIP. In File Explorer, open the folder that contains `learning_materials/`, then open a terminal there. Alternatively, use `cd` with the real folder path in quotes. Run these commands one at a time:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install jupyterlab
.\.venv\Scripts\python.exe -m jupyterlab --notebook-dir=learning_materials
```

JupyterLab opens in your browser. Open the current week's notebook from its file list. Leave PowerShell open while working. These commands call the environment's Python directly; you do not need to activate it or change PowerShell's execution policy. This follows Python's [virtual-environment guidance](https://docs.python.org/3/library/venv.html).

On another day, return to the same course folder and run only the last command. To stop the notebook server after saving, return to PowerShell, press **Ctrl+C**, and follow its shutdown prompt.

## 2C. Run locally on macOS

Install a supported stable Python using the [official macOS downloads](https://www.python.org/downloads/macos/), or use the university's prepared installation. Open **Terminal** and check `python3 --version`.

Extract the ZIP, then use `cd` to enter the folder that contains `learning_materials/`. Quote a path if it contains spaces. Run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install jupyterlab
.venv/bin/python -m jupyterlab --notebook-dir=learning_materials
```

Open the weekly notebook in the browser window. On later days, use only the last command from the same folder. Keep Terminal open; save your work before stopping the server with **Ctrl+C**. If a managed campus computer prevents installation, use the provided campus environment or the Colab route.

## 2D. Run locally on Linux / Ubuntu

Open a terminal and check `python3 --version`. On Ubuntu, if Python or `venv` is missing, the administrator can install the distribution's complete Python environment:

```sh
sudo apt update
sudo apt install python3-full python3-pip
```

Do this only on a machine you administer; ask campus support on a managed computer. On another Linux distribution, use its equivalent Python/`venv` packages. Ubuntu recommends keeping development packages in a virtual environment, separate from the system Python. [Ubuntu Python setup](https://ubuntu.com/developers/docs/howto/python-setup/)

Extract the course ZIP and enter the folder containing `learning_materials/`, then run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install jupyterlab
.venv/bin/python -m jupyterlab --notebook-dir=learning_materials
```

If you see `externally-managed-environment`, check that you used `.venv/bin/python -m pip`, not the system's `pip`. Keep the system Python intact. On later days, run only the last command from the same course folder.

The installation method uses the project team's [Jupyter installation guide](https://jupyter.org/install), with the environment's Python selected explicitly.

## Running a saved program from a terminal

Later notebooks may show a command such as `python programs/pickup_app.py`. Those are **terminal commands**, not Python statements to paste into a notebook cell. Because the setup above calls the virtual environment directly without activating it, use the same interpreter for these commands.

From a terminal whose working folder is `learning_materials/`:

| Local platform | Example command |
|---|---|
| Windows PowerShell | `..\.venv\Scripts\python.exe programs/pickup_app.py` |
| macOS / Linux | `../.venv/bin/python programs/pickup_app.py` |

The `..` means the parent folder: `.venv/` sits beside `learning_materials/`. If using a university-provided environment, use its confirmed Python command instead. In a notebook or Colab, use the `subprocess.run([sys.executable, ...])` example below to run a saved program with the notebook's own interpreter.

## 3. Check the same things on every platform

Run this in a notebook code cell, after the course setup cell:

```python
from pathlib import Path
import sqlite3
import sys

print("Python:", sys.version.split()[0])
print("Interpreter:", sys.executable)
print("Working folder:", Path.cwd())

assert Path("programs/pickup_app.py").is_file()
assert Path("final-data/offer_batches.csv").is_file()
assert 3 * 4 == 12
with sqlite3.connect(":memory:") as connection:
    assert connection.execute("SELECT 3 * 4").fetchone()[0] == 12
print("Ready: 12 planned portions; course files and SQLite are available.")
```

Then check a saved `.py` program from the same notebook. Using `sys.executable` chooses the notebook's Python on Windows, macOS, Linux and Colab:

```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "programs/pickup_app.py"],
    capture_output=True,
    text=True,
    check=True,
)
print(result.stdout)
```

The supplied program reports a plan for **12 portions**. It does not record a collection or delivery. When a later lesson asks you to change a program, change a copy and compare its output with an independent prediction.

Week 8 includes an actual local HTTP exercise. It exchanges requests inside the Python runtime, not through a public website; an offline replay is a different mode and must be labelled as such. The instructor will check this activity in the teaching environment. If sockets or subprocesses are blocked, record the exact failure and ask for the supported route rather than silently presenting a simulation as a successful HTTP test.

## 4. Save, reopen and ask for help

| Symptom | First thing to check |
|---|---|
| `FileNotFoundError` for `final-data` or `programs` | Run the setup cell; check the working folder and download the complete ZIP. |
| Colab cannot open a private notebook | Confirm GitHub access, then use the downloaded-notebook upload route. |
| Old output remains after an edit | Run the cell again; restart the kernel/runtime and rerun the relevant cells in order; complete marked tasks before expecting their checks to pass. |
| Wrong Python or missing JupyterLab | Use the `.venv` interpreter shown above; compare `sys.executable`. |
| A diagram is blank in Colab | Run its diagram-display cell after loading the ZIP, or view the asset in GitHub. |
| Colab files disappeared | Re-upload the course ZIP and restore your own saved notebook/files. Runtime storage is temporary. |
| Windows says `python3` is unknown | Use `py -3` or the exact `.venv\Scripts\python.exe` path. |

Ask during class or open a course GitHub Issue during or after class. Include the week, operating system, local/Colab route, the smallest relevant code, expected result, actual result and error text. Remove personal paths, tokens and unrelated data before sharing. Use [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com) for grades, attendance or other personal matters.

Before finishing each session, save, close and reopen your notebook to check that your edits are present. Keep the supplied starting files separate from your own work. Return to the [course home](README.md) for the current week, slides and reflection link.
