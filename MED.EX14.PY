import random

def quickselect(A, left, right, k):
    if left == right:  # If the list contains only one element
        return A[left]

    # Select a random pivot index
    pivot_index = random.randint(left, right)
    
    # Partition the array around the pivot
    pivot_index = partition(A, left, right, pivot_index)

    # The pivot is in its final sorted position
    if k == pivot_index:
        return A[k]
    elif k < pivot_index:
        # Recur on the left side
        return quickselect(A, left, pivot_index - 1, k)
    else:
        # Recur on the right side
        return quickselect(A, pivot_index + 1, right, k)

def partition(A, left, right, pivot_index):
    pivot_value = A[pivot_index]
    # Move pivot to the end
    A[pivot_index], A[right] = A[right], A[pivot_index]
    store_index = left

    # Move all elements smaller than pivot to the left
    for i in range(left, right):
        if A[i] < pivot_value:
            A[store_index], A[i] = A[i], A[store_index]
            store_index += 1

    # Move pivot to its final place
    A[right], A[store_index] = A[store_index], A[right]
    
    return store_index

# Main function to find the k-th smallest element
def find_kth_smallest(n, A, k):
    # k is 1-based index, so we convert it to 0-based for the function
    return quickselect(A, 0, n - 1, k - 1)

# Sample Input
n = 11
A = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]
k = 8

# Sample Output
result = find_kth_smallest(n, A, k)
print(result)
