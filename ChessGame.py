import chess

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
		if (turn == 'X' and n > 0) or turn == 'Y': # X doesnt showopponentmove on his first turn
			showOpponentMove(turn)

		if board.isCheckMate() or board.isStalemate(): #if checkmate or stalemate are true then break from the loop
			#update Log file
			break
		#moves = generateMoves(board) #Generate tree of possible moves
		if turn == 'X':
			mov = heuristicX(board)
		elif turn == 'Y':
			mov = heuristicY(board)
		move(turn, mov, board)


# Input: Yourself(X or Y), Next Move
# Output: None?
# Calls showMove and updates board state.
def move(turn, mov, board):
	board.push_uci(mov)
	player = turn
	piece = #Find piece based on mov
	coords = #Find coords based on mov
	showMove(turn, player, piece, coords, board)


# Input: Yourself(X or Y), Player whose move you are showing, Piece moved, New coordinate of piece.
# Output: None?
# Updates gameboard and log
def showMove(turn, player, piece, coords, board):
	board

	if turn == 'X':
		#update log X
	elif turn == 'Y':
		#update log Y


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
			value = #TODO use state to determine heuristicX value
			if value < point:
				point = value
			board.pop()
		board.pop()
		item.points = point
	maxPoints = float("-inf")
	bestMove = None
	for x in tree
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
			value = #TODO use state to determine heuristicY value
			if value < point:
				point = value
			board.pop()
		board.pop()
		item.points = point
	maxPoints = float("-inf")
	bestMove = None
	for x in tree
		if x.points > maxPoints:
			maxPoints = x.points
			bestMove = x.move
	return bestMove

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
def write_to_screen(board):
	board

# Input: None
# Output: None
# Setup Board with initial chess positions.
def setupBoard():
	return chess.Board(fen='2n1k3/8/8/8/8/8/8/4K1NR 2 KQkq - 0 1', chess960=False)

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