class ChessBoard:
   def __init__(self):
       #initialize as the first board
       self.new_board = True
       self.board = dict()
       #variables for printing the board
       self.topbottom=['*','a','b','c','d','e','f','g','h','*']
       self.sides=['1','2','3','4','5','6','7','8']
       self.tbspacer=' '*6
       self.rowspacer=' '*5
       self.cellspacer=' '*4
       self.empty=' '*3
       
   
   def setupBoard(self):
       
       #If it's the first board, initialize the positions
       if self.new_board:
           #Player X pieces
           self.board[(0,4)] = 'K'
           self.board[(0,7)] = 'R'
           self.board[(0,6)] = 'KN'

           #Player Y pieces
           self.board[(7,4)] = 'k'
           self.board[(7,2)] = 'kn'
           
           self.new_board = False

       #print top A-H columns
       for field in self.topbottom:
           print(("%4s") % field, end=' ')
       print('')
       
       #print the top of the board
       print(self.tbspacer+("_"*4+' ')*8)
       
        #print the rest of the board
       for row in range(8):
           #print the row numbers on the left
           print(("%4s") % self.sides[row], end=' ')
           #print the left edge of the board
           print('|', end=' ')
           
           #print the piece in the square if there is one and print the straight edges of the squares
           for col in range(8):
               if (row, col) not in self.board:
                   print((self.empty+'|'), end=' ')
               else:
                   print(("%2s") % self.board[(row, col)], end=' ')
                   print('|', end=' ')
                   
           #print the row numbers on the right
           print(("%2s") % self.sides[row])
           print
           #print a straight edge of the square and the horizontal edges of the squares
           print(self.rowspacer+'|'+(("_"*4+'|')*8), end=' ')
           print('')
       print('')
       
       #print the bottom A-H columns
       for field in self.topbottom:
           print(("%4s") % field, end=' ')
