# Temporal zero forcing

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21347118.svg)](https://doi.org/10.5281/zenodo.21347118)

Research archive for *Zero forcing on temporal graphs: Layer-local and
footprint-constrained dynamics* by Krishna Harish (Elkins High School,
Missouri City, Texas, United States).

The project develops two synchronous finite-lifetime variants of the standard
zero-forcing color-change rule:

- **Layer-local temporal zero forcing (LL-TZF):** uniqueness is evaluated in
  the active temporal layer.
- **Footprint-constrained temporal zero forcing (FC-TZF):** uniqueness is
  evaluated in the aggregate footprint, while the forcing edge must be active
  in the current layer.

The proved results include sharp growth bounds, exact values for alternating
paths and even cycles, aggregation and time-reversal separations, restricted
NP-completeness and W[2]-hardness, and fixed-parameter algorithms. The
claim-level prior-art assessment is deliberately calibrated: no exact prior
formulation of both invariants was found, but the definitions combine mature
zero-forcing and temporal-graph ideas. See
[`notes/novelty-audit.md`](notes/novelty-audit.md).

## Reproduce the computational checks

Requirements: Python 3.9 or newer and no third-party packages. The archived
release was tested with Python 3.13.7.

```bash
python3 src/verify.py
```

Expected output:

```text
Verified 127 formula instances and 4,096 exhaustive two-layer schedules; wrote .../results/verification.csv
```

The command regenerates `results/verification.csv`. Its expected SHA-256 digest
is `7035cd92c06c06b6fa2b1562d476a89ec541589162dad0811e6fedd5a70cfd45`.

## Archive contents

- [`paper/main.tex`](paper/main.tex) and
  [`paper/output/pdf/temporal-zero-forcing.pdf`](paper/output/pdf/temporal-zero-forcing.pdf):
  manuscript source and rendered PDF.
- [`src/verify.py`](src/verify.py): standard-library verification program.
- [`results/verification.csv`](results/verification.csv): 127 exact formula
  checks and optimum witnesses.
- [`results/verification_summary.json`](results/verification_summary.json):
  pass status and counts for the assertion-only exhaustive checks.
- [`supplement/S1_Code_and_results.zip`](supplement/S1_Code_and_results.zip):
  separately uploadable supporting-information archive.
- [`notes/novelty-audit.md`](notes/novelty-audit.md): claim-level novelty audit,
  closest prior work, and search limits.
- [`CITATION.cff`](CITATION.cff) and [`.zenodo.json`](.zenodo.json): citation and
  archival metadata.

## Citation

Use the citation metadata supplied by GitHub or Zenodo for release `v1.0.0`.
The version-specific DOI is
[`10.5281/zenodo.21347118`](https://doi.org/10.5281/zenodo.21347118). The
all-versions concept DOI is
[`10.5281/zenodo.21347117`](https://doi.org/10.5281/zenodo.21347117).

## Licensing

The verification software and associated documentation are available under
the [MIT License](LICENSE). The manuscript is available under
[CC BY 4.0](paper/LICENSE.md).
