import tempfile
import unittest
from pathlib import Path
from main import audit

class SubmoduleAuditTests(unittest.TestCase):
    def test_reports_missing_config(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(audit(folder)[0]["issue"], "missing-gitmodules")
    def test_reports_uninitialized_path(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / ".gitmodules").write_text('[submodule "docs"]\n path = vendor/docs\n url = https://example.com/docs.git\n', encoding="utf-8")
            (root / "vendor/docs").mkdir(parents=True)
            self.assertEqual(audit(root)[0]["issue"], "uninitialized")
    def test_flags_local_url(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / ".gitmodules").write_text('[submodule "local"]\n path = local\n url = file:///tmp/local.git\n', encoding="utf-8")
            (root / "local").mkdir()
            self.assertIn("local-only-url", [item["issue"] for item in audit(root)])

if __name__ == "__main__":
    unittest.main()
