# Status

Last documentation checkpoint: 2026-08-19.

- OpenReview ID: z0CHTAHame; submission 2615.
- Paper: Mitigating the Contractivity Trap in Diffusion ODEs via Stein Stabilization.
- Authors identified from the pinned source: Shigui Li and Delu Zeng.
- arXiv: 2606.07835.
- Live contract: six anchored claims / 12 maximum points; snapshots are preserved in contract/.
- Source: arXiv source archive and PDF are pinned under evidence/source/ and SHA-256 verified.
- Compute: local CPU/local GTX 1050 only; no HF CPU upgrade, Jobs, paid, or remote compute.
- Branches: main only; no orx or stale legacy branch is present.
- Intended normalized repository name: icml26-steindiff-contractivity-stabilization.
- Standardized dossier: `CLAIM_EVIDENCE.md`, `SOURCE_AUDIT.md`, `ENVIRONMENT.md`, `REPORT.md`, `BRANCH_AUDIT.md`, `CITATION.cff`, `AUTHOR_THANK_YOU.md`, `claims.json`, `reproduction_verdicts.json`, `EVIDENCE_MANIFEST.json`, and `verify_final.py`.

## Claim status

- Claim 1: toy passed. The source reference-free coefficient is at example_paper.tex lines 486–492, with the Stein identity at lines 479–482. A deterministic one-dimensional Gaussian forward-coupling fixture compares the source expression with the direct MSE optimum. Evidence is in outputs/claim1_attempt1/. This is not end-to-end diffusion, FID, or theorem verification.
- Claim 2: toy passed. The source theorem is labeled thm:mse_decay at example_paper.tex lines 534–635; the contract calls it Theorem 4.8. A local CPU paired-particle one-dimensional fixture evaluates the exact one-step identity, trajectory product, and eta bound for a synthetic noisy affine candidate. Evidence is in outputs/claim2_attempt1/. This is not learned SteinDiff inference, image/FID evaluation, or universal theorem verification.
- Claim 3: unverified. The paper source reports LSUN-Bedrooms 256 x 256 FID 21.29 to 7.64 at 5 NFE, but no local LSUN run exists.
- Claim 4: unverified. The paper source reports up to 45.8% ImageNet 64 x 64 FID reduction, but no local ImageNet run exists.
- Claim 5: source-supported, implementation unverified. The source contains Algorithm 1 and the Hutchinson estimator, but this repository does not contain the authors' PyTorch module or an independent high-dimensional implementation.
- Claim 6: source-supported, benchmark reproduction unverified. The source describes CIFAR-10, ImageNet 64 x 64, and LSUN-Bedrooms evaluations with DPM-Solver++, UniPC, Heun, FID, IS, and FD-DINOv2; the complete matrix has not been run here.

Publication remains closed. The reported paper-scale values are not local measurements from this repository.

## Next action

Perform an independent review of the Claim 2 toy against the literal source theorem, then begin the Claim 3 source audit. Do not promote a toy or source-supported claim to reproduced without a complete paper-scale evidence path.
