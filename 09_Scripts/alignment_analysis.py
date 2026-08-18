#!/usr/bin/env python3
"""
alignment_analysis.py

Reads a Clustal-format multiple sequence alignment (e.g.
03_Alignments/PPE18_alignment.aln) and computes:
  - a pairwise percent-identity matrix across all aligned sequences
  - the number and positions of fully conserved columns
  - the number and positions of variable columns (any disagreement, gaps
    included)
  - a per-lineage variability summary, if sequence headers/IDs contain a
    recognizable lineage tag (e.g. "Lineage_1", "lineage 2", etc.) — this is
    best-effort and simply reports "unclassified" for anything it can't
    parse a lineage from

This script parses the standard Clustal alignment block format directly, so
it has no dependency on BioPython. If BioPython is installed, that's fine
too — it just isn't required here.

Usage:
    python alignment_analysis.py path/to/PPE18_alignment.aln
    python alignment_analysis.py path/to/PPE18_alignment.aln --out identity_matrix.csv
"""

import argparse
import csv
import re
import sys
from pathlib import Path


def parse_clustal(path: Path):
    """
    Parses a Clustal-format alignment file into an ordered dict of
    {sequence_id: aligned_sequence_string}.

    Clustal files look like repeated blocks of:
        seq_id1     AC-GT...
        seq_id2     AC-GT...
                     * * *   (consensus line, ignored)
    """
    sequences = {}
    order = []
    header_seen = False

    with open(path, "r") as fh:
        for raw_line in fh:
            line = raw_line.rstrip("\n")
            if not line.strip():
                continue
            if not header_seen:
                # First non-empty line is usually "CLUSTAL O(1.2.4) ..." or similar
                header_seen = True
                if line.upper().startswith("CLUSTAL"):
                    continue
            if line.upper().startswith("CLUSTAL"):
                continue
            # Consensus/conservation lines start with whitespace and contain
            # only *, :, ., or spaces after the sequence block — detect and skip.
            stripped = line.strip()
            if set(stripped) <= set("*:. "):
                continue

            # A sequence line: "seq_id<whitespace>ALIGNED_CHARS[  optional count]"
            match = re.match(r"^(\S+)\s+([A-Za-z\-\.\*]+)\s*(\d+)?\s*$", line)
            if not match:
                continue
            seq_id, chunk, _count = match.groups()
            if seq_id not in sequences:
                sequences[seq_id] = []
                order.append(seq_id)
            sequences[seq_id].append(chunk)

    aligned = {seq_id: "".join(chunks) for seq_id, chunks in sequences.items()}
    return order, aligned


def percent_identity(seq_a: str, seq_b: str) -> float:
    """Percent identity over aligned columns, excluding columns where both are gaps."""
    if len(seq_a) != len(seq_b):
        raise ValueError("Sequences must be the same aligned length")
    matches = 0
    compared = 0
    for a, b in zip(seq_a, seq_b):
        if a in "-." and b in "-.":
            continue
        compared += 1
        if a == b:
            matches += 1
    return round(100 * matches / compared, 2) if compared else 0.0


def guess_lineage(seq_id: str) -> str:
    """Best-effort lineage tag extraction from a sequence ID/header."""
    m = re.search(r"lineage[_\s]?(\d)", seq_id, re.IGNORECASE)
    if m:
        return f"Lineage_{m.group(1)}"
    return "unclassified"


def column_conservation(order, aligned):
    """Returns (conserved_columns, variable_columns, alignment_length)."""
    if not aligned:
        return [], [], 0
    length = len(next(iter(aligned.values())))
    conserved = []
    variable = []
    for col in range(length):
        chars = {aligned[seq_id][col] for seq_id in order}
        if len(chars) == 1:
            conserved.append(col + 1)  # 1-indexed for readability
        else:
            variable.append(col + 1)
    return conserved, variable, length


def main():
    parser = argparse.ArgumentParser(
        description="Compute pairwise identity and conservation stats from a Clustal alignment."
    )
    parser.add_argument("alignment", type=Path, help="Path to a Clustal-format .aln file")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional path to write the pairwise identity matrix as CSV",
    )
    args = parser.parse_args()

    if not args.alignment.exists():
        print(f"Error: file not found: {args.alignment}", file=sys.stderr)
        sys.exit(1)

    order, aligned = parse_clustal(args.alignment)
    if not aligned:
        print(f"Error: no sequences parsed from {args.alignment}. Is this a Clustal-format file?", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(order)} aligned sequences from {args.alignment}\n")

    conserved, variable, aln_len = column_conservation(order, aligned)
    print(f"Alignment length (columns): {aln_len}")
    print(f"Fully conserved columns:    {len(conserved)} ({round(100*len(conserved)/aln_len, 1)}%)")
    print(f"Variable columns:           {len(variable)} ({round(100*len(variable)/aln_len, 1)}%)")
    if variable:
        preview = variable[:20]
        more = f" ... (+{len(variable)-20} more)" if len(variable) > 20 else ""
        print(f"First variable column positions (1-indexed): {preview}{more}")
    print()

    # Pairwise identity matrix
    print("Pairwise percent identity matrix:")
    header_row = ["seq_id"] + order
    matrix_rows = [header_row]
    print(" ".join(f"{h[:12]:>12}" for h in header_row))
    for id_a in order:
        row = [id_a]
        for id_b in order:
            pid = percent_identity(aligned[id_a], aligned[id_b])
            row.append(pid)
        matrix_rows.append(row)
        print(" ".join(f"{str(v)[:12]:>12}" for v in row))

    # Per-lineage summary (best-effort tag extraction)
    lineage_counts = {}
    for seq_id in order:
        lineage = guess_lineage(seq_id)
        lineage_counts.setdefault(lineage, []).append(seq_id)
    print("\nPer-lineage grouping (best-effort, based on sequence ID text):")
    for lineage, ids in sorted(lineage_counts.items()):
        print(f"  {lineage}: {len(ids)} sequence(s) -> {', '.join(ids)}")

    if args.out:
        with open(args.out, "w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerows(matrix_rows)
        print(f"\nPairwise identity matrix written to {args.out}")


if __name__ == "__main__":
    main()
