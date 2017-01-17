#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0028.py
功能: 模拟打字机输出字符串
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.03.23
"""

import sys
import time


def typewriter(string, interval=0.1):
    """模拟打字机输出字符串

    Arguments:
        string (str): 待输出的字符串

    Keyword Arguments:
        interval (float): 间隔，单位秒
    """
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(interval)
    if char != '\n':
        print


if __name__ == '__main__':
    typewriter(u'Hello, World! 你好，世界！')
