def partition_array(n, A):
    pivot = A[0]
    left = [x for x in A if x < pivot]       # Elements less than the pivot
    middle = [x for x in A if x == pivot]     # Elements equal to the pivot (in this case, just the pivot itself)
    right = [x for x in A if x > pivot]       # Elements greater than the pivot
    return left + middle + right

# Example usage
n = 9
A = [7, 2, 5, 6, 1, 3, 9, 4, 8]
result = partition_array(n, A)
print(" ".join(map(str, result)))


