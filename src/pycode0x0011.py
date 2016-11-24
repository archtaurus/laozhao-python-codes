#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0011.py
功能: 和电脑玩Blackjack
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.07.21
"""

from random import shuffle

# 常量
WELCOME_MESSAGE = '*** 和电脑玩 Blackjack ***\n'
PLAYER_CARDS = '你手上的牌是 {}'
PLAYER_SCORE = '你目前的点数是 {}'
YOUR_BUSTED = '你爆了。祝下次好运！'
PLAYER_DECISION = '你想再要一张牌 (H) 还是不要了 (S): '
COMPUTER_CARDS = '电脑手上的牌是 {}'
COMPUTER_SCORE = '电脑目前的点数是 {}'
COMPUTER_HIT = '电脑的点数少于 17，再要一张。'
COMPUTER_BUSTED = '电脑点数爆了！'
COMPUTER_STANDS = '电脑不要牌了。'
YOU_WIN = '你获胜了！'
YOU_LOSE = '你失败了！'
PLAY_AGAIN = '要再玩一把么？(Y/N): '


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


def count_score(cards_in_hand):
    "计算点数"
    scores = [0]
    for card in cards_in_hand:
        val = card[3:]  # UTF-8的花色字符在字符串中占三个字节
        if val == 'A':
            scores = [score + 1 for score in scores]            # A = 1
            scores += [score + 10 for score in scores]          # A = 11
        elif val.isalpha():
            scores = [score + 10 for score in scores]           # JQK
        else:
            scores = [score + int(val) for score in scores]     # 2~10
        if min(scores) > 21:
            return min(scores)                                  # 点数爆了
    return max(score for score in scores if score <= 21)        # 返回点数


def player_deal(cards):
    "玩家操作"
    player_hit = True                       # 是否要牌的标志
    player_cards = [take_one_card(cards)]   # 第一张牌
    while player_hit:
        # 拿一张牌
        player_cards.append(take_one_card(cards))
        print(PLAYER_CARDS.format(' '.join(player_cards)))
        # 算点数
        player_score = count_score(player_cards)
        print(PLAYER_SCORE.format(player_score))
        # 判断点数是否爆了
        if player_score > 21:
            print(YOUR_BUSTED)
            return player_score
        # 是否还要牌？
        while True:
            decision = raw_input(PLAYER_DECISION).lower()
            if decision == 'h':
                break
            elif decision == 's':
                return player_score
            else:
                print('无效输入！')


def computer_deal(cards):
    "电脑操作"
    computer_hit = True
    computer_cards = [take_one_card(cards)]
    while computer_hit:
        # 拿一张牌
        computer_cards.append(take_one_card(cards))
        print(COMPUTER_CARDS.format(' '.join(computer_cards)))
        # 算点数
        computer_score = count_score(computer_cards)
        print(COMPUTER_SCORE.format(computer_score))
        # 判断是否还要牌
        if computer_score > 21:
            print(COMPUTER_BUSTED)
            break
        if computer_score >= 17:
            print(COMPUTER_STANDS)
            break
        else:
            print(COMPUTER_HIT)

    return computer_score


def play_again():
    "询问是否再玩一把"
    while True:
        decision = raw_input(PLAY_AGAIN).lower()
        if decision == 'y':
            return True
        elif decision == 'n':
            return False
        else:
            print('无效输入！')


def play_balckjack():
    # 欢迎信息
    print(WELCOME_MESSAGE)
    # 洗牌
    cards = shuffled_cards()
    while True:
        # 玩家操作
        you_score = player_deal(cards)
        if you_score > 21:
            print(YOU_LOSE)
        # 电脑操作
        else:
            computer_score = computer_deal(cards)
            if computer_score > 21 or you_score > computer_score:
                print(YOU_WIN)
            else:
                print(YOU_LOSE)
        # 再玩一把？
        if not play_again():
            print('再见～～～')
            return


if __name__ == '__main__':
    play_balckjack()
