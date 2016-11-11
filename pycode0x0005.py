#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 求小于1000的整数中3或5的整倍数的和

print sum(n for n in xrange(1000) if n % 3 == 0 or n % 5 == 0)
