#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x002E.py
功能: 一个简单的Tkinter文本编辑器
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.12.05
"""

import fileinput
import tkFont
import tkMessageBox
from Tkinter import *
from ScrolledText import *
from tkFileDialog import *


class Editor(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('untitled')
        self.menubar = Menu(self.root)
        # file menu
        self.file_menu = Menu(self.menubar)
        self.file_menu.add_command(label='打开', command=self.openfile)
        self.file_menu.add_command(label='保存', command=self.savefile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='退出', command=self.exit)
        # help menu
        self.help_menu = Menu(self.menubar)
        self.help_menu.add_command(label='关于', command=self.about)
        # menu
        self.menubar.add_cascade(label='文件', menu=self.file_menu)
        self.menubar.add_cascade(label='帮助', menu=self.help_menu)
        self.root.config(menu=self.menubar)
        # frame
        self.frame = Frame(width=512)
        self.frame.pack(expand=1, fill=BOTH)
        # scrolled text
        ft = tkFont.Font(family='Consolas', size=12, weight=tkFont.NORMAL)
        self.st = ScrolledText(self.frame, bg='navyblue', fg='white', font=ft)
        self.st.pack(side=LEFT, fill=BOTH, expand=1)
        # run
        self.root.mainloop()

    def openfile(self):
        filename = askopenfilename(filetypes=[('Python files', '*.py'),
                                              ('Text files', '*.txt'),
                                              ('All files', '*.*')])
        if filename:
            self.root.title(filename)
            self.st.delete(1.0, END)
            for line in fileinput.input(filename):
                self.st.insert(END, line)

    def savefile(self):
        filename = asksaveasfilename(filetypes=[('Python files', '*.py')],
                                     defaultextension='py')
        if filename:
            ofp = open(filename, 'w')
            ofp.write(self.st.get(1.0, END))
            ofp.flush()
            ofp.close()
            self.root.title(filename)

    def exit(self):
        self.root.destroy()

    def about(self):
        tkMessageBox.showinfo('About Tkeditor', 'Tkeditor V1.0\nby Laozhao')


if __name__ == '__main__':
    Editor()
