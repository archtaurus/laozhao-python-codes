#!/usr/bin/env python
# coding: utf-8
"""老赵的Python代码碎片之一

文件: pycode0x0039.py
功能: 下载百度文库ppt文档内容的图片
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2017/02/14 17:24:17
"""
import os
import requests
from BeautifulSoup import BeautifulSoup

STORE_PATH = 'baiduwenku'

if not os.path.isdir(STORE_PATH):
    os.makedirs(STORE_PATH)

doc_url = 'http://wenku.baidu.com/view/95784486b9d528ea81c77930.html'  # 下载其它修改此地址
title = BeautifulSoup(requests.get(doc_url).content.decode('gbk')).title.text
output_path = os.path.join(STORE_PATH, title)

if not os.path.isdir(output_path):
    os.makedirs(output_path)

doc_id = doc_url[28:-5]
payload = {'doc_id': doc_id, 'type': 'ppt'}
data_url = 'http://wenku.baidu.com/browse/getbcsurl'
response = requests.get(data_url, params=payload)
data = response.json()
for item in data:
    page = item['page']
    url = item['zoom']
    page_filename = os.path.join(output_path, '{}.jpg'.format(page))
    with open(page_filename, 'wb') as img:
        img.write(requests.get(url).content)
    print (page_filename)
