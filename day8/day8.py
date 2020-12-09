import re

def readFile():
    with open("day8/input.txt", "r") as file:
        return [(line.split(" ")[0], int(line.split(" ")[1])) for line in file]

def calculateAccumulator(instructions):
    ptr = accum = 0
    infiniteLoop = False
    flags = { i: 0 for i in range(len(instructions)) } # keeps track of revisited instructions

    while(ptr < len(instructions)):
        flags[ptr] += 1
        if (flags[ptr] > 1):
            infiniteLoop = True
            break
        instr, arg = instructions[ptr]
        if (instr == "acc"):
            accum += arg
            ptr += 1
        elif (instr == "jmp"):
            ptr += arg
        else: # nop
            ptr += 1
    
    return accum, infiniteLoop

def part1():
    instructions = readFile()
    print(calculateAccumulator(instructions)[0])

def part2():
    instructions = readFile()
    accum = i = 0

    while (i < len(instructions)):
        newInstructions = instructions.copy()
        
        for instr, val in newInstructions[i:]:
            print(i, instr, val)
            if (instr != "acc"): # replace instruction 
                newInstructions[i] = ("nop" if instr == "jmp" else "jmp", val)
                break
            i += 1

        accum, infiniteLoop = calculateAccumulator(newInstructions)
        if (not infiniteLoop):
            break
        i += 1

    print(accum)

part1()
part2()
