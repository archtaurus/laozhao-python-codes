#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0031.py
功能: 城市空气质量数据抓取函数
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.12.12
"""

import re
import urllib


def url_read(url, coding=None):
    content = urllib.urlopen(url).read()
    if coding:
        content = content.decode(coding).encode('utf-8')
    return content


def re_get(url, regobj, count=-1, coding=None):
    content = url_read(url, coding)
    result = regobj.findall(content)
    if not result:
        return []
    if count == -1:
        return result
    if count == 1:
        return result[0]
    else:
        return result[:count]


def get_aqi(city_name_cn):
    cities_page_url = 'http://m.86kongqi.com/choicecity.html'
    city_url_regexp = re.compile('<a href="(pm/.+?.html)" >(.+?)</a>', re.S | re.I)
    city_urls = dict(map(lambda x: (x[1], 'http://m.86kongqi.com/' + x[0]),
                         re_get(cities_page_url, city_url_regexp)))
    if city_name_cn in city_urls:
        city_url = city_urls[city_name_cn]
        aqi_regexp = re.compile('>(\d+)<', re.S | re.I)
        aqi = int(re_get(city_url, aqi_regexp, 1))
        return aqi


if __name__ == '__main__':
    city_name_cn = '南京'
    aqi = get_aqi(city_name_cn)
    if not aqi:
        level = 'N/A'
    elif aqi < 50:
        level = '优'
    elif aqi < 100:
        level = '良'
    elif aqi < 150:
        level = '轻度污染'
    elif aqi < 200:
        level = '中度污染'
    elif aqi < 300:
        level = '重度污染'
    else:
        level = '严重污染'
    print '"{}"目前的AQI指数：{}，空气质量等级："{}"。'.format(city_name_cn, aqi, level)
