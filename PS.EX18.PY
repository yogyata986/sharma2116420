def k_smallest_elements(n, A, k):
    # Sort the array
    A_sorted = sorted(A)
    # Return the first k elements from the sorted array
    return A_sorted[:k]

# Sample Input
n = 10
A = [4, -6, 7, 8, -9, 100, 12, 13, 56, 17]
k = 3

# Get the k smallest elements
result = k_smallest_elements(n, A, k)
print(result)
