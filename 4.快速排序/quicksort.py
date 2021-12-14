def quicksort(array):
    if len(array) <= 1:
        return array  #基线条件：为空或者只包含一个元素的数组可以认为是 “有序的”
    else:
        pivot = array[0]  # 选择基准值
        less = [i for i in array[1:] if i <= pivot]  #由所有小于等于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]  #由所有大于基准值的元素组成的子数组
        return quicksort(less) + [pivot] + quicksort(greater)  # 递归


print(quicksort([1, 3, 2, 4, 8, 5, 7, 10, 9, 6]))
