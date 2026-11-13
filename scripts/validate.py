"""Check the course website before and after the MyST build.

    python scripts/validate.py .                                     # before the build
    python scripts/validate.py . --html _build/html --log myst-build.log   # after the build

Before the build it checks that every page in myst.yml exists, every link and Colab
button points to a real file, no instructor material is published, the kit ZIP passes
its own tests, and every student notebook (English and Khmer) runs from top to bottom
with this Python.
After the build it checks the generated pages, the static downloads and the build log.
This file is generated from tools/site_validate.py in the authoring workspace.
"""
import argparse
import builtins
import contextlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

PUBLIC_REPO = "loem-ms/programming-for-information-systems-site"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdM6P3ZrTaTwMAEcwZNa6-4Wl-ebus3ClRLIZinsTr4kXOBaA/viewform"
COLAB = "https://colab.research.google.com/github/" + PUBLIC_REPO + "/blob/main/content/"
PRIVATE = re.compile(r"programming-for-information-systems(?!-site)")
INSTRUCTOR = re.compile(r"INSTRUCTOR MODEL ANSWER|instructor-only|```\{solution\}|Model answer\.")
LINK = re.compile(r"\]\(([^)\s]+)\)")
REMOTE_PICTURE = re.compile(r"!\[[^\]]*\]\((https?://[^)\s]+)\)")
problems = []


def require(condition, message):
    if not condition:
        problems.append(message)


def toc_files(nodes):
    for node in nodes:
        if "file" in node:
            yield node["file"]
        yield from toc_files(node.get("children", []))


def markdown_of(path):
    if path.suffix == ".md":
        return path.read_text()
    notebook = json.loads(path.read_text())
    return "\n".join("".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "markdown")


def check_links(content, path):
    text = markdown_of(path)
    for picture in REMOTE_PICTURE.findall(text):   # MyST downloads these on every build; one failure fails the build
        require(False, "Remote picture in " + path.name + " (use a copy under assets/): " + picture)
    for target in LINK.findall(text):
        target = target.split("#")[0]
        if not target or target.startswith(("mailto:", "#")):
            continue
        if target.startswith("http"):
            require(not PRIVATE.search(target), "Link to the private repository in " + path.name + ": " + target)
            if "docs.google.com/forms" in target:
                require(target == FORM, "Unapproved form link in " + path.name + ": " + target)
            if target.startswith(COLAB):
                require((content / target[len(COLAB):]).is_file(), "Colab button to a missing file: " + target)
            continue
        if target.startswith("/"):
            require((content / target.lstrip("/")).is_file(), "Broken static link in " + path.name + ": " + target)
        elif target.startswith("data:"):
            continue
        else:
            require((path.parent / target).resolve().is_file(), "Broken link in " + path.name + ": " + target)


def check_notebook(path, colab):
    notebook = json.loads(path.read_text())
    require(notebook.get("nbformat") == 4, "Not an nbformat 4 notebook: " + path.name)
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            require(cell.get("outputs") == [] and cell.get("execution_count") is None,
                    "Notebook has outputs (publish clean notebooks only): " + path.name)
        require(not INSTRUCTOR.search("".join(cell["source"])), "Instructor material in " + path.name)
    has_setup = any("setup" in c.get("metadata", {}).get("tags", []) for c in notebook["cells"])
    if colab and has_setup:
        setup = "".join(next(c for c in notebook["cells"] if "setup" in c.get("metadata", {}).get("tags", []))["source"])
        require("_prepare_kit()" in setup and "import foodbridge as bridge" in setup,
                "Setup cell does not unpack the kit: " + path.name)
    if not colab:
        require(path.stat().st_size < 400000, "Website notebook embeds the kit (too large): " + path.name)


def run_notebook(path):
    """Run every code cell in a fresh folder. Return a problem message or None."""
    notebook = json.loads(path.read_text())
    namespace = {"__name__": "__main__"}
    here = os.getcwd()

    def no_input(prompt=""):
        raise RuntimeError("input() was called while running all cells")

    with tempfile.TemporaryDirectory() as folder:
        os.chdir(folder)
        original_input, builtins.input = builtins.input, no_input
        try:
            for number, cell in enumerate(notebook["cells"]):
                if cell["cell_type"] != "code":
                    continue
                source = "".join(cell["source"])
                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        exec(compile(source, path.name + " cell " + str(number), "exec"), namespace)
                except Exception as error:
                    return "cell " + str(number) + ": " + type(error).__name__ + ": " + str(error)
        finally:
            builtins.input = original_input
            if "bridge" in namespace and hasattr(namespace["bridge"], "stop_web"):
                namespace["bridge"].stop_web()
            os.chdir(here)
    return None


