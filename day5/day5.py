import math

def readFile():
    with open("day5/input.txt", "r") as file: # replace F, L with 0 and B, R with 1
        return [line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1").rstrip() for line in file]

def part1():
    boardingPasses = readFile()
    seatIdList = []
    for bp in boardingPasses:
        row = int(bp[0:7], 2) # convert binary to decimal
        col = int(bp[7:10], 2)
        seatIdList.append(row * 8 + col)
    print(max(seatIdList))
    return seatIdList

def part2(seatIdList):
    seatIdList.sort()
    i = seatIdList[0]
    for seatId in seatIdList:
        if (i == seatId):
            i += 1
    print(i)

seatIdList = part1()
part2(seatIdList)