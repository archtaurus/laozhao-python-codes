#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x001B-server.py
功能: socket通讯小例子（服务器端）
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2013.08.31
"""

import sys
import socket

HOST = '127.0.0.1'
PORT = 8001
SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCK.bind((HOST, PORT))
SOCK.listen(1)

while True:
    print 'Listening...'
    conn, addr = SOCK.accept()
    conn.settimeout(60)             # 60超时自动断开
    print 'Connected by', addr
    while True:
        try:
            data = conn.recv(1024)  # 接收到的数据
            if data:
                print 'Data received ->', data
                if data == 'bye':   # 接收bye则关闭连接
                    conn.send('bye')
                    break
                elif data == 'quit':   # 接收quit则关闭服务器
                    conn.send('Good bye!')
                    conn.close()
                    sys.exit(0)
                    break
                conn.send(data.upper()[::-1])   # 将数据后的数据发送回客户端
        except socket.timeout:
            print 'Time out...'
            conn.send('Time out!')
            break
    conn.close()
    print 'Connection closed~~'
