# Parse Data
data = []
with open('./crabbies.txt') as csv_data:
  # Pull in raw data as strings in a list.
  data = [int(value) for value in next(csv_data).split(',')]

def partOne():
  fuel = 0
  leastfuel = 400000

  for i in range(len(data)):
    fuel = 0
    for pos in data:
      fuel = fuel + abs(pos - data[i])
    if fuel < leastfuel:
      leastfuel = fuel

  print(leastfuel)
  # 340987 is correct

def partTwo():
  # the fuel for the distance between two spaces is that distance + every number below it

  distance = 0
  leastfuel = 100000000000

  def distfuel(distance):
    x = 0
    for i in range(distance + 1):
      x = x + i
    return x


  for i in range(len(data)):
    fuel = 0
    distance = 0
    for pos in data:
      distance = abs(pos - i)
      fuel = fuel + distfuel(distance)
      # fuel = fuel + (.5*(distance-1)*distance)
    if fuel < leastfuel:
      leastfuel = fuel

  print(leastfuel)
  # 290863999 is too high
  # 290176080 is too high
  #  96991009 is too high
  #  96987874 is pepega solution
partTwo()