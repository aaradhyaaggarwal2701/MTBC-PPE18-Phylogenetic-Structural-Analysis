# Phylogenetic Reconstruction — Simple Phylogeny

## Tool

- **Tool:** Simple Phylogeny, EMBL-EBI web service
  (https://www.ebi.ac.uk/jdispatcher/phylogeny/simple_phylogeny)
- **Access date:** [YYYY-MM-DD]
- **Job ID (from EBI dispatcher, if available):** [ ]

## Input

- **Input alignment:** `03_Alignments/PPE18_alignment.aln`

## Parameters

Copy these directly from the Simple Phylogeny job submission page / results
page rather than re-typing from memory:

| Parameter | Value |
|---|---|
| Clustering method | Neighbour-joining |
| Distance correction | OFF |
| Exclude gaps | OFF |
| Bootstrap replicates | Not performed (no bootstrap option in this run) |
| Output tree format | Phylip |
| Percent identity matrix | OFF |

If default EBI settings were used throughout, state that explicitly:

> All parameters were left at EBI Simple Phylogeny default settings
> (Neighbour-joining, no distance correction, gaps not excluded).## Output files

- `04_Trees/PPE18_tree.nwk` — Newick tree
- `04_Trees/PPE18_tree1.png`, `PPE18_tree1.svg` — [describe what this render
  shows, e.g. cladogram / rectangular tree]
- `04_Trees/PPE18_tree2.png`, `PPE18_tree2.svg` — [describe the second
  render, e.g. same tree with branch lengths / different layout]

### Newick tree (verbatim, for reference and reproducibility checks)

```newick
(
(
(
(
(
(
(
(
(
(
WP_057344543.1:0.00256,
WP_031711675.1:0.00256)
:0.00000,
WP_057327482.1:0.00256)
:0.00000,
WP_075878443.1:0.00256)
:0.00000,
WP_023641572.1:0.00256)
:0.00000,
WP_003898765.1:0.00000)
:0.00000,
(
(
WP_052647375.1:0.00000,
WP_057128163.1:0.00000)
:0.00000,
WP_003902024.1:0.00000)
:0.00256)
:0.00000,
WP_031707992.1:0.00256)
:0.00000,
WP_070901859.1:0.00256)
:0.00000,
WP_070894962.1:0.00256)
:0.00000,
(
WP_023643674.1:0.00256,
WP_075862301.1:0.00256)
:0.00000,
WP_009938333.1:0.00256);
```

This confirms most of the README's genetic-distance claims directly: most
pairwise branch lengths are **0.00000**, and the maximum single branch
length in the tree is **0.00256**. `09_Scripts/phylogeny_summary.py` recomputes
true pairwise patristic distances from this file so the numbers in the
README can be verified independently rather than taken on faith.

**⚠️ Discrepancy found while running `phylogeny_summary.py` against this
tree:** the README's Results section states "a maximum observed distance of
approximately 0.00256." Running the script shows the **true maximum
pairwise patristic distance (the sum of both branches between the two most
distant leaf taxa, e.g. WP_057344543.1 and WP_031711675.1) is 0.00512, not
0.00256.** The figure 0.00256 is a single branch length read directly off
the tree diagram — not the distance *between* two taxa, which sums both
their branches back to the shared ancestor. **The README's "Phylogenetic
Relationships" paragraph should be corrected** to state the maximum pairwise
distance is ≈0.00512 (or explicitly clarify that 0.00256 refers to the
longest individual branch length, if that framing is preferred instead).
Both figures are small and support the same "highly conserved, low
divergence" conclusion — only the exact number needs correcting.

## Interpretation notes

Genetic distances reported in the README were originally read as branch
lengths directly off the EBI Simple Phylogeny tree diagram. As found above,
this conflates "branch length" with "pairwise distance" for the maximum
figure — recompute and report actual pairwise patristic distances (using
`09_Scripts/phylogeny_summary.py path/to/PPE18_tree.nwk`) for any future
distance claims, rather than reading individual branch labels off the tree
image.
