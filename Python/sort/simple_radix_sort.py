# -*- coding: utf-8 -*-

import itertools


def simple_radix_sort(data, radix):
    '''
    最简化版本的基数排序，只针对>0的纯数字进行排序

    :param data: 待排序元素
    :param radix: 桶的基数，用于初始化桶
    :return: 排序后的元素
    '''

    if not isinstance(data, list):
        raise ValueError("input must be list type")

    # 判断待排序元素是否有负数
    if len(filter(lambda x: x < 0, data)) > 0:
        raise ValueError("simple_radix_sort only support positive number")

    if not data or len(data) == 0:
        return []

    # 设置桶的元素都为0
    buckets = [0 for _ in data]

    for n in data:
        idx = n - 1
        buckets[idx] += 1

    # 遍历桶，按桶slot中的元素个数，展开为list
    return map(lambda x: x, itertools.chain(*[[idx + 1] * x for idx, x in enumerate(buckets)]))


if __name__ == "__main__":
    data = [2, 4, 5, 5, 6, 1, 3, 8, 9]

    print simple_radix_sort(data, radix=max(data))
