# S1 File: code and machine-readable verification results

This supplement accompanies *Zero forcing on temporal graphs: Layer-local and
footprint-constrained dynamics* by Krishna Harish.

Version 1.0.0 is permanently archived at
[doi:10.5281/zenodo.21347118](https://doi.org/10.5281/zenodo.21347118). The
development repository is available at
<https://github.com/krishnatheaverage/temporal-zero-forcing>.

## Contents

- `src/verify.py` implements the two synchronous temporal zero-forcing rules,
  ordinary static zero forcing, exact seed-set enumeration, and the complete
  verification suite.
- `results/verification.csv` contains 127 checked formula instances and one
  optimum witness for each instance.
- `results/verification_summary.json` records the pass status and counts for
  the assertion-only exhaustive checks.
- `environment.txt` records the tested Python and operating-system versions.
- `LICENSE` contains the MIT software license.

## Requirements

- Python 3.9 or newer; tested with Python 3.13.7.
- No third-party Python packages.

## Reproduction

From the extracted `S1_Code_and_results` directory, run:

```bash
python3 src/verify.py
```

Expected terminal message:

```text
Verified 127 formula instances and 4,096 exhaustive two-layer schedules; wrote .../results/verification.csv
```

On the tested machine the run takes about seven seconds. The regenerated CSV
has SHA-256 digest:

```text
7035cd92c06c06b6fa2b1562d476a89ec541589162dad0811e6fedd5a70cfd45
```

## CSV columns

- `family`: checked temporal-graph family.
- `n`: number of labeled vertices.
- `lifetime`: number of temporal layers.
- `semantics`: layer-local, footprint-constrained, or static zero forcing.
- `computed`: exact value returned by exhaustive enumeration.
- `formula`: theorem value checked by the script.
- `witness`: one optimum zero-indexed seed set, space-separated.

The 4,096 universal two-layer checks are assertions rather than CSV rows. They
independently test dominance and footprint-constrained time-reversal invariance
for every temporal graph on four labeled vertices; their pass status and counts
are recorded in `results/verification_summary.json`.
