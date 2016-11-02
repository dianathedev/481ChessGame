import chess
import time
from fenparser import FenParser
from log import LogInterface
from Strategy import Strategy

interface = LogInterface()
#interface.clear_logs()
last_move_X = ""
last_move_Y = ""
user = raw_input("Which player are you? (X/Y): \n")

if user == 'X': 
    expected_line_number = 2
elif user == 'Y':
    expected_line_number = 1

class Tree():
    def __init__(self, move):
        self.move = move
        self.points = 0
        self.children = []

# Input: Maximum number of turns
# Output: Checkmate or Stalemate
# Drives the game forward.
def play(n):
    global interface
    global user
   
    board = setupBoard()

    turn = user
    for i in range(n):
        if (turn == 'X' and i >= 1) or turn == 'Y': # X doesnt showopponentmove on his first turn
        #if turn == 'X':
            #print("CONDITIONS MET\n")
            #print("ENTERING show(): ")
            showOpponentMove(turn, board)
            #cont = raw_input("Cont")

        if board.is_checkmate():
            interface.write_result_to_log(turn,"lose","checkmate")
            quit(-1)
        if board.is_stalemate(): #if checkmate or stalemate are true then break from the loop
            interface.write_result_to_log(turn,"tie","stalemate")
            quit(-1)

        mov = generateMoves(board, turn) #Generate tree of possible moves

        #try:
        #print("TRYING move():\n\n")
        move(turn, mov, board)

    # Reached max # of moves
    interface.write_result_to_log(turn,"tie","reached max # of moves")

# Input: Yourself(X or Y), Next Move
# Output: None?
# Calls showMove and updates board state.
def move(turn, mov, board):
    #print("ENTERED move():\n\n")
    #print("Turn: {}\nMove: {}\n".format(turn, mov))
    newboard = FenParser(board.fen())
    boardlist = newboard.parse()
    """
    print("BOARDLIST:\n{}".format(boardlist))
    
    for i in range(8):
        for j in range(8):
            print(boardlist[i][j] + " ")
        print("\n")
    """

    r = 7 - ( int(mov[1]) - 1)
    c = ord(mov[0]) - 97
    #print("move() r: {}\nc: {}\n".format(r,c))

    pieceAtLocation = boardlist[r][c]
    pieceAtLocation.upper()

    coordsFixed = mov[2:4].upper()    

    board.push_uci(mov)
    player = turn
    piece = pieceAtLocation #Find piece based on mov
    #if piece == ' ':
        #print("PIECE IS EMPTY\n")
    coords = coordsFixed #Find coords based on mov

    #print("Turn: {}\nPlayer: {}\nPiece: {}\nCoords: {}".format(turn, player, piece, coords))
    #print("TRYING showMove():\n\n")
    showMove(turn, player, piece, coords, board)

# Input: Yourself(X or Y), Player whose move you are showing, Piece moved, New coordinate of piece.
# Output: None?
# Updates gameboard and log
def showMove(turn, player, piece, coords, board):
    #print("ENTERED showMove():\n\n")
    global interface

    # Show the updated move
    print(board)   
    
    if turn == 'X':
        #update log X
        interface.write_to_log_X(player, piece, coords)

    elif turn == 'Y':
        #update log Y
        interface.write_to_log_Y(player, piece, coords)

    #print("FINISHED showMove():\n\n")

# Input: 
# Output: Best move
# Uses X heuristic and mini-max to determine the best move.
def generateMoves(board, turn):
    tree = []
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
        row, col = find(board, 'R')
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

    #print("ENTERED showOpponentMove():\n")
    #print(turn)
    global interface
    global expected_line_number

    notFound = True
    while notFound:
        try:
            line_number, player, piece, coords = interface.user_reading_opponent_log(turn)
            
            #print(line_number, " ", expected_line_number)
            #print("Made it here")
            if int(line_number) == expected_line_number:
                #print("Working as intended")
                expected_line_number += 2
                notFound = False
                coords = coords.lower()

                if player == "Y":
                    interface.write_to_log_X(player, piece, coords)
                elif player == "X":
                    interface.write_to_log_Y(player, piece, coords)
            else:
                #print("Try again")
                pass
        except:
            #print("Log was empty")
            pass

    newboard = FenParser(board.fen())
    boardlist = newboard.parse()
    # Change the capital letter to lowercase.
    #coords = coords.lower()

    # The piece is uppercase for X, lowercase for Y.
    if player == "Y":
        piece = piece.lower()

    # Get original coords of move.
    item = piece
    r, c = findTEST(boardlist, item)

    #print("row: {}".format(r))

    c = chr(c+97)
    r = abs(r-7) + 1

    # Combine
    finalMove = c+str(r)+coords

    #print("finalmove: {}".format(finalMove))

    board.push_uci(finalMove)
    print(board)
    #move(player, finalMove, board)

# Takes in a boardlist (fen format) and a piece to search for
def findTEST(l, elem):
    #for row, i in enumerate(l):
    for row, columnlist in enumerate(l):
        col = 0
        for piece in columnlist:
            if piece == elem:
                return row, col
            col += 1
                #print "Found it!"
                #return row,col
    return -1
    """
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1
    """

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
