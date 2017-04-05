#!/usr/bin/env python
# coding: utf-8
"""老赵的Python代码碎片之一

文件: pycode0x003B_server.py
功能: socket聊天程序客户端
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2017-04-06 07:05:05
"""

import re
import sys
import time
import socket
import select
import curses
from curses import panel
from curses import ascii


def update_panel(pan, data=''):
    title = pan.userptr()
    window = pan.window()
    window.clear()
    window.box()
    window.addstr(0, 1, title)
    if isinstance(data, list):
        for i, message in enumerate(data):
            window.addstr(i + 1, 2, message)
    else:
        window.addstr(1, 2, str(data))
    panel.update_panels()
    curses.doupdate()


while True:
    user_name = raw_input('Your name: ')
    if not re.match('^[A-z]{3,15}$', user_name):
        print 'User name should be 3~15 long and alpha characters only.'
    else:
        break

try:
    # socket initializing
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_sock.settimeout(3)
    client_sock.connect(('127.0.0.1', 5460))
    client_sock.send(user_name)

    # curses initializing
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    rows, cols = stdscr.getmaxyx()

    # create windows
    chat_win = curses.newwin(rows - 3, cols, 0, 0)
    send_win = curses.newwin(3, cols, rows - 3, 0)

    # set colors
    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        send_win.bkgdset(ord(' '), curses.color_pair(1))
    else:
        send_win.bkgdset(ord(' '), curses.A_STANDOUT)

    # create panels
    chat_pan = panel.new_panel(chat_win)
    chat_pan.set_userptr(' MESSAGES ')
    send_pan = panel.new_panel(send_win)
    send_pan.set_userptr(' SEND ')
    update_panel(chat_pan)
    update_panel(send_pan)

    # main loop
    message_out, message_in, messages = '', '', []
    max_lines, max_length = rows - 5, cols - 20
    while True:
        jobs = select.select([sys.stdin, client_sock], [], [])[0]
        for job in jobs:
            # message in
            if job == client_sock:
                message_in = client_sock.recv(1024)
                if not message_in:
                    time.sleep(3)
                    exit(0)
                messages.append(message_in)
                update_panel(chat_pan, messages[-max_lines:])
                curses.beep()
            # user input
            else:
                # message editing
                key_code = stdscr.getch()
                if ascii.isprint(key_code) and len(message_out) < max_length:
                    message_out += curses.keyname(key_code)
                elif key_code == 263:  # curses.KEY_BACKSPACE? Apple delet key?
                    message_out = message_out[:-1]
                # message send out
                elif key_code in [curses.KEY_ENTER, 10]:
                    client_sock.send(message_out)
                    message_out = ''
                update_panel(send_pan, message_out)
except (KeyboardInterrupt, SystemExit):
    pass
finally:
    client_sock.close()
    curses.endwin()
