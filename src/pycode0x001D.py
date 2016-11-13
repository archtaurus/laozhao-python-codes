#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x001D.py
# 功能: 打印字符串在内存里的二进制形式
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.11.13

string = 'I love coding!\0'
seperator = "|"
print seperator.join(bin(ord(c))[2:].zfill(8) for c in string)
