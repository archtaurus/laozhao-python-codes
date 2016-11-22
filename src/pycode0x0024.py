#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0024.py
# 功能: 命令行读取图片中二维码程序
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.11.22

import os
import sys
import argparse
import cStringIO
import requests
from PIL import Image
from pyzbar import pyzbar

parser = argparse.ArgumentParser(description=u"二维码识别程序")
parser.add_argument("image", help=u"图片文件名/网址")
args = parser.parse_args()


try:
    if args.image.startswith("http"):
        data = requests.get(args.image).content
        image = cStringIO.StringIO(data)
        img = Image.open(image).convert('L')
    else:
        args.image = os.path.abspath(args.image)
        img = Image.open(args.image).convert('L')
except:
    print u"读取'{}'失败！".format(args.image)
    sys.exit(1)

qrcodes = pyzbar.decode(img)
qrcode_data = qrcodes[0].data if qrcodes else ""
print unicode(qrcode_data.decode("utf-8"))
