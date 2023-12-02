test_case = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

x = test_case.splitlines()
print(x)
game_maxes = dict()
for game in x:
  temp_game = game.split(":")
  game_num = int(temp_game[0].strip("Game "))
  game_itters = temp_game[1].split(";")
  game_maxes[game_num]={"r":0,"g":0,"b":0}
  for itter in game_itters:
    temp_itter = itter.split(",")
    #print(temp_itter)
    for cube in temp_itter:
      temp_cube = cube.split(" ")
      #print(temp_cube)
      if int(temp_cube[1]) > game_maxes[game_num][temp_cube[2][0]]:
        game_maxes[game_num][temp_cube[2][0]] = int(temp_cube[1]) 
  #print(game_num, game_itters)
print(game_maxes)
red_cubes = 12
green_cubes = 13
blue_cubes = 14
total = 0
for k, v in game_maxes.items():
  if int(v.get("r")) <= red_cubes and v.get("g") <= green_cubes and v.get("b") <= blue_cubes:
    total = total + k

print(total)
