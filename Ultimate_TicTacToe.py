from colorama import Fore, Style

# Colours the output (X or O) such that visibility is enhanced
FORMATTED_X = Fore.RED + Style.BRIGHT + "X " + Fore.RESET + Style.RESET_ALL
FORMATTED_O = Fore.GREEN + Style.BRIGHT + "O " + Fore.RESET + Style.RESET_ALL
X_WINNER_DECLARATION = Fore.RED + Style.BRIGHT + "Won by X" + Fore.RESET + Style.RESET_ALL
O_WINNER_DECLARATION = Fore.GREEN + Style.BRIGHT + "Won by O" + Fore.RESET + Style.RESET_ALL
DRAW_DECLARATION = Fore.BLUE + Style.BRIGHT + " Drawn " + Fore.RESET + Style.RESET_ALL

UTT_BOARD = '''
      Board 1        |       Board 2        |        Board 3
                     |                      | 
      |     |        |       |     |        |        |     |    
   a1 |  a2 |  a3    |    b1 |  b2 |  b3    |     c1 |  c2 |  c3  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
   a4 |  a5 |  a6    |    b4 |  b5 |  b6    |     c4 |  c5 |  c6  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
   a7 |  a8 |  a9    |    b7 |  b8 |  b9    |     c7 |  c8 |  c9  
      |     |        |       |     |        |        |     |
_____________________|______________________|______________________
                     |                      |
      Board 4        |       Board 5        |        Board 6
                     |                      | 
      |     |        |       |     |        |        |     |    
   d1 |  d2 |  d3    |    e1 |  e2 |  e3    |     f1 |  f2 |  f3  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
   d4 |  d5 |  d6    |    e4 |  e5 |  e6    |     f4 |  f5 |  f6  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
   d7 |  d8 |  d9    |    e7 |  e8 |  e9    |     f7 |  f8 |  f9  
      |     |        |       |     |        |        |     |
_____________________|______________________|______________________
                     |                      |
      Board 7        |       Board 8        |        Board 9
                     |                      | 
      |     |        |       |     |        |        |     |    
   g1 |  g2 |  g3    |    h1 |  h2 |  h3    |     i1 |  i2 |  i3  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
   g4 |  g5 |  g6    |    h4 |  h5 |  h6    |     i4 |  i5 |  i6  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
   g7 |  g8 |  g9    |    h7 |  h8 |  h9    |     i7 |  i8 |  i9  
      |     |        |       |     |        |        |     |      
'''

def check_set_winner(y: set):
    if (y.issuperset({1, 2, 3})):
        return True
    elif (y.issuperset({4, 5, 6})):
        return True
    elif (y.issuperset({7, 8, 9})):
        return True
    elif (y.issuperset({1, 4, 7})):
        return True
    elif (y.issuperset({2, 5, 8})):
        return True
    elif (y.issuperset({3, 6, 9})):
        return True
    elif (y.issuperset({1, 5, 9})):
        return True
    elif (y.issuperset({3, 5, 7})):
        return True
    else:
        return False

class Board:
    def __init__(self) -> None:
        self.x = set()
        self.o = set()
        self.draws = set() #exclusive to big_board
    
    def check_winner(self):
        if check_set_winner(self.x):
            return 'X'
        
        elif check_set_winner(self.o):
            return 'O'
        
        else:
            if (self.x).union(self.o).union(self.draws) == {i for i in range(1, 10)}:
                return 'Draw'
            # for miniboards, self.draws is empty and doesn't affect anything
            # for the big board, it takes drawn miniboards into account

            elif (self.draws).issuperset({1, 5, 9}) or (self.draws).issuperset({3, 5, 7}):
                return 'Draw'
            
            else:
                return 'Playable Board'


