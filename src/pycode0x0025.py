#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0025.py
功能: 生成Github随机用户头像
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.11.22
"""

from PIL import Image
import numpy as np

face_data = np.ndarray((5, 5), int, np.random.randint(0, 2, 25))
face_data[:, 3] = face_data[:, 1]  # 使脸左右对称
face_data[:, 4] = face_data[:, 0]
print face_data  # ndarray

face_color = tuple(np.random.randint(64, 200, 3))
print face_color
background_color = 240, 240, 240
colors = face_color, background_color
data = [colors[face_data[y][x]] for x in range(5) for y in range(5)]
face = Image.new("RGB", (5, 5))  # 鼻子眼睛嘴
face.putdata(data)
face = face.rotate(90).resize((200, 200))  # 旋转放大

avatar = Image.new("RGB", (230, 230), colors[1])  # 为了留出15宽的边
avatar.paste(face, (15, 15))
avatar.show()  # image
avatar.save("random_avatar.png")
