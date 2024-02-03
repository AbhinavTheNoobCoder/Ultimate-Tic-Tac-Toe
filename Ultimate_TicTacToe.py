from colorama import Fore, Back, Style, init
init(autoreset=True)

sample_small_board = '''
      |     |    
   a1 |  b1 |  c1  
 _____|_____|_____
      |     |    
   a2 |  b2 |  c2  
 _____|_____|_____
      |     |    
   a3 |  b3 |  c3  
      |     |    
'''

def Winner(small_board):
   set_x = set()
   set_o = set()
   for index, character in enumerate(small_board):
      if character != sample_small_board[index]:
         if character == "X":
            set_x.add(sample_small_board[index: index+2])
         elif character == "O":
            set_o.add(sample_small_board[index: index+2])
   
   if set_x.issuperset({"a1","a2","a3"}):
      return "X"
   elif set_x.issuperset({"b1","b2","b3"}):
      return "X"
   elif set_x.issuperset({"c1","c2","c3"}):
      return "X"
   elif set_x.issuperset({"a1","b1","c1"}):
      return "X"
   elif set_x.issuperset({"a2","b2","c2"}):
      return "X"
   elif set_x.issuperset({"a3","b3","c3"}):
      return "X"
   elif set_x.issuperset({"a1","b2","c3"}):
      return "X"
   elif set_x.issuperset({"c1", "b2", "a3"}):
      return "X"
   
   elif set_o.issuperset({"a1","a2","a3"}):
      return "O"
   elif set_o.issuperset({"b1","b2","b3"}):
      return "O"
   elif set_o.issuperset({"c1","c2","c3"}):
      return "O"
   elif set_o.issuperset({"a1","b1","c1"}):
      return "O"
   elif set_o.issuperset({"a2","b2","c2"}):
      return "O"
   elif set_o.issuperset({"a3","b3","c3"}):
      return "O"
   elif set_o.issuperset({"a1","b2","c3"}):
      return "O"
   elif set_o.issuperset({"c1", "b2", "a3"}):
      return "O"
   else:
      for i in ["a", "b", "c"]:
         if i in small_board:
            return True
      return "Draw"

def Result(winners_dictionary):
   j = 1
   for player in winners_dictionary:
      if j == 1:
         x_boards = winners_dictionary[player]
      if j == 2:
         o_boards = winners_dictionary[player]
      j += 1

   if x_boards.issuperset({"A1","A2","A3"}):
      return "X"
   elif x_boards.issuperset({"B1","B2","B3"}):
      return "X"
   elif x_boards.issuperset({"C1","C2","C3"}):
      return "X"
   elif x_boards.issuperset({"A1","B1","C1"}):
      return "X"
   elif x_boards.issuperset({"A2","B2","C2"}):
      return "X"
   elif x_boards.issuperset({"A3","B3","C3"}):
      return "X"
   elif x_boards.issuperset({"A1","B2","C3"}):
      return "X"
   elif x_boards.issuperset({"C1", "B2", "A3"}):
      return "X"
   
   elif o_boards.issuperset({"A1","A2","A3"}):
      return "O"
   elif o_boards.issuperset({"B1","B2","B3"}):
      return "O"
   elif o_boards.issuperset({"C1","C2","C3"}):
      return "O"
   elif o_boards.issuperset({"A1","B1","C1"}):
      return "O"
   elif o_boards.issuperset({"A2","B2","C2"}):
      return "O"
   elif o_boards.issuperset({"A3","B3","C3"}):
      return "O"
   elif o_boards.issuperset({"A1","B2","C3"}):
      return "O"
   elif o_boards.issuperset({"C1", "B2", "A3"}):
      return "O"

