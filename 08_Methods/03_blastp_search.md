# BLASTP Search Parameters

Recording exact search parameters is what makes the BLASTP step reproducible.
Fill these in from the NCBI BLAST job you ran — either from the parameters
panel on the results page, or from your BLAST search history
(https://blast.ncbi.nlm.nih.gov/Blast.cgi under "Recent Results").

## Search configuration

| Parameter | Value |
|---|---|
| BLAST program | BLASTP (protein-protein BLAST) |
| Query | PPE18 (Rv1196) reference protein, H37Rv |
| Database | nr (non-redundant protein sequences) |
| Organism restriction | *Mycobacterium tuberculosis* (taxid: 1773) |
| Algorithm | blastp |
| Max target sequences | 100 |
| Short queries | Automatically adjust parameters for short input sequences: enabled |
| Expect (E) value threshold | 0.05 |
| Word size | 5 |
| Max matches in a query range | 0 (no limit) |
| Matrix | BLOSUM62 |
| Gap costs | Existence: 11, Extension: 1 |
| Compositional adjustments | Conditional compositional score matrix adjustment |
| Filter low-complexity regions | No |
| Mask for lookup table only | No |
| Mask lower case letters | No |
| Search date | 2026-08-19 |

## Hit selection criteria

- **Minimum % identity:** No explicit filter applied — the Percent Identity /
  E value / Query Coverage filter boxes on the results page were left blank.
- **Minimum query coverage:** No explicit filter applied (observed hits were
  ~100% query coverage without filtering).
- **Maximum E-value accepted:** No explicit filter applied (observed hits
  were E = 0.0 without filtering).
- **Number of hits retained:** 100 (all hits returned under the search's
  "Max target sequences = 100" setting; all 100 were selected via "select
  all" for downstream use).
- **Any hits manually excluded, and why:** None — all 100 returned hits were
  retained as-is.

## BLAST job record

| Field | Value |
|---|---|
| Job Title | PPE18_H37Rv |
| RID (Request ID) | 89C09VE4014 |
| Query ID | lcl\|Query_6556196 |
| Molecule type | amino acid |
| Query Length | 391 aa |
| Organism filter | Mycobacterium tuberculosis (taxid:1773) |

## Output files

- Raw BLASTP results (hit table / alignment view): downloaded from RID
  89C09VE4014 (note: NCBI BLAST results expire ~48h after the search — export
  and save the hit table/FASTA locally if not already archived in this repo)
- Retained hit accessions: see `02_Sequences/PPE18_all_sequences.fasta`
  headers; representative top hits include WP_003898765.1 (100.00% identity,
  100% query coverage — exact match to the H37Rv query), followed by a large
  set of WP_* accessions at 99.74% identity, 100% query coverage, E = 0.0
