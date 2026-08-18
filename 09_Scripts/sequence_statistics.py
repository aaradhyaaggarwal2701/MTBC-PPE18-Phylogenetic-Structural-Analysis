#!/usr/bin/env python3
"""
sequence_statistics.py

Reads a PPE18 protein multi-FASTA file (e.g. 02_Sequences/PPE18_all_sequences.fasta)
and reports:
  - per-sequence length
  - amino acid composition summary
  - basic length statistics (min/max/mean/stdev)
  - a per-record summary table, written to CSV

This script has no hard dependency on BioPython — it uses a small built-in
FASTA parser so it runs anywhere Python 3 runs. If BioPython is installed
(see requirements.txt), nothing changes; it just isn't required for this
particular script.

Usage:
    python sequence_statistics.py path/to/PPE18_all_sequences.fasta
    python sequence_statistics.py path/to/PPE18_all_sequences.fasta --out stats.csv
"""

import argparse
import csv
import statistics
import sys
from collections import Counter
from pathlib import Path


def parse_fasta(path: Path):
    """Minimal FASTA parser. Yields (header, sequence) tuples."""
    header = None
    seq_chunks = []
    with open(path, "r") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(seq_chunks)
                header = line[1:].strip()
                seq_chunks = []
            else:
                seq_chunks.append(line.strip())
        if header is not None:
            yield header, "".join(seq_chunks)


def amino_acid_composition(seq: str) -> Counter:
    return Counter(seq.upper())


def summarize(records):
    """records: list of (header, sequence)"""
    lengths = [len(seq) for _, seq in records]
    summary = {
        "n_sequences": len(records),
        "min_length": min(lengths) if lengths else 0,
        "max_length": max(lengths) if lengths else 0,
        "mean_length": round(statistics.mean(lengths), 2) if lengths else 0,
        "stdev_length": round(statistics.stdev(lengths), 2) if len(lengths) > 1 else 0.0,
    }
    return summary


def main():
    parser = argparse.ArgumentParser(description="Summarize PPE18 protein sequence statistics.")
    parser.add_argument("fasta", type=Path, help="Path to a protein multi-FASTA file")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional path to write a per-sequence CSV summary (default: print to stdout only)",
    )
    args = parser.parse_args()

    if not args.fasta.exists():
        print(f"Error: file not found: {args.fasta}", file=sys.stderr)
        sys.exit(1)

    records = list(parse_fasta(args.fasta))
    if not records:
        print(f"Error: no FASTA records found in {args.fasta}", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(records)} sequences from {args.fasta}\n")

    # Overall length statistics
    overall = summarize(records)
    print("Overall length statistics:")
    for k, v in overall.items():
        print(f"  {k}: {v}")
    print()

    # Per-sequence table
    rows = []
    for header, seq in records:
        comp = amino_acid_composition(seq)
        most_common_aa, most_common_count = comp.most_common(1)[0] if comp else ("-", 0)
        rows.append(
            {
                "header": header,
                "length": len(seq),
                "most_common_aa": most_common_aa,
                "most_common_aa_count": most_common_count,
                "unique_aa_count": len(comp),
            }
        )

    print("Per-sequence summary:")
    print(f"{'Header':<60} {'Length':>7} {'Most common AA':>16} {'Unique AAs':>11}")
    for r in rows:
        header_short = (r["header"][:57] + "...") if len(r["header"]) > 60 else r["header"]
        print(
            f"{header_short:<60} {r['length']:>7} "
            f"{r['most_common_aa'] + ' (' + str(r['most_common_aa_count']) + ')':>16} "
            f"{r['unique_aa_count']:>11}"
        )

    if args.out:
        with open(args.out, "w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nPer-sequence CSV written to {args.out}")


if __name__ == "__main__":
    main()
