# Status
- OpenReview ID: `z0CHTAHame`; submission 2615.
- Paper: *Mitigating the Contractivity Trap in Diffusion ODEs via Stein Stabilization* (arXiv:2606.07835).
- Live contract: six anchored claims / 12 maximum points; snapshot `outputs/live/20260802T183038Z` and immutable copies in `contract/`.
- Duplicate gate: eligible pool excluded local, DineshAI, team-tagged, coordination, and backlog IDs at selection time.
- Source: arXiv source/PDF pinned under `evidence/source/` and SHA-256 verified.
- Compute: local CPU/local GTX 1050 only; no HF CPU-upgrade, Jobs, paid, or remote compute.
- Claim 1: **toy**. The source formula at `example_paper.tex:479-497` was evaluated in a deterministic 1-D Gaussian forward-coupling fixture against its direct MSE optimum; it passed the pre-fixed comparison tolerance. This is not an end-to-end diffusion/FID/theorem verification. Evidence: `outputs/claim1_attempt1/`.
- Next: independent Claim-1 review, then Claim-2 source audit. Publication is blocked.
