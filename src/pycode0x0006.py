#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0006.py
功能: 求前一百个自然数的“和的平方”与它们的“平方的和”的差, 注0属于自然数。
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2011
"""

print sum(xrange(100))**2 - sum(n**2 for n in xrange(100))
