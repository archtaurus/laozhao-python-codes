#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0034.py
功能: 百度文字识别API简单演示
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016/12/22 16:56:08
使用方法:
    $ python pycode0x0034.py <image filename>
    识别到的文字
"""

import urllib
import urllib2
import json
import base64
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("image",
                    help="filename of image",
                    type=argparse.FileType("rb"))
args = parser.parse_args()
url = 'http://apis.baidu.com/idl_baidu/baiduocrpay/idlocrpaid'
data = {}
data['fromdevice'] = "pc"
data['clientip'] = "10.10.10.0"
data['detecttype'] = "LocateRecognize"
data['languagetype'] = "CHN_ENG"
data['imagetype'] = "1"
try:
    tmp = args.image.read()
finally:
    args.image.close()
data['image'] = base64.b64encode(tmp)
decoded_data = urllib.urlencode(data)
req = urllib2.Request(url, data=decoded_data)
req.add_header("Content-Type", "application/x-www-form-urlencoded")
req.add_header("apikey", "你自己的百度开发者apikey")
# 查看你自己的百度开发者apikey可访问：http://apistore.baidu.com/astore/usercenter
resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    try:
        print json.loads(content).get("retData")[0].get("word", "未识别到文字")
    except:
        print "识别失败"
