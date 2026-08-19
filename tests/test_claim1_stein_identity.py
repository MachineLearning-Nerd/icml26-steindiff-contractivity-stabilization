import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestSteinIdentityFixture(unittest.TestCase):
    def test_stein_identity_fixture(self):
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run(
                [sys.executable, "src/claim1_stein_identity_toy.py", "--out", directory],
                cwd=ROOT,
                check=True,
            )
            summary = json.loads((Path(directory) / "summary.json").read_text())
            self.assertTrue(summary["pass"])
            self.assertLess(summary["absolute_difference"], 0.01)


if __name__ == "__main__":
    unittest.main()
