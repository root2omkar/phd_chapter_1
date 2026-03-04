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

This repository contains all the code used for the statistical analysis of the systematic review of 217 phylogenetic studies of SARS-CoV-2. Below is the directory structure for the stats directory. 

```
(base) omarne@CCI3QD19XJALT stats % tree
.
├── count_annotation
│   ├── figure_f.pdf
│   ├── figure_f.py
│   └── review_papers.csv
├── count_data
│   ├── figure_d.pdf
│   ├── figure_d.py
│   └── review_papers.csv
├── count_fair
│   ├── figure_h.pdf
│   ├── figure_h.py
│   └── review_papers.csv
├── count_optimality
│   ├── figure_g.pdf
│   ├── figure_g.py
│   └── review_papers.csv
├── count_outgroups
│   ├── figure_a.pdf
│   ├── figure_a.py
│   └── review_papers.csv
├── count_root
│   ├── figure_b.pdf
│   ├── figure_b.py
│   └── review_papers.csv
├── count_support
│   ├── figure_c.pdf
│   ├── figure_c.py
│   └── review_papers.csv
├── environment.yml
├── index_annotation
│   ├── figure_l_boxplot.pdf
│   ├── figure_l_v3.py
│   └── review_papers.csv
├── index_fair
│   ├── figure_i_boxplot.pdf
│   ├── figure_i_v3.py
│   └── review_papers.csv
├── index_outgroup
│   ├── figure_j_boxplot.pdf
│   ├── figure_j_v3.py
│   └── review_papers.csv
├── journal_count.py
├── LICENSE
├── README_STATS.md
└── venn_data
    ├── figure_e.pdf
    ├── figure_e.py
    └── review_papers.csv

12 directories, 37 files
(base) omarne@CCI3QD19XJALT stats % 

```

- File: `figure_f.pdf`
- Description: This figure illustrates the gene annotation statistics in phylogenetic studies of SARS-CoV-2. It's a part of `figure_3: Methodological Patterns Across 217 SARS-CoV-2 Phylogenetic Studies` in the manuscript.
- File: `figure_f.py`
- Description: This is a Python code with all the required libraries generating `figure_f.pdf` in pdf format.
- File: `figure_d.pdf`
- Description: This figure illustrates the statistics of the type of data used in phylogenetic studies of SARS-CoV-2. It's a part of`figure_3: Methodological Patterns Across 217 SARS-CoV-2 Phylogenetic Studies` in the manuscript.
- File: `figure_d.py`
- Description: This is a Python code with all the libraries to generate the `figure_d.pdf` in `.pdf` format.
- File: `figure_h.pdf`
- Description: This figure illustrates the statistics of the usage of FAIR (Findability, Accessibility, Readability, Reusability) principles in phylogenetic studies of SARS-CoV-2. It's a part of `figure_3: Methodological Patterns Across 217 SARS-CoV-2 Phylogenetic Studies` in the manuscript.
- File: `figure_h.py`
- Description: This is a Python code with all the libraries to generate the `figure_f.pdf` in `.pdf` format.
- File: `figure_g.pdf`
- Description: This figure illustrates the statistics of the usage of the different optimality criteria used in the phylogenetic studies of SARS-CoV-2. It's a part of `figure_3: Methodological Patterns Across 217 SARS-CoV-2 Phylogenetic Studies` in the manuscript. 
- File: `figure_g.py`
- Description: This is a Python code with all the libraries to generate the `figure_g.pdf` in `.pdf` format.
- File: `figure_a.pdf`
- Description: This figure illustrates the statistics of the outgroup usage in phylogenetic studies of SARS-CoV-2. It's a part of`figure_3: Methodological Patterns Across 217 SARS-CoV-2 Phylogenetic Studies` in the manuscript.
- File: `figure_a.py`
- Description: This is a Python code with all the libraries to generate the `figure_a.pdf` in `.pdf` format.
- File: `figure_b.pdf`
- Description: This figure illustrates the statistics of the root usage in phylogenetic studies of SARS-CoV-2. It's a part of`figure_3: Methodological Patterns Across 217 SARS-CoV-2 Phylogenetic Studies` in the manuscript.
- File: `figure_b.py`
- Description: This is a Python code with all the libraries to generate the `figure_b.pdf` in `.pdf` format.
- File: `figure_c.pdf`
- Description: This figure illustrates the statistics of the branch support metric usage in phylogenetic studies of SARS-CoV-2. It's a part of`figure_3: Methodological Patterns Across 217 SARS-CoV-2 Phylogenetic Studies` in the manuscript.
- File: `figure_c.py`
- Description: This is a Python code with all the libraries to generate the `figure_c.pdf` in `.pdf` format.
- File: `figure_l.pdf`
- Description: This figure illustrates the Kruskal-Wallis statistical test of the gene annotation usage in phylogenetic studies of SARS-CoV-2. It's a part of`figure_4: Journal Impact Factor Distribution` in the manuscript.
- File: `figure_l_v3.py`
- Description: This is a Python code with all the libraries to generate the `figure_l.pdf` in `.pdf` format.
- File: `figure_i.pdf`
- Description: This figure illustrates the Mann_Whitney-u statistical test of the FAIR principles usage in phylogenetic studies of SARS-CoV-2. It's a part of`figure_4: Journal Impact Factor Distribution` in the manuscript.
- File: `figure_i_v3.py`
- Description: This is a Python code with all the libraries to generate the `figure_i.pdf` in `.pdf` format.
- File: `figure_j.pdf`
- Description: This figure illustrates the Mann_Whitney-u statistical test of the outgroup usage in phylogenetic studies of SARS-CoV-2. It's a part of`figure_4: Journal Impact Factor Distribution` in the manuscript.
- File: `figure_j_v3.py`
- Description: This is a Python code with all the libraries to generate the `figure_j.pdf` in `.pdf` format.
- File: `journal_count.py`
- Description: This is a Python code to count the number of journals in which the 217 phylogenetic studies of   SARS-CoV-2 are published. It uses `review_papers.csv`, which contains all the metadata.
- File: `environment.yml`
- Description: This file describes the software, libraries, and dependencies required to run the code.
- File: 'LICENSE`
- Description: This is a GNU General Public License (GPL v3) file. 

 
 





