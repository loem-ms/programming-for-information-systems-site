"""Check the course website before and after the MyST build.

    python scripts/validate.py .                                     # before the build
    python scripts/validate.py . --html _build/html --log myst-build.log   # after the build

Before the build it checks that every page in myst.yml exists, every link and Colab
button points to a real file, every embedded animation ({iframe}) and every link to this
site's own assets is a real file, no instructor material is published, the kit ZIP passes
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
from html.parser import HTMLParser
from pathlib import Path

PUBLIC_REPO = "loem-ms/programming-for-information-systems-site"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdM6P3ZrTaTwMAEcwZNa6-4Wl-ebus3ClRLIZinsTr4kXOBaA/viewform"
COLAB = "https://colab.research.google.com/github/" + PUBLIC_REPO + "/blob/main/content/"
SITE_ASSETS = "https://loem-ms.github.io/programming-for-information-systems-site/assets/"
FENCE = re.compile(r"^[ \t]*(`{3,}|~{3,}|:{3,})(.*)$")
ANIM_SRC = re.compile(re.escape(SITE_ASSETS) + r"anim/(?:km/)?[A-Za-z0-9_]+\.html")
ANIM_PAGE = re.compile(r"(?:km/)?[A-Za-z0-9_]+\.html")
CSS_REFERENCE = re.compile(r"""url\(\s*['"]?([^'")]*)['"]?\s*\)|@import\s+['"]([^'"]+)['"]""", re.I)
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


def iframe_sources(text):
    """The src of every {iframe} directive MyST would render: code blocks (``` with no {directive}) are skipped,
    the bodies of other directives are not (they can hold nested directives)."""
    sources, directives, code = [], [], None

    def closes(opening, found):
        return found.group(1)[0] == opening[0] and len(found.group(1)) >= len(opening) and not found.group(2).strip()
    for line in text.splitlines():
        found = FENCE.match(line)
        if code:
            if found and closes(code, found):
                code = None
            continue
        if not found:
            continue
        info = found.group(2).strip()
        if directives and closes(directives[-1], found):
            directives.pop()
        elif info.startswith("{"):
            directives.append(found.group(1))
            if re.match(r"\{iframe\}", info):
                sources.append(info[len("{iframe}"):].strip())
        else:
            code = found.group(1)
    return sources


def check_anim_link(content, path, url, kind):
    """An embedded or linked animation page: exactly assets/anim/(km/)<name>.html, the notebook's own edition,
    and the file is published."""
    km_notebook = "km" in path.relative_to(content).parts
    if not ANIM_SRC.fullmatch(url):
        require(False, kind + " that is not a course animation page in " + path.name + ": " + url)
    elif url[len(SITE_ASSETS):].startswith("anim/km/") != km_notebook:
        require(False, kind + " in the other language in " + str(path.relative_to(content)) + ": " + url)
    else:
        require((content / "assets" / url[len(SITE_ASSETS):]).is_file(),
                kind + " is missing in " + path.name + ": " + url)


def check_links(content, path):
    text = markdown_of(path)
    for source in iframe_sources(text):           # animations: only pages of this site, and they must exist
        check_anim_link(content, path, source, "Embedded page")
    for picture in REMOTE_PICTURE.findall(text):   # MyST downloads these on every build; one failure fails the build
        require(False, "Remote picture in " + path.name + " (use a copy under assets/): " + picture)
    for target in LINK.findall(text):
        target = target.split("#")[0]
        if not target or target.startswith(("mailto:", "#")):
            continue
        if target.startswith("http"):
            require(not PRIVATE.search(target), "Link to the private repository in " + path.name + ": " + target)
            if target.startswith(SITE_ASSETS + "anim/"):
                check_anim_link(content, path, target, "Link to an animation")
            elif target.startswith(SITE_ASSETS):
                rest = target[len(SITE_ASSETS):].split("?")[0]
                if "%" in rest or any(part in ("", ".", "..") for part in rest.split("/")):
                    require(False, "Link to a site asset with an unusual path in " + path.name + ": " + target)
                else:
                    require((content / "assets" / rest).is_file(),
                            "Link to a missing site asset in " + path.name + ": " + target)
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


class _Resources(HTMLParser):
    """The files an HTML page loads: src= on any tag, href= on <link>, url() and @import in <style> and style=.
    Text (for example inside <pre>) is not a reference."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.found, self.in_style = [], False

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key == "src" or (key == "href" and tag == "link"):
                self.found.append(value or "")
            elif key == "style" and value:
                self.found += css_references(value)
        self.in_style = tag == "style"

    def handle_endtag(self, tag):
        self.in_style = False

    def handle_data(self, data):
        if self.in_style:
            self.found += css_references(data)


def css_references(text):
    return [url or imported for url, imported in CSS_REFERENCE.findall(text)]


def anim_page_problems(folder):
    """Problems in a folder of animation pages (build/anim or content/assets/anim): every page exists in both
    editions (<name>.html and km/<name>.html), every file a page or a stylesheet loads exists in the folder,
    and nothing is loaded from the network."""
    folder = Path(folder).resolve()
    found, pages = [], sorted(folder.rglob("*.html"))
    names = {page.relative_to(folder).as_posix() for page in pages}
    for name in sorted(names):
        if not ANIM_PAGE.fullmatch(name):
            found.append("Unexpected animation page (want <name>.html or km/<name>.html): " + name)
        other = name[3:] if name.startswith("km/") else "km/" + name
        if other not in names:
            found.append("Animation page without its other edition: " + name + " (no " + other + ")")
    for path in pages + sorted(folder.rglob("*.css")):
        name, text = path.relative_to(folder).as_posix(), path.read_text(encoding="utf-8", errors="replace")
        if path.suffix == ".css":
            references = css_references(text)
        else:
            parser = _Resources()
            parser.feed(text)
            references = parser.found
        for reference in references:
            reference = reference.strip()
            if reference.startswith(("#", "data:")):
                continue
            if not reference:
                found.append("Animation file has an empty src/href: " + name)
            elif re.match(r"(?i)([a-z][a-z0-9+.-]*:|//)", reference):
                found.append("Animation file loads from the network (or another scheme): " + name + " -> " + reference)
            else:
                target = (path.parent / reference.split("#")[0].split("?")[0]).resolve()
                if folder not in target.parents or not target.is_file():
                    found.append("Animation file uses a missing file: " + name + " -> " + reference)
    return found


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


class _Anything:
    """Stands in for matplotlib when it is not installed (Colab has it): accepts any call and draws nothing."""
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return _Anything()

    def __getattr__(self, name):
        return _Anything()

    def __iter__(self):
        return iter([_Anything(), _Anything()])

    def __getitem__(self, key):
        return _Anything()


def fake_matplotlib():
    """Let notebooks that draw charts run where matplotlib is missing. Return True when the stand-in is used."""
    try:
        import matplotlib  # noqa: F401
        return False
    except ImportError:
        pass
    import types
    package, pyplot = types.ModuleType("matplotlib"), types.ModuleType("matplotlib.pyplot")
    package.__getattr__ = lambda name: _Anything()
    pyplot.__getattr__ = lambda name: _Anything()
    package.pyplot = pyplot
    sys.modules["matplotlib"], sys.modules["matplotlib.pyplot"] = package, pyplot
    return True


def write_file(source):
    """Do what %%writefile path does in Colab: save the rest of the cell as a file."""
    first, _, body = source.lstrip().partition("\n")
    words = first.split()[1:]
    path = [word for word in words if not word.startswith("-")][0]
    with open(path, "a" if ("-a" in words or "--append" in words) else "w", encoding="utf-8") as file:
        file.write(body)


def run_notebook(path):
    """Run every code cell in a fresh folder. Return a problem message or None."""
    notebook = json.loads(path.read_text())
    namespace = {"__name__": "__main__"}
    here = os.getcwd()

    def no_input(prompt=""):
        raise RuntimeError("input() was called while running all cells")

    fake_matplotlib()
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
                        if source.lstrip().startswith("%%writefile"):
                            write_file(source)
                        else:
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
    for leaked in (content / "notebooks" / "Midterm.ipynb", content / "downloads" / "Midterm.ipynb",
                   content / "km" / "notebooks" / "Midterm.ipynb", content / "downloads" / "km" / "Midterm.ipynb"):
        require(not leaked.exists(), "Plaintext Midterm.ipynb leaked into public site: " + str(leaked.relative_to(content)))
    for exam_page in (content / "exam" / "midterm.html", content / "exam" / "km" / "midterm.html"):
        require(exam_page.is_file(), "PIN-locked Midterm page is missing: " + str(exam_page.relative_to(content)))
        if exam_page.is_file():
            body = exam_page.read_text()
            require('"iv":' in body and '"data":' in body, "Midterm page is not encrypted: " + exam_page.name)
            require("most_overdue_id" not in body and not INSTRUCTOR.search(body),
                    "Plaintext Midterm content leaked into " + exam_page.name)
    if (content / "assets" / "anim").is_dir():
        for problem in anim_page_problems(content / "assets" / "anim"):
            require(False, problem)
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
        for static in ("slides", "downloads", "assets", "wip", "exam"):
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
