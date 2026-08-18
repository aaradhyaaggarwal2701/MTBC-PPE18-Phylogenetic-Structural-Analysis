# Structural Quality Assessment — Ramachandran Analysis

## Tool

- **Tool used:** MolProbity (via SWISS-MODEL Structure Assessment)
- **Access date:** [YYYY-MM-DD]
- **Input structure:** `05_Structures/PPE18_structure.pdb` (Model 01, chain A)

## Results — Ramachandran analysis

| Metric | Value |
|---|---|
| Ramachandran favoured | 89.97% |
| Ramachandran outliers | 3.34% |
| Ramachandran allowed (favoured + allowed = 100% − outliers) | 6.69% (derived: 100% − 89.97% − 3.34%) |
| Residues flagged as Ramachandran outliers | A374 VAL, A304 GLY, A367 ALA, A354 MET, A298 SER, A341 THR, A355 LEU, A216 GLN, A344 THR, A349 ARG, A345 SER, A359 PRO, A366 ARG |

## Results — full MolProbity report

MolProbity reports several additional structure-quality metrics beyond the
Ramachandran plot; recording them here gives a fuller picture of model
quality than the Ramachandran percentage alone.

| Metric | Value |
|---|---|
| MolProbity score | 1.59 |
| Clash score | 0.55 |
| Rotamer outliers | 2.94% (A289 MET, A355 LEU, A221 SER, A266 LEU, A296 LEU, A215 THR, A219 THR, A332 THR) |
| C-beta deviations | 10 (A341 THR, A366 ARG, A353 GLN, A216 GLN, A348 GLU, A344 THR, A298 SER, A354 MET, A367 ALA, A374 VAL) |
| Bad bonds | 1 / 2796 (A324 TRP) |
| Bad angles | 33 / 3825 |
| Cis non-proline | 5 / 364 |
| Twisted non-proline | 12 / 364 |
| Twisted prolines | 1 / 26 (A358 LEU–A359 PRO) |

## Output

- **Plot file:** `05_Structures/PPE18_Ramachandran.png`

## Interpretation

A MolProbity score of **1.59** is a good result — MolProbity scores are
percentile-ranked against structures of comparable resolution, and lower is
better; scores below ~2.0 are generally considered good quality, with very
high-resolution crystal structures typically scoring below 1.0. The clash
score of 0.55 (very low steric clash) and **89.97% of residues in favoured
Ramachandran regions** both support the claim in the README that the model
is structurally plausible.

The main quality concerns are concentrated in a small, specific stretch of
the model: most Ramachandran outliers, rotamer outliers, and C-beta
deviations cluster around residues ~298–374 (e.g. A341 THR, A344 THR,
A345 SER, A349 ARG, A354 MET, A355 LEU, A366 ARG, A367 ALA, A374 VAL appear
repeatedly across multiple metrics). This suggests one region of the model
— rather than the structure as a whole — is comparatively less reliable and
should be flagged as lower-confidence if this region is discussed
biologically (e.g. in any claims about a specific domain or binding site
falling in that range).

Because the template used for structural modelling was itself an AlphaFold
DB prediction rather than an experimental structure (see
`06_structural_modelling.md`), these MolProbity scores should be read as
validating the internal geometric quality of the SWISS-MODEL output, not as
confirmation of biological accuracy against an experimentally solved PPE18
structure.
