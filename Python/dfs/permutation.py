# -*- coding: utf-8 -*-

'''
深度优先方式生成全排列
'''

def permutate(valid_nums, result_buff=None):
    """广度优先生成排列
    
    :param data_set: 目前轮次可用的数据集
    :param buff: 结果缓存
    :param size: 排列的集合长度
    :return: None，找到排列后直接输出
    """

    # 第一层缓存变量初始化
    if not result_buff:
        result_buff = []

    # 走到了最后一层
    if len(valid_nums) == 0:
        print result_buff
        return

    # 每一层枚举可选值，并根据已用过的数字，过滤出可用值
    for num in valid_nums:
        result_buff.append(num)
        # 生成下一步的可用数据集
        next_valid_nums = valid_nums[:]
        next_valid_nums.remove(num)
        # print next_valid_nums
        permutate(next_valid_nums, result_buff)  # 递归生成下一层结果
        result_buff.remove(num)

if __name__ == "__main__":
    permutate([1,2,3])
