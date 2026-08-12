# Claim 1 protocol

The pinned source's reference-free estimator is at example_paper.tex lines 486–492; the Stein identity used to derive it is at lines 479–482. This deterministic one-dimensional Gaussian-forward-coupling fixture evaluates that formula and independently compares it with the direct MSE-optimal gamma. It is a reduced toy and does not verify trained diffusion or FID results.

Pre-execution fixed: seed 20260802; n = 200000; alpha = 0.8; sigma = 0.6; u = 1.7x; pass iff the absolute direct-versus-Stein gamma difference is below 0.01. Claim 1 formula toy only.
