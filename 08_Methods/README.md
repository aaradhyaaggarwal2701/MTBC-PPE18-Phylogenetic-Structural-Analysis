# Methods & Reproducibility

This folder documents the exact parameters, tools, and criteria used at
every stage of the analysis, so the pipeline described in the main
[README.md](../README.md) can be independently reproduced or audited.

Each numbered file corresponds to one stage of the workflow:

| File | Stage |
|---|---|
| [`01_genome_retrieval.md`](01_genome_retrieval.md) | BV-BRC genome selection criteria + full accession metadata table |
| [`dataset_metadata.csv`](dataset_metadata.csv) | Machine-readable version of the genome metadata table |
| [`02_reference_sequence.md`](02_reference_sequence.md) | Mycobrowser PPE18 (Rv1196) reference sequence retrieval |
| [`03_blastp_search.md`](03_blastp_search.md) | NCBI BLASTP search parameters and hit-selection thresholds |
| [`04_multiple_sequence_alignment.md`](04_multiple_sequence_alignment.md) | Clustal Omega alignment parameters |
| [`05_phylogenetic_reconstruction.md`](05_phylogenetic_reconstruction.md) | EMBL-EBI Simple Phylogeny settings and tree outputs |
| [`06_structural_modelling.md`](06_structural_modelling.md) | SWISS-MODEL template information and quality scores |
| [`07_structural_validation.md`](07_structural_validation.md) | Ramachandran / structural validation method and results |

## Status

Most fields in these files are now filled in with confirmed data from the
actual analysis sessions (BV-BRC, NCBI BLASTP, EBI Clustal Omega, EBI Simple
Phylogeny, SWISS-MODEL/MolProbity). Remaining `[ ]` placeholders are minor
(e.g. exact access dates, a couple of SWISS-MODEL similarity/coverage
figures) — see each file for what's still open.

**Two substantive findings surfaced while completing these docs, both now
documented and corrected:**

1. **Genome dataset composition** (`01_genome_retrieval.md`): the 18 files
   in `01_Genomes/` correspond to only 8 distinct genome assemblies, not 18
   independent isolates — confirmed by direct testing against BV-BRC's full
   624-genome *M. tuberculosis* pool. The main README's Dataset and
   Limitations sections have been updated to reflect this honestly.
2. **Phylogenetic distance figure** (`05_phylogenetic_reconstruction.md`):
   the originally reported "max distance ≈ 0.00256" was a single branch
   length, not a true pairwise distance. The correct maximum pairwise
   patristic distance, recomputed with `09_Scripts/phylogeny_summary.py`, is
   **0.00512**. The main README's Results section has been corrected.
