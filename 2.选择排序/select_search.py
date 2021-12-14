#选择排序
#时间复杂度O(n²)
def select_search(arr):
    newArr = []
    # rang(5) [0，5） 左闭右开
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


#这个方法用来找出数组最小元素
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    #从第二个元素开始
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


print(select_search([5, 3, 6, 2, 10]))
