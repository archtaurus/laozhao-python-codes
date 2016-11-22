#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x001F.py
# 功能: 用matplotlib画正弦余弦曲线
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.04.05

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Create a new figure of size 10x6 points, using 100 dots per inch
plt.figure(figsize=(10, 6), dpi=100)

# Create a new subplot from a grid of 1x1
plt.subplot(111)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Set x limits
plt.xlim(X.min() * 1.25, X.max() * 1.25)
# Set y limits
plt.ylim(C.min() * 1.25, C.max() * 1.25)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

# Set x ticks
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# Set y ticks
plt.yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])

# 画函数线
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="y=sin(x)")
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="--", label="y=cos(x)")

# 图例
plt.legend(loc='upper left', frameon=True)

# 关注点
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=1.0, linestyle=":")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=1.0, linestyle=":")
plt.scatter([t, ], [np.sin(t), ], 50, color='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# Save figure using 72 dots per inch
plt.savefig("exercise_1.png", dpi=72)

# Show result on screen
plt.show()
