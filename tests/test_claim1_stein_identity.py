import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_stein_identity_fixture():
 subprocess.run([sys.executable,'src/claim1_stein_identity_toy.py'],cwd=ROOT,check=True)
 d=json.loads((ROOT/'outputs/claim1_attempt1/summary.json').read_text());assert d['pass'] and d['absolute_difference']<.01
