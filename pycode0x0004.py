#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0004.py
# 功能: 三个玩家玩斗地主，洗牌、发牌、理牌、留3张底牌 ...
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.03.04

from random import shuffle

CARD_COLORS = {"S": "黑桃", "H": "红桃", "C": "草花", "D": "方块", "J": "王"}
CARD_RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

cards = ["J1", "J2"] + [color + rank for color in CARD_COLORS.keys()
                        for rank in CARD_RANKS]

print "A pair of new cards:"
print cards

# 洗牌
shuffle(cards)
print "Shuffled cards:"
print cards

# 发牌、理牌
player = [sorted(cards[0:-3:3]), sorted(cards[1:-3:3]), sorted(cards[2:-3:3])]
for n in [0, 1, 2]:
    print "Player %d:" % (n + 1)
    print player[n]

# 底牌
bottom_cards = sorted(cards[-3:])
print "Bottom cards:"
print bottom_cards
