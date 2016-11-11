#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0002.py
# 功能: 长度为n的斐波拉契数列生成器
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.04.04
#
# 斐波那契数列（Fibonacci sequence）又称黄金分割数列，因数学家列昂纳多·斐波那契
# 以兔子繁殖为例子而引入，故又称为“兔子数列”，指的是这样一个数列：
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
# 在数学上斐波纳契数列以如下递归的方法定义：
# F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) (n≥2, n∈N*)
# 在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用。


def fib(n):
    """长度为n的斐波拉契数列生成器"""
    a, b = 0, 1
    for _ in xrange(n):
        yield a
        a, b = a + b, a


if __name__ == "__main__":
    for i in fib(10):
        print i,
