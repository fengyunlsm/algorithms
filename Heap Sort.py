# -*- coding: utf-8 -*-

def max_heapify(heap, index):

    def left(i):
        return 2 * i + 1

    def right(i):
        return 2 * i + 2

    def parent(i):
        return  i / 2

    def has_left_leaf(index):
        if heap[index] <= len(heap) - 1:
            return True
        else:
            return False

    def has_right_leaf(index):
        if right(index) <= len(heap) - 1:
            return True
        else:
            return False

    def is_left_maximum(index):
        if heap[index] < heap[left(index)]:
            return True
        else:
            return False

    def max(index, leaf):
        # 如何获取最大值
        if has_right_leaf(index):
            if heap[leaf] < heap[right(index)]:
                return right(index)
            else:
                return leaf  # 这个改了！？
        else:
            return leaf

    def get_max_value(index):
        # 判断左右是不是为空再去比较
        if has_left_leaf(index):
            if is_left_maximum(index):
                return max(index, left(index)) # 这个是什么意思？
            else:
                return max(index, index)
        else:
            return index

    def exchange(largest, index):
        # 交换两者之间的数值
        heap[index], heap[largest] = heap[largest], heap[index]

    if left(index) < len(heap):
        largest = get_max_value(index) # 获取最大值，交换位置
        if largest == index:
            # mid end (这里死掉了)
            #
            return heap
        else:
            exchange(largest, index)
            return max_heapify(heap, largest)
    else:
        # end
        return heap



# 函数功能：建堆
def build_max_heap(heap):
    for index in range(len(heap) / 2 -1, -1, -1):
        # 进行排序
        max_heapify(heap, index)
    return heap


# 堆排序算法
def heap_sort(heap):

    heap_length = len(heap)

    def exchanged_heap(heap, heap_length):
        heap_prefix = heap[0:heap_length]
        heap_suffix = heap[heap_length:len(heap)]
        start = heap_length / 2 - 1
        end = -1
        for heap_index in range(start, end, -1):
            heap_prefix = max_heapify(heap=heap_prefix, index=heap_index)
        heap_prefix.extend(heap_suffix)
        heap = heap_prefix
        return heap

    def exchange_start_end(heap, start, end):
        heap[start], heap[end] = heap[end], heap[start]

    for i in range(len(heap) - 1, 0, -1):
        # 交换到２就结束
        exchange_start_end(heap=heap, start=0, end=i)
        heap_length = heap_length - 1
        heap = exchanged_heap(heap, heap_length)
    return heap


heap = [16,4,10, 14, 7, 9, 3, 2, 8, 1]
print max_heapify(heap, 1)

# build_heap = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# x = build_max_heap(build_heap)
# print heap_sort(x)