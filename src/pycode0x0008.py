#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0008.py
# 功能: 小学时代无聊时玩过的一个游戏(random.choice)
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.06.06

from random import choice

names = ["张三", "李四", "王五"]
places = ["学校", "厕所", "食堂", "游乐场"]
actions = ["游泳", "嗯嗯", "吃饭", "读书", "睡觉"]

oddity = "%s在%s里%s。" % (choice(names), choice(places), choice(actions))
print oddity
