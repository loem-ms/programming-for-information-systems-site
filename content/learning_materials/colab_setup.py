"""Prepare the supplied course files in Jupyter or a temporary Colab runtime.

The release builder embeds this source in a notebook setup cell, then calls
prepare_course_workspace(). Importing this module alone does not upload files.
"""
from pathlib import Path, PurePosixPath
import io
import os
import shutil
import stat
import tempfile
import zipfile


_REQUIRED = (
    "programs/pickup_app.py", "programs/first_pickup.py",
    "programs/rescue_cli.py", "programs/rescue_models.py",
    "programs/test_pickup_app.py", "programs/test_rescue_models.py",
    "final-data/offer_batches.csv", "final-data/pickup_requests.csv",
    "final-data/rescue_events.csv", "assets/diagrams/python_execution_modes.svg",
)
_ALLOWED = {".py", ".csv", ".md", ".svg", ".png", ".jpg", ".jpeg", ".ipynb", ".json"}


def is_course_directory(folder):
    """Recognize the student directory without requiring a particular week."""
    folder = Path(folder)
    return all((folder / name).is_file() for name in _REQUIRED)


def extract_course_zip(data, destination_parent=None):
    """Extract a unique learning_materials/ tree into a NEW directory and return its path.

    Supports the downloadable weekly ZIP and GitHub's repository ZIP. Other
    directories are ignored. Existing work is never replaced. No archive code
    runs during extraction; running notebook cells remains a separate action.
    """
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        candidates = set()
        for member in archive.infolist():
            parts = PurePosixPath(member.filename).parts
            if len(parts) >= 3 and parts[-3:] == ("learning_materials", "programs", "pickup_app.py"):
                candidates.add(parts[:-2])
        if len(candidates) != 1:
            raise ValueError("Choose a course or weekly ZIP with exactly one learning_materials/ folder. Do not upload the instructor workspace ZIP.")
        prefix = next(iter(candidates))
        files, paths, total = [], set(), 0
        for member in archive.infolist():
            raw = member.filename
            parts = PurePosixPath(raw).parts
            if parts[:len(prefix)] != prefix:
                continue
            if "\\" in raw or raw.startswith("/") or any(p in ("..", ".") or ":" in p for p in parts):
                raise ValueError("The course ZIP contains an unsafe file path.")
            relative = PurePosixPath(*parts[len(prefix):])
            if member.is_dir() or not relative.parts:
                continue
            if stat.S_ISLNK(member.external_attr >> 16):
                raise ValueError("The course ZIP contains a symbolic link.")
            if any(p.startswith(".") or p == "__pycache__" for p in relative.parts):
                continue
            if relative.suffix.lower() not in _ALLOWED:
                continue
            if str(relative) in paths:
                raise ValueError("The course ZIP contains duplicate file paths.")
            paths.add(str(relative))
            total += member.file_size
            if total > 100 * 1024 * 1024 or len(files) >= 3000:
                raise ValueError("The course student files exceed the expected package size.")
            files.append((member, relative))
        if not all(name in paths for name in _REQUIRED):
            raise ValueError("The ZIP is missing required programs, data or diagram files. Download the complete course package.")
        session = Path(tempfile.mkdtemp(prefix="campus_food_rescue_", dir=destination_parent))
        student = session / "learning_materials"
        try:
            for member, relative in files:
                target = student.joinpath(*relative.parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(member) as source, target.open("xb") as output:
                    shutil.copyfileobj(source, output)
        except Exception:
            shutil.rmtree(session)
            raise
    return student.resolve()


def prepare_course_workspace(force_upload=False):
    """Use a local student directory, or upload a course ZIP in Google Colab.

    force_upload=True creates a fresh Colab copy when course files are updated.
    It leaves the previous copy intact. Save your work before switching copies.
    """
    try:
        from google.colab import files
    except ImportError:
        for candidate in (Path.cwd(), Path.cwd() / "learning_materials"):
            if is_course_directory(candidate):
                os.chdir(candidate)
                print("Course files ready:", Path.cwd())
                return Path.cwd()
        raise FileNotFoundError("Open this notebook from the course learning_materials/ folder. Keep programs/, assets/ and final-data/ beside it; see SETUP.md.")
    if not force_upload and is_course_directory(Path.cwd()):
        print("Reusing this session's course files:", Path.cwd())
        return Path.cwd()
    print("Upload ONE course ZIP downloaded from GitHub or this week's course page.")
    print("Only its learning_materials/ files will be copied into a fresh temporary folder.")
    previous = Path.cwd()
    # Colab writes uploaded bytes into its current folder before returning them.
    # Keep that operation away from an existing notebook/program workspace.
    with tempfile.TemporaryDirectory(prefix="course_upload_") as upload_folder:
        try:
            os.chdir(upload_folder)
            uploaded = files.upload()
        finally:
            os.chdir(previous)
    if len(uploaded) != 1:
        raise ValueError("Select exactly one course ZIP, then run this setup cell again.")
    name, data = next(iter(uploaded.items()))
    if not name.lower().endswith(".zip"):
        raise ValueError("Choose the .zip package, not an individual notebook or Python file.")
    folder = extract_course_zip(data, destination_parent="/content" if Path("/content").is_dir() else None)
    os.chdir(folder)
    print("Course files ready:", folder)
    print("Runtime files are temporary. Save your notebook and download any created files before leaving.")
    return folder
