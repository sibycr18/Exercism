def to_rna(dna_strand):
    nucleotide_complement = {'G' : 'C', 'C' : 'G', 'A' : 'U', 'T' : 'A'}
    return ''.join(nucleotide_complement[strand] for strand in dna_strand)
