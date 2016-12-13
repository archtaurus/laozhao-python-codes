#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0032.py
功能: 当日bing.com背景获取程序
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016/12/13 15:04:37
"""

import requests
import re

wallpaper = re.findall('http://s.cn.bing.net.+?1920x1080\.jpg',
                       requests.get('http://cn.bing.com').content, re.I)[0]
imagename = wallpaper.split('/')[-1]
with open(imagename, 'wb') as imagefile:
    imagefile.write(requests.get(wallpaper).content)
