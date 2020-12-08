import re

def readFile(): # returns map of bags and its contents
    with open("day7/input.txt", "r") as file:
        bagsDict = dict()
        for line in file:
            groups = re.findall("(\\d?)\\s?(\\w* \\w*) bag[s]?", line.rstrip())
            bagsDict[groups[0][1]] = None if groups[1][1] == "no other" else groups[1:] # store as tuples, None if no bags
        return bagsDict

def part1():
    bagsDict = readFile()
    num = 0
    for contents in bagsDict.values(): # loop through each bag in a bag
        if contents is None: 
            continue
        queue = contents.copy() # avoid deep referencing
        while len(queue) > 0:
            color = queue.pop(0)[1]
            if bagsDict[color] is not None:
                if color == "shiny gold":
                    num += 1
                    break
                else:
                    queue += bagsDict[color]
    print(num)

def calculateQty(color, bagsDict):
    if bagsDict[color] is None: # base case (bag has no other bag)
        return 0
    else: # recursive case, bag has one to many bags
        totalQty = 0
        for qty, bag in bagsDict[color]:
            totalQty += int(qty) + int(qty) * calculateQty(bag, bagsDict)
        return totalQty

def part2():
    print(calculateQty("shiny gold", readFile()))


part1()
part2()