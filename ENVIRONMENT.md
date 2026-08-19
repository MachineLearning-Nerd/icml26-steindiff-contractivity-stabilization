# Environment and reproduction boundary

## Policy

This audit uses local CPU and the local GTX 1050 only. It does not use HF Jobs, paid compute, remote execution, or a CPU/GPU upgrade.

## Lightweight checks

From the repository root:

```bash
python3 -m unittest tests/test_claim1_stein_identity.py tests/test_claim2_stepwise_decay.py
python3 src/claim1_stein_identity_toy.py --out /tmp/steindiff-claim1-check
python3 src/claim2_stepwise_decay_toy.py --out /tmp/steindiff-claim2-check
python3 verify_final.py
```

The scripts and tests accept an explicit output directory, so these checks do not overwrite the pinned evidence. The checked-in `SHA256SUMS` files remain the evidence boundary.

## Not executed

- CIFAR-10 EDM sampling;
- ImageNet 64×64 EDM/logSNR sampling;
- LSUN-Bedrooms 256×256 latent-diffusion sampling;
- DPM-Solver++, UniPC, or Heun paper-scale benchmark matrices;
- 50,000-sample FID, IS, or FD-DINOv2 evaluation;
- a learned model's VJP/Hutchinson divergence implementation;
- independent proof validation beyond the finite formula toys.

The pinned paper reports NVIDIA 3090/4090D experiments and pretrained models. Those requirements must not be inferred from the local CPU fixtures.

