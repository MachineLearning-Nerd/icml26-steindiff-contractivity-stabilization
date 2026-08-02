# Claim 2 — Step-wise error decay

**Outcome: toy.** The source Theorem 4.8 (`evidence/source/arxiv_source.tar.gz`, `example_paper.tex:534-633`) states the exact-coefficient one-step identity, the trajectory product, and the `eta` bound.

A local CPU finite 1-D paired-particle fixture evaluates the literal algebra with a synthetic noisy affine candidate over four steps. All four finite-sample one-step identities, the product identity, and the eta bound pass. Paired `gamma=1` and wrong-sign controls are retained in `outputs/claim2_attempt1/results.csv`.

This is **not** an end-to-end SteinDiff inference run, learned diffusion model, image-generation/FID evaluation, or universal theorem verification. The candidate is deliberately synthetic and the finite particle averages only diagnose the stated formula. Evidence and checksums: `outputs/claim2_attempt1/`.
