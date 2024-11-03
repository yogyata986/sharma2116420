def heapify(A, n, i):
    # Maintains the max-heap property for the subtree rooted at index i
    largest = i
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If the left child is larger than the root
    if left < n and A[left] > A[largest]:
        largest = left

    # If the right child is larger than the largest so far
    if right < n and A[right] > A[largest]:
        largest = right

    # If the largest element is not the root
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # Swap
        # Recursively heapify the affected subtree
        heapify(A, n, largest)

def heap_sort(A):
    n = len(A)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move the current root (largest) to the end
        A[0], A[i] = A[i], A[0]
        # Call heapify on the reduced heap
        heapify(A, i, 0)

    return A

# Sample Input
n = 9
A = [2, 6, 7, 1, 3, 5, 4, 8, 9]

# Perform Heap Sort
sorted_A = heap_sort(A)
print(sorted_A)
