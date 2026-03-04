# Supplementary Materials

## Manuscript Title

"Advancing FAIR Phylogenetics for Health Threats: A Systematic Review of SARS-CoV-2 Research and Guidelines for Future Outbreaks."

## Authors

- Omkar Marne (1,2)
- Denis Jacob Machado (1,2)

## Affiliation

1. University of North Carolina at Charlotte (UNC Charlotte), College of Computing and Informatics (CCI), Department of Bioinformatics and Genomics, Charlotte, NC, USA.
2. University of North Carolina at Charlotte (UNC Charlotte), Center for Computational Intelligence to Predict Health and Environmental Risks (CIPHER), Charlotte, NC, USA.

## Overview

This repository contains all figures, datasets, and supporting materials associated with the systematic review of 217 phylogenetic studies of SARS-CoV-2. The materials are organized to ensure transparency, reproducibility, and compliance with FAIR data principles.

## Figures

### Figure 1: Workflow of Phylogenetic Analysis

- File: `figure_1.pdf`
- Description: This figure illustrates the generalized workflow of a phylogenetic analysis. White boxes represent the primary operational stages, while connected grey boxes indicate selected methodological choices at each stage.

### Figure 2: PRISMA Flow Diagram

- File: `figure_2.pdf`
- Description: This figure presents the PRISMA flow diagram detailing the study selection process employed in this systematic review.

### Figure 3: Methodological Patterns Across 217 SARS-CoV-2 Phylogenetic Studies

- File: `figure_3.pdf`
- Description: Figure 3 summarizes methodological trends identified in the reviewed literature.

#### Figure 3a: Outgroup Usage

Out of 217 studies:

- 185 did not use an outgroup  
- 32 used an outgroup  

#### Figure 3b: Tree Rooting

- 196 studies reported rooted trees  
- 3 studies reported unrooted trees  
- 13 studies did not clearly specify rooting strategy  

#### Figure 3c: Branch Support Metrics

- 164 used Bootstrap (BS)  
- 3 used Posterior Probabilities (PP)  
- 1 used Goodman–Bremer (GB) support  
- 49 did not clearly specify branch support metrics  

#### Figure 3d: Gene Annotation

- 187 used gene annotation  
- 29 did not use gene annotation  
- 1 did not clearly specify annotation usage  

#### Figure 3e: FAIR Data Compliance

- 20 studies met FAIR principles  
- 197 studies did not meet FAIR standards  

#### Figure 3f: Type of Molecular Data

- 208 used nucleotide data  
- 8 used both nucleotide and amino acid data  
- 4 used amino acid data only  
- 1 did not clearly specify data type  

#### Figure 3g: Type of Phylogenetic Analysis

- 201 conducted whole-genome analyses  
- 13 conducted single-gene analyses  
- 6 conducted multi-gene analyses  
- 1 did not clearly specify analysis type  

#### Figure 3h: Optimality Criteria

- 168 used Maximum Likelihood (ML)  
- 48 used Bayesian Inference (BI)  
- 12 used Parsimony (P)  
- 16 used Neighbor Joining (NJ)  
- 1 used UPGMA  
- 1 used Chaos Game Representation (CGR)  
- 1 did not clearly specify the optimality criterion  

### Figure 4: Journal Impact Factor Distribution

This figure presents the distribution of journal impact factors across the 217 studies, stratified by methodological choices.

## Datasets

### File `review_papers.xlsx`

This Excel file contains the complete dataset and metadata extracted from the 217 phylogenetic studies.

### File `review_papers.csv`

This file contains the same dataset as the Excel file, provided in Comma-Separated Values (CSV) format.

### File `review_papers_APA_format.txt`

This file contains the full bibliographic list of the 217 included studies formatted according to APA guidelines.

## Statistical Analysis

Please see the compressed zip file `stats.zip`, and the details on the `README_STATS.md` file inside of it.

## Reproducibility and Transparency Statement

All data were manually curated from peer-reviewed publications. The dataset is provided in open formats (XLSX and CSV) to facilitate reproducibility and reuse.