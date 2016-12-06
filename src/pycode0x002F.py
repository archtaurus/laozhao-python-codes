#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x002F.py
功能: Pygame的生命游戏
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.12.06
"""

import sys
import copy
import random
import pygame

BORDER_COLOR = 0, 0, 0
LIFE_COLOR = 0, 255, 0
BG_COLOR = 255, 255, 255
LIFE, DEAD = 1, 0


def count_neighbor(x, y):
    """获取坐标所处九宫格范围内的邻居生命数量"""
    count = 0
    for i in (x - 1, x, x + 1):
        for j in (y - 1, y, y + 1):
            if (i == x and j == y) or (i < 0 or i > 47 or j < 0 or j > 47):
                continue
            count += lives[i][j]
    return count


lives = [[random.choice((LIFE, DEAD)) for i in xrange(48)] for i in xrange(48)]
"""随机生成的第一代生命"""
space = [[0] * 48 for i in xrange(48)]
"""放置下一代生命的空间"""
pygame.init()
screen = pygame.display.set_mode((480, 480), 0, 32)
pygame.display.set_caption('Life')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BG_COLOR)
    for x in xrange(48):
        for y in xrange(48):
            neighbors = count_neighbor(x, y)
            if neighbors == 2:
                space[x][y] = lives[x][y]   # 生存
            elif neighbors == 3:
                space[x][y] = LIFE          # 诞生
            else:
                space[x][y] = DEAD          # 死亡
            if space[x][y]:
                screen.fill(LIFE_COLOR, (y * 10, x * 10, 10, 10))
                pygame.draw.rect(screen, BORDER_COLOR,
                                 (y * 10, x * 10, 10, 10), 1)
    lives = copy.deepcopy(space)
    pygame.display.update()
    pygame.time.wait(100)
