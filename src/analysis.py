import os
import csv
"""
Dataset-level analysis
FASTA -> sequence metrics table
"""

from fasta_reader import read_fasta
from sequence_metrics import (
    sequence_length,
    gc_content,
    nucleotide_frequency,
    at_skew,
    gc_skew
)

if __name__ == "__main__":
    fasta_path = "data/raw/ecoli_cds.fasta"
    sequences = read_fasta(fasta_path)

   
    results = []

   
    for gene_id, sequence in sequences.items():
        length = sequence_length(sequence)
        gc = gc_content(sequence)
        freqs = nucleotide_frequency(sequence)
        at = at_skew(sequence)
        gc_s = gc_skew(sequence)

        gene_data = {
            "gene_id": gene_id,
            "length": length,
            "gc_percent": gc,
            "at_skew": at,
            "gc_skew": gc_s,
            "A": freqs["A"],
            "T": freqs["T"],
            "G": freqs["G"],
            "C": freqs["C"]
        }

        results.append(gene_data)

    
os.makedirs("results", exist_ok=True)

output_path = "results/sequence_metrics.csv"

fieldnames = list(results[0].keys())

with open(output_path, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)




    
