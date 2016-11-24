#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x000B.py
功能: 返回公元年份的天干地支
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.06.06
"""


def ganzhi(year):
    """將任意公元年份數轉換爲天干地支的形式

    天干地支產生於炎黄时期，簡稱“干支”。在中國古代歷法中，
    甲、乙、丙、丁、戊、己、庚、辛、壬、癸被稱為“十天干”，
    子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥被稱作“十二地支”。
    十干和十二支依次相配，組成六十個基本單位，兩者按固定的順序相互配合組成干支
    紀法。甲子、乙丑、丙寅一直到癸亥，共得到60个组合，称为六十甲子，如此周而复
    始，无穷无尽。用六十甲子依次纪年，六十年一个轮回。比如公元4年爲甲子年。1911
    年是辛亥年，爆发了辛亥革命。
    """
    tiangan = u"甲乙丙丁戊己庚辛壬癸"
    dizhi = u"子丑寅卯辰巳午未申酉戌亥"
    i = (year - 4) % 10
    j = (year - 4) % 12
    return tiangan[i] + dizhi[j]


if __name__ == '__main__':
    years = 4, 1911, 2016, -221, 1987
    for year in years:
        print (u"%d年 (%s年)" % (year, ganzhi(year))).replace("-", u"公元前")
