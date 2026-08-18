# Analysis Scripts

Three standalone Python scripts that recompute and verify claims made
elsewhere in this repository directly from the underlying data files,
rather than asking a reader to take the README's numbers on faith.

## Setup

```bash
pip install -r requirements.txt
```

(`sequence_statistics.py` and `alignment_analysis.py` have no external
dependencies and will run with plain Python 3; only `phylogeny_summary.py`
needs BioPython.)

## Scripts

### `sequence_statistics.py`
Reads a protein multi-FASTA file and reports sequence length statistics and
amino acid composition per sequence.

```bash
python sequence_statistics.py ../02_Sequences/PPE18_all_sequences.fasta
python sequence_statistics.py ../02_Sequences/PPE18_all_sequences.fasta --out stats.csv
```

### `alignment_analysis.py`
Reads a Clustal-format alignment (`.aln`) and computes a pairwise percent-
identity matrix, plus conserved vs. variable column counts.

```bash
python alignment_analysis.py ../03_Alignments/PPE18_alignment.aln
python alignment_analysis.py ../03_Alignments/PPE18_alignment.aln --out identity_matrix.csv
```

### `phylogeny_summary.py`
Reads the Newick tree and recomputes true pairwise patristic distances
between every pair of leaf taxa — this is what caught and corrected a real
error in an earlier draft of this README (a single branch length was being
reported as a "maximum pairwise distance," when the two figures aren't the
same thing).

```bash
python phylogeny_summary.py ../04_Trees/PPE18_tree.nwk
python phylogeny_summary.py ../04_Trees/PPE18_tree.nwk --out distances.csv
```

## Why these exist

Anyone can claim "PPE18 is highly conserved" or "max distance ≈ X" in a
README. These scripts let a reader independently regenerate those specific
numbers from the raw data files in this repo, in under a second per script,
with no manual steps. That's the difference between a repo that *reports*
an analysis and one that *demonstrates* it.
