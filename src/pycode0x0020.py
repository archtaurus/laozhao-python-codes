#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0020.py
功能: 用matplotlib画动态随机折线
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.04.05
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani


def get_data():
    while 1:
        yield np.random.rand(101)


def update_line(data):
    line.set_ydata(data)
    return line


figure = plt.figure(figsize=(10, 4))
ax = plt.axes(xlim=(0, 100), ylim=(0, 1), xticks=[0, 100], yticks=[0, 0.5, 1])
line = ax.plot(np.zeros(101))[0]
animation = ani.FuncAnimation(figure, update_line, get_data, interval=100)

plt.show()