def UltimateTTT(player1, player2):
   big_board = '''
      Board A1       |       Board B1       |        Board C1
                     |                      | 
      |     |        |       |     |        |        |     |    
   a1 |  b1 |  c1    |    a4 |  b4 |  c4    |     a7 |  b7 |  c7  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
   a2 |  b2 |  c2    |    a5 |  b5 |  c5    |     a8 |  b8 |  c8  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
   a3 |  b3 |  c3    |    a6 |  b6 |  c6    |     a9 |  b9 |  c9  
      |     |        |       |     |        |        |     |
_____________________|______________________|______________________
                     |                      |
      Board A2       |       Board B2       |        Board C2
                     |                      | 
      |     |        |       |     |        |        |     |    
  A10 | B10 | C10    |   A13 | B13 | C13    |    A16 | B16 | C16  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
  A11 | B11 | C11    |   A14 | B14 | C14    |    A17 | B17 | C17  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
  A12 | B12 | C12    |   A15 | B15 | C15    |    A18 | B18 | C18  
      |     |        |       |     |        |        |     |
_____________________|______________________|______________________
                     |                      |
      Board A3       |       Board B3       |        Board C3
                     |                      | 
      |     |        |       |     |        |        |     |    
  A19 | B19 | C19    |   A22 | B22 | C22    |    A25 | B25 | C25  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
  A20 | B20 | C20    |   A23 | B23 | C23    |    A26 | B26 | C26  
 _____|_____|_____   |  _____|_____|_____   |   _____|_____|_____
      |     |        |       |     |        |        |     |    
  A21 | B21 | C21    |   A24 | B24 | C24    |    A27 | B27 | C27  
      |     |        |       |     |        |        |     |                                                 
'''
   list_of_boards = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
   dict_of_boards = {}.fromkeys(list_of_boards,
   '''
      |     |    
   a1 |  b1 |  c1  
 _____|_____|_____
      |     |    
   a2 |  b2 |  c2  
 _____|_____|_____
      |     |    
   a3 |  b3 |  c3  
      |     |    
''')
   dict_of_wins = {player1: set(), player2: set()}

   print(big_board)
   print(f"{player1} is playing as X.") #First player is X
   print(f"{player2} is playing as O.") #Second player is O

   initial_board = input(f"{player1}, enter the board where you want to start: ").upper() #initial move of the game

   player1_move = input("Enter the coordinate where you want to place the piece: ")
   big_board = big_board.replace(player1_move, Fore.RED + Style.BRIGHT + " X " + Fore.RESET + Style.RESET_ALL)\
      if len(player1_move) == 3 else big_board.replace(player1_move, Fore.RED + Style.BRIGHT + "X " + Fore.RESET + Style.RESET_ALL)

   relative_player1_move = f"{player1_move[0].lower()}{int(player1_move[1:])%3}" #used to determine next_board
   if "0" in relative_player1_move:
      relative_player1_move = relative_player1_move.replace("0", "3") #example c18 = c{18%3} = c0 = c3
   
   dict_of_boards[initial_board] = dict_of_boards[initial_board].replace(relative_player1_move, "X ")
   print(big_board)

   while True:
      next_board = relative_player1_move.upper() #example: a19 = a{19%3} = a1 = Board A1 

      if Winner(dict_of_boards[next_board]) != "X" and Winner(dict_of_boards[next_board]) != "O" and Winner(dict_of_boards[next_board]) != "Draw": #no winner there
         print(f"{player2}, you are forced to play in Board {next_board}.")
      else:
         print(f"{player2}, you may play in any board.")
         next_board = input("Enter the board where you want to play: ").upper()

      player2_move = input("Enter the coordinate where you want to place the piece: ")
      big_board = big_board.replace(player2_move, Fore.GREEN + Style.BRIGHT + " O " + Fore.RESET + Style.RESET_ALL)\
      if len(player2_move) == 3 else big_board.replace(player2_move, Fore.GREEN + Style.BRIGHT + "O " + Fore.RESET + Style.RESET_ALL) #to maintain aesthetic

      relative_player2_move = f"{player2_move[0].lower()}{int(player2_move[1:])%3}" #same logic as previous one
      if "0" in relative_player2_move:
         relative_player2_move = relative_player2_move.replace("0", "3")

      dict_of_boards[next_board] = dict_of_boards[next_board].replace(relative_player2_move, "O ")

      for miniboard in list_of_boards:
         if Winner(dict_of_boards[miniboard]) == "X" or Winner(dict_of_boards[miniboard]) == "O":
            colour = Fore.RED if Winner(dict_of_boards[miniboard]) == "X" else Fore.GREEN
            winner = colour + Style.BRIGHT + f"Won by {Winner(dict_of_boards[miniboard])}" + Fore.RESET + Style.RESET_ALL
            big_board = big_board.replace(f"Board {miniboard}", winner) #winner of miniboard is visible
         elif Winner(dict_of_boards[miniboard]) == "Draw":
            winner = Style.BRIGHT + "  Draw  " + Style.RESET_ALL
            big_board = big_board.replace(f"Board {miniboard}", winner)
         if Winner(dict_of_boards[miniboard]) == "X":
            dict_of_wins[player1].add(miniboard)
         elif Winner(dict_of_boards[miniboard]) == "O":
            dict_of_wins[player2].add(miniboard)
      
      print(big_board)

      if Result(dict_of_wins) == "X":
         print(f"Game won by {player1}.")
         break
      elif Result(dict_of_wins) == "O":
         print(f"Game won by {player2}.")
         break
      else:
         if "a" not in big_board and "b" not in big_board and "c" not in big_board:
            print("Game drawn.")
            break

      next_board = relative_player2_move.upper()
      
      if Winner(dict_of_boards[next_board]) != "X" and Winner(dict_of_boards[next_board]) != "O": #no winner there
         print(f"{player1}, you are forced to play in Board {next_board}.")
      else:
         print(f"{player1}, you may play in any board.")
         next_board = input("Enter the board where you want to play: ").upper()

      player1_move = input("Enter the coordinate where you want to place the piece: ")
      big_board = big_board.replace(player1_move, Fore.RED + Style.BRIGHT + " X " + Fore.RESET + Style.RESET_ALL)\
      if len(player1_move) == 3 else big_board.replace(player1_move, Fore.RED + Style.BRIGHT + "X " + Fore.RESET + Style.RESET_ALL)

      relative_player1_move = f"{player1_move[0].lower()}{int(player1_move[1:])%3}"
      if "0" in relative_player1_move:
         relative_player1_move = relative_player1_move.replace("0", "3")

      dict_of_boards[next_board] = dict_of_boards[next_board].replace(relative_player1_move, "X ")

      for miniboard in list_of_boards:
         if Winner(dict_of_boards[miniboard]) == "X" or Winner(dict_of_boards[miniboard]) == "O":
            colour = Fore.RED if Winner(dict_of_boards[miniboard]) == "X" else Fore.GREEN
            winner = colour + Style.BRIGHT + f"Won by {Winner(dict_of_boards[miniboard])}" + Fore.RESET + Style.RESET_ALL
            big_board = big_board.replace(f"Board {miniboard}", winner) #winner of miniboard is visible
         elif Winner(dict_of_boards[miniboard]) == "Draw":
            winner = Style.BRIGHT + "  Draw  " + Style.RESET_ALL
            big_board = big_board.replace(f"Board {miniboard}", winner)
         if Winner(dict_of_boards[miniboard]) == "X":
            dict_of_wins[player1].add(miniboard)
         elif Winner(dict_of_boards[miniboard]) == "O":
            dict_of_wins[player2].add(miniboard)
      
      print(big_board)

      if Result(dict_of_wins) == "X":
         print(f"Game won by {player1}.")
         break
      elif Result(dict_of_wins) == "O":
         print(f"Game won by {player2}.")
         break
      else:
         for l in ["A", "B", "C", "a", "b", "c"]:
            if l in big_board:
               break
         else:
            print("Game drawn.")
            break

def main():
   import random
   a = input("Enter first player name: ")
   b = input("Enter second player name: ")
   playerlist = [a,b]
   first_to_play = random.choice(playerlist)
   playerlist.remove(first_to_play)
   second_to_play = playerlist[0]
   UltimateTTT(first_to_play, second_to_play)

if __name__ == "__main__":
   main()