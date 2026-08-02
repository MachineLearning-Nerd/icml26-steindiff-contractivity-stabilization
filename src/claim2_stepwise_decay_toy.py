"""Finite 1-D diagnostic of the exact Theorem 4.8 step-wise MSE identity.
This is a reduced formula fixture, not SteinDiff model inference or a theorem proof.
"""
import csv, hashlib, json, math, random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "claim2_attempt1"


def mean(xs):
    return sum(xs) / len(xs)


def mse(xs):
    return mean([x * x for x in xs])


def run(seed=20260802, n=50000, steps=4, lam=0.35, noise_sd=0.25):
    """Apply x <- x-gamma*u where u=x-T(x)=lam*(x-x*)-xi."""
    rng = random.Random(seed)
    err = [rng.gauss(0.0, 1.0) for _ in range(n)]
    rows = []
    product = 1.0
    initial = mse(err)
    for k in range(steps, 0, -1):
        xi = [rng.gauss(0.0, noise_sd) for _ in range(n)]
        u = [lam * e - z for e, z in zip(err, xi)]
        e_k = mse(err)
        b = mean([a * b_ for a, b_ in zip(u, err)])
        c = mean([a * a for a in u])
        gamma = b / c
        corrected = [e - gamma * a for e, a in zip(err, u)]
        vanilla = [e - a for e, a in zip(err, u)]
        wrong = [e + gamma * a for e, a in zip(err, u)]
        next_e = mse(corrected)
        identity_rhs = e_k - b * b / c
        rho = b * b / (c * e_k)
        product *= (1.0 - rho)
        rows.append({
            "k": k, "E_k": e_k, "b_k": b, "c_k": c,
            "gamma_star": gamma, "rho_k": rho,
            "E_kminus1_stein": next_e, "identity_rhs": identity_rhs,
            "identity_abs_error": abs(next_e - identity_rhs),
            "E_kminus1_vanilla_gamma1": mse(vanilla),
            "E_kminus1_wrong_negative_gamma": mse(wrong),
        })
        err = corrected
    terminal = mse(err)
    eta = min(row["rho_k"] for row in rows)
    theorem_product = initial * product
    theorem_bound = initial * (1.0 - eta) ** steps
    return {"seed": seed, "n": n, "steps": steps, "lambda": lam,
            "candidate_noise_sd": noise_sd, "E_N": initial, "E_0_stein": terminal,
            "product_rhs": theorem_product, "eta": eta, "eta_bound_rhs": theorem_bound,
            "product_abs_error": abs(terminal - theorem_product),
            "bound_holds": terminal <= theorem_bound + 1e-12,
            "max_identity_abs_error": max(row["identity_abs_error"] for row in rows),
            "rows": rows}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    data = run()
    protocol = """Pre-execution Claim-2 toy protocol\n
Source: Theorem 4.8, example_paper.tex lines 534-633.  Fixed before run: seed=20260802; n=50000 paired 1-D particles; N=4; lambda=.35; candidate noise SD=.25. At each step T(x)=x-lambda*(x-x*)+xi, u=x-T(x), and gamma*=mean(u*(x-x*))/mean(u^2). Primary metrics are the theorem one-step identity E_{k-1}=E_k-b_k^2/c_k, trajectory product, and eta bound. Controls report gamma=1 (vanilla) and -gamma* (wrong-sign), on the same particle/candidate-noise draws. Pass iff every finite-sample identity error <=1e-12, product error <=1e-12, all c_k>0 and 0<=rho_k<=1, and eta bound holds. This is a finite synthetic formula fixture: it is not a learned diffusion model, Algorithm-1 estimator, image/FID result, or universal theorem verification.\n"""
    (OUT / "PROTOCOL.md").write_text(protocol)
    with (OUT / "results.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data["rows"][0].keys())
        writer.writeheader(); writer.writerows(data["rows"])
    summary = {k: v for k, v in data.items() if k != "rows"}
    summary["pass"] = (summary["max_identity_abs_error"] <= 1e-12 and
                       summary["product_abs_error"] <= 1e-12 and summary["bound_holds"] and
                       all(r["c_k"] > 0 and 0 <= r["rho_k"] <= 1 for r in data["rows"]))
    summary["verdict"] = "toy"
    summary["scope"] = "Finite 1-D paired-particle execution of Theorem-4.8 algebra with a synthetic noisy affine candidate; not end-to-end SteinDiff or theorem verification."
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    locations = """# Claim 2 source mapping

Pinned `evidence/source/arxiv_source.tar.gz`, `example_paper.tex` lines 534-633, defines `u_k=x_k-T_theta(x_k)`, `b_k=E[<u_k,x_k-x*>]`, `c_k=E[||u_k||^2]`, `gamma*_k=b_k/c_k`, the one-step identity, `rho_k`, trajectory product, and eta bound. `src/claim2_stepwise_decay_toy.py` directly computes those quantities from paired synthetic particles. The fixture intentionally uses a synthetic noisy affine candidate, so it cannot establish the theorem for learned diffusion solvers.\n"""
    (OUT / "SOURCE_MAPPING.md").write_text(locations)
    files = ["PROTOCOL.md", "SOURCE_MAPPING.md", "results.csv", "summary.json"]
    (OUT / "SHA256SUMS").write_text("".join(f"{sha256(OUT / name)}  {name}\n" for name in files))

if __name__ == "__main__":
    main()
