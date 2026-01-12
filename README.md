# DNA Sequence Analysis Toolkit

A lightweight, modular Python toolkit for parsing FASTA files and computing gene-level and dataset-level DNA sequence metrics.  
Designed as a foundational bioinformatics project with clean code structure and reproducible analysis.

---

## Project Overview

This project implements a mini bioinformatics pipeline that:

- Parses DNA sequences from FASTA files  
- Computes biologically relevant sequence metrics  
- Aggregates results across a dataset  
- Exports results in a structured CSV format for downstream analysis  

The toolkit is intentionally framework-free (pure Python) to emphasize core algorithmic logic, clean modular design, and reproducibility.

---

## Biological Motivation

DNA sequence composition metrics such as:

- GC content  
- AT / GC skew  
- Nucleotide frequencies  

are widely used in:

- Genome annotation  
- Comparative genomics  
- Gene characterization  
- Detecting compositional bias  

This project demonstrates how such metrics can be computed **from scratch**, without relying on external bioinformatics libraries.

---

## Module Description

### `fasta_reader.py`
- Parses FASTA files  
- Returns sequences as `{header: sequence}` dictionary  
- Handles multi-line FASTA formatting  

### `sequence_metrics.py`
Pure functions for gene-level metrics:
- Sequence length  
- GC content (%)  
- Nucleotide frequency (A, T, G, C)  
- AT skew  
- GC skew  

### `analysis.py`
- Dataset-level analysis  
- Integrates FASTA parsing and metrics  
- Exports results to CSV format  

---

## How to Run

### Requirements
- Python 3.9+
- No external dependencies

### Run analysis
From project root:

```bash
python src/analysis.py

## Author

Harshit Belwal  
GitHub: [@harshGenix]  
Bioinformatics & Computational Biology (aspirant)

## License

This project is released under the **MIT License**.



