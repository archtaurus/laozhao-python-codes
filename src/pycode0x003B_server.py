#!/usr/bin/env python
# coding: utf-8
"""老赵的Python代码碎片之一

文件: pycode0x003B_server.py
功能: socket聊天程序服务端
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2017-04-06 07:05:05
"""

import socket
import select

import logging
# logging levels: INFO, DEBUG, WARNING, ERROR, CRITICAL
logging.basicConfig(filename='chatting.log', level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(message)s')
logging.info('chat server starting')

try:
    # socket initializing
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info('socket created')

    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_port = 5460
    server_sock.bind(('', server_port))
    server_sock.listen(5)
    logging.info('server initialized and listening at port {}'.format(server_port))
    print 'Chat server started'

    # main loop
    clients = {}
    while True:
        active_socks = select.select([server_sock] + clients.keys(), [], [])[0]
        for active_sock in active_socks:
            # accept new client's connection
            if active_sock is server_sock:
                new_client_sock, new_client_addr = server_sock.accept()
                new_client_username = new_client_sock.recv(1024)
                clients[new_client_sock] = (new_client_username, new_client_addr)
                message = '[{}] {} has joined this chat.'.format(new_client_username, new_client_addr)
            # listen to all clients
            else:
                client_username, client_addr = clients[active_sock]
                # receive client's message
                try:
                    data = active_sock.recv(1024)
                    assert data
                    message = '{} : {}'.format(client_username, data)
                # client is off-line or whatever error is happend
                except Exception:
                    del clients[active_sock]
                    active_sock.close()
                    message = '[{}] {} has left.'.format(client_username, client_addr)
            # message broadcasting
            print message
            logging.info(message)
            for client_sock in clients.keys():
                client_sock.send(message)
except (KeyboardInterrupt, SystemExit):
    exit_message = 'Chat server shutdown'
except socket.error, error:
    logging.error('socket.error: %s' % error)
    exit_message = 'Chat server shutdown with socket.error:\n%s' % error
except Exception, error:
    logging.error('%s' % error)
    exit_message = 'Chat server shutdown with error:\n%s' % error
# last thing last...
finally:
    logging.info('chat server stopping')

    print '\rClosing sockets ...'
    server_sock.close()
    print '\t[X] server socket'
    logging.info('server socket closed')
    for client_sock, (client_username, client_addr) in clients.items():
        print '\t[X] [{}] {}'.format(client_username, client_addr)
        client_sock.send('*** CHAT SERVER SHUTDOWN ***')
        client_sock.close()
    logging.info('all clients sockets closed')

    print exit_message
    logging.info('chat server shutdown')
