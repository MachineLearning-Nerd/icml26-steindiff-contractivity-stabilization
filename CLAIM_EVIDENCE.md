# Claim-to-evidence ledger

This ledger separates the six challenge claims, the paper's production paths, and the evidence actually stored here. `Toy` means a finite local formula fixture. `Source-supported` means the pinned source contains the stated method or result. None of the paper-scale image claims is marked reproduced.

## Overall verdict

`INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOYS` — C1 and C2 have bounded deterministic CPU toys; C3–C6 remain paper/source claims without learned diffusion sampling, generated images, FID/IS/FD-DINOv2 outputs, or an independent implementation. `publication_allowed` remains `false`.

## Claims

### C1 — reference-free Stein coefficient

**Contract claim:** SteinDiff derives a reference-free Stein-identity estimator for the MSE-optimal correction coefficient.

**How the paper produces it:** define the rectified update in `example_paper.tex` lines 405–414, assume the ideal Gaussian forward coupling at lines 422–431, derive the clean-target optimum at lines 433–455, and apply Stein's identity at lines 479–492. The source labels the reference-free result `thm:stainopt_gamma`.

**Evidence here:** `src/claim1_stein_identity_toy.py` uses a fixed one-dimensional Gaussian coupling and linear residual candidate, computes the direct MSE-optimal coefficient and the source expression, and records the difference in `outputs/claim1_attempt1/`.

**Status:** `TOY_SOURCE_STEIN_IDENTITY`. The finite check is not a learned score model, Hutchinson implementation, discretized sampler, or theorem proof.

### C2 — step-wise error decay

**Contract claim:** Theorem 4.8 gives `E_0^Stein <= (1-eta)^N E_N` over N inference steps.

**How the paper produces it:** define `u_k`, `b_k`, `c_k`, and `gamma_k*=b_k/c_k`; establish the exact one-step identity; define `rho_k`; multiply the trajectory factors; and upper-bound them with `eta = min rho_k`. The pinned source labels this result `thm:mse_decay` at `example_paper.tex` lines 534–635.

**Evidence here:** `src/claim2_stepwise_decay_toy.py` runs four finite one-dimensional paired-particle steps with a synthetic noisy affine candidate and records the one-step identity, product, eta bound, and controls in `outputs/claim2_attempt1/`.

**Status:** `TOY_SOURCE_STEPWISE_DECAY_ALGEBRA`. This is not learned SteinDiff inference, Algorithm 1, a universal theorem validation, or image generation.

### C3 — LSUN-Bedrooms FID

**Contract claim:** at 256×256 LSUN-Bedrooms and 5 NFE, FID falls from 21.29 to 7.64.

**How the paper produces it:** run the Latent Diffusion model with DPM-Solver++ and SteinDiff at the listed NFE values, generate the evaluation set, and compute FID. The source table `tab:ldm_lsun_beds` is at lines 882–903; the 5-NFE rows are lines 895–897.

**Evidence here:** the pinned source contains the reported values, but no LSUN model, generated sample set, sampler run, or FID evaluator is stored.

**Status:** `UNVERIFIED_PAPER_REPORTED_ONLY`.

### C4 — ImageNet FID reduction

**Contract claim:** ImageNet 64×64 has FID reductions up to 45.8% with gains across DPM-Solver++ and UniPC.

**How the paper produces it:** run the ImageNet 64×64 model under logSNR and EDM schedules with DPM-Solver++, UniPC, and Heun, compare base versus SteinDiff FID, and compute the percentage improvements. The source table is `tab:sampler_comparison_with_improv` at lines 1805–1864; the 45.8% row is line 1819 for logSNR/Heun at 3 steps.

**Evidence here:** the source table and protocol are pinned; no ImageNet model, samples, evaluator, or solver matrix is reproduced locally.

**Status:** `UNVERIFIED_PAPER_REPORTED_ONLY`.

### C5 — Algorithm 1 implementation

**Contract claim:** Algorithm 1 uses batch statistics, Hutchinson divergence estimation, and a lower clip `gamma_min`.

**How the paper produces it:** compute `s_xu`, `s_uu`, and `s_div` from a batch, estimate the divergence with Hutchinson probes, form the stabilized coefficient, apply the lower safeguard, and use it in the solver update. The algorithm and estimator discussion are in the pinned source around lines 665–706; the setup states five random probes at lines 2007–2013.

**Evidence here:** source text and the two formula fixtures are present. There is no independent high-dimensional PyTorch module, VJP/Hutchinson run, or author implementation to execute.

**Status:** `SOURCE_SUPPORTED_IMPLEMENTATION_UNVERIFIED`.

### C6 — solver and benchmark coverage

**Contract claim:** SteinDiff is evaluated against DPM-Solver++, UniPC, and Heun on CIFAR-10, ImageNet 64×64, and LSUN-Bedrooms 256×256 using FID, IS, and FD-DINOv2 at 5–20 NFE.

**How the paper produces it:** use the listed public solvers and pretrained models, generate 50,000 samples for FID, compute IS and FD-DINOv2, and compare NFE curves and tables. The source setup at lines 2007–2017 names the datasets, hardware, metrics, sample count, and five Hutchinson probes.

**Evidence here:** the source archive and protocol description are pinned. The complete benchmark matrix, generated images, metric environments, and solver outputs are absent.

**Status:** `SOURCE_SUPPORTED_BENCHMARK_UNVERIFIED`.

## Evidence boundary

The C1/C2 toys validate finite algebra under their declared synthetic inputs. They do not validate the learned diffusion model, the reference-free estimator in high dimension, the discretized sampler, the theorem for all allowed distributions, or any paper-reported image-quality value.

