#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0009.py
# 功能: 已知10个半径，求圆面积的和，要求保留3位小数(派和四舍五入)
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.06.06

from math import pi

radius = [45, 58, 21, 61, 42, 69, 49, 88, 83, 27]
area = round(sum(pi * r**2 for r in radius), 3)  # 四舍五入

print area
