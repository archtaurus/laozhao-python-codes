#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x001E.py
# 功能: numpy.array demo
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.11.22

import numpy as np


array_a = np.array([1, 2, 3, 4])        # 一维数组
array_b = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])   # 二维数组
print "type(array_a) ->", type(array_a)
print "type(array_a.dtype) ->", type(array_a.dtype)
print "array_a ->", array_a
print "array_a.dtype ->", array_a.dtype
"""其它的numpy.dtype有：uint8, int8, int32, str, float, complex等"""
print "array_b ->"
print array_b

print "打印数组的维数"
print "array_a.shape ->", array_a.shape
print "array_b.shape ->", array_b.shape
"""(4,) (3, 4)"""

# 改变数组的位数
array_a.shape = 2, -1
print "array_a.shape ->", array_a.shape
print "array_a ->"
print array_a
"""当某个轴的元素为-1时,将根据数组元素的个数自动计算此轴的长度
[[1 2]
 [3 4]] (2, 2)
"""

# reshape
array_c = array_b.reshape((4, 3))
array_b[2][3] = 999
print "array_c.shape ->", array_a.shape
print "array_c ->"
print array_c
"""数组array_b和array_c其实共享数据存储内存区域,因此修改其中任意一个数组的
元素都会同时修改另外一个数组的内容
[[  1   2   3]
 [  4   5   6]
 [  7   8   9]
 [ 10  11 999]] (4, 3)
"""

# arange
print "np.arange(0, 1, 0.1) ->", np.arange(0, 1, 0.1)
"""不包含end值1
[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9]
"""

# linspace
print "np.linspace(0, 1, 11) ->", np.linspace(0, 1, 11)
"""linspace默认包含end
[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1. ]
"""

# fromstring
array_d = np.fromstring("abcdefgh", dtype=np.int8)
print "np.fromstring('abcdefgh', dtype=np.int8) ->", array_d
"""[ 97  98  99 100 101 102 103 104]"""

# fromfunction
array_e = np.fromfunction(lambda x, y: (x + 1) * (y + 1),
                          (9, 9),
                          dtype=np.int)
print "np.fromfunction(lambda x, y: (x + 1) * (y + 1),(9, 9),dtype=np.int)"
print array_e
"""生成一个99乘法口诀表"""

# 取array_b的第一列
print "取array_b的第一列 array_b[:, 0] ->", array_b[:, 0]
"""和Python的列表序列不同,通过下标范围获取的新的数组是原始数组的一个视图。
它与原始数组共享同一块数据空间 [1 5 9]
"""

# 通过布尔值选择元素
print array_d[np.array([True, False, True, False, True, False, True, False])]
"""[ 97  99 101 103]"""

# 产生一个bool的ndarray
print array_c % 2 == 0
"""
[[False  True False]
 [ True False  True]
 [False  True False]
 [ True False False]]
 """

# 收集数组中的偶数
print array_c[array_c % 2 == 0]
"""二维数组中的偶数，返回的是一个一维数组[ 2  4  6  8 10]"""
