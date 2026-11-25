# Setup

You need only a web browser and a Google account. Every notebook carries its own copy of the course system, so there is **nothing to install and no files to upload**.

Read this page before you open your first notebook, and come back to it whenever a notebook will not run. Most students use Option A; Option B is there if you prefer to work offline.

## Option A · Google Colab (recommended)

1. On the [course home](README.md), click **Open in Colab** for your week.
2. **File → Save a copy in Drive.** Do this first, every week. Changes you make before saving a copy can be lost.
3. Work in your copy (its name starts with "Copy of").
4. Run the first code cell, **▶ Run this cell first (setup)**. It prints `✅ FoodBridge system ready`.
5. Work from top to bottom. Use **Shift + Enter** to run a cell.

**Things to know about Colab**

- If Colab says the runtime was reset or disconnected, run the setup cell again, then the cells you need.
- When confused, use **Runtime → Restart session and run all**. This runs everything fresh, in order.
- **From Week 4 onward**, the setup cell offers to connect Google Drive so your `my_foodbridge/` folder is saved in `MyDrive/my_foodbridge` and stays with you from week to week. If you decline Drive access, Colab keeps `my_foodbridge/` in a temporary folder for the current session only — it **disappears when the runtime disconnects** (download a copy or reconnect Drive if you want to keep your files). Your notebook itself is always safe in Drive once you save a copy.
- Colab currently uses Python 3.13 (checked in November 2026). The course works with any Python from 3.9 on, so a newer Colab version is fine.

## Option B · Your own computer

If Colab is not an option for you, the same notebooks also run on your own computer. Use this if you prefer working offline.

1. Install the latest **Python 3** from [python.org](https://www.python.org/downloads/) (any version from 3.9 on works).
2. Install Jupyter and matplotlib: open a terminal and run `python -m pip install notebook matplotlib` (on some computers, `python3 -m pip install notebook matplotlib`). `matplotlib` is used for charts in Weeks 8–9.
3. On the course home, use **Download** to save the week's `.ipynb` file into a folder.
4. In a terminal in that folder, run `python -m notebook` and open the file.
5. Run the setup cell. It creates a `foodbridge_kit` folder (and, from Week 4 onward, your `my_foodbridge` folder) next to the notebook.

VS Code with the Python and Jupyter extensions also works: open the `.ipynb` file and choose a Python 3 kernel.

## The final project at home (optional)

Your Final project is your own `my_foodbridge/` folder. To run it outside a notebook:

1. Download the folder (Google Drive → right-click `my_foodbridge` → **Download**) and unzip it.
2. Open a terminal in the `my_foodbridge/` folder.
3. Run `python app.py` (`python3` on Mac or Linux), then type `1`, `2`, `3` or `q`.

The web app (`bridge.start_web`) runs only in a notebook.

The [FoodBridge kit ZIP](/downloads/foodbridge_kit.zip) is the same system with the default settings.

## When something goes wrong

Most problems have a quick fix. Find what you see in the table and do what it says.

| What you see | What to do |
|---|---|
| `NameError: name 'bridge' is not defined` | Run the setup cell first. |
| A name you defined is "not defined" | Run the cell that defines it, or use **Restart session and run all**. |
| A check shows ❌ | Read the 💡 hint under it. The check never stops your notebook; fix and run again. |
| `⚠️ your … fell back to the default` | Your function crashed or returned something unexpected; the system used its own rule. Read the message. |
| `bridge.show()` marks a file with `🔧` (model version) | Either that file is not in `my_foodbridge/` yet, or it has a Python error. Check the problem note in `bridge.show()` and re-run the `%%writefile` cell or fix the file. |
| The setup cell shows a new version number | Fine: a newer course version was unpacked. Your `my_foodbridge/` folder (and any earlier `my_settings.py` / `my_rules.py`) were kept. |

Still stuck? See [questions and help](CONTRIBUTING.md).
