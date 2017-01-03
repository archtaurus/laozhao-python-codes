#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0036.py
功能: 解析url
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2017-01-03 22:26:21
"""

import urlparse  # renamed to urllib.parse in Python3

url = 'http://user:pass@host:8080/path/file;parameters?key=test&data=value&data=value2#anchor'
scheme, netloc, path, params, query, fragment = result = urlparse.urlparse(url)
print result.geturl()
print 'scheme:  ', scheme
print 'netloc:  ', netloc
print 'username:', result.username
print 'password:', result.password
print 'hostname:', result.hostname  # lowcase
print 'port:    ', result.port      # integer
print 'path:    ', path
print 'params:  ', params
print 'query:   ', query
print '         ', urlparse.parse_qs(query)
print '         ', urlparse.parse_qsl(query)
print 'fragment:', fragment

# 输出内容
# http://user:pass@host:8080/path/file;parameters?key=test&data=value&data=value2#anchor
# scheme:   http
# netloc:   user:pass@host:8080
# username: user
# password: pass
# hostname: host
# port:     8080
# path:     /path/file
# params:   parameters
# query:    key=test&data=value&data=value2
#           {'data': ['value', 'value2'], 'key': ['test']}
#           [('key', 'test'), ('data', 'value'), ('data', 'value2')]
# fragment: anchor
