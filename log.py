#!/usr/bin/python
# Author: Eric Roe
# Comments still need to be added, but here is a brief introduction.

# Description:
#   This currently handles reading and writing to the log text file. It doesn't have any checking to make sure the
#   file successfully opens. Reading from a file with improper format (outlined below) will not break anything,
#   but it will not split the content up correctly.

# Future additions:
#   None

# TEXT FILE FORMAT:
#   The text file has the format "number player:piece:coords" where:
#       number      is 1 and is incremented each line
#       player      is X or Y
#       piece       is K for King, N for Knight, or R for Rook
#       coords      is in the format of "rank" + "file" -> a1

# ex: log_X.txt
"""
1 X:K:g2
2 Y:K:e7
3 X:N:f3
4 Y:N:a6
5 X:R:a3 
"""

# ex: log_Y.txt
"""
1 X:K:g2
2 Y:K:e7
3 X:N:f3
4 Y:N:a6
5 X:R:a3
6 NEXT MOVE
"""

# HOW IT WORKS:
#   Player X writes to log_X.txt and reads from log_Y.txt
#   Player Y writes to log_Y.txt and reads from log_X.txt

import re
import sys

class LogInterface:
    def __init__(self):
        self.log_X = "log_X.txt"
        self.log_Y = "log_Y.txt"
        self.line_X = 1
        self.line_Y = 1

        # Try to open the log file for X. If it does not exist (first time run),
        # it will be created. Otherwise, it confirms success.
        with open(self.log_X,"a+") as f:
            pass

        # Try to open the log file for Y. If it does not exist (first time run),
        # it will be created. Otherwise, it confirms success.
        with open(self.log_Y,"a+") as f:
            pass


    '''Clear the log values'''
    # Empties the logs.
    def clear_logs(self):
        with open(self.log_X,"w") as f:
            f.write("")
        with open(self.log_Y,"w") as f:
            f.write("")


    ''' For writing to the log'''
    #   @param player   - The current player, X or Y. This is needed to tell us which
    #                     file we should be writing to, log_X.txt or log_Y.txt.
    #   @param piece    - The piece being moved.
    #   @param coords   - The new coordinates to write.
    def write_to_log_X(self, player, piece, coords):
        new_line = str(self.line_X) + " " + player + ":" + piece + ":" + coords + "\n"
        self.line_X += 1

        with open(self.log_X, "a") as f:
            f.write(new_line)


    ''' For writing to the log'''
    #   @param player   - The current player, X or Y. This is needed to tell us which
    #                     file we should be writing to, log_X.txt or log_Y.txt.
    #   @param piece    - The piece being moved.
    #   @param coords   - The new coordinates to write.
    def write_to_log_Y(self, player, piece, coords):
        new_line = str(self.line_Y) + " " + player + ":" + piece + ":" + coords + "\n"
        self.line_Y += 1

        with open(self.log_Y, "a") as f:
            f.write(new_line)


    ''' For reading from the logs'''
    #   @param player   - The current player, X or Y. This is needed to tell us which
    #                     file we should be writing to, log_X.txt or log_Y.txt.
    def user_reading_opponent_log(self, player):
        file_lines = []
        RE_line = ""
        pattern = re.compile(r" |:|\n")
        
        if player == "Y":
            with open(self.log_X, "r") as f:
                for line in f:
                    file_lines.append(line)


        elif player == "X":
            with open(self.log_Y, "r") as f:
                for line in f:
                    file_lines.append(line)
            
        # Split the final line into its parts: player, piece, coords
        RE_line = pattern.split(file_lines[-1])
        # Remove the newline
        if RE_line[-1] is "\n":
            del RE_line[1]
       
        # Return 3 variables: player, piece, coords (end location)
        return RE_line[1],RE_line[2],RE_line[3]


    ''' For writing the final result'''
    #   @param player   - The current player, X or Y. This is needed to tell us which
    #                     file we should be writing to, log_X.txt or log_Y.txt.
    #   @param result   - The result for this player. Will be one of: 
    #                     ['win', 'lose', 'tie']
    #   @param reason   - Why we are writing this result. Will be one of:
    #                     ['checkmate', 'stalemale', 'maximum # of moves reached']
    def write_result_to_log(self, player, result, reason):
        last_line = result + ": " + reason
        
        if player == "X":
            # Open the log file for X for appending.
            with open(self.log_X,"a+") as f:
                f.write(last_line)

        elif player == "Y":
            # Open the log file for Y for appending.
            with open(self.log_Y,"a+") as f:
                f.write(last_line)







