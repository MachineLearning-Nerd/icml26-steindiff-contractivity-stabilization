# Source audit

## Pinned paper artifacts

| Artifact | SHA-256 |
| --- | --- |
| `evidence/source/arxiv.pdf` | `96b980d93196b1441ec30ec2ec0f695fdde075d8f96dcd39851e181836bd0ca3` |
| `evidence/source/arxiv_source.tar.gz` | `392b56425f9c7f9e1275c79e971573268637eb384eb3bcb140293259ee100229` |

The source archive contains `example_paper.tex`, bibliography/style files, and the paper's image/figure assets. The archive is retained as evidence; it is not treated as an executable implementation.

## Author-code boundary

The pinned source does not contain an author-code or project URL. A title/method/author search in the prior audit did not identify a separate public implementation. This repository therefore documents the paper and runs independent formula fixtures; it does not claim author-code equivalence.

## Production map

1. A pretrained diffusion model and ODE solver produce the candidate `T_theta(x_k)`.
2. The residual `u_k = x_k - T_theta(x_k)` is evaluated at each inference step.
3. Batch inner products, residual energy, and divergence are combined into the reference-free coefficient.
4. The coefficient is clipped/safeguarded and used in the rectified update.
5. Generated samples are evaluated with FID, IS, and FD-DINOv2 over the listed datasets and NFE budgets.

C1 and C2 cover only a reduced algebraic slice of steps 2–4. They do not exercise a learned diffusion network, Hutchinson VJPs, solver state transitions, or step 5.

## Source anchors

- Rectified update and ideal Gaussian coupling: `example_paper.tex:405-431`.
- Clean-target optimum and Stein estimator: `example_paper.tex:433-492`.
- Step-wise identity, product, and eta bound: `example_paper.tex:534-635`.
- LSUN table: `example_paper.tex:882-903`.
- ImageNet solver comparison: `example_paper.tex:1805-1864`.
- Experimental hardware, datasets, metrics, 50,000 samples, and five probes: `example_paper.tex:2007-2017`.

The contract's theorem names are retained for traceability; source labels such as `thm:stainopt_gamma` and `thm:mse_decay` are the authoritative source anchors.

