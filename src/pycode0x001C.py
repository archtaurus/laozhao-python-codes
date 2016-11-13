#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x001C.py
# 功能: Pygame方向键控制运动方向演示程序
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2013.08.31

import sys
import pygame

pygame.init()
pygame.mouse.set_visible(0)
pygame.display.set_caption("Pygame方向键控制演示程序")

BLACK = 0, 0, 0
WHITE = 255, 255, 255
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE = 640, 480
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
CLOCK = pygame.time.Clock()
BLOCK_SIZE = 10
MAX_X, MAX_Y = SCREEN_WIDTH - BLOCK_SIZE, SCREEN_HEIGHT - BLOCK_SIZE
CONTROL_KEYS = {pygame.K_UP: (0, -1),
                pygame.K_DOWN: (0, 1),
                pygame.K_LEFT: (-1, 0),
                pygame.K_RIGHT: (1, 0)}

x, y = 0, 200
dx, dy = 1, 0
speed = 2

while True:
    # update display
    CLOCK.tick(60)
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, (x, y, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()
    # user control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        # 用上下左右按键控制运动方向
        if event.type == pygame.KEYDOWN and event.key in CONTROL_KEYS:
            dx, dy = CONTROL_KEYS.get(event.key)
    # update data
    x += speed * dx
    y += speed * dy
    if (x < 0):
        x = 0
    elif (x > MAX_X):
        x = MAX_X
    if (y < 0):
        y = 0
    elif (y > MAX_Y):
        y = MAX_Y
