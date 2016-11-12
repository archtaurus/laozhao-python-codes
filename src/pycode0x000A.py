#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x000A.py
# 功能: 求出两个三位数的乘积中最大的回文数(分片、max、生成器推导式)
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.06.06


def is_palnum(n):
    "判断十进制数n是否是回文数(palindromic number)"
    # 简洁的，但低效的方式: return str(n) == str(n)[::-1]
    sn = str(n)         # string n
    hl = len(sn) / 2    # half of length
    left, right = sn[:hl], sn[hl:][::-1]  # half of string (both L2R and R2L)
    return all(left[i] == right[i] for i in xrange(hl))


if __name__ == '__main__':
    print max(x * y
              for x in xrange(100, 1000)
              for y in xrange(100, 1000)
              if is_palnum(x * y))
