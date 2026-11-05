"""Scaffold CLI checks only; these tests do not test product behavior."""

import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE = "melodiecli_agents_run_history"


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", MODULE, *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
        timeout=60,
    )


class ScaffoldCliTests(unittest.TestCase):
    def test_status_reports_planned_json(self):
        result = run_cli("status")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "PLANNED")
        self.assertEqual(payload["implementation"], "SCAFFOLD_ONLY")
        self.assertEqual(payload["operations_performed"], [])

    def test_verify_reports_not_configured(self):
        result = run_cli("verify")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("not configured", result.stdout)

    def test_help_exits_zero(self):
        result = run_cli("--help")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_configuration_example_contains_no_credentials(self):
        example = (ROOT / ".env.example").read_text(encoding="utf-8")
        self.assertIn("SERVICE_BASE_URL=", example)
        self.assertIn("API_TOKEN=", example)
        self.assertNotRegex(example, r"(?m)^(?:SERVICE_BASE_URL|API_TOKEN)=.+$")

    def test_policy_documents_exist(self):
        self.assertTrue((ROOT / "EVIDENCE.md").is_file())
        self.assertTrue((ROOT / "SECURITY.md").is_file())
        self.assertTrue((ROOT / ".github" / "SECURITY.md").is_file())


if __name__ == "__main__":
    unittest.main()
