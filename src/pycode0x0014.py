#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0014.py
# 功能: N-queens puzzle solver
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.03.03

from itertools import permutations


class Nqueens:
    '''

    N-queens puzzle solver

        The N-queens puzzle is the problem of placing N chess
        queens on a N x N chessboard so that no two queens
        attack each other. Thus, a solution requires that no
        two queens share the same row, column, or diagonal.
        There are solutions exist for all natural numbers N
        with the exception of 2 and 3.
        Go http://en.wikipedia.org/wiki/Eight_queens_puzzle
        for more information.

        A solution sample of 92 solutions for 8 queens puzzle.

          Solution:     1
          ---------------
        0 Q . . . . . . .
        4 . . . . Q . . .
        7 . . . . . . . Q
        5 . . . . . Q . .
        2 . . Q . . . . .
        6 . . . . . . Q .
        1 . Q . . . . . .
        3 . . . Q . . . .
          ---------------
    Useage:

        Nqueens(n = 8) --> a 'n' queens puzzle solver object

            nqueens = Nqueens(8)
            nqueens.output()

        n is the number of queens, default is 8. n should be
        a natural number in range(4, 11), the return value
        is the same object.

    This code is referenced to the following code from
    en.wikipedia.org/wiki/Eight_queens_puzzle:

        from itertools import permutations
        n = 8
        cols = range(n)
        for vec in permutations(cols):
            if (n == len(set(vec[i] + i for i in cols))
                  == len(set(vec[i] - i for i in cols))):
                print vec
    '''

    def __init__(self, n=8):
        '''return a N-queens puzzle object, n should be in range(4, 11).'''
        self.n = n
        self.solutions = []

    def solve(self):
        '''solve the N-queens puzzle'''
        if self.n not in range(4, 11):
            print ('Cancled ... %d is out of range(4, 11)...' % self.n)
            return
        rows = range(self.n)
        for solution in permutations(rows):
            if (self.n == len(set(solution[_] + _ for _ in rows)) ==
                    len(set(solution[_] - _ for _ in rows))):
                self.solutions.append(solution)
        self.solutions_count = len(self.solutions)

    def output(self):
        '''print out all sulotions'''
        if not self.solutions:
            return
        print ('%d solutions for %d-queens puzzle' % (self.solutions_count,
                                                      self.n))
        width = self.n * 2 - 1
        title = ("  Solution:%?d\n".replace('?', str(width - 9)) +
                 "  " + "-" * width)
        for i in range(self.solutions_count):
            print (title % (i + 1))
            for j in self.solutions[i]:
                print (str(j) + ' ' + '. ' * j +
                       "Q" + " ." * (self.n - 1 - j))
            print ('  ' + "-" * width)


if __name__ == '__main__':
    nqueens = Nqueens(8)
    nqueens.solve()
    nqueens.output()
