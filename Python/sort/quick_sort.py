# -*- coding: utf-8 -*-



def quick_sort(data, left, right):
    '''
    递归方式实现quick sort

    :param data: 待排序的数据，list类型
    :param left: 本次排序的下界
    :param right: 本次排序的上界
    :return: 排序后的数据
    '''

    if left > right:
        return

    lower_idx = left
    upper_idx = right

    # left第一个选为交换判断的哨兵
    sentinel = data[left]

    while lower_idx < upper_idx:

        # 找到右边小余sentiel的值 （因为sentinel取的left one，因此必须先从右半边开始搜索，否则有问题）
        while (data[upper_idx] >= sentinel) and lower_idx < upper_idx:
            upper_idx -= 1

        # 找到左边大于sentinel的值
        while (data[lower_idx] <= sentinel) and lower_idx < upper_idx:
            lower_idx += 1

        # 左边的大值 <-> 右边的小值
        if lower_idx < upper_idx:
            data[lower_idx], data[upper_idx] = data[upper_idx], data[lower_idx]

    # 退出循环时，sentinel移到正确的位置(left right交汇处)
    data[left], data[lower_idx] = data[lower_idx], sentinel

    # 递归处理后sentinel的左半部分和有半部分
    quick_sort(data, left, lower_idx - 1)
    quick_sort(data, lower_idx + 1, right)

    return data


def sort(data, inplace=False):
    '''
    排序入口函数

    :param data: 待排序的对象，list类型
    :param inplace: 是否原地排序，False则会copy一份数据进行排序
    :return: 排序后的对象
    '''

    if not isinstance(data, list):
        raise ValueError("input data must be list type")

    if len(data) == 0:
        return data

    left = 0
    right = len(data) - 1

    if inplace:
        arr = data
    else:
        arr = data[:]

    return quick_sort(arr, left=left, right=right)


if __name__ == "__main__":
    # test data
    data = [2, 1, 8, 4, 3, 9, 5]

    print sort(data, inplace=False)
    print data
