import csv, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_claim2_theorem_identity_toy():
    subprocess.run([sys.executable, "src/claim2_stepwise_decay_toy.py"], cwd=ROOT, check=True)
    summary = json.loads((ROOT / "outputs/claim2_attempt1/summary.json").read_text())
    rows = list(csv.DictReader((ROOT / "outputs/claim2_attempt1/results.csv").open()))
    assert summary["pass"] and summary["verdict"] == "toy"
    assert len(rows) == 4
    assert all(float(r["c_k"]) > 0 and 0 <= float(r["rho_k"]) <= 1 for r in rows)
    assert max(float(r["identity_abs_error"]) for r in rows) <= 1e-12
