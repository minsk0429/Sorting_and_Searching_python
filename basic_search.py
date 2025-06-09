def sequential_search(A, key, low, high):
    for i in range(low, high + 1):
        if A[i] == key:
            return i
    return -1

def binary_search(A, key, low, high):
    if (low > high) :
        return -1
    
    middle = (low + high) // 2

    if (key == A[middle]):
        return middle
    elif (key < A[middle]):
        return binary_search(A, key, low, middle - 1)
    else:
        return binary_search(A, key, middle + 1, high)
    
def interpolation_search(A, key, low, high):
    if low > high or A[low] == A[high]:
        return -1
    
    middle = int(low + (high - low) * (key - A[low]) / (A[high] - A[low]))

    if middle < low or middle > high:
        return -1

    if A[middle] == key:
        return middle
    elif key < A[middle]:
        return interpolation_search(A, key, low, middle - 1)
    else:
        return interpolation_search(A, key, middle + 1, high)

    
    