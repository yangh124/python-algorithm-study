def count_num(arr):
    if arr == []:
        return 0
    else:
        return 1 + count_num(arr[1:])


print(count_num([1, 2, 3, 4, 5, 6]))
