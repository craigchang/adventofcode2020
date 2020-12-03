import re

def part1():
    grid = readFile()
    print(numTrees(grid,3,1))

def part2():
    grid = readFile()
    print(
        numTrees(grid,1,1) * 
        numTrees(grid,3,1) *
        numTrees(grid,5,1) *
        numTrees(grid,7,1) *
        numTrees(grid,1,2) 
    )

def readFile():
    with open("day3/input.txt", "r") as file:
        grid = [line.rstrip() for line in file]
    return grid

def numTrees(grid, xSlope, ySlope):
    col = xSlope
    rowSize = len(grid[0])
    count = 0

    for row in range(0, len(grid), ySlope):
        if (row == 0): continue # skip 1st iter
        if (grid[row][col] == "#"): count += 1
        col = (col + xSlope) % rowSize # reset pos to left of grid
    return count

part1()
part2()
