#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0007.py
# 功能: 把2的1000次方的数值各位上的数字加在一起是多少？
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2011

print sum(map(int, list(str(2**1000))))
