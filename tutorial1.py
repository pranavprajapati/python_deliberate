import itertools


game = [[0,0,0],
        [0,0,0],
        [0,0,0],]


def win(current_game):

  def all_same(l):
    if l.count(l[0]) == len(l) and l[0] != 0:
      return True
    else:
      return False

    
  # ROW WINNER
  for row in game:
    print(row)
    if all_same(row):
      print(f"Player {row[0]} is Horizontal Winner")
      return True

  # VERTICAL WINNER

  for col in range(len(game)):
    check = []

    for row in game:
      check.append(row[col])

  if all_same(check):
    print(f"Player {row[0]} is Vertical Winner(|)")
    return True


  # DIAGONAL WINNER
  diags = []
  for col,row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])
  if all_same(diags):
      print(f"Player {diags[0]} is Diagonal Winner (/)!")
      return True

  diags = []
  for ix in range(len(game)):
    diags.append(game[ix][ix])
  if all_same(diags):
      print(f"Player {diags[0]} is Diagonal Winner (\\)!")
      return True
  
  return False


def game_board(game_map,player=0,row=0,column=0,just_display= False):
  
  try:
    if game_map[row][column] != 0:
      print("Occupied! Choose another")
      return game_map,False

    print("  " + "  ".join([str(i) for i in range(len(game_map))]))
    if not just_display:
      game_map[row][column] = player
    for count, row in enumerate(game_map):
      print(count,row)
    return game_map, True
  except IndexError as e:
    print("Error:Something went wrong!!",e)
    return game_map,False
  except Exception as e:
    print("Kuch toh problem hai!",e)
    return game_map,False
  
play = True
players = [1,2]

while play:
  
  game_size = int(input("Size of TTT: "))
  game = [[0 for i in range(game_size)] for i in range(game_size)]
  
  game_won = False
  game, _ =  game_board(game,just_display= True)
  player_choice = itertools.cycle([1,2])

  while not game_won:

    current_player = next(player_choice)
    print(f"Current player: {current_player}")
    played = False 

    while not played:

      column_choice = int(input("What column you want (0,1,2): "))
      row_choice = int(input("What row you want (0,1,2): "))

      game, played = game_board(game,current_player,row_choice,column_choice)

    if win(game):
      game_won = True
      again = input("Play again ? (y/n)")

      if again.lower() == "y":
        print("Restarting")

      elif again.lower() == "n":
        print("Bye")
        play = False

      else:
        print("Not a valid answer!")
        play = False
