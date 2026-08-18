# Phylogenetic and Structural Analysis of PPE18 (Rv1196) across *Mycobacterium tuberculosis* Lineages

[![Analysis](https://img.shields.io/badge/Analysis-Computational%20Biology-blue)]()
[![Organism](https://img.shields.io/badge/Organism-*M.%20tuberculosis*-red)]()
[![Target](https://img.shields.io/badge/Target-PPE18%20%2F%20Rv1196-green)]()
[![Focus](https://img.shields.io/badge/Focus-Phylogenetics%20%20%7C%20Structural%20Bioinformatics-purple)]()

## Overview

This repository contains a computational analysis of **PPE18 (Rv1196; Mtb39A)** across selected *Mycobacterium tuberculosis* strains representing Lineages 1, 2, 3, and 4.

The project integrates **comparative genomics, protein sequence analysis, multiple sequence alignment, phylogenetic reconstruction, three-dimensional structural modelling, and structural validation** to investigate the sequence conservation, evolutionary relationships, and structural characteristics of PPE18.

PPE18 belongs to the PE/PPE protein family of *Mycobacterium tuberculosis*, a group of proteins associated with host–pathogen interactions, immune modulation, and antigenic variation. PPE18 is also of particular interest because it is a component of the **M72/AS01E tuberculosis vaccine candidate**.

The analysis was designed to examine the extent of PPE18 sequence conservation across selected *M. tuberculosis* lineages and to complement the sequence-level analysis with phylogenetic and structural characterization.

---

## Research Objectives

The primary objective of this project was to investigate the **sequence conservation, phylogenetic relationships, and structural characteristics of PPE18 (Rv1196)** across selected *M. tuberculosis* strains.

### Specific objectives

- Retrieve representative *M. tuberculosis* genomes from Lineages 1, 2, 3, and 4.
- Retrieve the reference PPE18 (Rv1196) sequence.
- Identify homologous PPE18 protein sequences using BLASTP.
- Compare PPE18 sequences using multiple sequence alignment.
- Reconstruct phylogenetic relationships among the analysed PPE18 sequences.
- Generate a three-dimensional structural model of PPE18.
- Assess the quality of the predicted structural model.
- Integrate sequence, evolutionary, and structural observations.

---

# Study Workflow

```text
Selected *M. tuberculosis* Genomes
                │
                ▼
             BV-BRC
                │
                ▼
      Lineages 1, 2, 3 & 4
                │
                ▼
     Reference PPE18 (Rv1196)
                │
                ▼
          Mycobrowser
                │
                ▼
             BLASTP
                │
                ▼
     PPE18 Homologous Sequences
                │
                ▼
     Multiple Sequence Alignment
          (Clustal Omega)
                │
                ▼
      Phylogenetic Reconstruction
         (Simple Phylogeny)
                │
                ├──────────────────┐
                ▼                  ▼
       Evolutionary Analysis   Structural Analysis
                                     │
                                     ▼
                                SWISS-MODEL
                                     │
                                     ▼
                              3D PPE18 Model
                                     │
                                     ▼
                            Structural Validation
                             (Ramachandran)
```

---

# Dataset

## Genome Dataset

Genome FASTA files were retrieved from BV-BRC and organized into
lineage-labelled folders under `01_Genomes/`. Of the genomes retrieved, **8
are distinct genome assemblies carrying an explicit lineage label** in
BV-BRC's metadata:

| Lineage   | Distinct labelled genome assemblies |
| --------- | -----------------------------------: |
| Lineage 1 |                                    2 |
| Lineage 2 |                                    1 |
| Lineage 3 |                                    1 |
| Lineage 4 |                                    3 (incl. RW-TB008, MT-0080 as additional Lineage 4 references) |
| **Total** |                              **8** |

**A note on dataset composition:** the `01_Genomes/` folder contains 18
FASTA files in total, organized into per-lineage sub-folders. However, only
8 of these correspond to distinct genome assemblies — several sub-lineage
file slots reference the same underlying BV-BRC assembly. This reflects a
genuine limitation in genome availability rather than a deliberate sampling
choice: BV-BRC's *M. tuberculosis* collection (Complete + Good quality +
Human host filters, 624 genomes total) contains only 6 genomes with an
explicit lineage label in their metadata at all, and this project's Lineage
1–3 folders could not be filled to 5 genuinely independent genomes each
using name-based lineage metadata. Reaching a true 5-genomes-per-lineage
design would require downloading additional, unlabelled complete genomes and
running dedicated lineage-typing software (e.g. TB-Profiler,
fast-lineage-caller) locally — outside the scope of the current analysis.
See `08_Methods/01_genome_retrieval.md` for the full investigation and the
per-genome accession table.

**Downstream analyses in this repository (BLASTP, alignment, phylogeny) were
performed on PPE18 protein sequences and their strain-level metadata, not on
these 18 genome files directly** — see `08_Methods/03_blastp_search.md` onward
for exactly which sequences were used at each step.

The genome files are organized according to lineage:

```text
01_Genomes/
├── Lineage_1/
├── Lineage_2/
├── Lineage_3/
└── Lineage_4/
```

This organization preserves the lineage information associated with each
genomic input, where known.

---

# Target Protein

## PPE18 / Rv1196

**Gene:** *ppe18*
**Locus tag:** Rv1196
**Protein:** PPE18
**Alternative designation:** Mtb39A
**Organism:** *Mycobacterium tuberculosis*

The reference PPE18 sequence was retrieved from **Mycobrowser** and used as the reference sequence for downstream protein sequence analysis.

The resulting sequence dataset is maintained in:

```text
02_Sequences/
```

---

# Methodology

## 1. Genome Retrieval from BV-BRC

Selected *M. tuberculosis* genomes representing Lineages 1, 2, 3, and 4 were obtained from the **Bacterial and Viral Bioinformatics Resource Center (BV-BRC)**.

The final genomic dataset consisted of 18 genome FASTA files:

* 5 genomes from Lineage 1
* 5 genomes from Lineage 2
* 5 genomes from Lineage 3
* 3 genomes from Lineage 4

The raw genomic input files are organized under:

```text
01_Genomes/
```

### Figure

`07_Figures/01_BV-BRC.png`

**Figure 1.** Selection and retrieval of *Mycobacterium tuberculosis* genomic sequences representing the analysed lineages from BV-BRC.

---

## 2. PPE18 Reference Sequence Retrieval

The reference PPE18 (Rv1196) sequence was retrieved from **Mycobrowser**.

Mycobrowser was used to obtain the relevant gene/protein information and reference sequence for PPE18.

### Figure

`07_Figures/02_Mycobrowser.png`

**Figure 2.** Mycobrowser record showing the reference PPE18 (Rv1196) gene/protein information used as the starting point for downstream sequence analysis.

---

## 3. BLASTP Analysis

The reference PPE18 protein sequence was used as a query in **NCBI BLASTP** to identify homologous PPE18 protein sequences.

The search was restricted to *Mycobacterium tuberculosis* to focus the analysis on the target organism.

High-similarity hits were examined using sequence identity and query coverage as the primary criteria for sequence selection.

### Figures

`07_Figures/03_BLAST_results.png`

**Figure 3.** NCBI BLASTP results obtained using the PPE18 reference protein sequence as the query.

`07_Figures/04_BLAST_graphic_summary.png`

**Figure 4.** BLASTP graphical summary showing the distribution and similarity of identified PPE18-related sequence hits.

---

## 4. Multiple Sequence Alignment

Selected PPE18 protein sequences were aligned using **Clustal Omega**.

The multiple sequence alignment was used to assess:

* overall sequence conservation;
* conserved amino acid positions;
* variable positions;
* sequence-level similarities and differences; and
* the sequence relationships used for downstream phylogenetic analysis.

The alignment file is stored under:

```text
03_Alignments/
```

### Figure

`07_Figures/05_Clustal_alignment.png`

**Figure 5.** Multiple sequence alignment of the analysed PPE18 protein sequences generated using Clustal Omega.

---

## 5. Phylogenetic Reconstruction

Phylogenetic relationships among the analysed PPE18 sequences were reconstructed using the **Simple Phylogeny** tool from EMBL-EBI.

The resulting phylogenetic trees are provided in both image and vector formats where available, together with the Newick representation of the tree.

The phylogenetic outputs are stored under:

```text
04_Trees/
```

### Tree outputs

```text
PPE18_tree1.png
PPE18_tree1.svg
PPE18_tree2.png
PPE18_tree2.svg
PPE18_tree.nwk
```

### Figure

`07_Figures/06_Phylogenetic_tree.png`

**Figure 6.** Phylogenetic reconstruction of the analysed PPE18 sequences, illustrating the evolutionary relationships among the sampled strains.

---

## 6. Three-Dimensional Structural Modelling

A three-dimensional structural model of PPE18 from the H37Rv reference background was generated using **SWISS-MODEL**.

Homology-based structural modelling was used to obtain a predicted three-dimensional representation of PPE18 and provide a structural perspective complementary to the sequence and phylogenetic analyses.

The structural outputs are stored under:

```text
05_Structures/
```

### Figure

`07_Figures/07_Structure.png`

**Figure 7.** Predicted three-dimensional structure of PPE18 generated using SWISS-MODEL.

---

## 7. Structural Quality Assessment

The predicted PPE18 structure was evaluated using structural quality assessment and a **Ramachandran plot**.

The Ramachandran analysis showed that the majority of residues were located within favoured conformational regions, supporting the overall plausibility of the predicted model.

### Figure

`07_Figures/08_Ramachandran.png`

**Figure 8.** Ramachandran plot for the predicted PPE18 structural model, showing the distribution of amino acid residues across allowed and favoured conformational regions.

---

# Results

## 1. PPE18 Sequence Conservation

The analysed PPE18 sequences demonstrated **high overall sequence similarity**.

The BLASTP results identified highly similar PPE18-related sequences, while the multiple sequence alignment enabled direct examination of conserved and variable amino acid positions.

Overall, the analysed dataset showed relatively limited sequence divergence.

---

## 2. Phylogenetic Relationships

The reconstructed PPE18 phylogenies demonstrated **very low genetic distances among the analysed sequences**.

Most pairwise distances were reported as **0.00000**. Branch lengths in the tree reach a maximum of **0.00256**; the true maximum pairwise patristic distance between the two most divergent taxa (summing both branches back to their shared ancestor) is **0.00512** — recomputed and verified directly from the Newick tree file using `09_Scripts/phylogeny_summary.py`.

The resulting phylogenetic relationships did not show a strong, clearly separated lineage-specific clustering pattern based solely on PPE18.

This indicates that, within the sampled dataset, PPE18 displays substantial conservation and may provide limited phylogenetic resolution for distinguishing the major *M. tuberculosis* lineages represented here.

---

## 3. Structural Modelling

A three-dimensional structural model of PPE18 was successfully generated using SWISS-MODEL.

The predicted structure provides a structural representation of the conserved PPE18 protein and complements the sequence-based analysis.

---

## 4. Structural Validation

The Ramachandran plot indicated that the **majority of residues occupied favoured conformational regions**.

Although some residues were located outside the most favoured regions, the overall distribution supported the plausibility of the predicted structural model.

Structural validation should be interpreted as an assessment of the computational model rather than experimental confirmation of the PPE18 structure.

---

# Key Findings

### High sequence conservation

PPE18 showed high sequence similarity among the analysed *M. tuberculosis* strains.

### Low observed sequence divergence

The phylogenetic analysis showed very small genetic distances among most analysed PPE18 sequences.

### Limited lineage-specific phylogenetic separation

The PPE18 phylogeny did not demonstrate strong separation corresponding to the four sampled *M. tuberculosis* lineages.

### Successful structural modelling

A three-dimensional model of PPE18 was generated using SWISS-MODEL.

### Overall structural plausibility

The Ramachandran analysis showed that most residues occupied favoured conformational regions.

---

# Interpretation

The combined sequence and phylogenetic analyses indicate that **PPE18 is highly conserved within the sampled dataset**.

The very low genetic distances observed among the analysed sequences and the lack of strong lineage-specific clustering suggest that PPE18 alone may have limited discriminatory power for resolving the major *M. tuberculosis* lineages represented in this dataset.

The structural analysis provides a complementary perspective by demonstrating that the PPE18 protein can be computationally modelled and evaluated using established structural-quality approaches.

However, the observed conservation should be interpreted within the context of the **limited sampling size and lineage composition** of the present dataset and should not be generalized to the entire global *M. tuberculosis* population.

---

# Limitations

The following limitations should be considered when interpreting this analysis:

* **The genome dataset comprises only 8 distinct, explicitly lineage-labelled genome assemblies, not 18 independent isolates** — Lineages 1–3 are represented by 1–2 distinct genomes each rather than 5, reflecting a scarcity of lineage-labelled complete genomes in BV-BRC rather than a deliberate sampling design. See `08_Methods/01_genome_retrieval.md` for the full investigation.
* The dataset contains a relatively small number of distinct genomes compared with the global diversity of *M. tuberculosis*.
* Genome sampling was highly uneven across lineages: 2 for Lineage 1, 1 for Lineage 2, 1 for Lineage 3, and 3 for Lineage 4.
* Only four major lineages were considered.
* The analysis focused on a single PPE gene rather than a genome-wide phylogenomic dataset.
* High sequence conservation may reduce the phylogenetic signal available for distinguishing closely related strains.
* The structural model was built on an AlphaFold DB predicted template (L7N675), not an experimentally determined structure — see `08_Methods/06_structural_modelling.md`.
* Structural quality assessment (MolProbity/Ramachandran) does not substitute for experimental structural validation.

---

# Future Directions

The analysis could be extended through:

* expansion of the genome dataset within each lineage;
* inclusion of additional globally diverse clinical isolates;
* analysis of additional PE/PPE genes such as **PPE57** and **PE/PGRS** proteins;
* residue-level analysis of lineage-associated substitutions;
* investigation of predicted functional consequences of sequence variation;
* comparative epitope conservation analysis;
* integration of long-read genome assemblies to better resolve repetitive PE/PPE regions;
* comparison with genome-wide phylogenomic relationships; and
* structural comparison of naturally occurring PPE18 variants.

---

# Repository Structure

```text
MTBC-PPE18-Phylogenetic-Structural-Analysis/
│
├── README.md
├── LICENSE
├── CITATION.cff
│
├── 01_Genomes/
│   ├── Lineage_1/
│   │   ├── lineage 1.1.fasta   (OW052570)
│   │   ├── lineage 1.2.fasta   (OW052188)
│   │   ├── lineage 1.3.fasta   (duplicate assembly — see 08_Methods/01_genome_retrieval.md)
│   │   ├── lineage 1.4.fasta   (duplicate assembly)
│   │   └── lineage 1.5.fasta   (duplicate assembly)
│   │
│   ├── Lineage_2/
│   │   ├── lineage 2.1.fasta   (OW052189)
│   │   ├── lineage 2.2.fasta   (duplicate assembly)
│   │   ├── lineage 2.3.fasta   (duplicate assembly)
│   │   ├── lineage 2.4.fasta   (duplicate assembly)
│   │   └── lineage 2.5.fasta   (duplicate assembly)
│   │
│   ├── Lineage_3/
│   │   ├── lineage 3.1.fasta   (OW052302)
│   │   ├── lineage 3.2.fasta   (duplicate assembly)
│   │   ├── lineage 3.3.fasta   (duplicate assembly)
│   │   ├── lineage 3.4.fasta   (duplicate assembly)
│   │   └── lineage 3.5.fasta   (duplicate assembly)
│   │
│   └── Lineage_4/
│       ├── lineage 4.1.fasta   (OW052571)
│       ├── lineage 4.2.fasta   (OW052573)
│       └── lineage 4.3.fasta   (CP041207 / MT-0080)
│
├── 02_Sequences/
│   └── PPE18_all_sequences.fasta
│
├── 03_Alignments/
│   └── PPE18_alignment.aln
│
├── 04_Trees/
│   ├── PPE18_tree1.png
│   ├── PPE18_tree1.svg
│   ├── PPE18_tree2.png
│   ├── PPE18_tree2.svg
│   └── PPE18_tree.nwk
│
├── 05_Structures/
│   ├── PPE18_structure.pdb
│   ├── PPE18_structure.png
│   └── PPE18_Ramachandran.png
│
├── 06_Report/
│   └── PPE18_Analysis_Report.pdf
│
├── 07_Figures/
│   ├── 01_BV-BRC.png
│   ├── 02_Mycobrowser.png
│   ├── 03_BLAST_results.png
│   ├── 04_BLAST_graphic_summary.png
│   ├── 05_Clustal_alignment.png
│   ├── 06_Phylogenetic_tree.png
│   ├── 07_Structure.png
│   └── 08_Ramachandran.png
│
├── 08_Methods/
│   ├── 01_genome_retrieval.md
│   ├── 02_reference_sequence.md
│   ├── 03_blastp_search.md
│   ├── 04_multiple_sequence_alignment.md
│   ├── 05_phylogenetic_reconstruction.md
│   ├── 06_structural_modelling.md
│   ├── 07_structural_validation.md
│   └── dataset_metadata.csv
│
└── 09_Scripts/
    ├── requirements.txt
    ├── sequence_statistics.py
    ├── alignment_analysis.py
    └── phylogeny_summary.py
```

**Note:** the "duplicate assembly" labels above are placeholders pending the
exact per-file mapping — see `08_Methods/01_genome_retrieval.md` for the full
accession-to-file investigation and which specific assembly each
placeholder file actually corresponds to.

---

# Software, Databases & Resources

| Resource                      | Purpose                                         |
| ----------------------------- | ----------------------------------------------- |
| **BV-BRC**                    | Retrieval of *M. tuberculosis* genome sequences |
| **Mycobrowser**               | PPE18 / Rv1196 gene and protein information     |
| **NCBI BLASTP**               | Protein sequence similarity analysis            |
| **Clustal Omega**             | Multiple sequence alignment                     |
| **EMBL-EBI Simple Phylogeny** | Phylogenetic reconstruction                     |
| **SWISS-MODEL**               | Three-dimensional protein structure modelling   |
| **Ramachandran analysis**     | Structural quality assessment                   |

---

# Figures

The `07_Figures/` directory contains visual documentation of the major stages of the computational workflow.

| Figure       | Description                                      |
| ------------ | ------------------------------------------------ |
| **Figure 1** | BV-BRC genome retrieval and lineage selection    |
| **Figure 2** | Mycobrowser PPE18 / Rv1196 reference information |
| **Figure 3** | NCBI BLASTP results                              |
| **Figure 4** | BLASTP graphical summary                         |
| **Figure 5** | Clustal Omega multiple sequence alignment        |
| **Figure 6** | PPE18 phylogenetic reconstruction                |
| **Figure 7** | Predicted three-dimensional PPE18 structure      |
| **Figure 8** | Ramachandran structural validation plot          |

---

# Reproducibility

The repository is organized according to the chronological computational workflow used in the analysis:

```text
Genome Retrieval
      ↓
Reference Sequence Retrieval
      ↓
BLASTP
      ↓
Sequence Selection
      ↓
Multiple Sequence Alignment
      ↓
Phylogenetic Reconstruction
      ↓
Structural Modelling
      ↓
Structural Validation
```

The numbered directories preserve the major input datasets, sequence-analysis files, phylogenetic outputs, structural results, figures, and final report.

This structure is intended to facilitate **inspection, reproducibility, reuse, and extension** of the analysis.

---

# References

1. **Mycobrowser.** *Mycobacterium tuberculosis* genome and gene/protein annotation resource.

2. Homolka, S., et al. (2016). High sequence variability of the *ppe18* gene of clinical *Mycobacterium tuberculosis* complex strains potentially impacts effectiveness of vaccine candidate M72/AS01E. *PLoS ONE*, 11(3), e0152200.

3. Cole, S. T., et al. (1998). Deciphering the biology of *Mycobacterium tuberculosis* from the complete genome sequence. *Nature*, 393, 537–544.

4. Gey van Pittius, N. C., et al. (2006). Evolution and expansion of the *Mycobacterium tuberculosis* PE and PPE multigene families. *BMC Evolutionary Biology*, 6, 95.

---

# Author

**Aaradhya Aggarwal**

Computational Biology & Structural Bioinformatics

---

## Project Focus

**Comparative Genomics · Protein Sequence Analysis · Multiple Sequence Alignment · Phylogenetics · Structural Bioinformatics · Mycobacterial Genomics**
