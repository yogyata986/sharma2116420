

def dominant_phenotype_probability(k, m, n):
    #Total number of organisms
    total = k + m + n

    #total pairings
    total_pairs = total * (total - 1)

    # calculate proability of each type of pairing resulting in a dominant phenotype 
    prob_dominant = (
        #pairing: AA x AA
        k * (k - 1) +
        # pairing : AA X Aa
        2 * k * m +
        # pairing : AA X aa
        2 * k * n +
        # pairing : Aa x Aa ( 75% chance of dominant phenotype )
        m * (m - 1) * 0.75 +
        # pairing : Aa x aa (50% chance of dominant phenotype ) 
        2 * m * n * 0.5

    ) / total_pairs
    
    return prob_dominant

with open("input.txt", "r") as file:
    k,  m, n = map(int, file.read().strip().split())

    print(dominant_phenotype_probability(k,m,n))