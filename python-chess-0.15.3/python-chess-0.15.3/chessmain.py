#!/usr/bin/python3
# Author: Team Deshawn
# Class: CS 481 - Artificial Intelligence
# Instructor: Ryu
# Date: Fall 2016
'''
# Description:
#   This file handles importing all the chess modules and running the main program.
#   
#   To run:
#       1. Start two terminals (T1 and T2)
#       2. T1: navigate to /481ChessGame/python-chess-0.15.3/python-chess-0.15.3
#       3. T2: navigate to /481ChessGame/python-chess-0.15.3/python-chess-0.15.3
#       4. T1: Run this command to start the game as player X.
#           python3 chessmain.py X
#       5. T2: Run this command to start the game as player Y.
#           python3 chessmain.py Y
#       6. Watch either terminal (or both at the same time) to see the game play.
#       7. Review the log files log_X.txt and log_Y.txt 
#
#   To change the maximum allowed number of moves:
#       Open config.txt and change the value.
#       Enter it as a positive integer.
#
#   To change the ply (search depth):
#       Within the Global declarations below, change the value of ply.
#       Enter it as a positive integer.
#
#
'''
# Future additions:
#   Better heuristics for X and Y.

''' Imports. '''
import sys
import chess
import time
import datetime
from fenparser import FenParser
from log import LogInterface
from strategy import Strategy

''' Global declarations. '''
# Create our global variables for interacting with the log files, importing the
# strategy, keeping track of time, and the user (X or Y) who is running this
# instance of the program.
interface = LogInterface()
strat = Strategy()
startTime = datetime.datetime.now()
user = sys.argv[1]
ply = 3

# These are global variables for expectations for reading the log files.
if user == 'X': 
    # Clear the logs for the new game.
    interface.clear_logs()
    expected_line_number = 2
elif user == 'Y':
    expected_line_number = 1


''' Setup the chess board with the initial chess positions. '''
# Input:
#   None
# Output:
#   The board with the initial chess positions.
def setupBoard():
    # The board starts with this setup.
    return chess.Board('2n1k3/8/8/8/8/8/8/4K1NR w K - 0 1')


''' The function initiating and handling the game being played. '''
# Drives the game forward and ends the play loop if the maximum number of moves has been reached.
# Input:
#   @param n    - Maximum number of turns
# Output:
#   Play has no output, but will call the other functions to run the game.
def play(n):
    global interface # For log
    global user # The player in this instance of the program
    global startTime # Starting time on my turn
    global ply # The depth we are searching in the game tree
   
    # Setup the initial board and keep track of the user.
    board = setupBoard()
    turn = user
    alpha = -float('inf')
    beta = float('inf')

    # This loop will handle playing the game. Continue until the game ends or
    # the maximum number of moves has been reached.
    for i in range(n):
        startTime = datetime.datetime.now() # Get the current time.
        # X makes the first move. For all other moves, check the opponent's move.
        if (turn == 'X' and i >= 1) or turn == 'Y':
            showOpponentMove(turn, board)

        # The opponent has made a move, we need to check if the game is over.
        checkBoardStatus(turn, board)
        
        # Use the Minimax algorithm with Alpha-Beta pruning to find the move.
        bestscore, mov = alphaBetaMax(turn, board, alpha, beta, ply)

        # Call move to complete the best move found by the algorithm.
        move(turn, mov, board)

        # I have made a move, we need to check if the game is over.
        checkBoardStatus(turn, board)

    # Outside of loop, meaning we reached the max # of moves
    interface.write_result_to_log(turn,"tie","reached max # of moves")


''' Checks the status of the board to see if the game is over. Done after updating
    the board. If the game is over, write the result to the log and quit. '''
# Input:
#   @param turn     - The player playing the game (X or Y) so we can evaluate the
#                     correct board.
#   @param board    - Need the board state to print the board state.
# Output:
#   Writes to the log file and ends game when applicable.
def checkBoardStatus(turn, board):
    if board.result() != "*":

        # See if it is a checkmate.
        if board.is_checkmate():
            time.sleep(1)
            interface.write_result_to_log(turn,"lose","checkmate")
            sys.exit(1)

        # See if it is a stalemale.
        elif board.is_stalemate():
            time.sleep(1)
            interface.write_result_to_log(turn,"tie","stalemate")
            sys.exit(1)

        # See if it is a threefold repetition.
        elif board.can_claim_threefold_repetition():
            time.sleep(1)
            interface.write_result_to_log(turn,"tie","threefold repetition")
            sys.exit(1)


