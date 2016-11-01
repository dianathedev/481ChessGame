class Strategy(object):

    #ATTACK_KING_BONUS = 5000
    #ATTACK_ROOK_BONUS = 1000

    self.king = [
        [-50,-40,-30,-20,-20,-30,-40,-50,],
        [-30,-20,-10,  0,  0,-10,-20,-30,],
        [-30,-10, 20, 30, 30, 20,-10,-30,],
        [-30,-10, 30, 40, 40, 30,-10,-30,],
        [-30,-10, 30, 40, 40, 30,-10,-30,],
        [-30,-10, 20, 30, 30, 20,-10,-30,],
        [-30,-30,  0,  0,  0,  0,-30,-30,],
        [-50,-30,-30,-30,-30,-30,-30,-50]
    ]

    self.rook = [
        [0,  0,  0,  0,  0,  0,  0,  0,],
        [5, 10, 10, 10, 10, 10, 10,  5,],
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


    """
    @staticmethod
    def squareToValue(square, color):
        piece = square.getPiece()

        row = square.getRow()
        column = square.getColumn()

        # Pseudo-mirror array using Python's reverse list lookup
        if color == 'black':
            row *= -1
            column *= -1

        if piece.getType() == 'Rook':
            return Strategy.rook[row][column]
        elif piece.getType() == 'King':
            return Strategy.king[row][column]
        """