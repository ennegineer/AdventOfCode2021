import os
import csv

file = os.path.join('.', 'input.txt')

oxbinary = []
cobinary = []
with open(file, 'r') as input:
    csvreader = csv.reader(input)
    
    for row in csvreader:
        oxbinary.append(row)
        cobinary.append(row)
        # print(row)
print(len(oxbinary))
print(len(cobinary))

oxygen = ''
zero = 0
one = 0
    
# from 0 to end of rows, 0, 0 to 12
for i in range(12):
    print(len(oxbinary))
    zero = 0
    one = 0
    for row in oxbinary:
        if row[0][i] == '0':
            zero = zero + 1
        else:
            one = one + 1
    if zero > one:
        print(f"oxygen {i + 1} is 0")
        oxygen = oxygen + '0'
    elif zero < one:
        print(f"oxygen {i + 1} is 1")  
        oxygen = oxygen + '1'
    else:
        print(f"oxygen {i + 1} is 1")  
        oxygen = oxygen + '1' 
    for row in oxbinary:        
        if zero > one:
            if row[0][i] == '1' and len(oxbinary) > 1:
                oxbinary.remove(row)
        elif zero < one:
            if row[0][i] == '0' and len(oxbinary) > 1:
                oxbinary.remove(row)
        else:
            if row[0][i] == '0' and len(oxbinary) > 1:
                oxbinary.remove(row)
    print(len(oxbinary))
    print(f" ")
print(f"oxygen: {oxygen}")
print(oxbinary)