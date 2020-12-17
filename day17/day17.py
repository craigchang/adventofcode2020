from copy import deepcopy

def readFile(filename=""):
    with open("day17/input.txt", "r") as file:
        return [ list(line.rstrip()) for line in file]

def initGrid(grid):
    gridDict = dict()
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            if (x,y,0) not in gridDict:
                gridDict[(x,y,0)] = grid[y][x]
    return gridDict

def initGrid4d(grid):
    gridDict = dict()
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            if (x,y,0,0) not in gridDict:
                gridDict[(x,y,0,0)] = grid[y][x]
    return gridDict

def addZeroPadding(gridDict, minGridCol, maxGridCol, minGridRow, maxGridRow, minZLayer, maxZLayer):
    for z in range(minZLayer, maxZLayer):
        for x in range(minGridRow, maxGridRow): # add row on top
            gridDict[(x,minGridCol,z)] = "."
        for x in range(minGridRow, maxGridRow): # add row on bottom
            gridDict[(x,maxGridCol-1,z)] = "."
        for y in range(minGridCol, maxGridCol): # add col on left
            gridDict[(minGridRow,y,z)] = "."
        for y in range(minGridCol, maxGridCol): # add col on right
            gridDict[(maxGridRow-1,y,z)] = "."

def addZeroPadding4d(gridDict, minGridCol, maxGridCol, minGridRow, maxGridRow, minZLayer, maxZLayer, minWLayer, maxWLayer):
    for w in range(minWLayer, maxWLayer):
        for z in range(minZLayer, maxZLayer):
            for x in range(minGridRow, maxGridRow): # add row on top
                gridDict[(x,minGridCol,z,w)] = "."
            for x in range(minGridRow, maxGridRow): # add row on bottom
                gridDict[(x,maxGridCol-1,z,w)] = "."
            for y in range(minGridCol, maxGridCol): # add col on left
                gridDict[(minGridRow,y,z,w)] = "."
            for y in range(minGridCol, maxGridCol): # add col on right
                gridDict[(maxGridRow-1,y,z,w)] = "."

def addZlayer(gridDict, minZLayer, maxZLayer):
    for (x,y,z), val in (deepcopy(gridDict)).items():
        gridDict[(x,y,minZLayer)] = "."
        gridDict[(x,y,maxZLayer-1)] = "."

def addZWlayer(gridDict, minZLayer, maxZLayer, minWLayer, maxWLayer):
    for (x,y,z,w), val in (deepcopy(gridDict)).items():
        gridDict[(x,y,minZLayer,minWLayer)] = "."
        gridDict[(x,y,minZLayer,w)] = "."
        gridDict[(x,y,minZLayer,maxWLayer - 1)] = "."

        gridDict[(x,y,maxZLayer-1,minWLayer)] = "."
        gridDict[(x,y,maxZLayer-1,w)] = "."
        gridDict[(x,y,maxZLayer-1,maxWLayer - 1)] = "."

        gridDict[(x,y,z,minWLayer)] = "."
        gridDict[(x,y,z,maxWLayer-1)] = "."

def changeStatus(gridDict, newGridDict, coord, numActive):
    if (gridDict[coord] == "#"):
        newGridDict[coord] = "#" if (numActive == 2 or numActive == 3) else "."
    else: # if "."
        newGridDict[coord] = "#" if (numActive == 3) else "."

def part1():
    grid = readFile()

    minGridCol, maxGridCol = 0, len(grid)
    minGridRow, maxGridRow = 0, len(grid[0])
    minZLayer, maxZLayer = 0, 1

    gridDict = initGrid(grid)

    cycle = 0
    while (cycle < 6):
        newGridDict = deepcopy(gridDict)

        minGridCol -= 1
        maxGridCol += 1
        minGridRow -= 1
        maxGridRow += 1
        minZLayer -= 1
        maxZLayer += 1

        addZlayer(gridDict, minZLayer, maxZLayer)
        addZeroPadding(gridDict, minGridCol, maxGridCol, minGridRow, maxGridRow, minZLayer, maxZLayer)
        
        for coord, val in gridDict.items():
            x,y,z = coord
            numActive = 0
            for nx in range(x - 1, x + 2):
                for ny in range(y - 1, y + 2):
                    for nz in range(z - 1, z + 2):
                        if (nx == x and ny == y and nz == z): # if itself skip
                            continue
                        if ((nx,ny,nz) in gridDict and gridDict[(nx,ny,nz)] == "#"): # if coord found and active
                            numActive += 1

            changeStatus(gridDict, newGridDict, coord, numActive)

        gridDict = deepcopy(newGridDict)
        cycle += 1

    print( sum( [1 for c,val in gridDict.items() if val == "#"] ) )

def part2():
    grid = readFile()

    minGridCol, maxGridCol = 0, len(grid)
    minGridRow, maxGridRow = 0, len(grid[0])
    minZLayer, maxZLayer = 0, 1
    minWLayer, maxWLayer = 0, 1

    gridDict = initGrid4d(grid)

    cycle = 0
    while (cycle < 6):
        newGridDict = deepcopy(gridDict)

        minGridCol -= 1
        maxGridCol += 1
        minGridRow -= 1
        maxGridRow += 1
        minZLayer -= 1
        maxZLayer += 1
        minWLayer -= 1
        maxWLayer += 1

        addZWlayer(gridDict, minZLayer, maxZLayer, minWLayer, maxWLayer)
        addZeroPadding4d(gridDict, minGridCol, maxGridCol, minGridRow, maxGridRow, minZLayer, maxZLayer, minWLayer, maxWLayer)
        
        for coord, val in gridDict.items():
            x,y,z,w = coord
            numActive = 0
            for nx in range(x - 1, x + 2):
                for ny in range(y - 1, y + 2):
                    for nz in range(z - 1, z + 2):
                        for nw in range(w - 1, w + 2):
                            if (nx == x and ny == y and nz == z and nw == w):
                                continue
                            if ((nx,ny,nz,nw) in gridDict and gridDict[(nx,ny,nz,nw)] == "#"):
                                numActive += 1

            changeStatus(gridDict, newGridDict, coord, numActive)

        gridDict = deepcopy(newGridDict)
        cycle += 1
        
    print( sum( [1 for c,val in gridDict.items() if val == "#"] ) )
    

part1()
part2()
