import chess
import time
from fenparser import FenParser
from log import LogInterface

interface = LogInterface()
turn = "X"
last_move_X = ""
last_move_Y = ""

class Tree():
    def __init__(self, move, children):
        self.move = move
        self.points = None
        self.children = None

# Input: Maximum number of turns
# Output: Checkmate or Stalemate
# Drives the game forward.
def play(n):
    turn = input("Which player are you?(X/Y)")
    board = setupBoard()

    for i in range(n):
        if (turn == 'X' and n > 1) or turn == 'Y': # X doesnt showopponentmove on his first turn

            showOpponentMove(turn, board)

        if board.isCheckMate() or board.isStalemate(): #if checkmate or stalemate are true then break from the loop
            #TODO: 
            #write_result_to_log(turn)
            #update Log file
            print("Made it!")
            break
        
        #mov = generateMoves(board, turn)

        mov = input("Enter move e.g. E4->F5")
        move(turn, mov, board)


# Input: Yourself(X or Y), Next Move
# Output: None?
# Calls showMove and updates board state.
def move(turn, mov, board):
    newboard = FenParser(board.fen())
    boardlist = newboard.parse()

    r = int(mov[1]) - 1
    c = ord(mov[0]) - 98

    pieceAtLocation = boardlist[r][c]
    pieceAtLocation.upper()

    coordsFixed = mov[2:4].upper()    

    board.push_uci(mov)
    player = turn
    piece = pieceAtLocation #Find piece based on mov
    coords = coordsFixed #Find coords based on mov

    showMove(turn, player, piece, coords, board)

# Input: Yourself(X or Y), Player whose move you are showing, Piece moved, New coordinate of piece.
# Output: None?
# Updates gameboard and log
def showMove(turn, player, piece, coords, board):
    print(board)   
    global interface
    if turn == 'X':
        #update log X
        interface.write_to_log_X(self, player, piece, coords)

    elif turn == 'Y':
        #update log Y
        interface.write_to_log_X(self, player, piece, coords)




# Input: 
# Output: Best move
# Uses X heuristic and mini-max to determine the best move.
def generateMoves(board):
    tree = ()
    moves = board.legal_moves
    for move in moves:  #save every move as a Tree node
        tree.append(Tree(str(move)))
    for item in tree:  #for every move
        point = float("inf")
        board.push_uci(item.move)
        for i in board.legal_moves:
            item.children.append(str(i))
        for y in item.children: #for evey child of move
            board.push_uci(y)
            state = board.fen()
            if turn is 'X':
                value = heuristicX(state)
            elif turn is 'Y':
                value = heuristicY(state)
            if value < point:
                point = value
            board.pop()
        board.pop()
        item.points = point
    maxPoints = -float("inf")
    bestMove = None
    for x in tree:
        if x.points > maxPoints:
            maxPoints = x.points
            bestMove = x.move
    return bestMove

# Input: A single board state
# Output: Best move
# Uses Y heuristic and mini-max to determine the best move.
def heuristicX(state):

    strat= Strategy()
    value = 0
    newBoard = FenParser(state)
    board = newBoard.parse()

    #find King Value
    try:
        row, col = find(board, 'K')
    except:
        return -float("inf")
    value += strat.getKing()[row][col]

    #find rook value
    try:
        row col = find(board, 'R')
        value += strat.getRook()[row][col]
    except:
        value -= 20

    #find night value

    try:
        row, col = find(board, 'N')
        value += strat.getNight()[row][col]
    except:
        value -= 5

    #find enemy night
    try:
        row, col = find(board, 'n')
    except:
        value += 20
    return value

def heuristicY(state):
    strat= Strategy()
    value = 0
    newBoard = FenParser(state)
    board = newBoard.parse()

    #find king value
    try:
        row, col = find(board, 'k')
        value += strat.getKing()[row][col]
    except:
        -float("inf")

    #find night value
    try:
        row, col = find(board, 'n')
        value += strat.getNight()[row][col]
    except:
        value -= 5

    #find enemy rook
    try:
        row, col = find(board, 'R')
    except:
        value += 50

    #find enemy night
    try:
        row, col = find(board, 'N')
    except:
        value += 15
    return value


# Input: Yourself(X or Y)
# Output: None?
# Updates board and log with opponents last move.
def showOpponentMove(turn, board):
    player, piece, coords = user_reading_opponent_log(turn)

    newboard = FenParser(board.fen())
    boardlist = newboard.parse()

    # Change the capital letter to lowercase.
    coords.lower()

    # The piece is uppercase for X, lowercase for Y.
    if player == "Y":
        piece = str.lower(piece)

    # Get original coords of move.
    item = piece
    r, c = find(boardlist, item)
    
    r = r-1
    c = ord(c)-65

    # Combine
    finalMove = c+r+coords

    move(player, finalMove, board)



# Takes in a boardlist (fen format) and a piece to search for
def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1





# Input: Yourself(X or Y)
# Output: Player who last made a move, Piece moved, New coordinates of piece
# Reads the opponents log and returns details of their new move.
def read_from_log(turn):
    pass
# Input: Player who made move, Piece moved, New coordinates of piece
# Output: None
# Update the on screen board with new move.
def write_to_screen(board):
    board

# Input: None
# Output: None
# Setup Board with initial chess positions.
def setupBoard():
    board = chess.Board(fen='2n1k3/8/8/8/8/8/8/4K1NR 2 KQkq - 0 1', chess960=False)
    print(board)
    return chess.Board(fen='2n1k3/8/8/8/8/8/8/4K1NR 2 KQkq - 0 1', chess960=False)


def main():
    with open("config.txt","r") as ifh:
        n = int(ifh.readline())

    play(n)


if __name__ == "__main__":
    main()

def find(l,elem):
	for row, i in enumerate(l):
		try:
			column = i.index(elem)
		except ValueError:
			continue
		return  row, column
	return -1

"""
# Input: Current board state
# Output: Tree off all moves depth 3
# Generate all possible moves thinking ahead 2 steps
def generateMoves(board):
	moves = Tree()
	moves.children = board.legal_moves
	moves.parent = None
	for x in moves.children:
"""
