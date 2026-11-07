# Setup

You need only a web browser and a Google account. Every notebook carries its own copy of the course system, so there is **nothing to install and no files to upload**.

## Option A · Google Colab (recommended)

1. On the [course home](README.md), click **Open in Colab** for your week.
2. **File → Save a copy in Drive.** Do this first, every week. Changes you make before saving a copy can be lost.
3. Work in your copy (its name starts with "Copy of").
4. Run the first code cell, **▶ Run this cell first (setup)**. It prints `✅ FoodBridge system ready`.
5. Work from top to bottom. Use **Shift + Enter** to run a cell.

**Things to know about Colab**

- If Colab says the runtime was reset or disconnected, run the setup cell again, then the cells you need.
- When confused, use **Runtime → Restart session and run all**. This runs everything fresh, in order.
- Files that your code writes (for example `my_offers.json` in Week 7) live in a temporary folder and **disappear when the runtime resets**. Your notebook itself is safe in Drive.
- Colab currently uses Python 3.13 (checked in November 2026). The course works with any Python from 3.9 on, so a newer Colab version is fine.

## Option B · Your own computer

Use this if you prefer working offline.

1. Install the latest **Python 3** from [python.org](https://www.python.org/downloads/) (any version from 3.9 on works).
2. Install Jupyter: open a terminal and run `python -m pip install notebook` (on some computers, `python3 -m pip install notebook`).
3. On the course home, use **Download** to save the week's `.ipynb` file into a folder.
4. In a terminal in that folder, run `python -m notebook` and open the file.
5. Run the setup cell. It creates a `foodbridge_kit` folder next to the notebook.

VS Code with the Python and Jupyter extensions also works: open the `.ipynb` file and choose a Python 3 kernel.

## The final project at home (optional)

In the final project (Level 4) you can download **your own** system as a ZIP and run it outside a notebook:

1. Unzip `my_foodbridge.zip`.
2. Open a terminal in the `foodbridge_kit` folder.
3. Run `python run_web.py` and open http://localhost:8000 in your browser. Stop it with **Ctrl + C**.
4. `python run_menu.py` starts a text menu; `python run_tests.py` runs the system's tests.

The [FoodBridge kit ZIP](/downloads/foodbridge_kit.zip) is the same system with the default settings.

## When something goes wrong

| What you see | What to do |
|---|---|
| `NameError: name 'bridge' is not defined` | Run the setup cell first. |
| A name you defined is "not defined" | Run the cell that defines it, or use **Restart session and run all**. |
| A check shows ❌ | Read the 💡 hint under it. The check never stops your notebook; fix and run again. |
| `⚠️ your … fell back to the default` | Your function crashed or returned something unexpected; the system used its own rule. Read the message. |
| The setup cell shows a new version number | Fine: a newer course version was unpacked. Your `my_settings.py` and `my_rules.py` were kept. |

Still stuck? See [questions and help](CONTRIBUTING.md).
