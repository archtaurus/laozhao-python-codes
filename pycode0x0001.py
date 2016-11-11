#!/usr/bin/env python2
# -*- coding:utf-8 -*-

# 数字1、2、3、4能组成多少个无重复数字的三位数？

numbers = [100 * i + 10 * j + k
           for i in [1, 2, 3, 4] for j in [1, 2, 3, 4] for k in [1, 2, 3, 4]
           if i != j and j != k and k != i]
count = len(numbers)
print count, numbers