def check_kit_zip(path):
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        for needed in ("foodbridge_kit/foodbridge/__init__.py", "foodbridge_kit/run_tests.py",
                       "foodbridge_kit/run_web.py", "foodbridge_kit/my_settings.py"):
            require(needed in names, "Kit ZIP is missing " + needed)
        require(not any("__pycache__" in n or "saved_data" in n for n in names), "Kit ZIP contains cache or data")
        with tempfile.TemporaryDirectory() as folder:
            archive.extractall(folder)
            result = subprocess.run([sys.executable, "run_tests.py"], cwd=os.path.join(folder, "foodbridge_kit"),
                                    capture_output=True, text=True)
            require(result.returncode == 0, "Kit tests failed:\n" + result.stdout[-1500:] + result.stderr[-1500:])
            last = (result.stdout.strip().splitlines() or ["?"])[-1]
            print("  kit tests: " + last)


def validate(folder, html=None, log=None, run=True):
    folder = folder.resolve()
    content = folder / "content"
    book = json.loads((folder / "myst.yml").read_text())
    require(book["site"]["template"] == "book-theme", "Use the standard MyST book theme")
    pages = list(toc_files(book["project"]["toc"]))
    for page in pages:
        require((folder / page).is_file(), "Page in myst.yml is missing: " + page)
    for path in sorted(content.rglob("*")):
        if path.suffix in (".md", ".ipynb"):
            check_links(content, path)
            if path.suffix == ".md":
                require(not INSTRUCTOR.search(path.read_text()), "Instructor material in " + path.name)
    site_notebooks, downloads = [], []
    for pages_folder, download_folder in ((content / "notebooks", content / "downloads"),
                                          (content / "km" / "notebooks", content / "downloads" / "km")):
        pages_here, downloads_here = sorted(pages_folder.glob("*.ipynb")), sorted(download_folder.glob("*.ipynb"))
        require([p.name for p in pages_here] == [p.name for p in downloads_here],
                "Each website notebook needs a matching Colab download: " + str(pages_folder.relative_to(content)))
        site_notebooks += pages_here
        downloads += downloads_here
    for path in site_notebooks:
        check_notebook(path, colab=False)
    for path in downloads:
        check_notebook(path, colab=True)
    check_kit_zip(content / "downloads" / "foodbridge_kit.zip")
    if run and not problems:
        python = sys.version.split()[0]
        for path in downloads:
            problem = run_notebook(path)
            require(problem is None, "Notebook does not run on Python " + python + ": " + str(path.relative_to(content)) +
                    " (" + str(problem) + ")")
            print(("  ✅ " if problem is None else "  ❌ ") + str(path.relative_to(content)) + " runs on Python " + python)
    if html:
        html = html.resolve()
        require((html / "index.html").is_file(), "MyST HTML entry point is missing")
        for page in pages[1:]:
            slug = re.sub(r"[_\s]+", "-", Path(page).with_suffix("").as_posix().lower())
            require((html / slug / "index.html").is_file(), "Missing rendered page: " + slug)
        for static in ("slides", "downloads", "assets"):
            for path in (content / static).rglob("*"):
                if path.is_file():
                    require((html / static / path.relative_to(content / static)).is_file(),
                            "Static file missing from the build: " + static + "/" + path.name)
    if log:
        markers = ("⛔", "Duplicate identifier", "No target for internal reference", "Cross reference target was not found")
        issues = [line for line in log.read_text().splitlines() if any(m in line for m in markers)]
        require(not issues, "MyST reported broken content:\n" + "\n".join(issues))
    if problems:
        print("FAIL\n- " + "\n- ".join(problems))
        sys.exit(1)
    print("PASS " + str(len(pages)) + " pages, " + str(len(downloads)) + " notebooks, links, downloads and kit"
          + (", rendered site" if html else ""))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--html", type=Path)
    parser.add_argument("--log", type=Path)
    parser.add_argument("--no-run", action="store_true", help="skip running the notebooks")
    args = parser.parse_args()
    validate(args.folder, args.html, args.log, run=not args.no_run and args.html is None)
