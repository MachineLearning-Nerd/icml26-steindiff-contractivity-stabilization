# Claim 2 source-faithful toy protocol

Source: the theorem labeled thm:mse_decay in example_paper.tex lines 534–635. The contract calls this theorem Theorem 4.8. Fixed before run: seed = 20260802; n = 50000 paired one-dimensional particles; N = 4; lambda = 0.35; candidate noise standard deviation = 0.25.

At each step T(x) = x - lambda * (x - x*) + xi, u = x - T(x), and gamma* = mean(u * (x - x*)) / mean(u^2). Primary metrics are the theorem one-step identity E_(k-1) = E_k - b_k^2 / c_k, the trajectory product, and the eta bound. Controls report gamma = 1 (vanilla) and -gamma* (wrong sign) on the same particle and candidate-noise draws.

Pass iff every finite-sample identity error is at most 1e-12, product error is at most 1e-12, all c_k are positive, 0 <= rho_k <= 1, and the eta bound holds. This is a finite synthetic formula fixture: it is not a learned diffusion model, Algorithm 1 estimator, image/FID result, or universal theorem verification.
