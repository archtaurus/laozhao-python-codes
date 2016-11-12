#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x001A.py
# 功能: 读心术（电脑版）
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.02.27

# define the constants
COMPUTER_TRY = "The computer guesses: {0}"
PLAY_REPLY = "Is the number too high (H), too low (L), or correct (C)?"
COMPUTER_ANGRY = "It's IMPOSSIBLE!!!"  # computer hates cheater
COMPUTER_WON = "I've won again! I guessed %d times."
TOO_LOW = 'l'
TOO_HIGH = 'h'
BINGO = 'c'


def guess_game():
    '''Computer guess a random number you choosed in range 0~100
    '''
    # define the variables
    min_guess = 0
    max_guess = 100
    guess = 50
    result = None
    times = 0

    # game start
    print ("Let's play a guessing game!\n\n"
           "Please think of a number between 0 and 100.\n"
           "When you have thought of a number, press enter to continue.")
    raw_input()  # wait player to enter

    # game playing
    while True:

        # computer makes a guess
        guess = min_guess + (max_guess - min_guess) // 2
        print (COMPUTER_TRY.format(guess))
        times += 1

        # player checks the guess
        result = raw_input(PLAY_REPLY).strip().lower()

        # when player cheats on computer
        if min_guess == guess == max_guess:
            if result != BINGO:
                print (COMPUTER_ANGRY)
                break
        elif result == BINGO:                   # computer's guess is right
            break
        elif result == TOO_LOW:                 # computer's guess is lower
            min_guess = guess + 1
        elif result == TOO_HIGH:                # computer's guess is higher
            max_guess = guess - 1
        else:                                   # pass wrong input
            pass

    # computer always wins
    print (COMPUTER_WON % times)


if __name__ == '__main__':
    guess_game()
