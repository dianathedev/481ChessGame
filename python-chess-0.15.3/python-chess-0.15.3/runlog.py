# runlog.py

from log import LogInterface

interface = LogInterface()

interface.clear_logs()

# X makes a move and writes to log X
interface.write_to_log_X("X","K","e5")
# Y reads the move from log X
player,piece,coords = interface.user_reading_opponent_log("Y")
# Y writes the move to log Y
interface.write_to_log_Y(player,piece,coords)
# Y makes a move and writes to log Y
interface.write_to_log_Y("Y","N","f7")
# X reads from log Y
player2,piece2,coords2 = interface.user_reading_opponent_log("X")
# X writes the move to log X
interface.write_to_log_X(player2,piece2,coords2)
# X makes a move and writes to log X
interface.write_to_log_X("X","N","c2")
# Y reads the move from log X
player3,piece3,coords3 = interface.user_reading_opponent_log("Y")
# Y writes the move to log Y
interface.write_to_log_Y(player3,piece3,coords3)


interface.write_result_to_log("X","win","checkmate")
interface.write_result_to_log("Y","lose","checkmate")

print(player + " " + piece + " " + coords)
print(player2 + " " + piece2 + " " + coords2)
print(player3 + " " + piece3 + " " + coords3)
