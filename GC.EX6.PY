def calculate_gc_content(dna):
    """calculate the GC content of DNA string """
    g_count = dna.count('G')
    c_count = dna.count('C')
    gc_content = (g_count + c_count) / len(dna) * 100 
    return gc_content
    
def parse_fasta(filename):
    """Parse the FASTA formatted file and return a dictionary of IDs and their corresponding DNA strings."""

    with open ("input.txt", "r")as file :
       fasta_data = file.read().strip().split('>')

       fasta_dict={}

    for entry in fasta_data[1:]:
        lines = entry.strip().splitlines()
        identifier = lines[0]
        dna_string = ''.join(lines[1:])  # Join the rest of the lines into a single string
        fasta_dict[identifier] = dna_string
    
    return fasta_dict

def main():
    filename = "input.txt"  # Ensure the input file name matches your text file
    fasta_dict = parse_fasta(filename)
    
    max_gc_id = ""
    max_gc_content = 0.0
    
    for identifier, dna in fasta_dict.items():
        gc_content = calculate_gc_content(dna)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = identifier
    
    # Print the result
    print(max_gc_id)
    print(f"{max_gc_content:.6f}")  # Print with six decimal places

# Call the main function to run the program
if __name__ == "__main__":
     main()
