# -*- coding: utf-8 -*-

'''
随机扰乱数组顺序
'''
import random
import numpy as np
import copy

def shuffle(arr, inplace=False):

    if inplace:
        buff = arr
    else:
        buff = copy.copy(arr)

    size = len(buff)
    for i in range(size):
        swap_slot = random.randint(0, size-1)
        buff[i], buff[swap_slot] = buff[swap_slot], buff[i]

    return buff

if __name__ == "__main__":
    arr = [2, 5, 1, 6, 3, 4, 8, 7, 9]
    print shuffle(arr)
