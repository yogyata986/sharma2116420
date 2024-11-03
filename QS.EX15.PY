import random

def quicksort(A, left, right):
    if left < right:
        # Partition the array and get the pivot index
        pivot_index = partition(A, left, right)
        
        # Recursively apply quicksort to the left and right partitions
        quicksort(A, left, pivot_index - 1)
        quicksort(A, pivot_index + 1, right)

def partition(A, left, right):
    # Choose a random pivot index and move it to the end
    pivot_index = random.randint(left, right)
    pivot_value = A[pivot_index]
    A[pivot_index], A[right] = A[right], A[pivot_index]
    
    store_index = left
    
    # Move all elements less than pivot to the left
    for i in range(left, right):
        if A[i] < pivot_value:
            A[store_index], A[i] = A[i], A[store_index]
            store_index += 1
    
    # Move pivot to its final place
    A[store_index], A[right] = A[right], A[store_index]
    return store_index

def quicksort_main(n, A):
    # Call quicksort on the entire array
    quicksort(A, 0, n - 1)
    return A

# Sample Input
n = 7
A = [5, -2, 4, 7, 8, -10, 11]

# Run quicksort
sorted_A = quicksort_main(n, A)
print(sorted_A)
