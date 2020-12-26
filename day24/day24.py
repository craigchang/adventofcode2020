import re
from copy import deepcopy
import math
import matplotlib.pyplot as plt

REGEX = "(se|sw|nw|ne|w|e)"
DIRECTIONS = {
    "se": (0.5, -0.5), 
    "sw": (-0.5, -0.5), 
    "nw": (-0.5, 0.5), 
    "ne": (0.5, 0.5), 
    "w": (-1, 0), 
    "e": (1, 0)
}
print(DIRECTIONS.values())

def readFile():
    with open("day24/sample.txt", "r") as file:
        return [ re.findall(REGEX, line) for line in file ]

def calcNumOfAdjBlackTiles(hexMap, tempHexMap, x, y):
    numAdjBlackTiles = 0

    for i,j in DIRECTIONS.values():
        adjX, adjY = x + i, y + j
        if (adjX, adjY) in hexMap and hexMap[(adjX, adjY)] == 1:
            numAdjBlackTiles += 1
        elif (adjX, adjY) not in hexMap: # initialize edges if needed
            tempHexMap[(adjX, adjY)] = 0

    return numAdjBlackTiles

def part1():
    lines = readFile()
    hexMap = dict()
    hexMap[(0,0)] = 0
    
    for line in lines:
        x,y = 0,0
        for d in line:
            i, j = DIRECTIONS[d]
            x, y = (x + i), (y + j)
            if (x,y) not in hexMap:
                hexMap[(x, y)] = 0
        hexMap[(x,y)] = 0 if hexMap[(x,y)] == 1 else 1

    print(sum([v for v in hexMap.values() if v == 1]))
    return hexMap

def part2():
    hexMap = part1()
    day = 1

    # initialize edges of hex if any
    tempHexMap = deepcopy(hexMap)
    for k,v in hexMap.items():
        x,y = k
        for i,j in DIRECTIONS.values():
            adjX, adjY = x + i, y + j
            if (adjX, adjY) not in hexMap:
                tempHexMap[(adjX, adjY)] = 0
    hexMap = deepcopy(tempHexMap)

    while day <= 100:
        tempHexMap = deepcopy(hexMap)
        for k,v in hexMap.items():
            x,y = k
            if hexMap[(x,y)] == 1: # black tile
                numAdjBlackTiles = calcNumOfAdjBlackTiles(hexMap, tempHexMap, x, y)
                if (numAdjBlackTiles == 0 or numAdjBlackTiles > 2):
                    tempHexMap[(x,y)] = 0
            else: # white tile
                numAdjBlackTiles = calcNumOfAdjBlackTiles(hexMap, tempHexMap, x, y)
                if (numAdjBlackTiles == 2):
                    tempHexMap[(x,y)] = 1
            
        hexMap = deepcopy(tempHexMap)
        #print(f"Day {day}: {sum([v for v in hexMap.values() if v == 1])}")
        day += 1
    print(sum([v for v in hexMap.values() if v == 1]))

part2()