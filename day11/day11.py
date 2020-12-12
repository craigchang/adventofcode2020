import copy

ADJACENT_INDICES = [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(1, -1),(-1,1)]

def readFile():
    with open("day11/input.txt", "r") as file: # add boundary for looping purposes
        lines = [["x"] + list(line.rstrip()) + ["x"] for line in file]
        return [["x"] *  len(lines[0])] + lines + [["x"] *  len(lines[0])]

def isNotDuplicate(grid1, grid2):
    for y in range(len(grid1)):
        for x in range(len(grid1[0])):
            if grid1[y][x] != grid2[y][x]:
                return True
    return False

def printGrid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x], end="")
        print("")
    print()

def numOfSeatsOccupied(grid):
    return sum([1 for y in range(len(grid)) for x in range(len(grid[0])) if (grid[y][x] == "#")])

def numOfAdjSeatsOccupied(grid, x, y):
    return [1 if grid[y+j][x+i] == "#" else 0 for j,i in ADJACENT_INDICES].count(1)

def isSeatOccupied(grid, x, y, xRange, yRange, rowMax, colMax): # checks each direction for occupied seat
    j = y
    i = x
    for j,i in zip(yRange, xRange):
        if (grid[j][i] != "."):
            if (grid[j][i] == "#"):
                return 1
            return 0
    return 0

def numOfDirectionalSeatsOccupied(grid, x, y):
    rowMax = len(grid)
    colMax = len(grid[0])
    numSeatsOccupied = 0

    # bottom
    numSeatsOccupied += isSeatOccupied(grid, x, y, list([x] * (rowMax-y-2)), list(range(y+1, rowMax - 1)), rowMax, colMax)
    # top
    numSeatsOccupied += isSeatOccupied(grid, x, y, list([x] * (y-1)), list(range(y-1, 0, -1)), rowMax, colMax)
    # right
    numSeatsOccupied += isSeatOccupied(grid, x, y, list(range(x+1, colMax - 1)), list([y] * (colMax-x-2)), rowMax, colMax)
    # left
    numSeatsOccupied += isSeatOccupied(grid, x, y, list(range(x-1, 0, -1)), list([y] * (x-1)), rowMax, colMax)
    # top left
    numSeatsOccupied += isSeatOccupied(grid, x, y, list(range(x-1, 0, -1)), list(range(y-1, 0, -1)), rowMax, colMax)
    # top right
    numSeatsOccupied += isSeatOccupied(grid, x, y, list(range(x+1, colMax - 1)), list(range(y-1, 0, -1)), rowMax, colMax)
    # bottom left
    numSeatsOccupied += isSeatOccupied(grid, x, y, list(range(x-1, 0, -1)), list(range(y+1, rowMax - 1)), rowMax, colMax)
    # bottom right
    numSeatsOccupied += isSeatOccupied(grid, x, y, list(range(x+1, colMax - 1)), list(range(y+1, rowMax - 1))
, rowMax, colMax)

    return numSeatsOccupied

def part1():
    grid = readFile()
    newGrid = copy.deepcopy(grid)
    rowMax = len(grid)
    colMax = len(grid[0])

    while(True):
        for y in range(1, rowMax - 1):
            for x in range(1, colMax - 1):
                if (grid[y][x] == "L" and numOfAdjSeatsOccupied(grid, x, y) == 0):
                    newGrid[y][x] = "#"
                elif (grid[y][x] == "#" and numOfAdjSeatsOccupied(grid, x, y) >= 4):
                    newGrid[y][x] = "L"
        
        if (not isNotDuplicate(grid, newGrid)):
            break
        else:
            grid = copy.deepcopy(newGrid)

    print(numOfSeatsOccupied(grid))

def part2():
    grid = readFile()
    newGrid = copy.deepcopy(grid)
    rowMax = len(grid)
    colMax = len(grid[0])

    while(True):
        for y in range(1, rowMax - 1):
            for x in range(1, colMax - 1):
                if (grid[y][x] == "L" and numOfDirectionalSeatsOccupied(grid, x, y) == 0):
                    newGrid[y][x] = "#"
                elif (grid[y][x] == "#" and numOfDirectionalSeatsOccupied(grid, x, y) >= 5):
                    newGrid[y][x] = "L"
        
        if (not isNotDuplicate(grid, newGrid)):
            break
        else:
            grid = copy.deepcopy(newGrid)

    print(numOfSeatsOccupied(grid))


part1()
part2()