#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0011.py
# 功能: 和电脑玩Blackjack
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.21

from random import shuffle

# 常量
WELCOME_MESSAGE = '*** Simple Blackjack ***\n'
PLAYER_DEAL = 'You are dealt a {}.'
PLAYER_SCORE = 'Your score is: {}'
YOUR_BUSTED = 'You busted. Better luck next time!'
PLAYER_DECISION = 'Would you like to hit (H) or stand (S): '
COMPUTER_DEAL = 'The computer is dealt a {}.'
COMPUTER_SCORE = 'The computer\'s score is {}'
COMPUTER_HIT = 'The computer\'s score is below 17 and takes another card.'
COMPUTER_BUSTED = 'The computer busted!'
COMPUTER_STANDS = 'The computer stands.'
YOU_WIN = 'You win!'
YOU_LOSE = 'You lose!'
PLAY_AGAIN = 'Would you like to play again? (Y/N): '


def shuffled_cards():
    "返回一副洗好的牌"
    cards = [suit + rank
             for suit in ['♠', '♥', '♣', '♦']
             for rank in ('2', '3', '4', '5', '6', '7',
                          '8', '9', '10', 'J', 'Q', 'K', 'A')]
    shuffle(cards)
    return cards


def take_one_card(cards):
    "发一张牌"
    if not cards:
        cards.extend(shuffled_cards())      # 牌用完了重新洗牌
    return cards.pop()


def count_score(player_cards):
    scores = [0]
    for card in player_cards:       # for each card in hand
        val = card[3:]                  # get point value str from card
        if val == 'A':
            scores = [score + 1 for score in scores]            # for A = 1
            scores += [score + 10 for score in scores]          # for A = 11
        elif val.isalpha():
            scores = [score + 10 for score in scores]           # for JQK
        else:
            scores = [score + int(val) for score in scores]     # for 2~10
        if min(scores) > 21:
            return min(scores)                                  # busted
    scores = [score for score in scores if score <= 21]         # valid scores
    return max(scores)                                          # final score


def player_deal(cards):
    player_hit = True  # player's decision
    player_cards = []  # cards in player's hand
    while player_hit:

        # take one card and put it into hand
        card = take_one_card(cards)
        print(PLAYER_DEAL.format(card))
        player_cards.append(card)

        # calculate score
        player_score = count_score(player_cards)
        print(PLAYER_SCORE.format(player_score))

        # player busted?
        if player_score > 21:
            print(YOUR_BUSTED)
            return player_score

        # deal another card?
        while True:
            decision = raw_input(PLAYER_DECISION).lower()
            if decision == 'h':
                break
            elif decision == 's':
                return player_score
            else:
                print('Invalid input!')


def computer_deal(cards):
    computer_hit = True
    computer_cards = []
    while computer_hit:

        # take one card
        card = take_one_card(cards)
        print(COMPUTER_DEAL.format(card))
        computer_cards.append(card)

        # calculate score
        computer_score = count_score(computer_cards)
        print(COMPUTER_SCORE.format(computer_score))

        # need another card?
        if computer_score > 21:
            print(COMPUTER_BUSTED)
            break
        if computer_score >= 17:
            print(COMPUTER_STANDS)
            break
        else:
            print(COMPUTER_HIT)
    return computer_score


def ask_play_again():
    while True:
        decision = raw_input(PLAY_AGAIN).lower()
        if decision == 'y':
            return True
        elif decision == 'n':
            return False
        else:
            print('Invalid input!')


def play_balckjack():

    # 欢迎信息
    print(WELCOME_MESSAGE)
    # 洗牌
    cards = shuffled_cards()

    while True:

        # player's round
        you_score = player_deal(cards)
        if you_score > 21:
            print(YOU_LOSE)

        # computer's round
        else:
            computer_score = computer_deal(cards)
            if computer_score > 21 or you_score > computer_score:
                print(YOU_WIN)
            else:
                print(YOU_LOSE)

        # play again?
        if not ask_play_again():
            print('Goodbye')
            return


if __name__ == '__main__':
    play_balckjack()