def main():
    def update_big_board():
    # This function updates both the Board object big_board for checking result
    # as well as the str playing_board for enhanced visibility
    # nonlocal keyword used as the variables are inside main(), not global scope

        nonlocal miniboard_tracker, big_board, playing_board

        for board_number, actual_board in miniboard_tracker.items():
            result = actual_board.check_winner()
            if result == 'X':
                big_board.x.add(board_number)
                playing_board = playing_board.replace(f"Board {board_number} ", X_WINNER_DECLARATION)
            
            elif result == 'O':
                big_board.o.add(board_number)
                playing_board = playing_board.replace(f"Board {board_number} ", O_WINNER_DECLARATION)
            
            elif result == 'Draw':
                big_board.draws.add(board_number)
                playing_board = playing_board.replace(f"Board {board_number}", DRAW_DECLARATION)


    def game_over():
        nonlocal big_board
        update_big_board()
        if big_board.check_winner() != "Playable Board":
            return True
        
        else:
            return False


    print("While inputting, player1 plays first, player2 goes next.")
    PLAYER_X = input("Enter player1: ") # X
    PLAYER_O = input("Enter player2: ") # O
    print(f"{PLAYER_X}, you play X. {PLAYER_O}, you play O.")

    playing_board = UTT_BOARD
    big_board = Board()

    # ASCII values: a = 97 = 96 + 1 ; i = 105 = 96 + 9
    # we want key-value pairs like {"a": 1, "b": 2, ..., "i": 9}
    move_to_board_mapping = {chr(96 + i): i for i in range(1, 10)}

    miniboard_tracker: dict[int, Board] = {}
    for i in range(1, 10):
        miniboard_tracker[i] = Board() # board number : board pairs

    # There are no do-while loops in Python, so we put this outside the loop
    print(playing_board)
    x_move = input(f"{PLAYER_X}, enter the coordinate to play your piece: ").strip().lower()
    # strip -> removes whitespace added by user, if any
    # move[0] -> letter which indicates board, eg: "h6"[0] = "h" -> Board 8
    # move[1] -> integer (in string format)

    board_used: Board = miniboard_tracker[move_to_board_mapping[x_move[0]]]
    board_used.x.add(int(x_move[1]))

    board_num_redirected_to = int(x_move[1])
    playing_board = playing_board.replace(x_move, FORMATTED_X)
    print(playing_board)

    while True:
        # O MOVE
        if miniboard_tracker[board_num_redirected_to].check_winner() != 'Playable Board':
            print(f"{PLAYER_O}, you may play in any board.")
            random_move = True # player may play anywhere

        else:
            print(f"{PLAYER_O}, you must play in Board {board_num_redirected_to}.")
            random_move = False # player is restricted to a board

        o_move = input(f"{PLAYER_O}, enter the coordinate to play your piece: ").strip().lower() 

        board_used_num = move_to_board_mapping[o_move[0]]
        board_used: Board = miniboard_tracker[board_used_num]
        
        # ILLEGAL MOVE IDENFITICATION
        if (not random_move) and (board_used_num != board_num_redirected_to):
            raise ValueError(f"Board in play was Board {board_num_redirected_to}. Board played in was Board {board_used_num}.")

        if (int(o_move[1]) in (board_used.x).union(board_used.o)):
            # if coordinated has already been taken
            raise ValueError(f"Coordinate {o_move} was already used in earlier moves.")

        board_used.o.add(int(o_move[1])) # marking the coordinate in the board's relevant set
        board_num_redirected_to = int(o_move[1])

        playing_board = playing_board.replace(o_move, FORMATTED_O)

        # CHECKING GAME OVER
        if game_over():
            result = big_board.check_winner()
            print(playing_board) # reference to users to see why it's a win/draw
            if result == "Draw":
                print("Game drawn.")
            
            elif result == "X":
                print(f"{PLAYER_X} won the game.")
            
            elif result == "O":
                print(f"{PLAYER_O} won the game.")

            break

        # printing playing_board after checking game_over() as the function modifies
        # the playing_board to enhance visibility if any board has a result
        print(playing_board)

        # X MOVE
        if miniboard_tracker[board_num_redirected_to].check_winner() != 'Playable Board':
            print(f"{PLAYER_X}, you may play in any board.")
            random_move = True # player may play anywhere

        else:
            print(f"{PLAYER_X}, you must play in Board {board_num_redirected_to}.")
            random_move = False # player is restricted to a board

        x_move = input(f"{PLAYER_X}, enter the coordinate to play your piece: ").strip().lower()

        board_used_num = move_to_board_mapping[x_move[0]]
        board_used: Board = miniboard_tracker[board_used_num]

        # ILLEGAL MOVE IDENITIFCATION
        if (not random_move) and (board_used_num != board_num_redirected_to):
            raise ValueError(f"Board in play was Board {board_num_redirected_to}. Board played in was Board {board_used_num}.")

        if (int(x_move[1]) in (board_used.x).union(board_used.o)):
            raise ValueError(f"Coordinate {x_move} was already used in earlier moves.")

        board_used.x.add(int(x_move[1]))
        board_num_redirected_to = int(x_move[1])

        playing_board = playing_board.replace(x_move, FORMATTED_X)

        # CHECKING GAME OVER
        if game_over():
            result = big_board.check_winner()
            print(playing_board)
            if result == "Draw":
                print("Game drawn.")
            
            elif result == "X":
                print(f"{PLAYER_X} won the game.")
            
            elif result == "O":
                print(f"{PLAYER_O} won the game.")

            break
        
        print(playing_board)

if __name__ == "__main__":
    main()
