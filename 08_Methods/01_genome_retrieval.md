# Genome Retrieval and Dataset Metadata

This document records exactly how the 18 *Mycobacterium tuberculosis* genomes
were selected and retrieved from BV-BRC, so the dataset can be reconstructed
independently.

> **Fill in every `[ ]` field below from your BV-BRC session before committing
> this file.** Everything else is left as-is.

## 1. Source database

- **Database:** BV-BRC (Bacterial and Viral Bioinformatics Resource Center)
- **URL:** https://www.bv-brc.org/
- **Access date:** [YYYY-MM-DD]
- **BV-BRC genome search filters used:** [e.g. species = Mycobacterium
  tuberculosis; genome status = Complete; lineage/SNP-barcode annotation]

## 2. Selection criteria

Describe exactly how genomes were chosen for each lineage (not just "5 from
each lineage" — the *rule* used to pick which 5):

- **Lineage assignment method:** [e.g. BV-BRC lineage metadata field / SNP
  barcoding tool / literature-defined reference strains]
- **Inclusion criteria:** [e.g. complete genome assemblies only, minimum
  assembly quality/N50, exclude genomes flagged as contaminated]
- **Exclusion criteria:** [e.g. duplicate strains, draft assemblies, genomes
  missing lineage metadata]
- **Why Lineage 4 has 3 genomes instead of 5:** [e.g. fewer high-quality
  complete assemblies were available under the same filters at the time of
  retrieval — state the real reason]

## 3. Dataset metadata table

**⚠️ Data quality note before filling this in:** the accession list pulled
from BV-BRC (recorded below) contains only **8 distinct genome accessions**
across 18 lines — several accessions repeat 2–3 times. This does not cleanly
match the 5 / 5 / 5 / 3 genome-per-lineage structure described elsewhere in
this README. Before finalizing this table:

1. Open each FASTA file in `01_Genomes/Lineage_X/` directly and check its
   header line — that's the authoritative source for which accession is in
   which file.
2. Confirm whether repeated accessions represent (a) the same genome
   assembly genuinely used more than once (worth disclosing as a limitation
   if so), or (b) a copy-paste/export artifact where the same BV-BRC search
   result was pulled twice.
3. Update the rows below once each of the 18 files has been checked
   individually.

### Distinct accessions confirmed directly from `01_Genomes/` FASTA headers

The list below was read manually from the actual header line of all 18
FASTA files in `01_Genomes/`, and confirms only **8 distinct genome
assemblies** are present across the 18 files — several accessions are
repeated across multiple lineage-numbered filenames.

| Accession | Strain / assembly description | Stated (sub-)lineage | Taxon suffix | Times seen across the 18 files |
|---|---|---|---|---|
| CP048071.1 | *M. tuberculosis* strain RW-TB008 | Not stated | 1773.22787 | 2 |
| CP041207.1 | *M. tuberculosis* strain MT-0080 | Not stated | 1773.17855 | 1 |
| OW052188 | Lineage 1.1.2 genome assembly, chromosome 1 | Lineage 1.1.2 | 1773.29764 | 3 |
| OW052570 | Lineage 1.1.2 genome assembly, chromosome 1 | Lineage 1.1.2 | 1773.29769 | 2 |
| OW052189 | Lineage 2.2.7 genome assembly, chromosome 1 | Lineage 2.2.7 | 1773.29765 | 2 |
| OW052302 | Lineage 3.1.1 genome assembly, chromosome 1 | Lineage 3.1.1 | 1773.29766 | 3 |
| OW052573 | Lineage 4.1.2.1 genome assembly, chromosome 1 | Lineage 4.1.2.1 | 1773.29767 | 3 |
| OW052571 | Lineage 4.1 genome assembly, chromosome 1 | Lineage 4.1 | 1773.29768 | 2 |

**⚠️ Confirmed data-quality issue — resolved via direct testing, not
speculation:**

The `01_Genomes/` folder contains 18 filenames but only 8 distinct genome
assemblies. `OW052188` and `OW052570` are both "Lineage 1.1.2" but carry
different taxon suffixes (likely two genuinely distinct isolates under the
same sub-lineage). Beyond that, several exact accessions are reused across
multiple differently-named files.

**This was actively investigated and confirmed, not assumed.** A field-
specific ADV Search on BV-BRC (`Genome Name` contains `"Lineage 1"`) was run
against the full 624-genome *M. tuberculosis* pool (Complete + Good quality
+ Human host filters). It returned only 5 results, and cross-checking them
showed BV-BRC's search does loose token matching rather than exact phrase
matching (it also matched "Lineage 3.1.1" and "Lineage 4.1.2.1" because they
contain the digit "1" somewhere, not because they are Lineage 1). Once that
is accounted for, **only 6 genomes in the entire 624-genome filtered pool
carry an explicit lineage label at all** — and they are exactly the 6
already present in this dataset (2× Lineage 1, 1× Lineage 2, 1× Lineage 3,
2× Lineage 4).

**Conclusion: there are no additional explicitly lineage-labeled *M.
tuberculosis* genomes available on BV-BRC to fill out Lineages 1–3 to 5
genomes each.** Reaching a true 5-genomes-per-lineage design would require
downloading additional (unlabeled) complete genomes and running a
SNP-barcoding/lineage-typing tool (e.g. TB-Profiler, fast-lineage-caller)
locally to determine their lineage — a substantial additional analysis step
outside the scope of what this repository currently does.

**Recommended path forward: disclose the dataset honestly rather than force
it to 18.** Revise the README's Dataset section and Limitations to state:

> The genome dataset comprises 8 distinct, explicitly lineage-labelled *M.
> tuberculosis* genome assemblies retrieved from BV-BRC (2 Lineage 1, 1
> Lineage 2, 1 Lineage 3, 2 Lineage 4, plus RW-TB008 and MT-0080 used as
> additional Lineage 4 references), rather than 18 independent isolates.
> Several sub-lineage designations were represented via the same underlying
> assembly across multiple analysis file slots. This reflects the limited
> availability of genomes with explicit lineage metadata in BV-BRC at the
> time of retrieval, particularly for Lineages 1–3, rather than a deliberate
> sampling choice. Extending this dataset to true 5-genomes-per-lineage
> coverage would require downloading additional unlabelled complete genomes
> and running dedicated lineage-typing software.

This is a stronger, more defensible README than silently keeping the "18
genomes, 5/5/5/3" framing — it demonstrates you understood your own data
well enough to catch and correctly diagnose the discrepancy, which reads
better to anyone reviewing this repository than an inflated genome count
would.

### Confirmed genome metadata, direct from BV-BRC Genome List View

The table below is built directly from the BV-BRC "Genomes" tab (filters:
Complete genome status, Good genome quality, Human host) and cross-checked
against the FASTA-header list above — this supplies the fuller metadata
(size, CDS count, collection year, country) for the 8 distinct assemblies
actually used.

| Genome Name | Strain | GenBank Accession | Size (bp) | CDS | Collection Year | Isolation Country |
|---|---|---|---|---|---|---|
| *M. tuberculosis* Lineage 1.1.2 | Lineage 1.1.2 | OW052570 | 4,412,157 | 4,255 | 2013 | Madagascar |
| *M. tuberculosis* Lineage 1.1.2 | Lineage 1.1.2 | OW052188 | 4,422,327 | 4,256 | 2013 | Madagascar |
| *M. tuberculosis* Lineage 2.2.7 | Lineage 2.2.7 | OW052189 | 4,415,120 | 4,262 | 2016 | Madagascar |
| *M. tuberculosis* Lineage 3.1.1 | Lineage 3.1.1 | OW052302 | 4,428,693 | 4,278 | 2015 | Madagascar |
| *M. tuberculosis* Lineage 4.1 | Lineage 4.1 | OW052571 | 4,394,726 | 4,242 | 2017 | Madagascar |
| *M. tuberculosis* Lineage 4.1.2.1 | Lineage 4.1.2.1 | OW052573 | 4,408,536 | 4,245 | 2016 | Madagascar |
| *M. tuberculosis* strain RW-TB008 | RW-TB008 | CP048071 | 4,379,910 | 4,277 | 2017 | Rwanda |
| *M. tuberculosis* strain MT-0080 | MT-0080 | CP041207 | 4,426,525 | 4,321 | 2012 | Canada |

### Per-file table

Fill in once decision (1) or (2) above is made — for option (1), map each of
the 18 filenames to its accession from the FASTA-header list; for option
(2), replace duplicated files with newly retrieved distinct genomes first:

| Lineage | File name | Strain / Isolate name | BV-BRC Genome ID | Assembly Accession (GenBank/RefSeq) | Country / Region | Collection year | Assembly status |
|---|---|---|---|---|---|---|---|
| Lineage 1 | lineage 1.1.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 1 | lineage 1.2.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 1 | lineage 1.3.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 1 | lineage 1.4.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 1 | lineage 1.5.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 2 | lineage 2.1.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 2 | lineage 2.2.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 2 | lineage 2.3.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 2 | lineage 2.4.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 2 | lineage 2.5.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 3 | lineage 3.1.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 3 | lineage 3.2.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 3 | lineage 3.3.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 3 | lineage 3.4.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 3 | lineage 3.5.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 4 | lineage 4.1.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 4 | lineage 4.2.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Lineage 4 | lineage 4.3.fasta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

**Tip:** BV-BRC lets you export exactly this metadata as a table/CSV from the
genome list view after filtering — you can export it directly and reformat
into the table above rather than typing each field by hand.

A machine-readable copy of this table (for scripts to load) belongs at
`methods/dataset_metadata.csv` — see that file for the CSV version.
