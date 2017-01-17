#!/usr/bin/env python
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

CELL, EMPTY = 1, 0
SIZE, COLS, ROWS = 10, 100, 60
BODY = 0, 200, 100
SKIN = 0, 100, 50
BACKGROUND = 200, 255, 200
SPEED = 10

pygame.init()
screen = pygame.display.set_mode((SIZE * COLS + 1, SIZE * ROWS + 1), 0, 32)
pygame.display.set_caption('Life')
lifes = [[random.choice((CELL, EMPTY)) for _ in xrange(COLS)] for _ in xrange(ROWS)]
"""随机生成第一代生命"""
while True:
    screen.fill(BACKGROUND)
    space = [[0] * COLS for i in xrange(ROWS)]
    """放置下一代生命的空间"""
    for x in xrange(COLS):
        for y in xrange(ROWS):
            neighbors = sum(lifes[i][j] for i in (y - 1, y, y + 1) for j in (x - 1, x, x + 1)
                            if (0 <= i < ROWS) and (0 <= j < COLS)) - lifes[y][x]
            if (lifes[y][x] + neighbors == 3) or neighbors == 3:
                space[y][x] = CELL
                screen.fill(BODY, (SIZE * x, SIZE * y, SIZE, SIZE))
                pygame.draw.rect(screen, SKIN, (SIZE * x, SIZE * y, SIZE + 1, SIZE + 1), 1)
    lifes = copy.deepcopy(space)
    pygame.display.flip()
    pygame.time.wait(1000 / SPEED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
