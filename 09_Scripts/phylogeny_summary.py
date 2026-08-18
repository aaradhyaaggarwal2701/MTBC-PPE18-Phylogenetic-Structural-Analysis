#!/usr/bin/env python3
"""
phylogeny_summary.py

Reads a Newick-format phylogenetic tree (e.g. 04_Trees/PPE18_tree.nwk) and
computes pairwise patristic (branch-length-sum) distances between every pair
of leaf taxa. This lets you independently verify claims like "most pairwise
distances were 0.00000, with a maximum of ~0.00256" directly from the tree
file, rather than taking the README's numbers on faith.

Uses BioPython's Bio.Phylo module (see requirements.txt) since writing a
correct Newick parser from scratch is easy to get subtly wrong on edge
cases (nested parentheses, unnamed internal nodes, etc.) — this is the one
script in this folder that isn't dependency-free, on purpose.

Usage:
    python phylogeny_summary.py path/to/PPE18_tree.nwk
    python phylogeny_summary.py path/to/PPE18_tree.nwk --out distances.csv
"""

import argparse
import csv
import sys
from itertools import combinations
from pathlib import Path

try:
    from Bio import Phylo
except ImportError:
    print(
        "Error: BioPython is required for this script.\n"
        "Install it with: pip install biopython --break-system-packages\n"
        "(or: pip install -r requirements.txt)",
        file=sys.stderr,
    )
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Compute pairwise patristic distances from a Newick tree."
    )
    parser.add_argument("newick", type=Path, help="Path to a Newick-format .nwk tree file")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional path to write the full pairwise distance table as CSV",
    )
    args = parser.parse_args()

    if not args.newick.exists():
        print(f"Error: file not found: {args.newick}", file=sys.stderr)
        sys.exit(1)

    tree = Phylo.read(args.newick, "newick")
    terminals = tree.get_terminals()
    names = [t.name for t in terminals]

    if len(names) < 2:
        print("Error: tree has fewer than 2 leaf taxa; nothing to compare.", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded tree with {len(names)} leaf taxa from {args.newick}\n")

    pairs = []
    for a, b in combinations(terminals, 2):
        dist = tree.distance(a, b)
        pairs.append((a.name, b.name, round(dist, 5)))

    distances_only = [d for _, _, d in pairs]
    print(f"Total pairwise comparisons: {len(pairs)}")
    print(f"Minimum pairwise distance: {min(distances_only)}")
    print(f"Maximum pairwise distance: {max(distances_only)}")
    print(f"Mean pairwise distance:    {round(sum(distances_only)/len(distances_only), 5)}")
    zero_count = sum(1 for d in distances_only if d == 0.0)
    print(f"Pairs with distance 0.00000: {zero_count} / {len(pairs)} "
          f"({round(100*zero_count/len(pairs), 1)}%)\n")

    # Show the most distant pairs first — usually the most biologically interesting
    pairs_sorted = sorted(pairs, key=lambda x: x[2], reverse=True)
    print("Top 10 most distant pairs:")
    print(f"{'Taxon A':<20} {'Taxon B':<20} {'Distance':>10}")
    for a, b, d in pairs_sorted[:10]:
        print(f"{a:<20} {b:<20} {d:>10}")

    if args.out:
        with open(args.out, "w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["taxon_a", "taxon_b", "distance"])
            writer.writerows(pairs)
        print(f"\nFull pairwise distance table written to {args.out}")


if __name__ == "__main__":
    main()
