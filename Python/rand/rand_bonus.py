# -*- coding: utf-8 -*-

'''
红包分裂，每次生成当前余额的0.01 ~ 2 * mean的红包，最后一次直接返回余额
'''

from __future__ import division
import random
import numpy as np

def split_bonus(total, k):
    remain = total
    out = []
    for i in range(k - 1):
        mean = remain / (k - i)
        new_bonus = 0.01 + random.random() * mean * 2
        remain -= new_bonus
        out.append(new_bonus)
    else:
        out.append(remain)

    return out

if __name__ == "__main__":
    results =  split_bonus(100, 10)
    assert np.sum(results) == 100
    print results
