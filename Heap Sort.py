# -*- coding: utf-8 -*-


# 函数的输入：
# 函数的功能：保持堆的性质(选择的节点大于其所有子节点)

def max_heapify(heap, index):
    # 进行堆排序
    # 如何进行堆排序
    def left(i):
        return 2 * i + 1

    def right(i):
        return 2 * i + 2

    def root(i):
        return  i / 2

    def get_max_value(index):
        # 判断左右是不是为空再去比较
        if left(index) < len(heap) - 1:
            if heap[index] < heap[left(index)]:
                if right(index) < len(heap) - 1:
                    if heap[left(index)] < heap[right(index)]:
                        return right(index)
                    else:
                        return left(index)
                else:
                    return left(index)
            else:
                if right(index) < len(heap) - 1:
                    if heap[index]>heap[right(index)]:
                        return index
                    else:
                        return right(index)
                else:
                    return index
        else:
            return index


    def exchange(largest, index):
        # 交换两者之间的数值
        temp = heap[index]
        heap[index] = heap[largest]
        heap[largest] = temp

    print left(index)
    if left(index) < len(heap):
        # 继续
        largest = get_max_value(index) # 获取最大值，交换位置
        if largest == index:
            print heap
        else:
            exchange(largest, index)
        # 再进行递归
            max_heapify(heap, largest)
    else:

        print heap

        # stop

def build_max_heap(heap):
    for index in range(len(heap) / 2 -1, -1, -1):
        # 进行排序
        print index
        max_heapify(heap, index)

    print heap


# heap = [16,4,10, 14, 7, 9, 3, 2, 8, 1]
# max_heapify(heap, 1)

build_heap = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
build_max_heap(build_heap)