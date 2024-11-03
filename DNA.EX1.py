#sample DNA string

with open("input.txt", "r") as file:
    dna_string =file.read().strip()

#count occurences of each nucleotides
count_A = dna_string.count("A")
count_C = dna_string.count("C")
count_G = dna_string.count("G")
count_T = dna_string.count("T")

#print
print(count_A, count_C, count_G, count_T)

