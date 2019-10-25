def ninetyNineBottles(bottles):
  if bottles == 2:
    print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer.\nTake one down and pass it around, " + str(bottles-1) + " bottle of beer on the wall.\n")
    # ninetyNineBottles(bottles-1)
  elif bottles == 1:
    print(str(bottles) + " bottle of beer on the wall, " + str(bottles) + " bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n")

  elif bottles == 0:
    print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n")

  elif bottles > 2:
    print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer.\nTake one down and pass it around, " + str(bottles-1) + " bottles of beer on the wall.\n")
  elif bottles < 0: 
    return False

  ninetyNineBottles(bottles-1)

ninetyNineBottles(99)

# working code tested here: https://repl.it/repls/RobustCapitalTrees