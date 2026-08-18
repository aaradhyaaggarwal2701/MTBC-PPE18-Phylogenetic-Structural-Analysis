# Multiple Sequence Alignment — Clustal Omega

## Tool

- **Tool:** Clustal Omega, EMBL-EBI web service
  (https://www.ebi.ac.uk/jdispatcher/msa/clustalo)
- **Access date:** [YYYY-MM-DD]
- **Job ID (from EBI dispatcher, if available):** [ ]

## Input

- **Input file:** `02_Sequences/PPE18_all_sequences.fasta`
- **Number of sequences aligned:** 15
- **Sequence type:** Protein

## Parameters

The EBI Clustal Omega job page shows the exact parameters used under "Show
more options" before submission, and lists them again on the results page —
copy them from there rather than re-typing from memory.

| Parameter | Value |
|---|---|
| Output alignment format | ClustalW with character counts |
| Order | Aligned |
| Number of iterations (`--iterations`) | Combined iterations: default (0) |
| Max guide tree iterations | Default |
| Max HMM iterations | Default |
| Other non-default options changed | Output guide tree: yes · Distance matrix: no · Dealign input: no · mBed-like clustering guide-tree: yes · mBed-like clustering iteration: yes · Sequence type: protein |

If default EBI settings were used throughout, state that explicitly:

> All parameters were left at EBI Clustal Omega default settings.

## Output

- **Alignment file:** `03_Alignments/PPE18_alignment.aln`
- **Alignment length (with gaps, columns):** [ ]
- **% overall sequence identity reported by Clustal Omega (if available from
  the percent identity matrix):** [ ]

## Notes

Note here whether any post-alignment manual trimming or editing was
performed (e.g. removing a poorly aligned terminal region), or state "used
as generated, no manual edits."
