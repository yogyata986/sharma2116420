def rna_to_protein(rna_sequence):
    # RNA codon table dictionary
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
        'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    # Initialize the protein string
    protein_string = ""
    
    # Loop through the RNA sequence in steps of 3 (each codon)
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, 'Stop')
        
        # Stop translation if we hit a stop codon
        if amino_acid == 'Stop':
            break
        protein_string += amino_acid
    
    return protein_string

# Function to read RNA sequence from a text file
def read_rna_sequence_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read the first line in the file and strip any extra whitespace
        rna_sequence = file.readline().strip()
    return rna_sequence

# Main part of the code to use the file input
file_path = 'input.txt'  # Replace with the path to your file
rna_sequence = read_rna_sequence_from_file(file_path)
protein_string = rna_to_protein(rna_sequence)
print(protein_string)
