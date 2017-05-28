# -*- coding: utf-8 -*-

"""斐波拉契数量"""

from functools import wraps


def fib(i):
    """递归方式实现"""
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memo
def fib2(i):
    """动态规方式实现，使用decorator缓存中间计算结果"""
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)


if __name__ == "__main__":
    print fib(4)

    print fib2(4)
