def read_fasta(filepath):
  
    """
    Reads a FASTA file and returns a dictionary:
    {header: sequence}
    """
    sequences = {}
    current_header = None
    current_sequence = []

    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                if current_header is not None:
                    sequences[current_header] = "".join(current_sequence)

                current_header = line[1:]
                current_sequence = []
            else:
                current_sequence.append(line.upper())

        
        if current_header is not None:
            sequences[current_header] = "".join(current_sequence)

    return sequences



