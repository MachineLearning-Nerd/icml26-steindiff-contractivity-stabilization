# Branch and attribution audit

| Item | Required state | Evidence |
| --- | --- | --- |
| Canonical repository | `MachineLearning-Nerd/icml26-steindiff-contractivity-stabilization` | `git remote -v`, `verify_final.py` |
| Former repository | `MachineLearning-Nerd/icml26-repro-z0CHTAHame-steindiff-contractivity-trap` | `AUTONOMOUS_STATE.json` |
| Canonical branch | `main` | local and fresh-clone branch checks |
| Local branch set | exactly `main` | `verify_final.py` |
| Stale backup refs | none under `refs/original` | `verify_final.py` |
| Commit identity | `MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>` for author and committer | every reachable `main` commit checked by `verify_final.py` |
| Co-authorship trailers | none | commit-message scan in `verify_final.py` |

The pinned source does not identify an author-maintained GitHub implementation or project URL. The current repository is therefore an independent formula/toy audit, not a mirror of author code.

Only `main` is used. No orx, experiment, or stale legacy branch contributes evidence to the verdict.

