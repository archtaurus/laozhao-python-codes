#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x000F.py
# 功能: Pygame摄像头捕获演示程序
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.11.12

import os
import sys
import pygame
import pygame.camera

# Center the window is easy with single monitor
os.environ['SDL_VIDEO_CENTERED'] = "1"
# But if you have two or more monitors, you can only set the absolute position.
os.environ['SDL_VIDEO_WINDOW_POS'] = "1664, 300"

# 初始化
pygame.init()
pygame.camera.init()
pygame.display.set_caption("Pygame摄像头捕获演示程序")

# 获取摄像头列表
cameras = pygame.camera.list_cameras()
if not cameras:
    sys.stderr.write("Error: no camera found!\n")
    sys.exit(1)

# 选择第一个摄像头，设定其分辨率，并启动它
CAMERA = pygame.camera.Camera(cameras[0], (640, 480))
CAMERA.start()

# 设定其它对象、常量
SCREEN = pygame.display.set_mode(CAMERA.get_size())
CLOCK = pygame.time.Clock()
MAX_FPS = 30

# 主循环
while True:
    CLOCK.tick(MAX_FPS)                 # 控制每秒最大帧数
    frame_image = CAMERA.get_image()    # 获取摄像头的图像
    SCREEN.blit(frame_image, (0, 0))    # 获取摄像头的图像
    pygame.display.flip()               # 更新窗口画面
    for event in pygame.event.get():
        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or
                event.type == pygame.QUIT):     # ESC或关闭窗口时...
            CAMERA.stop()   # 关闭摄像头
            pygame.quit()   # 结束pygame
            sys.exit(0)     # 退出python