''' The move function completes a board move and then calls showMove to display it''' 
# Input:
#   @param turn     - The player playing the game (X or Y) so we can evaluate the
#                     correct board.
#   @param mov      - The move to be made as a string in uci format.
#   @param board    - Need the board state to print the board state.
# Output:
#   Completes the specified move and sends the required parameters to showMove.
def move(turn, mov, board):

    # Create an instance of the board in FEN format
    newboard = FenParser(board.fen())
    boardlist = newboard.parse()

    # Calculate the row and column index of the move.
    rowIndex = 7 - ( int(mov[1]) - 1)
    colIndex = ord(mov[0]) - 97

    # Get the piece at the specified location
    pieceAtLocation = boardlist[rowIndex][colIndex]
    pieceAtLocation.lower()

    coordsFixed = mov[2:4].upper()    

    board.push_uci(mov)
    player = turn
    piece = pieceAtLocation #Find piece based on mov
    coords = coordsFixed #Find coords based on mov

    showMove(player, piece, coords, board)


''' Shows the move on the screen, outputs the move to the player's log file '''
# Input:
#   @param player     - The player playing the game (X or Y)
#   @param piece      - The piece which needs to be written to the log file 
#                       (K, N, or R).
#   @param coords     - The final coordinates of the piece which moved
#                       (i.e. e4).
#   @param board      - Need the board state to print the board state.
# Output:
#   Displays the board and updates the log file.
def showMove(player, piece, coords, board):
    global interface

    # Show the updated move on the screen.
    print("{}'s move\n".format(player))
    print(board)
    print("\n")
    
    if player == 'X':
        # Update log X
        interface.write_to_log_X(player, piece, coords)

    elif player == 'Y':
        # Update log Y
        interface.write_to_log_Y(player, piece, coords)


''' For reading the Opponent's move from the log file '''
# Input: Yourself(X or Y)
# Output: None?
# Updates board and log with opponents last move.
def showOpponentMove(turn, board):
    global interface
    global expected_line_number

    # 
    Found = False
    while not Found:
        try:
            line_number, player, piece, coords = interface.user_reading_opponent_log(turn)

            if int(line_number) == expected_line_number:
                #print("Working as intended")
                expected_line_number += 2
                Found = True
                coords = coords.lower()

                if player == "Y":
                    interface.write_to_log_X(player, piece, coords)
                elif player == "X":
                    interface.write_to_log_Y(player, piece, coords)
            else:
                # The log has not been updated. Sleep and try again.
                time.sleep(0.1)
        except:
        # The log was empty. Sleep and try again.
            time.sleep(0.1)

    newboard = FenParser(board.fen())
    boardlist = newboard.parse()
    # Change the capital letter to lowercase.
    #coords = coords.lower()

    # The piece is uppercase for X, lowercase for Y.
    if player == "Y":
        piece = piece.lower()

    # Get original coords of move, checking if it was possible
    try:
        row, col = findPieceRankFileFormat(boardlist, piece)
    except:
        print("The specified move is not possible.\n")
        sys.exit(1)

    # Combine the parts of the move.
    finalMove = col + str(row) + coords

    board.push_uci(finalMove)

    print("{}'s move\n".format(player))
    print(board)
    print("\n")


''' Starts the minimax algorithm with alpha-beta pruning. Generate all moves, then
    for each move, evaluate the move using alphaBetaMin, and undo the move. Keep
    track of the best move and the time. '''
# Input:
#   @param turn         - The player playing the game (X or Y) so we can evaluate
#                         the move using the correct heuristic.
#   @param boardstate   - Need the board state to print the board state.
#   @param alpha        - The highest value encountered.
#   @param beta         - The lowest value encountered.
#   @param levelsToGo   - The remaining number of levels to go down.
# Output:
#   When levelsToGo = 0, returns the value from the heuristic on that state.
#   When levelsToGo > 1, returns the alpha value and best move (unless pruned or
#   maximum time is reached.
def alphaBetaMax(turn, boardstate, alpha, beta, levelsToGo):
    # When we've reached the final level, analyze the state with the heuristic.
    if levelsToGo == 0:
        if turn == "X":
            return (heuristicX(boardstate), None)
        elif turn == "Y":
            return (heuristicY(boardstate), None)

    bestMove = None # Begin with no best move
    # Generate all legal moves and loop through them, applying the algorithm.
    for move in boardstate.legal_moves:
        #bestMove = None
        move = str(move)
        # Make move
        boardstate.push_uci(move)
        currentMove = move
        score, moveparam = alphaBetaMin(turn, boardstate, alpha, beta, levelsToGo - 1)
        # Unmake move
        boardstate.pop()

        if score >= beta:
            return (beta, currentMove)      # fail hard beta-cutoff
        if score > alpha:
            bestMove = currentMove 
            alpha = score                   # alpha acts like max in MiniMax
        currentTime = datetime.datetime.now()
        timeDifference = (currentTime - startTime)
        timeDifference = timeDifference.total_seconds()
        if timeDifference > 8.5:
            print("Time taken: {}".format(timeDifference))
            break

    return (alpha, bestMove)


''' The mini portion of Minimax algorithm with alpha-beta pruning. Generate all 
    moves, then for each move, evaluate the move using alphaBetaMin, and undo the
    move. Keep track of the best move and the time. '''
