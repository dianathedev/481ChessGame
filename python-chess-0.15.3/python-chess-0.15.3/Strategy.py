class Strategy(object):

    ATTACK_KING_BONUS = 5000
    ATTACK_ROOK_BONUS = 1000

    def __init__(self):
        self.king = [
            [-5,-4,-3,-2,-2,-3,-4,-5,],
            [-3,-2,-1,  1,  1,-1,-2,-3,],
            [-3,-1, 2, 3, 3, 2,-1,-3,],
            [-3,-1, 3, 4, 4, 3,-1,-3,],
            [-3,-1, 3, 4, 4, 3,-1,-3,],
            [-3,-1, 2, 3, 3, 2,-1,-3,],
            [-3,-3,  1,  1,  1,  1,-3,-3,],
            [-5,-3,-3,-3,-3,-3,-3,-5]
        ]

        self.rook = [
            [0,  0,  0,  0,  0,  0,  0,  0,],
            [5, 10, 10, 10, 10, 10, 10,  8,],
            [-5,  0,  0,  0,  0,  0,  0, -5,],
            [-5,  0,  0,  0,  0,  0,  0, -5,],
            [-5,  0,  0,  0,  0,  0,  0, -5,],
            [-5,  0,  0,  0,  0,  0,  0, -5,],
            [-5,  0,  0,  0,  0,  0,  0, -5,],
            [0,  0,  0,  5,  5,  0,  0,  0]
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

