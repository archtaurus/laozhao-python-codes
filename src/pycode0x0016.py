#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0016.py
功能: 一个WSGI接口WEB服务器
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.02.11
"""

from wsgiref.simple_server import make_server

HTTP_PORT = 8000


def application(environ, start_response):
    """HTTP入口WSGI处理函数

    environ：一个包含所有HTTP请求信息的dict对象；
    start_response：一个发送HTTP响应的函数。
    """

    # 发送 HTTP Response Code + HTTP Header
    start_response("200 OK", [("Content-Type", "text/html")])

    # HTTP Body
    body = "<h1>Hello, %s!</h1>" % (environ['PATH_INFO'][1:] or 'web')
    return body.encode("UTF-8")


if __name__ == "__main__":
    httpd = make_server("", HTTP_PORT, application)
    print("Serving HTTP on port %d..." % HTTP_PORT)
    httpd.serve_forever()
