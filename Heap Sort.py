# -*- coding: utf-8 -*-


# 函数的输入：
# 函数的功能：保持堆的性质(选择的节点大于其所有子节点)
# 构造堆属性
def max_heapify(heap, index):
    # 进行堆排序
    # 如何进行堆排序
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
        if right(index) < len(heap) - 1:
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
            return
        else:
            exchange(largest, index)
            max_heapify(heap, largest)
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
    # 将第一个元素放到最后一位
    # 再保持堆的属性
    def exchange(start, end):
        # 交换第一个位置和最后一个位置
        heap[start], heap[end] = heap[end], heap[start]

    heap_len_temp = len(heap)
    for i in range(len(heap) - 1, 1, -1):
        # 交换到２就结束
        exchange(0, i)
        heap_len_temp = heap_len_temp - 1
        print heap
        for index in range(heap_len_temp / 2 -1, -1, -1):
            # 使之最大化
            max_heapify(heap, index)    # 堆栈化
        print heap

    print heap



# heap = [16,4,10, 14, 7, 9, 3, 2, 8, 1]
# heap = [1, 14, 10, 8, 7, 9, 3, 2, 4]
# max_heapify(heap, 1)

build_heap = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
x = build_max_heap(build_heap)
print x

heap_sort(x)