def max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] > max(arr[1:]):
            return arr[0]
        else:
            return max(arr[1:])


print(max([1, 2, 3, 4, 5]))
