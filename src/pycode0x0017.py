#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0017.py
功能: 和电脑玩石头剪刀布
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.04.05
"""

from random import choice

# constants
GAME_NAME = 'Rock, Paper, Scissors!'
QUERY = 'Choose (r)ock, (p)aper, (s)cissors, or (q)uit:'
ROCK, PAPER, SCISSORS, QUIT = 'r', 'p', 's', 'q'
SHAPES = [ROCK, PAPER, SCISSORS]
KILLER = {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK}
SHAPE_NAME = {ROCK: 'rock', PAPER: 'paper', SCISSORS: 'scissors'}
PLAYER, COMPUTER, TIE = 'player', 'computer', 'tie'
WINNER = {PLAYER: 'The computer chooses {}. You win!',
          COMPUTER: 'The computer chooses {}. You lose!',
          TIE: 'You both choose {}. Tie game!'}
WIN_NUMBERS = [3, -2, -1]  # ASCII code differences to win
RESULT = '''Game over.
Computer wins: {score[%s]}
Player wins: {score[%s]}
Ties: {score[%s]}
Rock selected {record[%s]}
Paper selected {record[%s]}
Scissors selected {record[%s]}''' % (COMPUTER, PLAYER, TIE,
                                     ROCK, PAPER, SCISSORS)

# variables
record = {ROCK: 0, PAPER: 0, SCISSORS: 0}
score = {COMPUTER: 0, PLAYER: 0, TIE: 0}

# game starts
print(GAME_NAME)

# game loop
while True:
    # player making choice...
    you_choice = raw_input(QUERY).strip().lower()

    # when player choice is a valid shape
    if you_choice in SHAPES:
        # computer making choice...
        history = sorted(record.items(), key=lambda d: d[1], reverse=True)
        # try to beat player's prefered choice
        if history[0][1] - history[1][1] > 0:
            cpu_choice = KILLER[history[0][0]]
        # otherwise choose randomly
        else:
            cpu_choice = choice(SHAPES)

        # comparing choices
        result = ord(you_choice) - ord(cpu_choice)
        if result == 0:
            winner = TIE
        elif result in WIN_NUMBERS:
            winner = PLAYER
        else:
            winner = COMPUTER

        # show result and update data
        print(WINNER[winner].format(SHAPE_NAME[cpu_choice]))
        record[you_choice] += 1
        score[winner] += 1

    # enter q to end the game loop
    elif you_choice == QUIT:
        break

# statistic analysising
print(RESULT.format(score=score, record=record))
