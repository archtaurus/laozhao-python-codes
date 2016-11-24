#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0021.py
功能: 用matplotlib画动态正弦曲线
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.04.05
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as ani

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(figsize=(16, 9), dpi=72)
ax = plt.axes(xlim=(-np.pi, np.pi), ylim=(-1.25, 1.25))
lines = ax.plot([], [], lw=2, color="b")
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))


def update(i):
    x = np.linspace(-np.pi, np.pi, 1000)
    y = np.sin(np.pi * (x / 2 - 0.02 * i))
    lines[0].set_data(x, y)
    return lines

# call the animator. blit=True means only re-draw the parts that have changed.
animation = ani.FuncAnimation(fig, update, frames=200, interval=20, blit=True)
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
