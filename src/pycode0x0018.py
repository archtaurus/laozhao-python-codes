#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0018.py
# 功能: 用乌龟(Turtle)画方块套方块、圈圈套圈圈
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.03.12

# involved moudules
import turtle
from random import randint

# my constants
SPEED = 'fastest'
DRAW_SQUARES = '1'
DRAW_CIRCLES = '2'
BORDER_COLOR = 'black'


def turtle_go():
    '''Main function

    Return: None
    '''

    # ask for options
    print ('***Turtle Graphics Shape Generator***\n'
           '1. Draw squares\n'
           '2. Draw circles')
    option = raw_input('Selection: ')

    # check the selection and ask for more options
    if option == DRAW_SQUARES:
        number = int(raw_input('Enter number of squares to draw: '))
        width = int(raw_input('Enter square width: '))
        draw_squares_round_and_round(number, width)
    elif option == DRAW_CIRCLES:
        number = int(raw_input('Enter number of circles to draw: '))
        radius = int(raw_input('Enter circle radius: '))
        draw_circles_ring_upon_ring(number, radius)
    else:
        print ('sorry, only 1 or 2 is available option.')


def random_color():
    '''Generate a random color code in hex style RGB format

    Returns:
        str: a random color
    '''
    return '#%06X' % randint(0, 0xFFFFFF)


def draw_squares_round_and_round(number, width):
    '''Draw squares round and round

    Args:
        number (int): number of squares to draw
        width (int): square width

    Returns: None
    '''

    # preparing
    turtle.speed(SPEED)
    turn = 360 / number

    # drawing ...
    for i in range(number):
        turtle.color(BORDER_COLOR, random_color())
        turtle.begin_fill()
        for j in range(4):
            turtle.forward(width)
            turtle.left(90)
        turtle.end_fill()
        turtle.left(turn)

    # finishing
    turtle.up()
    turtle.home()
    turtle.done()


def draw_circles_ring_upon_ring(number, radius):
    '''Draw circles ring upon ring

    Args:
        number (int): number of circles to draw
        radius (int): circle radius

    Returns: None
    '''

    # preparing
    turtle.speed(SPEED)
    delta = radius / number

    # drawing ...
    for i in range(number):
        r = radius - delta * i
        turtle.up()
        turtle.sety(-r)
        turtle.color(BORDER_COLOR, random_color())
        turtle.down()
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

    # finishing
    turtle.up()
    turtle.home()
    turtle.done()


if __name__ == '__main__':
    turtle_go()
