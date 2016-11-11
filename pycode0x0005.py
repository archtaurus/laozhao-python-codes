#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0005.py
# 功能: 求小于1000的整数中3或5的整倍数的和
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2011

print sum(n for n in xrange(1000) if n % 3 == 0 or n % 5 == 0)
