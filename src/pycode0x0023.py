#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0023.py
# 功能: 命令行二维码图片生成程序
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.04.05

import qrcode
import argparse

parser = argparse.ArgumentParser(description="二维码生成程序")
parser.add_argument("filename", help="二维码输出图片文件名")
parser.add_argument("string", help="二维码信息字符串")
args = parser.parse_args()

qrimage = qrcode.make(args.string)
qrimage.save(args.filename)
