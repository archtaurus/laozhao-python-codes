#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0025.py
# 功能: 生成Github随机用户头像
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.11.22


from PIL import Image
import numpy as np

face = np.ndarray((5, 5), int, np.random.randint(0, 2, 25))
face[:, 3] = face[:, 1]
face[:, 4] = face[:, 0]
print face  # ndarray


avatar = Image.new("RGB", (5, 5))
colors = (176, 200, 101), (240, 240, 240)
data = [colors[face[y][x]] for x in range(5) for y in range(5)]  # color list
avatar.putdata(data)
avatar = avatar.rotate(90).resize((200, 200))  # 旋转放大
avatar.show()  # image
