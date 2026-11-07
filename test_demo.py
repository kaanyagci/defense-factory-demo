import json
import subprocess
import sys
import unittest
from pathlib import Path


class DemoCommandTests(unittest.TestCase):
    def run_demo(self, *args):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("demo.py")), *args],
            check=True, capture_output=True, text=True,
        )
        return json.loads(result.stdout)

    def test_owner_can_read_mock_document(self):
        self.assertEqual(self.run_demo("--user", "alice", "--document", "report-1")["owner"], "alice")

    def test_unknown_document_returns_null(self):
        self.assertIsNone(self.run_demo("--document", "missing"))


if __name__ == "__main__":
    unittest.main()
