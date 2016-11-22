#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0023.py
# 功能: 命令行二维码图片生成程序
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.04.05

import os
import qrcode
import argparse

parser = argparse.ArgumentParser(description=u"二维码生成程序")
parser.add_argument("filename", help=u"二维码输出PNG格式图片文件名(.png)")
parser.add_argument("string", help=u"二维码信息字符串")
args = parser.parse_args()

warning = "File '%s' already exists, overwrite (y/n) ? "

if not args.filename.lower().endswith(".png"):
    print u"图片文件名必须以.png结尾"
else:
    qrimage = qrcode.make(args.string)
    if (not os.path.exists(args.filename) or
            raw_input(warning % args.filename) == 'y'):
        qrimage.save(args.filename)
        print(u"信息'{}'已保存在{}".format(args.string, args.filename))
