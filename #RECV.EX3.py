#RECV.EX3.PY
with open("input.txt", "r") as file:
    dna_string =file.read().strip()

#Reverse the DNA string 
reversed_dna = dna_string[::-1]

# create complement using a dictionary mapping 
complement_mapping = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'

}

#use list comprehesion to get complement for each nucleotides in the reversed
reverse_complement = ''.join(complement_mapping[base] for base in reversed_dna)

#print 
print(reverse_complement)