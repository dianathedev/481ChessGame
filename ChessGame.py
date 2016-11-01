# Input: Maximum number of turns
# Output: Checkmate or Stalemate
# Drives the game forward.
def play(n):
	turn = input("Which player are you?(X/Y)")
	setupBoard()
	for i in range(n):
		if (turn == 'X' and n > 0) or turn == 'Y':
			showOpponentMove(turn)
		#Check for Checkmate/Stalemate here?
		moves = #Generate tree of possible moves
		if turn == 'X':
			mov = heuristicX(moves)
		elif turn == 'Y':
			mov = heuristicY(moves)
		move(mov)


# Input: Yourself(X or Y), Next Move
# Output: None?
# Calls showMove and updates board state.
def move(turn, mov):
	player = turn
	piece = #Find piece based on mov
	coords = #Find coords based on mov
	showMove(turn, player, piece, coords)


# Input: Yourself(X or Y), Player whose move you are showing, Piece moved, New coordinate of piece.
# Output: None?
# Updates gameboard and log
def showMove(turn, player, piece, coords):
	write_to_screen(player, piece, coords)

	if turn == 'X':
		#update log X
	elif turn == 'Y':
		#update log Y


# Input: Tree of possible moves, depth of 3?
# Output: Best move
# Uses X heuristic and mini-max to determine the best move.
def heuristicX(moves):

# Input: Tree of possible moves, depth of 3?
# Output: Best move
# Uses Y heuristic and mini-max to determine the best move.
def heuristicY(moves):

# Input: Yourself(X or Y)
# Output: None?
# Updates board and log with opponents last move.
def showOpponentMove(turn):
	player, piece, coords = read_from_log(turn)
	showMove(turn, player, piece, coords)

# Input: Yourself(X or Y)
# Output: Player who last made a move, Piece moved, New coordinates of piece
# Reads the opponents log and returns details of their new move.
def read_from_log(turn):

# Input: Player who made move, Piece moved, New coordinates of piece
# Output: None
# Update the on screen board with new move.
def write_to_screen(player, piece, coords):

# Input: None
# Output: None
# Setup Board with initial chess positions.
def setupBoard():
	#Use API to set board with initial positions.