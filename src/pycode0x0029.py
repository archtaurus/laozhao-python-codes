#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0029.py
功能: 下载某网站整站视频的脚本
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.11.29
"""

import os
import sys
import urllib
from bs4 import BeautifulSoup


def puts(s):
    sys.stdout.write(s)
    sys.stdout.flush()


p = 'http://www.budejie.com/video/%d'      # pages_pattern
t = 'div', {'class': 'j-r-list-c-desc'}    # title_pattern
v = 'div', {'class': 'j-video'}            # video_pattern
if not os.path.exists('mp4'):
    os.mkdir('mp4')
for page_num in xrange(1, 51):
    page = urllib.urlopen(p % page_num).read()
    soup = BeautifulSoup(page, 'html.parser')
    for title, video in zip([_.text.strip() for _ in soup.findAll(*t)],
                            [_['data-mp4'].strip() for _ in soup.findAll(*v)]):
        for c in '\/:*?"<>':
            title = title.replace(c, '')    # make filename valid
        path = 'mp4/' + title + '.mp4'
        puts('=' * 68 + '\n')
        puts('[TITLE] "%s"\n[VIDEO] "%s"\n' % (title, video))
        if os.path.exists(path):
            puts(u'already exists!\n')
            continue  # skip downloaded video
        with open(path, 'wb') as mp4:
            data = None
            # retry until to get response
            while not data:
                try:
                    req = urllib.urlopen(video)
                    data = req.read(4096)
                except:
                    puts('retry...\n')
            downloaded = len(data)
            size = int(req.headers.get('content-length'))
            flags = range(size)[::4096 * max(size / 4096 / 50, 1)]
            puts('[FETCH] ')
            while data:
                mp4.write(data)
                data = req.read(4096)
                downloaded += len(data)
                if downloaded in flags:
                    puts('.')
            else:
                puts('DONE\n[SAVED] "%s"\n' % path)
