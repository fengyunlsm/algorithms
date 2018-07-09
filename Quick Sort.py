# -*- coding: utf-8 -*-

# print 'aaa'

def quick_sort(array, left ,right):

    # 拆分
    # 停止
    # 保存起始点
    i = left
    def inplace_sort(array, left, right):
        # 原地排序
        control_point = array[left]
        while(1):
            if array[right] < control_point:
                # 停止
                # left 继续前行 直到 大于基准点就停止
                # 一种是碰到了right ,那交换right,left的位置
                if left == right:
                    # 停止，并交换 基准点和 array[left]
                    temp = array[right]
                    array[right] = array[i]
                    array[i] = temp
                    return left
                else:
                    if array[left] <= control_point:
                        left = left + 1
                    else:
                        # 交换两者之间的位置
                        temp = array[right]
                        array[right] = array[left]
                        array[left] = temp
            else:
                right = right + 1
                # right 继续前行

    if left >= right:
        # 结束的标志位
        return
    else:
        mid = inplace_sort(array, left, right)

        # 函数功能：左排序
        # 函数合约：array
        # 函数名字：left_sort(array,left, mid-1)
        quick_sort(array, left, mid-1)
        # 右排序
        # 函数名字：right_sort(array,mid+1,right)

        quick_sort(array, mid+1,right)
    print array


array = [10, 3, 4, 12, 5, 0]
quick_sort(array, 0, 2)
