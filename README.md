# Phylogenetic and Structural Analysis of PPE18 (Rv1196) across *Mycobacterium tuberculosis* Lineages

[![Language](https://img.shields.io/badge/Analysis-Computational%20Biology-blue)]()
[![Organism](https://img.shields.io/badge/Organism-*M.%20tuberculosis*-red)]()
[![Target](https://img.shields.io/badge/Target-PPE18%20%2F%20Rv1196-green)]()
[![Domain](https://img.shields.io/badge/Domain-Phylogenetics%20%7C%20Structural%20Bioinformatics-purple)]()

## Overview

This repository contains a reproducible computational analysis of **PPE18 (Rv1196; Mtb39A)** across major *Mycobacterium tuberculosis* lineages.

The project integrates **genome retrieval, reference sequence annotation, protein sequence similarity analysis, multiple sequence alignment, phylogenetic reconstruction, three-dimensional structural modelling, and structural quality assessment** to investigate the sequence conservation and evolutionary relationships of PPE18.

PPE18 belongs to the PE/PPE protein family, a major mycobacterial protein family associated with host–pathogen interactions, immune modulation, and antigenic variation. PPE18 is also of particular interest because it is a component of the **M72/AS01E tuberculosis vaccine candidate**.

The analysis was designed to examine whether PPE18 displays substantial sequence variation across *M. tuberculosis* lineages and whether the observed sequence conservation is reflected in its inferred evolutionary relationships and structural characteristics.

---

## Research Objective

The primary objective of this project was to investigate the **sequence conservation, phylogenetic relationships, and structural characteristics of PPE18 (Rv1196)** across *M. tuberculosis* Lineages 1, 2, 3, and 4.

### Specific objectives

- Retrieve representative *M. tuberculosis* genomes from multiple major lineages.
- Obtain the reference PPE18 (Rv1196) sequence.
- Identify homologous PPE18 protein sequences using BLASTP.
- Compare PPE18 sequences through multiple sequence alignment.
- Reconstruct phylogenetic relationships among the analysed PPE18 sequences.
- Generate a three-dimensional structural model of PPE18.
- Evaluate the quality of the predicted structural model.
- Integrate sequence-level, evolutionary, and structural observations.

---

# Study Workflow

```text
*M. tuberculosis* genomes
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
PPE18 homologous sequences
        │
        ▼
 Multiple Sequence Alignment
     (Clustal Omega)
        │
        ▼
 Phylogenetic Reconstruction
   (Simple Phylogeny)
        │
        ├───────────────┐
        ▼               ▼
 Sequence Analysis   Structural Analysis
                        │
                        ▼
                   SWISS-MODEL
                        │
                        ▼
                3D PPE18 Model
                        │
                        ▼
             Structural Validation
              (Ramachandran plot)
