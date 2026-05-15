import re
# Codon to amino acid dictionary
codon_table = {
    "UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
    "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
    "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
    "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
    "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
    "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
    "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
    "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
    "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
    "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
    "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
    "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
    "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
    "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
    "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
    "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"
}
rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
codons = re.findall(r'.{3}', rna)
#translate codons to protein
protein = ''
for codon in codons:
    amino_acid = codon_table.get(codon)
    print("codon:", codon, "Amino acid:", amino_acid)
    if amino_acid == "Stop":
        break
    protein += amino_acid
print(protein)

def find_motif_locations(dna, motif):
    positions = []
    for match in re.finditer(f'(?={motif})', dna):
        positions.append(match.start() + 1)
    return positions

# Example input
dna = "GATATATGCATATACTT"
motif = "ATAT"
positions = find_motif_locations(dna, motif)
print(" ".join(map(str, positions)))