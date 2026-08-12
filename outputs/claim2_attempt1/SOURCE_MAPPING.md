# Claim 2 source mapping

The pinned source archive, example_paper.tex lines 534–635, labels the result thm:mse_decay and defines u_k = x_k - T_theta(x_k), b_k = E[<u_k, x_k - x*>], c_k = E[||u_k||^2], gamma*_k = b_k / c_k, the one-step identity, rho_k, the trajectory product, and the eta bound. The contract retains the numeric name Theorem 4.8 for traceability.

src/claim2_stepwise_decay_toy.py directly computes those quantities from paired synthetic particles. The fixture intentionally uses a synthetic noisy affine candidate, so it cannot establish the theorem for learned diffusion solvers.
