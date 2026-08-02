# Claim 2 source mapping

Pinned `evidence/source/arxiv_source.tar.gz`, `example_paper.tex` lines 534-633, defines `u_k=x_k-T_theta(x_k)`, `b_k=E[<u_k,x_k-x*>]`, `c_k=E[||u_k||^2]`, `gamma*_k=b_k/c_k`, the one-step identity, `rho_k`, trajectory product, and eta bound. `src/claim2_stepwise_decay_toy.py` directly computes those quantities from paired synthetic particles. The fixture intentionally uses a synthetic noisy affine candidate, so it cannot establish the theorem for learned diffusion solvers.
