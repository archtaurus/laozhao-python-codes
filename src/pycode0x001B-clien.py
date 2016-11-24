#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x001B-clien.py
功能: socket通讯小例子（客户端）
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2013.08.31
"""

import socket

HOST = '127.0.0.1'
PORT = 8001
SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCK.connect((HOST, PORT))

while True:
    data = raw_input('Input data: ')
    SOCK.send(data)
    feedback = SOCK.recv(4096)
    print 'Server feedback:', feedback
    if feedback in ['Time out!', 'Good bye!', 'bye']:
        break

SOCK.close()
