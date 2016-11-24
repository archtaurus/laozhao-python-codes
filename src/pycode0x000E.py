#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x000E.py
功能: 谁是罪犯？
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.11.01
"""

suspects = "abcde"  # 嫌疑人
evidences = {}      # 证词
right = 3

evidences["a"] = "d"                                    # 指认 d
evidences["b"] = suspects.replace("b", "")              # 自认无辜
evidences["c"] = suspects.replace("e", "")              # 认为e无辜
evidences["d"] = suspects.replace(evidences["a"], "")   # 指认a作伪证
evidences["e"] = evidences["b"]                         # 同意 b

for suspect in suspects:
    count = 0
    for evidence in evidences:
        if suspect in evidences[evidence]:
            print evidence, "真话",
            count += 1
        else:
            print evidence, "假话",
    if count == right:
        print "(%s是罪犯！)" % suspect
    else:
        print
