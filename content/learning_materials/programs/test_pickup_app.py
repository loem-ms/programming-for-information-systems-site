"""From learning_materials/: python -m unittest discover -s programs -p "test_*.py"."""
import contextlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from pickup_app import planned_portions
from rescue_cli import main

PROGRAMS = Path(__file__).resolve().parent


class PlanningTests(unittest.TestCase):
    def test_multiple_containers(self):
        self.assertEqual(planned_portions(3, 4), 12)

    def test_zero_containers_in_arithmetic_contract(self):
        self.assertEqual(planned_portions(3, 0), 0)

    def test_zero_declared_portions_in_arithmetic_contract(self):
        self.assertEqual(planned_portions(0, 4), 0)


class CommandTests(unittest.TestCase):
    def test_explicit_arguments(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main(["--portions-per-container", "5", "--containers", "2"])
        self.assertEqual(status, 0)
        self.assertEqual(output.getvalue(), "Planned portions: 10\n")

    def test_invalid_counts_have_no_planning_result(self):
        for args in [["--containers", "0"], ["--portions-per-container", "-1"]]:
            with self.subTest(args=args):
                output, error = io.StringIO(), io.StringIO()
                with contextlib.redirect_stdout(output), contextlib.redirect_stderr(error):
                    status = main(args)
                self.assertEqual(status, 2)
                self.assertEqual(output.getvalue(), "")
                self.assertIn("must be positive", error.getvalue())

    def test_malformed_integer(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as failure:
                main(["--containers", "many"])
        self.assertEqual(failure.exception.code, 2)

    def test_import_is_quiet_in_a_fresh_process(self):
        result = subprocess.run([sys.executable, "-c", "import pickup_app; import rescue_cli; import rescue_models"],
                                cwd=PROGRAMS, capture_output=True, text=True)
        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))

    def test_absolute_file_path_from_another_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            result = subprocess.run([sys.executable, str(PROGRAMS / "rescue_cli.py"), "--containers", "3"],
                                    cwd=folder, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "Planned portions: 9\n")

    def test_process_status_reports_invalid_input(self):
        result = subprocess.run([sys.executable, str(PROGRAMS / "rescue_cli.py"), "--containers", "-1"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("must be positive", result.stderr)


if __name__ == "__main__":
    unittest.main()
