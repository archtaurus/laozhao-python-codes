#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0019.py
功能: 读心术（人类版）
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.02.27
"""

# import randint for make_a_guess
from random import randint as make_a_guess

# define the constants
MIN, MAX = 0, 100
BINGO = make_a_guess(MIN, MAX)
REQUEST_INPUT = "Take a guess: "
TOO_LOW = "Your guess was too low!\n"
TOO_HIGH = "Your guess was too high!\n"
PLAYER_WON = "You've guessed my number in %d times!"


def guess_game():
    """Player guess a random number in range 0~100
    """
    # define the variables
    guess = None
    user_input = ''
    times = 0

    # game start
    print ("Let's play a guessing game!\n\n"
           "The computer will think of a number\n"
           "I(the computer) have thought of a number between 0 and 100.\n")

    # game playing
    while True:
        while True:
            # player makes a guess
            user_input = raw_input(REQUEST_INPUT).strip()
            # validate user input
            if user_input.isdigit():
                break
        guess = int(user_input)
        times += 1

        # computer checks the guess
        if guess < BINGO:       # player's guess is lower
            print (TOO_LOW)
        elif guess > BINGO:     # player's guess is higher
            print (TOO_HIGH)
        else:                   # otherwise is BINGO
            break

    # computer always wins
    print (PLAYER_WON % times)


if __name__ == '__main__':
    guess_game()
