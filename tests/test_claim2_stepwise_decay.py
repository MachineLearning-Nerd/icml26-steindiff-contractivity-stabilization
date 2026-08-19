import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestStepwiseDecayFixture(unittest.TestCase):
    def test_claim2_theorem_identity_toy(self):
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run(
                [sys.executable, "src/claim2_stepwise_decay_toy.py", "--out", directory],
                cwd=ROOT,
                check=True,
            )
            output = Path(directory)
            summary = json.loads((output / "summary.json").read_text())
            with (output / "results.csv").open() as handle:
                rows = list(csv.DictReader(handle))
            self.assertTrue(summary["pass"])
            self.assertEqual(summary["verdict"], "toy")
            self.assertEqual(len(rows), 4)
            self.assertTrue(
                all(float(row["c_k"]) > 0 and 0 <= float(row["rho_k"]) <= 1 for row in rows)
            )
            self.assertLessEqual(summary["max_identity_abs_error"], 1e-12)


if __name__ == "__main__":
    unittest.main()
