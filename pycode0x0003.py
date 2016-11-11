#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 用字符c画边长为n的正方形和菱形


def square(c, n):
    "用字符c画边长为n的正方形"
    print (("%c\x20" % c) * n + "\n") * n


def diamond(c, n):
    "用字符c画边长为n的菱形"
    lines = ['\x20' * (n - 1 - i) + '*' * (1 + i * 2) for i in xrange(n)]
    lines = lines + lines[:-1][::-1]
    print '\n'.join(lines)


if __name__ == '__main__':
    square('*', 6)
    diamond('*', 6)
