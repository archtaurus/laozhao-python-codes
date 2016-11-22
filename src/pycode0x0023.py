#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0023.py
# 功能: 命令行二维码图片生成程序
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.04.05

import os
import sys
import qrcode  # see https://pypi.python.org/pypi/qrcode
import argparse

parser = argparse.ArgumentParser(description=u"二维码生成程序")
parser.add_argument("filename", help=u"二维码输出PNG格式图片文件名(.png)")
parser.add_argument("string", help=u"二维码信息字符串")
args = parser.parse_args()

if not args.filename.lower().endswith(".png"):
    print u"图片文件名必须以.png结尾。"
    sys.exit(1)

args.filename = os.path.abspath(args.filename)
if os.path.exists(args.filename):
    print u"文件'{}'已存在，是否覆盖(y/n)？".format(args.filename),
    if raw_input() != 'y':
        print u"中止..."
        sys.exit(1)

qrimage = qrcode.make(args.string)
qrimage.save(args.filename)
print(u"信息'{}'已保存在二维码图片'{}'中。".format(args.string, args.filename))
