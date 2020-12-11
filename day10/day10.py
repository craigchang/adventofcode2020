from itertools import combinations
from itertools import groupby
from math import factorial

def readFile():
    with open("day10/input.txt", "r") as file:
        return [int(x) for x in file]

def calcCombination(num, inc):
    count = 0
    currentLength = num - inc
    numSelected = 1

    while(currentLength - numSelected >= 0):
        count += factorial(currentLength) / (factorial(numSelected) * factorial(currentLength - numSelected))
        numSelected += 1
        currentLength -= inc
    
    return count

def part1():
    joltages = readFile()
    joltages.sort()
    joltages = [0] + joltages + [max(joltages) + 3]
    diffList = [y - x for x,y in zip(joltages[0:], joltages[1:])]
    print(diffList.count(1) * diffList.count(3))
    return diffList

def part2(diffList):
    combList = []
    for x in groupby(diffList):
        num = len(list(x[1]))
        if (x[0] == 1 and num > 1):
            combList.append(num)
    
    count = 1
    for comb in combList:
        count *= 1 if comb == 1 else int(1 + calcCombination(comb, 1) + calcCombination(comb, 2))
    print(count)

diffList = part1()
part2(diffList)