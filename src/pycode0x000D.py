#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x000D.py
# 功能: 求Python之禅中字符的出现频率(百分率，不区分大小写字母)
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.11.11

from __future__ import division

zen_of_python = '''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although this that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! is.'''

total = len(zen_of_python)

char_counter = {}
for char in zen_of_python:
    char = char.lower()
    if char in char_counter:
        char_counter[char] += 1
    else:
        char_counter[char] = 1

for char in sorted(char_counter):
    print "%4r -> %5.2f%%" % (char, char_counter[char] * 100 / total)

# OUTPUT
"""
'\n' ->  2.20%
 ' ' -> 14.58%
 '!' ->  0.12%
 "'" ->  0.46%
 '*' ->  0.23%
 ',' ->  0.46%
 '-' ->  0.69%
 '.' ->  2.20%
 'a' ->  6.13%
 'b' ->  2.43%
 'c' ->  1.97%
 'd' ->  1.97%
 'e' -> 10.65%
 'f' ->  1.39%
 'g' ->  1.27%
 'h' ->  3.70%
 'i' ->  6.37%
 'k' ->  0.23%
 'l' ->  3.82%
 'm' ->  1.85%
 'n' ->  4.86%
 'o' ->  4.98%
 'p' ->  2.55%
 'r' ->  3.82%
 's' ->  5.56%
 't' ->  9.26%
 'u' ->  2.43%
 'v' ->  0.58%
 'w' ->  0.46%
 'x' ->  0.69%
 'y' ->  1.97%
 'z' ->  0.12%
"""