# Input:
#   @param turn         - The player playing the game (X or Y) so we can evaluate
#                         the move using the correct heuristic.
#   @param boardstate   - Need the board state to print the board state.
#   @param alpha        - The highest value encountered.
#   @param beta         - The lowest value encountered.
#   @param levelsToGo   - The remaining number of levels to go down.
# Output:
#   When levelsToGo = 0, returns the value from the heuristic on that state.
#   When levelsToGo > 1, returns the beta value and best move (unless pruned or
#   maximum time is reached.
def alphaBetaMin(turn, boardstate, alpha, beta, levelsToGo):
    global startTime
    if levelsToGo == 0:
        if turn == "X":
            return (heuristicX(boardstate), None)
        if turn == "Y":
            return (heuristicY(boardstate), None)

    bestMove = None
    for move in boardstate.legal_moves:
        #bestMove = None
        move = str(move)
        # Make move
        boardstate.push_uci(move)
        currentMove = move        
        score, moveparam = alphaBetaMax(turn, boardstate, alpha, beta, levelsToGo - 1)
        # Unmake move
        boardstate.pop()

        if score <= alpha:
            return (alpha, currentMove)     # fail hard alpha-cutoff
        if score < beta:
            bestMove = currentMove 
            beta = score                    # beta acts like min in MiniMax
        currentTime = datetime.datetime.now()
        timeDifference = (currentTime - startTime)
        timeDifference = timeDifference.total_seconds()
        if timeDifference > 8.5:
            print("Time taken: {}".format(timeDifference))
            break

    return (beta, bestMove)


''' The heuristic for X.  Try to optimize X's move. '''
# Input:
#   @param state     - A single board state (based on a potential move)
# Output:
#   The value of the potential move.
def heuristicX(state):
    global strat

    # The value is initialized as 0
    value = 0

    # Split the board into row and column for cross-referencing with our strategy
    newBoard = FenParser(state.fen())
    board = newBoard.parse()

    # Find King Value
    row, col = find(board, 'K')
    value += strat.getKing()[row][col]

    # Check the condition of the board and reduce score if any bad conditions are met
    #if state.is_check():
        #value -= 10
    if state.is_checkmate():
        value -= 10000
    elif state.is_stalemate():
        value -= 30
    elif state.can_claim_threefold_repetition():
        value -= 50

    # Find rook value
    try:
        row, col = find(board, 'R')
        value += strat.getRook()[row][col]
    except:
        value -= 20

    # Find night value
    try:
        row, col = find(board, 'N')
        value += strat.getNight()[row][col]
    except:
        value -= 5

    # Find enemy night value
    try:
        row, col = find(board, 'n')
    except:
        value += 18

    # Return the calculated value of the potential move
    return value


''' The heuristic for Y.  Try to optimize Y's move. '''
# Input:
#   @param state     - A single board state (based on a potential move)
# Output:
#   The value of the potential move.
def heuristicY(state):
    global strat

    # The value is initialized as 0
    value = 0

    # Split the board into row and column for cross-referencing with our strategy
    newBoard = FenParser(state.fen())
    board = newBoard.parse()

    # Find king Value
    row, col = find(board, 'k')
    value += strat.getKing()[row][col]

    # Check the condition of the board and reduce score if any bad conditions are met
    if state.is_check():
        value -= 20
    elif state.is_checkmate():
        value -= 10000
    elif state.is_stalemate():
        value -= 30
    elif state.can_claim_threefold_repetition():
        value -= 50

    # Find night value
    try:
        row, col = find(board, 'n')
        value += strat.getNight()[row][col]
    except:
        value -= 20

    # Find enemy rook
    try:
        row, col = find(board, 'R')
    except:
        value += 50

    # Find enemy night
    try:
        row, col = find(board, 'N')
    except:
        value += 15

    # Return the calculated value of the potential move
    return value



''' Takes in a boardlist (FEN format) and a piece to search for. Returns piece location in
    rank/file format. '''
# Input:
#   @param fenBoard   - Takes a board in FEN format
#   @param elem       - The element to find.
# Output:
#   Returns the row and column in the format of rank, file. 
def findPieceRankFileFormat(fenBoard, elem):
    # Enumerate the board and parse through it.
    for row, columnList in enumerate(fenBoard):
        col = 0
        for piece in columnList:
            # If the piece is found, return the row and col indexes.
            if piece == elem:
                # Convert the indexes into: letter (column) + number (row).
                row = abs(row - 7) + 1
                col = chr(col + 97)
                return row, col
            col += 1
    return -1


''' Takes in a boardlist (FEN format) and a piece to search for. Returns piece location in
    (row, col) index notation. '''
# Input:
#   @param fenBoard -   The 
def find(fenBoard, elem):
    for row, columnList in enumerate(fenBoard):
        try:
            column = columnList.index(elem)
        except ValueError:
            continue
        return row, column
    return -1


''' The main function. This runs first when the program is ran '''
def main():
    with open("config.txt","r") as ifh:
        n = int(ifh.readline())

    play(n)

# Check that it is the right main to avoid conflict with other main functions
if __name__ == "__main__":
    main()
