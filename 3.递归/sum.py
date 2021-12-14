#求和
def sum(arr):
    print(arr)
    num = arr[0]
    if len(arr) == 1:
        return num
    else:
        arr.pop(0)
        return num + sum(arr)


print(sum([1, 2, 3, 4, 5]))
