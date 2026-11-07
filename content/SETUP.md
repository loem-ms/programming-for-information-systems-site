# Open your weekly notebook

## Weeks 1–2: start directly in Colab

Choose your week on the [course home](README.md), then click **Open in Colab**. The button opens that exact weekly notebook, not the Colab home page.

1. Choose **File → Save a copy in Drive** once, give the copy a recognisable name and work in it. Sign in to Google if prompted. Opening the course link alone does not create or save a personal copy.
2. Connect to a normal Python runtime, then run the first lesson code cell. No GPU, paid plan, API key, GitHub authorization or installation is needed.
3. Read and run one cell at a time. Make predictions before running and complete the marked student tasks yourself. An untouched starter is not completed work.

**There is no notebook upload, ZIP upload, support-file download or setup cell for Weeks 1–2.** All required code, inputs and exercises are already in each notebook. Optional reference links open the course website. You do not need to open them to finish the required work.

Colab may show its standard warning before running a notebook from GitHub. Read it and run only course code you have reviewed. Never paste passwords or tokens into a notebook. This course does not mount your Google Drive or request access to private GitHub files.

## Save your work and return to it

- Return to your named copy in Drive next time, rather than starting again from the course link. **File → Save** keeps your notebook edits and saved outputs; **File → Download → Download .ipynb** makes a separate backup.
- The website button always opens the instructor's starting notebook. It cannot find or overwrite your personal copy. Your changes do not update the course repository.
- A fresh Colab runtime loses Python variables. Rerun your own notebook from the top; Weeks 1–2 need no files to restore. A browser tab left open is not a backup.
- If you choose the optional saved-file exercise, download any files you create separately. Saving a notebook to Drive does not save runtime files.
- Follow the private submission instructions and contact [submit.progmis@gmail.com](mailto:submit.progmis@gmail.com) for access or course questions. Do not post assessed work or personal information in shared Issues.

Google's [Colab FAQ](https://research.google.com/colaboratory/faq.html) explains notebook storage and runtime lifetime.

## Offline alternative: one notebook in Jupyter

Download **Week 1 notebook** or **Week 2 notebook** from the matching course page before going offline. Open that `.ipynb` in an existing Python 3 Jupyter installation. Save a personal copy such as `Week_01_MyWork.ipynb` in any folder. No neighbouring course files are needed for these weeks.

If you need Jupyter, install a supported stable Python 3 release (Python 3.12 or newer recommended) from [python.org](https://www.python.org/downloads/) or use the university's prepared environment. Installation needs internet access once. From the folder where you saved the notebook:

**Windows PowerShell**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install jupyterlab
.\.venv\Scripts\python.exe -m jupyterlab
```

**macOS / Linux terminal**

```sh
python3 -m venv .venv
.venv/bin/python -m pip install jupyterlab
.venv/bin/python -m jupyterlab
```

Open your saved notebook in Jupyter's file list. On later days, run only the last command from the same folder. Keep the terminal open; save your work before stopping the server with Ctrl+C. If a campus computer blocks installation, ask campus support or use Colab. Do not change system Python or security settings.

## Optional full reference package

The [PDFs and downloads page](resources.md) retains weekly ZIPs for offline reference. These contain the notebook, PDFs, Python Basics and shared programs/data. They are **not required for Weeks 1–2**. The full Python Basics reference includes later file/program examples that use those support files; its own setup guide applies only to that optional reference. Keep an extracted full package together and never replace a folder containing your own work without backing it up.

The older [full-package setup PDF](/slides/Setup.pdf) describes ZIP-based setup. Use this web guide for the current standalone Week 1–2 workflow.

## Private class repository access, if requested later

You can read this public site and open its Colab notebooks without a GitHub account. If the instructor asks you to join the private class repository, create or reuse a free [GitHub account](https://github.com/signup), verify your email and send only your name and GitHub username to the course contact. Accept the instructor's invitation while signed in to that account. A 404 may mean the invitation was not accepted or the wrong account is signed in. Never send passwords, codes or access tokens. You do not need to install Git or create your own repository.
