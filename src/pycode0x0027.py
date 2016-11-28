#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0027.py
功能: 从zlib压缩的二进制文件中读取100万以内的质数数据
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.03.23
"""

import os
from zlib import decompress
from struct import unpack

__path__ = os.path.dirname(__file__)

# 从zlib压缩的二进制文件中读取100万以内的质数数据，共78498个。
with open(os.path.join(__path__, 'primes_below_one_million.z'), 'rb') as _:
    primes_below_one_million = unpack('78498I', decompress(_.read()))

print primes_below_one_million, len(primes_below_one_million)
