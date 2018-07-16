# -*- coding: utf-8 -*-

def merge_sort(merge_array, left, right):
    # 分解
    # 排序
    # 合并
    def merge(left, mid, right):
        # 预防胜于治疗
        left_array = merge_array[left:mid+1]
        right_array = merge_array[mid+1:right+1]
        left_array_index = 0
        right_array_index = 0

        for merge_array_index in range(left, right+1, 1):
            def is_left_index_exist(left_array_index):
                if left_array_index > len(left_array) - 1:
                    return False
                else:
                    return True

            def is_right_index_exist(right_array_index):
                if right_array_index > len(right_array) - 1:
                    return False
                else:
                    return True

            def is_right_larger():
                if left_array[left_array_index] < right_array[right_array_index]:
                    return True
                else:
                    return False

            def move_left_to_merge(left_array_index):
                merge_array[merge_array_index] = left_array[left_array_index]


            def move_right_to_merge(right_array_index):
                merge_array[merge_array_index] = right_array[right_array_index]


            if not is_left_index_exist(left_array_index):
                move_right_to_merge(right_array_index)
                right_array_index = right_array_index + 1
            elif not is_right_index_exist(right_array_index):
                move_left_to_merge(left_array_index)
                left_array_index = left_array_index + 1
            else:
                if is_right_larger():
                    move_left_to_merge(left_array_index)
                    left_array_index = left_array_index + 1
                else:
                    move_right_to_merge(right_array_index)
                    right_array_index = right_array_index + 1

    array_length = len(merge_array[left:right+1])
    if array_length == 2:
        if merge_array[left] < merge_array[right]:
            pass
        else:
            merge_array[left], merge_array[right] = merge_array[right],merge_array[left]
        return
    elif array_length < 2 :
        return
    else:
        mid = (left + right ) / 2
        merge_sort(merge_array, left, mid)   # 功能
        merge_sort(merge_array, mid+1, right)
        merge(left, mid, right)
    return merge_array

# [8, 9, 1, 0, 5, 33, 5]
print merge_sort([8, 9, 1, 0, 5, 33, 11], 0, 6)

print merge_sort([4, 6, 1, 5], 0, 3)