#选择排序
#时间复杂度O(n²)
def select_search(arr):
    for i in range(len(arr)):
        smallest = arr[i]
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        #交换
        if smallest_index != i:
            temp = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = temp
    return arr


print(select_search([5, 3, 6, 2, 10]))