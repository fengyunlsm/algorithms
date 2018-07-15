# -*- coding: utf-8 -*-

# 从小到大的排序
def bubble_sort(bubble_array):
    def exchange_latter_former(latter, former):
        bubble_array[latter], bubble_array[former] = bubble_array[former], bubble_array[latter]


    def is_latter_larger(index):
        if bubble_array[index] > bubble_array[index - 1]:
            return True
        else:
            return False

    def put_maxnum_to_maxlocation(max_location):
        end = len(bubble_array) - 1
        start = max_location
        for index in range(end, start, -1):
            if (is_latter_larger(index)):
                exchange_latter_former(index, index - 1)
            else:
                pass

    for max_location in range(0, len(bubble_array)-2, 1):
        put_maxnum_to_maxlocation(max_location)
    return bubble_array


bubble_array = [4, 5, 1, 7, 9, 2]
print bubble_sort(bubble_array)

