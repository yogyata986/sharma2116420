
def rabbit_pairs(n,k):
    # array to store the no ofrabbits pairs for each month 
    F = [0] * ( n + 1)

    #initial conditions 
    F[1] = 1 # MONTH 1 
    if n > 1:
        F[2] = 1 #month 2 

        #fill the array using the recurrence relation 
    for month in range (3, n + 1):
        F[month] = F[month - 1] + k * F[month -2]

    return F[n]
   

with open ("input.txt", "r")as file :
    n,k = map(int, file.read().strip().split())

    print(rabbit_pairs(n,k))

    

        

