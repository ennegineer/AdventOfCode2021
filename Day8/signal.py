import csv

# Parse Data
data = []
with open('./signal.txt', 'r') as csv_data:
  # Pull in raw data as strings in a list.
    csvreader = csv.reader(csv_data, delimiter=' ')
    
    for row in csvreader:
        data.append(row)
# data = [data[0]]


def sortString (input: str) -> str:
    '''Given a string, return a new string that is sorted alphabetically.'''
    input =  [letter for letter in input]
    input.sort()
    input = "".join(input)
    return input

def partOne():
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

# partOne()
# Correct answer:
# ones: 75 | fours: 85 | sevens: 84 | eights: 74
# 318

def partTwo():
    totalsum = 0

    for row in data:
        row = [sortString(digit) for digit in row]

        print("The new new", row)
        outputdigits = '0'
        L1 = ""
        L2 = ""
        L3 = ""
        L4 = ""
        L5 = ""   
        L6 = ""
        L7 = ""
        L8 = "" 
        L9 = ""
        L0 = "" 
        lenFive = []

        for i,ele in enumerate(row[0:10]):
            if len(ele) == 2:
                # both of these letters are in 3, 9, 0
                # at least one of these letters is not in 2, 5, 6
                L1 = ele 
                print(f"1: {L1}")
            elif len(ele) == 4:
                # all of these letters are in 9
                # at least some of these letters are not in2, 3, 5, 6, 0
                L4 = ele
                print(f"4: {L4}")
            elif len(ele) == 3:
                # these letters are also in 3, 9, 0
                # at least one of these letters is not in 2, 5, 6
                L7 = ele
                print(f"7: {L7}")
            elif len(ele) == 7:
                L8 = ele
                print(f"8: {L8}")
            # up to this point we would have: 1, 4, 7, 8.

        for i,ele in enumerate(row[0:10]):  
            if len(ele) == 5:
                if set(L1).issubset(set(ele)):
                    L3 = ele
                    print(f"3: {L3}") 
                elif not set(L1).issubset(set(ele)):
                    lenFive.append(row[i])
                    print(f"lenfive = {lenFive}")
            elif len(ele) == 6:
                if not set(L1).issubset(set(ele)):
                    L6 = ele
                    print(f"6: {L6}")
                elif set(L1).issubset(set(ele)):
                    if set(L4).issubset(set(ele)):    # and both letters in L1 are present, then 0
                        L9 = ele
                        print(f"9: {L9}")
                    elif not set(L4).issubset(set(ele)):     
                        L0 = ele
                        print(f"0: {L0}")
            # up to this point we would have: 0, 1, 3, 4, 6, 7, 8, 9. 

        # compare all elements in lenFive to find 2 and 5
        for i,ele in enumerate(lenFive):
            if len(set(L4).intersection(set(ele))) == 3:
                L5 = ele
                print(f"5: {L5}")
            elif len(set(ele).intersection(set(L4))) == 2:
                L2 = ele
                print(f"2: {L2}")  
            else:
                print("There is an error here.", ele)


        for i,ele in enumerate(row[11:15]):
            if ele == L0:
                outputdigits = (outputdigits + '0')
                print(F"{ele} is 0")
            if ele == L1:
                outputdigits = (outputdigits + '1')
                print(F"{ele} is 1")
            if ele == L2:
                outputdigits = (outputdigits + '2')
                print(F"{ele} is 2")
            if ele == L3:
                outputdigits = (outputdigits + '3')
                print(F"{ele} is 3")
            if ele == L4:    
                outputdigits = (outputdigits + '4')
                print(F"{ele} is 4")
            if ele == L5:
                outputdigits = (outputdigits + '5')
                print(F"{ele} is 5")
            if ele == L6:
                outputdigits = (outputdigits + '6')
                print(F"{ele} is 6")
            if ele == L7:
                outputdigits = (outputdigits + '7')
                print(F"{ele} is 7")
            if ele == L8:
                outputdigits = (outputdigits + '8')
                print(F"{ele} is 8")
            if ele == L9:
                outputdigits = (outputdigits + '9')
                print(F"{ele} is 9")
        print(int(outputdigits))
            # look at the 4 outputs and write the number based on the above.
        totalsum = totalsum + int(outputdigits)

    # print(f"ones: {ones} | fours: {fours} | sevens: {sevens} | eights: {eights}")
    print(f"totalsum = {totalsum}")
partTwo()

                # at least 3 letters are common between 2, 3, 5, 6, 8
