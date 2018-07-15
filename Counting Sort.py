# -*- coding: utf-8 -*-

# 前提是array存放的是整数
# array
# result:长度是len的数组
# k 是　某个整数
def couning_sort(array, result, k):
    # 初始化 temp的数组
    temp = []
    for temp_index in range(0, k+1, 1):
        temp.append(0)

    for array_index in range(0, len(array), 1):
        result.append(0)
    print result

    #创建长度为len(array)的列表result


    # 统计array 中的元素的个数
    for temp_index in range(0, k+1, 1):
        for array_index in range(0, len(array), 1):
            if temp_index == array[array_index]:
                temp[temp_index] = temp[temp_index] + 1
            else:
                pass

    # 统计每个元素前面有多少个元素,相当于这些元素的位置
    for temp_index in range(1, k+1, 1):
        # 统计temp_index 前面的元素的个数
        temp[temp_index] = temp[temp_index] + temp[temp_index-1]

        # 将元素放在temp[index]-1的为位置上
        # 再将位置减去－
    for array_index in range(len(array)-1, -1, -1):
        result[temp[array[array_index]]-1] = array[array_index]
        temp[array[array_index]] = temp[array[array_index]] -1

    return result
    # 将元素存放到result


array = [2, 1, 8, 0, 5, 1]
print couning_sort(array, [], 10)