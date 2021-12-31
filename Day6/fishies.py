from collections import defaultdict

# Parse Data
data = []
with open('./fish.txt') as csv_data:
  # Pull in raw data as strings in a list.
  data = [int(value) for value in next(csv_data).split(',')]

def partone():
    days = 80
    fishies = data.copy()
    fish = len(fishies)
    # print(len(testInput))
    # print(fish)

    # Lanternfish reproduction cycle
    #   each day, every number decreases by 1
    #   any 0 becomes a 6 and adds a new 8 to the list

    for day in range(days):
        for i in range(fish):
            if fishies[i] > 0:
                fishies[i] = fishies[i] - 1
            elif fishies[i] == 0:
                fishies[i] = 6
                fishies.append(8)
            fish = len(fishies)
        # print(f"At day {day} there are {len(testInput)} fish.")
    print(f"part one: At day {day + 1} there are {len(fishies)} fish.")
        # input = [fish-1 for fish in testInput if fish>0]

def parttwo():
    allFish = data.copy()
    DAYS = 256
    fishMap = {}
    for fish in allFish:
        if fish not in fishMap:
            fishMap[fish] = 0
        fishMap[fish] += 1

    for day in range(DAYS):
        updatedFishMap = defaultdict(int)

        for fish, count in fishMap.items():
            if fish == 0:
                updatedFishMap[6] += count
                updatedFishMap[8] += count
            else:
                updatedFishMap[fish-1] += count
            
            fishMap = updatedFishMap

    print(f"part two: At day 256 there are {sum(fishMap.values())} fish.")
    return(sum(fishMap.values()))

partone()
parttwo()