#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0013.py
# 功能: 将base64字符串转为文件对象
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.11.12

import base64
import cStringIO
from PIL import Image


def file_from_base64string(string):
    "将base64字符串转为文件对象"
    data = base64.decodestring(string)
    file = cStringIO.StringIO()
    file.write(data)
    file.seek(0)
    return file


if __name__ == '__main__':
    string = ("iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAA"
              "AAXNSR0IArs4c6QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAA"
              "d0SU1FB90DHRMRNZytqtkAAABASURBVDjL7dOhFQAgCEXRp"
              "4f1GIr9YCYMBrNo5PUL6Y/MpFREkKXcXVXlnLnJzIDJQ40b"
              "N/6NZY957/P6c1kCC4gUSmG+i0o0AAAAAElFTkSuQmCC")
    file = file_from_base64string(string)   # 文件对象
    image = Image.open(file)                # 打开图片文件
    image.show()                            # 显示图片
