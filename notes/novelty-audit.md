# Claim-level novelty audit

Search date: 2026-07-12.

## Verdict

**Potentially novel, medium confidence.** No indexed paper, preprint, thesis,
repository, or relevant patent located in the search defines both of the exact
invariants studied here.  The bare move of putting zero forcing on a temporal
graph nevertheless has substantial obvious-combination risk.  Defensible
novelty lies in exact formulas, structural separations, restricted hardness,
and algorithms.

## Atomic claims

| Claim | Closest prior work | Assessment |
|---|---|---|
| Persistent seed diffusion on temporal layers | Schierreich, temporal target-set selection (AAAI 2023) | Framework known; source-side unique-neighbor rule differs |
| Zero forcing with changing network structure | Mousavi--Haeri--Mesbahi (IEEE TAC 2021) | Strong application-level overlap; no finite chronological layer process |
| Layer-local versus footprint-constrained uniqueness | No close source found | Strongest definitional gap |
| Temporal-versus-aggregate seed differences | Michalski et al. (2014) | General phenomenon known; exact TZF separations may be new |
| Lifetime-two hardness | Temporal target-set selection already has it | Do not claim broadly; only rule-specific restricted hardness survives |
| Footprint-constrained forcing chains | Chakraborty et al. (MFCS 2024) and Cioni et al. (arXiv 2026) on temporal path covers | Close structural adjacency; forcing additionally requires footprint uniqueness |
| Temporal paths and trees | Static propagation time and temporal path-cover work | Exact TZF formulas/characterizations remain promising |
| One-layer version | Maximum open irredundance | Already known under another name |
| Reversal of forcing chains | Barioli et al. (2010) for static zero forcing | Static fact known; temporal schedule preservation is the possible new step |

## Closest sources

1. S. Schierreich, *Maximizing Influence Spread through a Dynamic Social
   Network*, AAAI 37 (2023), DOI:
   [10.1609/aaai.v37i13.27018](https://doi.org/10.1609/aaai.v37i13.27018).
2. M. V. Srighakollapu, R. K. Kalaimani, and R. Pasumarthy, *On Strong
   Structural Controllability of Temporal Networks*, IEEE Control Systems
   Letters 6 (2022), DOI:
   [10.1109/LCSYS.2021.3133320](https://doi.org/10.1109/LCSYS.2021.3133320).
3. S. S. Mousavi, M. Haeri, and M. Mesbahi, *Strong Structural
   Controllability of Networks under Time-Invariant and Time-Varying
   Topological Perturbations*, IEEE TAC 66 (2021),
   [preprint](https://arxiv.org/abs/1904.09960).
4. L. Hogben et al., *Propagation Time for Zero Forcing on a Graph*,
   Discrete Applied Mathematics 160 (2012), DOI:
   [10.1016/j.dam.2012.04.003](https://doi.org/10.1016/j.dam.2012.04.003).
5. S. Yadav et al., *Finding a Minimum Source Set in Temporal Graphs*,
   Theoretical Computer Science 1060 (2026), DOI:
   [10.1016/j.tcs.2025.115624](https://doi.org/10.1016/j.tcs.2025.115624).
6. M. R. Fellows et al., *The Private Neighbor Cube*, SIAM Journal on
   Discrete Mathematics 7 (1994), DOI:
   [10.1137/S0895480191199026](https://doi.org/10.1137/S0895480191199026).
7. D. Chakraborty, A. Dailly, F. Foucaud, and R. Klasing, *Algorithms and
   Complexity for Path Covers of Temporal DAGs*, MFCS 2024, DOI:
   [10.4230/LIPIcs.MFCS.2024.38](https://doi.org/10.4230/LIPIcs.MFCS.2024.38).
8. L. Cioni et al., *Temporal Path Covers: Dilworth Properties and
   Parameterized Complexity*, arXiv:2607.00118 (revised 2026-07-03),
   [preprint](https://arxiv.org/abs/2607.00118).
9. F. Barioli et al., *Zero Forcing Parameters and Minimum Rank Problems*,
   Linear Algebra and its Applications 433 (2010), DOI:
   [10.1016/j.laa.2010.03.008](https://doi.org/10.1016/j.laa.2010.03.008).
10. N. Monshizadeh, S. Zhang, and M. K. Camlibel, *Zero Forcing Sets and
    Controllability of Dynamical Systems Defined on Graphs*, IEEE TAC 59
    (2014), DOI:
    [10.1109/TAC.2014.2308619](https://doi.org/10.1109/TAC.2014.2308619).

The July 2026 exact-phrase sweep for “temporal zero forcing” and “dynamic
zero forcing” found signal-processing uses of zero-forcing equalization and
beamforming, but no graph color-change parameter matching either definition.
Those name collisions are irrelevant prior art for the graph invariant but
are a reason to define the terminology carefully.

## Safe positioning

> We introduce and analyze two temporally scheduled variants of the standard
> zero-forcing color-change rule, distinguished by whether uniqueness is
> evaluated in the current layer or in the aggregate footprint.  Prior
> temporal diffusion, path-cover, and controllability models do not appear to
> study these exact invariants.  We establish exact formulas, asymptotic separations,
> restricted hardness, and parameterized algorithms.

Do not claim the first temporal seed-selection model, the first comparison of
temporal and aggregate diffusion, the first lifetime-two hardness result, or
the first connection between zero forcing and time-varying controllability.

## Search limits

The search covered exact and synonym queries across scholarly indexes,
preprints, theses, repositories, patents, temporal diffusion, graph searching,
temporal path covers, and controllability literature.  Paywalled full text, non-English work,
unindexed workshops, private manuscripts, and future disclosures remain blind
spots.  “Not found” is not proof of nonexistence.
