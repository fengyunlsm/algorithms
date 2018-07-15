# -*- coding: utf-8 -*-



def insert_sort(insert_array):

    def insert_to_some_location(wait_for_insert_index):
        def find_location(wait_for_insert_index):

            def is_wait_insert_larger(index, wait_for_insert_index):
                if insert_array[wait_for_insert_index] > insert_array[index]:
                    return True
                else:
                    return False

            for index in range(0, wait_for_insert_index, 1):
                if is_wait_insert_larger(index, wait_for_insert_index):
                    pass
                else:
                    return index

        def move_rest(start):
            # 确认是否保存的问题
            if start is not None:
                for j in range(wait_for_insert_index-1, start-1, -1):
                    insert_array[j+1] = insert_array[j]
            else:
                # 不需要移动
                pass

        def insert_to_location(temp, start):
            if start is not None:
                insert_array[start] = temp
            else:
                pass

        start = find_location(wait_for_insert_index)    # 寻找
        move_rest(start)
        insert_to_location(temp, start)

    for wait_for_insert_index in range(0, len(insert_array), 1):
        temp = insert_array[wait_for_insert_index]
        insert_to_some_location(wait_for_insert_index)

    return insert_array



array = [3, 4, 1, 8, 10, 7, 5]

print insert_sort(array)
