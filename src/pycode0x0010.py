#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0010.py
# 功能: 打印输出Pygame的事件对象信息
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.11.12

import sys
import pygame

pygame.init()
pygame.display.set_caption("Pygame Events")
SCREEN = pygame.display.set_mode((800, 600))

while True:
    event = pygame.event.wait()
    if event.type != pygame.QUIT:
        print event
    else:
        pygame.quit()
        sys.exit(0)
