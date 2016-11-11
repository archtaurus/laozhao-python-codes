#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 小学时代无聊时玩过的一个游戏(random.choice)

from random import choice

names = ["张三", "李四", "王五"]
places = ["学校", "厕所", "食堂", "游乐场"]
actions = ["游泳", "嗯嗯", "吃饭", "读书", "睡觉"]

oddity = "%s在%s里%s。" % (choice(names), choice(places), choice(actions))
print oddity
