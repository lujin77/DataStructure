# -*- coding: utf-8 -*-


def sort(data, inplace=False):
    '''
    冒泡排序简化版本，支持哨兵

    :param data: 待排序元素
    :param radix: 桶的基数，用于初始化桶
    :return: 排序后的元素
    '''

    if not isinstance(data, list):
        raise ValueError("input must be list type")

    if not data or len(data) == 0:
        return []

    # 根据inpalce标志，赋值待排序数组
    if inplace:
        arr = data
    else:
        arr = data[:]

    size = len(arr)
    for i in range(0, size):

        # 标志位
        isSwap = False

        for j in range(1, size - 1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                isSwap = True

        # 若某一轮无交换，则说明有序，可以直接退出
        if not isSwap:
            return arr

    return arr

if __name__ == "__main__":
    data = [2, 4, 5, 5, 6, 1, 3, 8, 9]

    print sort(data, inplace=False)
