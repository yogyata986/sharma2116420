#RNA.ex2.py
#sample dna string
with open("input.txt", "r") as file:
    dna_string =file.read().strip()
#Transcribe DNA to RNA by replacing "T" with"U"
rna_string = dna_string.replace("T","U")

#print
print(rna_string)