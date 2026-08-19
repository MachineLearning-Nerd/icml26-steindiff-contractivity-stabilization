# Reproduction report

## Result

`INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOYS`

The repository is a source-pinned audit with two finite algebra fixtures, not a full diffusion sampling reproduction.

| Claim | Local evidence | Verdict |
| --- | --- | --- |
| C1 | One-dimensional Gaussian Stein coefficient comparison | Toy only |
| C2 | Four-step finite one-dimensional MSE identity/product/eta check | Toy only |
| C3 | LSUN table and protocol pinned | Unverified paper result |
| C4 | ImageNet solver table and 45.8% row pinned | Unverified paper result |
| C5 | Algorithm and Hutchinson protocol source-audited | Implementation unverified |
| C6 | Dataset/solver/metric setup source-audited | Benchmark matrix unverified |

## Publication gate

`publication_allowed: false` for any paper-scale score, theorem validation, or end-to-end SteinDiff claim.

## Next checkpoint

If the required model checkpoints, datasets, dependencies, and compute become available, audit C3 first. Any new result must preserve the exact solver, schedule, NFE, sample count, evaluator, control, and hash artifacts.

