#!/usr/bin/python3
# Author: Team Deshawn
# Class: CS 481 - Artificial Intelligence
# Instructor: Ryu
# Date: Fall 2016
'''
# Description:
#   This file holds a static set of board position values for the various pieces.
#   The heuristic functions in the chessmain.py file refer to these values when
#   evaluating their new location.
#   
#   We prioritize the following:
#       King    - Middle of the board
#       Night   - Total number of moves from current location
#       Rook    - Control of the 7th rank
'''
# Future additions:
#   Better board optimization strategy.

class Strategy(object):

    def __init__(self):
        self.king = [
            [-5,-4,-3,-2,-2,-3,-4,-5,   ],
            [-3,-2,-1,  1,  1,-1,-2,-3, ],
            [-3,-1, 2, 3, 3, 2,-1,-3,   ],
            [-3,-1, 3, 4, 4, 3,-1,-3,   ],
            [-3,-1, 3, 4, 4, 3,-1,-3,   ],
            [-3,-1, 2, 3, 3, 2,-1,-3,   ],
            [-3,-3, 1, 1, 1, 1,-3,-3,   ],
            [-5,-3,-3,-3,-3,-3,-3,-5    ]
        ]

        self.rook = [
            [0,  0,  0,  0,  0,  0,  0,  0, ],
            [5, 10, 10, 10, 10, 10, 10,  5, ],
            [-5,  0,  0,  0,  0,  0,  0, -5,],
            [-5,  0,  0,  0,  0,  0,  0, -5,],
            [-5,  0,  0,  0,  0,  0,  0, -5,],
            [-5,  0,  0,  0,  0,  0,  0, -5,],
            [-5,  0,  0,  0,  0,  0,  0, -5,],
            [0,  0,  0,  5,  5,  0,  0,  0  ]
        ]

        self.night = [
            [2,  3,  4,  4,  4,  4,  3, 2,],
            [3,  4,  6,  6,  6,  6,  4, 3,],
            [4,  6,  8,  8,  8,  8,  6, 4,],
            [4,  6,  8,  8,  8,  8,  6, 4,],
            [4,  6,  8,  8,  8,  8,  6, 4,],
            [4,  6,  8,  8,  8,  8,  6, 4,],
            [3,  4,  6,  6,  6,  6,  4, 3,],
            [2,  3,  4,  4,  4,  4,  3, 2 ]
        ]

    def getKing(self):
        return self.king

    def getRook(self):
        return self.rook

    def getNight(self):
        return self.night

