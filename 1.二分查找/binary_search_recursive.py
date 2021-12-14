def binary_search_recursive(array, left, right, num):
    if left > right:  #递归结束条件
        return -1
    mid = (left + right) // 2
    if num < array[mid]:
        right = mid - 1
    elif num > array[mid]:
        left = mid + 1
    else:
        return mid
    return binary_search_recursive(array, left, right, num)


my_list = [1, 3, 5, 7, 9]

print(binary_search_recursive(my_list, 0, len(my_list) - 1, 9))
