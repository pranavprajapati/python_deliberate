
game = [[0,0,0],[0,0,0],[0,0,0],]

    
def game_board(game_map,player=0,row=0,column=0,just_display= False):
  try:

    print("   0  1  2")
    if not just_display:
      game_map[row][column] = player
    for count, row in enumerate(game_map):
      print(count,row)
    return game_map
  except IndexError as e:
    print("Error:Something went wrong!!",e)
  except Exception as e:
    print("Kuch toh problem hai",e)
  

game =  game_board(game,just_display= True)
game = game_board(game_board,player=1,row=3,column=1)


 