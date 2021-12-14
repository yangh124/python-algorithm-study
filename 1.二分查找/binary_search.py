# 时间复杂度 O(log n)
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        temp = list[mid]
        if temp == item:
            return mid
        if temp > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 9))
print(binary_search(my_list, -1))