#!/usr/bin/env python
# coding: utf-8
"""老赵的Python代码碎片之一

文件: pycode0x003D.py
功能: Tkinter密码输入demo
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016/08/10 15:49:08
"""

from Tkinter import *
from Crypto.Hash import SHA


class App:

    def __init__(self):
        self.root = Tk()
        self.password = StringVar()
        self.frame = Frame(self.root)
        self.frame.pack()
        self.passwd_entry = Entry(self.frame, textvariable=self.password,
                                  show="*")
        self.passwd_entry.pack()
        self.passwd_entry.focus_set()
        self.button_login = Button(self.frame, text="Login",
                                   command=self.check_password)
        self.button_login.pack()
        self.root.mainloop()

    def check_password(self):
        passwd_hash = "1b8c90fd5699f3b05e3b3434564e99a8a3f3141b"
        if SHA.new(self.password.get()).hexdigest() == passwd_hash:
            print "ok"
        else:
            print "wrong passwd!"
        self.passwd_entry.delete(0, END)


if __name__ == '__main__':
    App()
