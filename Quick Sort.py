# -*- coding: utf-8 -*-

# print 'aaa'
# 暂时想不到怎么解决这个问题
def quick_sort(array, left ,right):

    # 拆分
    # 停止
    # 保存起始点

    i = left
    def inplace_sort(array, left, right):
        # 原地排序
        control_point = array[left]
        while(1):
            #
            if len(array) ==1:
                return   # 这个地方是有错误的
            if array[right] < control_point:
                # 停止
                # left 继续前行 直到 大于基准点就停止
                # 一种是碰到了right ,那交换right,left的位置
                if left == right:
                    # 停止，并交换 基准点和 array[left]
                    array[right], array[control_point] = array[control_point], array[right]
                    return left
                else:
                    if array[left] <= control_point:
                        left = left + 1
                    else:
                        array[right], array[left] = array[left], array[right]
            else:
                right = right - 1

    if left >= right:
        # 结束的标志位
        return
    mid = inplace_sort(array, left, right)


        # 函数功能：左排序
        # 函数合约：array
        # 函数名字：left_sort(array,left, mid-1)
    quick_sort(array, left, mid-1)
        # 右排序
        # 函数名字：right_sort(array,mid+1,right)

    quick_sort(array, mid+1,right)
    print array



# 不知道怎么修改数据之后数值保持不变

array = [10, 3, 4, 12, 5, 0]
quick_sort(array, 0, 5)
