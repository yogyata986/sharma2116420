def merge_sorted_arrays(A, B):
    # Initialize pointers for both arrays and the result array
    i, j = 0, 0
    C = []
    
    # Merge elements until we reach the end of one of the arrays
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    # Append remaining elements from A (if any)
    while i < len(A):
        C.append(A[i])
        i += 1

    # Append remaining elements from B (if any)
    while j < len(B):
        C.append(B[j])
        j += 1

    return C

# Function to read input from a text file

    with open(file_path, 'r') as file:
        n = int(file.readline().strip())  # Read size of array A (optional, can be ignored in the logic)
        A = list(map(int, file.readline().strip().split()))  # Read elements of array A
        m = int(file.readline().strip())  # Read size of array B (optional, can be ignored in the logic)
        B = list(map(int, file.readline().strip().split()))  # Read elements of array B
    return A, B

# Main code execution
if __name__ == "__main__":
    # File path to input file
    file_path = 'input.txt'  # Ensure this file exists with correct format in the same directory
    
    
    