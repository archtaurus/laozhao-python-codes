#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0026.py
功能: 用matplotlib画双曲面
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.11.22
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
X, Y = np.meshgrid(X, Y)
Z = Y ** 2 - X ** 2
ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap='rainbow')
plt.show()
