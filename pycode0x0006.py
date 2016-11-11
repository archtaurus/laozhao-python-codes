#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 求前一百个自然数的“和的平方”与它们的“平方的和”的“差”
# 注，0属于自然数。

print sum(xrange(100))**2 - sum(n**2 for n in xrange(100))
