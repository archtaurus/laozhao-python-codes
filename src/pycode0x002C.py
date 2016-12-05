#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""猜动物

文件: pycode0x002C.py
功能: 猜动物
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.03.23
"""

class Node:
    """Question Node"""

    def __init__(self, question, left=None, right=None):
        self.question = question
        self.left = left
        self.right = right


def yes_or_no(question):
    """Force the user to answer 'yes' or 'no' or something similar."""

    while True:
        answer = raw_input(question + '(yes/no) ').strip().lower()
        if answer in ['yes', 'yeah', 'y']:
            return True
        if not answer or answer in ['no', 'nope', 'n']:
            return False


def main():
    """Guess animal"""

    knowledge = Node('bird')
    while True:
        if not yes_or_no('\nAre you thinking of an animal? '):
            break
        k = knowledge
        while k.left is not None:
            k = k.right if yes_or_no(k.question + '? ') else k.left
        if yes_or_no('Is it a ' + k.question + '? '):
            continue
        animal = question = ''
        while not animal:
            animal = raw_input('What is the animals name? ').strip().lower()
        while not question:
            question = raw_input('What question would distinguish '
                                 'a %s from a %s? ' % (animal, k.question))
        k.left = Node(k.question)  # Add a new node for a wrong guess
        k.right = Node(animal)
        k.question = question
        if not yes_or_no('If the animal were %s the answer would be ? ' %
                         animal):
            k.right, k.left = k.left, k.right


if __name__ == '__main__':
    main()
