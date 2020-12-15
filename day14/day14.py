import re
from itertools import permutations
from itertools import combinations

def set_bit(val, index, bit):
    mask = 1 << index
    if (bit == 1):              
        return val | mask       # mask bits to 1, use OR
    else:                       
        return val & ~mask      # mask bits to 0, negate mask and use AND

def readFile():
    with open("day14/input.txt", "r") as file: # add boundary for looping purposes
        instructions = []        
        for line in file.readlines():
            if (line.startswith("mask")):
                mask = re.search("mask = (.+)", line.rstrip())[1]
                instructions.append(("mask", mask))
            else:
                addr, val = re.findall("mem\[(\d+)\] = (\d+)", line.rstrip())[0]
                instructions.append((int(addr), int(val)))
    return instructions

def part1():
    instructions = readFile()

    maskDict = dict()
    mem = dict()

    for addr, val in instructions:
        if (addr == "mask"): # assign new mask
            maskDict = dict()
            mask = val[::-1]
            for i in range(len(mask)):
                if mask[i] != 'X':
                    maskDict[i] = int(mask[i])
        else:
            for index, bit in maskDict.items(): # apply each mask bit that is 0 or 1 to value
                val = set_bit(val, index, bit)
            mem[addr] = val

    print(sum(mem.values()))

def part2():
    instructions = readFile()

    maskOnesList = []
    maskFloatingList = []
    mem = dict()

    for addr, val in instructions:
        if (addr == "mask"): # assign new mask
            maskOnesList = []
            maskFloatingList = []
            mask = val[::-1]
            for i in range(len(mask)): # ignore 0s
                if (mask[i] == "X"):
                    maskFloatingList.append(i)
                elif (mask[i] == "1"):
                    maskOnesList.append(i)
            numFloating = len(maskFloatingList)
            # combinations of bits for floats
            maskCombinations = [list(map(int, format(i, 'b').zfill(numFloating))) for i in range(2 ** numFloating)]
        else:
            addr = int(addr)
            for onesIndex in maskOnesList: # first apply the 1 bit override, 0 is unchanged
                addr = set_bit(addr, onesIndex, 1)

            for comb in maskCombinations: # then apply floating bits for all combiations
                combIndex = 0 
                addrTemp = addr
                for floatIndex in maskFloatingList: # apply 0 or 1 for floating bits
                    addrTemp = set_bit(addrTemp, int(floatIndex), comb[combIndex])
                    combIndex += 1
                mem[addrTemp] = val

    print(sum(mem.values()))

part1()
part2()
