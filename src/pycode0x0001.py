#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0001.py
# 功能: 求数字1、2、3、4能组成多少个无重复数字的三位数？
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.11.11

numbers = [100 * i + 10 * j + k
           for i in [1, 2, 3, 4] for j in [1, 2, 3, 4] for k in [1, 2, 3, 4]
           if i != j and j != k and k != i]
count = len(numbers)
print count, numbers
