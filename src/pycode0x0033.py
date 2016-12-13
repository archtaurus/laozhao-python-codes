#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0032.py
功能: wxPython-demo-文字编辑器
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016/12/13 15:41:03
"""

import os
import wx

wrkpath = os.path.dirname(__file__)


def load(event):
    file = open(os.path.join(wrkpath, fninput.GetValue()))
    txteditor.SetValue(file.read().decode('utf-8'))
    file.close()


def save(event):
    file = open(os.path.join(wrkpath, fninput.GetValue()), 'w')
    file.write(txteditor.GetValue().encode('utf-8'))
    file.close()


app = wx.App()
win = wx.Frame(None, title='Simple Editor', size=(640, 480))
mbox = wx.Panel(win)
loadbtn = wx.Button(mbox, label='Open')
loadbtn.Bind(wx.EVT_BUTTON, load)
savebtn = wx.Button(mbox, label='Save')
savebtn.Bind(wx.EVT_BUTTON, save)
fninput = wx.TextCtrl(mbox)
txteditor = wx.TextCtrl(mbox, style=wx.TE_MULTILINE | wx.HSCROLL)
hbox = wx.BoxSizer()
hbox.Add(fninput, proportion=1, flag=wx.EXPAND)
hbox.Add(loadbtn, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(savebtn, proportion=0, flag=wx.LEFT, border=5)
vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(txteditor, proportion=1, flag=wx.EXPAND |
         wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
mbox.SetSizer(vbox)
win.Show()
app.MainLoop()
