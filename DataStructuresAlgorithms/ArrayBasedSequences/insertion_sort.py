def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for i in range(1, len(A)):
        value = A[i]
        hole = i
        while hole > 0 and A[hole-1] > value:
            A[hole] = A[hole-1]
            hole -= 1
        A[hole] = value
    return A

print(insertion_sort([4, 2, 1, 5, 0]))