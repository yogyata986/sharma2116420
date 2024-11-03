def three_way_partition(n, A):
    pivot = A[0]
    less = []
    equal = []
    greater = []
    
    for num in A:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    
    # Concatenate the lists to form the desired partitioned array B
    B = less + equal + greater
    return B

# Sample Input
n = 9
A = [4, 5, 6, 4, 1, 2, 5, 7, 4]
result = three_way_partition(n, A)

print(result)
