def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.

    The search only consider the portion from dat[low] to data[high] inclusive.
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            # print('Target present at:', mid)
            return True
        elif target < data[mid]:
            # Recur to the protion left of the middle 
            return binary_search(data, target, low, mid - 1)
        else:
            # Recur on the portion right of the middle
            return binary_search(data, target, mid+1, high)

numbers = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
# print(len(numbers))
low = 0
high = len(numbers) - 1
print(binary_search(numbers, 22, 0, high))