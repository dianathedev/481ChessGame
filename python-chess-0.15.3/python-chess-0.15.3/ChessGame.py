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
    global interface
    turn = raw_input("Which player are you?(X/Y)")
    board = setupBoard()
    print(board)

    for i in range(n):
        if (turn == 'X' and n > 1) or turn == 'Y': # X doesnt showopponentmove on his first turn

            showOpponentMove(turn, board)

        if board.is_checkmate() or board.is_stalemate(): #if checkmate or stalemate are true then break from the loop
            #TODO: 
            #write_result_to_log(turn)
            #update Log file
            print("Made it!")
            break
        #moves = generateMoves(board) #Generate tree of possible moves
        if turn == 'X':
            #mov = heuristicX(board)
            pass
        elif turn == 'Y':
            #mov = heuristicY(board)
            pass
        mov = raw_input("\nEnter move e.g. e4e5\n")
        print(mov)

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
        interface.write_to_log_X(player, piece, coords)

    elif turn == 'Y':
        #update log Y
        interface.write_to_log_X(player, piece, coords)




# Input: 
# Output: Best move
# Uses X heuristic and mini-max to determine the best move.
def heuristicX(board):
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
            value = 0#TODO use state to determine heuristicX value
            if value < point:
                point = value
            board.pop()
        board.pop()
        item.points = point
    maxPoints = float("-inf")
    bestMove = None
    for x in tree:
        if x.points > maxPoints:
            maxPoints = x.points
            bestMove = x.move
    return bestMove

# Input: 
# Output: Best move
# Uses Y heuristic and mini-max to determine the best move.
def heuristicY(board):
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
            value = 0#TODO use state to determine heuristicY value
            if value < point:
                point = value
            board.pop()
        board.pop()
        item.points = point
    maxPoints = float("-inf")
    bestMove = None
    for x in tree:
        if x.points > maxPoints:
            maxPoints = x.points
            bestMove = x.move
    return bestMove

# Input: Yourself(X or Y)
# Output: None?
# Updates board and log with opponents last move.
def showOpponentMove(turn, board):
    global interface
    try:    
        player, piece, coords = interface.user_reading_opponent_log(turn)
    except:
        print("Log was empty")
        return

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
    pass

# Input: None
# Output: None
# Setup Board with initial chess positions.
def setupBoard():
    #board = chess.Board('2n1k3/8/8/8/8/8/8/4K1NR 2 KQkq - 0 1')
    #print(board)
    #return board    
    return chess.Board('2n1k3/8/8/8/8/8/8/4K1NR w K - 0 1')


def main():
    with open("config.txt","r") as ifh:
        n = int(ifh.readline())

    play(n)


if __name__ == "__main__":
    main()

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
