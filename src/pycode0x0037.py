#!/usr/bin/env python
# coding: utf-8
"""老赵的Python代码碎片之一

文件: pycode0x0037.py
功能: PyOpenGL茶壶DEMO
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2017/01/11 10:10:26
"""
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glutWireTeapot(0.5)             # glutSolidTeapot(0.5)
    glRotatef(0.1, 0, 1, 0)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutInitWindowPosition(200, 200)
glutCreateWindow("OpenGL Wire Teapot")
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
glutMainLoop()
