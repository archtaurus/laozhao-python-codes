#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x001D.py
功能: 打印字符串在内存里的二进制形式
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.11.13
"""

string = 'I love coding!\0'
seperator = ""
print seperator.join(bin(ord(c))[2:].zfill(8) for c in string)

# OUTPUT:
# 010010010010000001101100011011110111011001100101001000000110001101101111011001000110100101101110011001110010000100000000
