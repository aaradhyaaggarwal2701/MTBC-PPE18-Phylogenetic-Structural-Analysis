# Three-Dimensional Structural Modelling — SWISS-MODEL

## Tool

- **Tool:** SWISS-MODEL (https://swissmodel.expasy.org/)
- **Access date:** [YYYY-MM-DD]
- **SWISS-MODEL project/job ID:** [ ]

## Target sequence

- **Sequence modelled:** PPE18 (Rv1196), H37Rv reference background
- **Sequence length modelled (aa):** 391
- **Modelling mode:** Automated template search (SWISS-MODEL searched 28 candidate templates and selected the top match automatically)

## Template information

This is the single most important piece of missing metadata for
reproducibility — SWISS-MODEL always reports which experimental structure(s)
it used as a template. Copy this directly from the SWISS-MODEL results page
("Template" section):

| Field | Value |
|---|---|
| Template accession | L7N675.1.A |
| Template chain | A |
| Template description | AlphaFold DB model of PPE18_MYCTU (gene: PPE18), organism *Mycobacterium tuberculosis* strain ATCC 25618 / H37Rv |
| Sequence identity to template (%) | 100.00% |
| Sequence similarity to template (%) | [ ] |
| Coverage of target sequence (%) | ~72% (approx.) — the QMEANDisCo local quality plot shows strong template-based confidence (0.5–0.8 similarity) from roughly residue 1 to ~280, then drops sharply to a flat low-confidence region (~0.2–0.3) from ~280–391. Confirm the exact modelled residue range from the SWISS-MODEL "Download files" output. |
| GMQE (Global Model Quality Estimate) | 0.69 |
| QMEANDisCo global score | 0.53 ± 0.05 |
| Method (template structure) | **AlphaFold DB predicted model — not an experimentally determined structure.** No X-ray/Cryo-EM resolution applies; the template itself is a computational prediction, so this PPE18 model is a homology model built on a predicted template rather than an experimental one. |

**Additional model metadata:**
- **Oligomeric state:** Monomer
- **Model rank:** Model 01 (of 2 models generated), ranked by GMQE
- **Templates searched:** 28
- **Target sequence length:** 391 aa (matches full-length PPE18)

## Output

- **Model file:** `05_Structures/PPE18_structure.pdb`
- **Model render:** `05_Structures/PPE18_structure.png`
- **Model quality/validation report:** [attach or link if downloaded
  separately from SWISS-MODEL]

## Notes

**Important:** The structural model was built using an AlphaFold DB predicted
structure (L7N675.1.A) as the template, not an experimentally determined
structure (X-ray/Cryo-EM/NMR). This means the PPE18 model here is a
homology model built on a computational prediction, one step removed from
experimental structural data. This should be stated explicitly in the README
and in any discussion of "structural validation," since Ramachandran/QMEAN
scores assess internal geometric plausibility of the model — they do not
substitute for validation against an experimentally solved PPE18 structure
(none exists publicly at the time of writing, which is itself worth noting).

State whether the model covers the full-length PPE18 protein or only a
domain/partial region (common for PPE proteins with disordered C-terminal
regions), since this materially affects how the structure should be
interpreted. Based on the model summary bar, template coverage appears
limited to roughly the N-terminal region of the 391-aa protein — confirm the
exact modelled range from the "Download files" output before finalizing this
note.
