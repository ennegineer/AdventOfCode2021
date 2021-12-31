import csv

# Parse Data
data = []
with open('./signal.txt', 'r') as csv_data:
  # Pull in raw data as strings in a list.
    csvreader = csv.reader(csv_data, delimiter=' ')
    
    for row in csvreader:
        data.append(row)

def partOne():
    output = [11, 12, 13, 14]
    ones = 0
    fours = 0
    sevens = 0
    eights = 0

    for row in data:
        for i,ele in enumerate(row[11:15]):
            if len(ele) == 2:
                ones = ones + 1
            elif len(ele) == 4:
                fours = fours + 1
            elif len(ele) == 3:
                sevens = sevens + 1
            elif len(ele) == 7:
                eights = eights + 1
            else:
                pass
    print(f"ones: {ones} | fours: {fours} | sevens: {sevens} | eights: {eights}")
    print(ones + fours + sevens + eights)

partOne()
# Correct answer:
# ones: 75 | fours: 85 | sevens: 84 | eights: 74
# 318