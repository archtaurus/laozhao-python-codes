#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0026.py
功能: 求n以内的质数
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.03.23
"""

import numpy as np

__all__ = ['primes_numpy', 'primes_generator']


def primes_numpy(n):
    """求n以内的质数

    利用numpy高效的数组运算求n以内的质数。

    参数:
        n (int): 质数上界

    返回:
        numpy.ndarray: 质数数组
    """
    nums = np.arange(2, n + 1)  # 从2到n的整数数组，长度为n-1
    for i in xrange(n - 1):     # 遍历nums数组
        p = nums[i]             # 当前的数值为p
        if p != 0:              # 若非0则为质数
            nums[i + p::p] = 0  # 将p以后p整倍数的整数置0
    return nums[nums != 0]      # 返回数组中的非0项


def primes_generator(n):
    """n以内的质数的生成器

    用排除法求n以内的质数。

    参数:
        n (int): 质数上界

    生成:
        int: 下一个质数
    """
    nums = range(2, n + 1)      # 从2到n的整数列表，长度为n-1
    for i in xrange(n - 1):     # 遍历nums列表
        p = nums[i]             # 当前的数值为p
        if p != 0:              # 若非0则为质数
            yield p
            for j in xrange(i + p, n - 1, p):
                nums[j] = 0     # 将p以后p整倍数的整数置0


if __name__ == '__main__':
    print primes_numpy(100)
    print list(primes_generator(100))
