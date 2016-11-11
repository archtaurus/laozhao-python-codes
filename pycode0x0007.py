#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 把2的1000次方的数值各位上的数字加在一起是多少？

print sum(map(int, list(str(2**1000))))
