"""
Sequence metrics module
Pure functions for DNA sequence analysis
"""
def sequence_length(sequence):
    """
    Returns the length of a DNA sequence.

    """
    return len(sequence)

def gc_content(sequence):
    """
    Returns the GC content percentage of a DNA sequence.

    """
    sequence = sequence.upper()

    if len(sequence) == 0:
        return 0.0
    
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_percent = (g_count + c_count)/len (sequence) *100
    return gc_percent 

def nucleotide_frequency(sequence):
    """
    Returns nucleotide counts for a DNA sequence.
    """
    sequence = sequence.upper()

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }

def at_skew(sequence):
    """
    Returns AT skew of a DNA sequence.
    """
    sequence = sequence.upper()

    a_count = sequence.count("A")
    t_count = sequence.count("T")

    if a_count + t_count == 0:
        return 0.0

    return (a_count - t_count) / (a_count + t_count)

def gc_skew(sequence):
    """
    Returns GC skew of a DNA sequence.
    """
    sequence = sequence.upper()

    g_count = sequence.count("G")
    c_count = sequence.count("C")

    if g_count + c_count == 0:
        return 0.0

    return (g_count - c_count) / (g_count + c_count)

