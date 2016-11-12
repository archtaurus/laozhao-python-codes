#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0012.py
# 功能: 自定义my_sorted函数排序一个列表
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.03.05


def pop_min(input_list):
    "pop the smallest number from the list"
    min_index, min_value = 0, input_list[0]
    # 找最小的数和它的索引
    for index, value in enumerate(input_list):
        if value < min_value:
            min_index, min_value = index, value
    del input_list[min_index]     # 从列表中删除最小的元素
    return min_value


def my_sorted(original_list):
    "return a sorted list"
    sorted_list = []
    # 将最小的数逐一从原列表搬到新列表中
    while original_list:
        sorted_list.append(pop_min(original_list))
    return sorted_list


if __name__ == '__main__':
    original_list = [-2, 1, -1, 8, -3, -4, 11, 13]
    sorted_list = my_sorted(original_list)
    print (sorted_list)
