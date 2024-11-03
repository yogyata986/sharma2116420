def heapify(A, n, i):
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # left child index in zero-based array
    right = 2 * i + 2    # right child index in zero-based array

    # If left child exists and is greater than root
    if left < n and A[left] > A[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and A[right] > A[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # Swap
        heapify(A, n, largest)

def build_max_heap(A):
    n = len(A)
    # Start from the last non-leaf node and go up to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    return A

# Example usage
n = 5
A = [1, 3, 5, 7, 2]
result = build_max_heap(A)
print(" ".join(map(str, result)))
