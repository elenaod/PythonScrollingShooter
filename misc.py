# define some constants
SIZE = 10
MAX_HEALTH = 10
TIMER = 5

def outside_of_board(x, y):
    return x < 0 or y < 0 or x >= SIZE or y >= SIZE

def valid(x, y, board):
    return not outside_of_board(x, y) and board.rows[x][y] == None           

def get_command_console():
    command = input(">:")
    command = command[0]
    if command == 'a':
        return "move_player_left"
    elif command == 'd':
        return "move_player_right"
    elif command == 'w':
        return "move_player_up"
    elif command == 'x':
        return "move_player_down"
    if command == 's':
        return "player_shoot"
    if command == 'q':
        return "game_stop"
