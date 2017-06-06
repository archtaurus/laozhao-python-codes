#!/usr/bin/env python
# coding: utf-8
"""老赵的Python代码碎片之一

文件: pycode0x003C.py
功能: 将学生按成绩分组
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016/02/10 15:49:08
"""

import itertools

data = (("濮阳婧怡", 290), ("许杰", 288), ("屠雨露", 279), ("陈怡", 277),
        ("张劭然", 274), ("汪睿琳", 271.5), ("汪伟轮", 270), ("祁飞宇", 269),
        ("张雨欣", 268.5), ("陈鑫煜", 268), ("王太煜", 266), ("鲁瑞芃", 265),
        ("章昂", 264), ("张雅婷", 263), ("肖雅妮", 261), ("郭旭阳", 259.5),
        ("俞浩然", 257), ("许家菊", 256.5), ("顾雅冰", 256), ("付晓松", 254),
        ("韦秀一", 252.5), ("时天", 252), ("俞乐", 252), ("翁凌志", 252),
        ("张天佑", 250.5), ("任佳瑶", 250), ("陈冠璋", 246), ("杨乐", 245.5),
        ("郭子恋", 244), ("王嘉琪", 243), ("闪婧悦", 243), ("邢运亮", 242.5),
        ("毕月榕", 241), ("常雨阳", 230.5), ("毛千尹", 216), ("沈梦茹", 213.5),
        ("凌昕曈", 211))

d = dict()
for i, (name, score) in enumerate(data):
    d[i] = (name, score)


def foo(d1, d2):
    return tuple(x for x in d1 if x not in d2)


def ave(dd):
    return 1.0 * sum(d[i][1] for i in dd) / len(dd)


def mysum(g):
    return abs(sum(d[i][1] for i in g) - 1531) < 0.2


def bar():
    for g1 in itertools.combinations(d, 6):
        if mysum(g1):
            l1 = foo(d, g1)
            for g2 in itertools.combinations(l1, 6):
                if mysum(g2):
                    l2 = foo(l1, g2)
                    for g3 in itertools.combinations(l2, 6):
                        if mysum(g3):
                            l3 = foo(l2, g3)
                            for g4 in itertools.combinations(l3, 6):
                                if mysum(g4):
                                    l4 = foo(l3, g4)
                                    for g5 in itertools.combinations(l4, 6):
                                        if mysum(g5):
                                            g6 = foo(l4, g5)
                                            yield g1, g2, g3, g4, g5, g6


mm = 100
ll = None
for g1, g2, g3, g4, g5, g6 in bar():
    haha = ave(g1), ave(g2), ave(g3), ave(g4), ave(g5), ave(g6)
    hoho = max(haha) - min(haha)
    if hoho < mm:
        mm = hoho
        ll = g1, g2, g3, g4, g5, g6
        print ll, mm
        for g in ll:
            for i in g:
                print "%d %s %g, " % (i + 1, d[i][0], d[i][1]),
            print "总分 %g" % sum(d[k][1] for k in g)
        print "均分差", mm
        break
