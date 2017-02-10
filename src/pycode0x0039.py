#!/usr/bin/env python
# coding: utf-8
"""老赵的Python代码碎片之一

文件: pycode0x0039.py
功能: 分组分割数据文件
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2017/02/10 15:49:08
"""

import os

DATA_FILENAME = 'sl.fasta'
OUTPUT_PATH = 'output'
GROUP_SIZE = 200

file_counter = 0
data_counter = 0
data_file = open(DATA_FILENAME)
if not os.path.isdir(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)
output_file = None

for line in data_file:
    if line.startswith('>'):
        data_counter += 1
        if data_counter % GROUP_SIZE == 1:
            if output_file:
                output_file.close()
            file_counter += 1
            ouptput_filename = '{}/sl_{:03d}.fasta'.format(OUTPUT_PATH, file_counter)
            output_file = open(ouptput_filename, 'w')
            print ouptput_filename
    output_file.write(line)

data_file.close()
if output_file:
    output_file.close()
