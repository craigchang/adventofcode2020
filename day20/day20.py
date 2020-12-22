import re
from copy import deepcopy
import math
from itertools import permutations
from itertools import combinations

class ImageTile:
    def __init__(self, tileId, grid, coord):
        self.tileId = tileId
        self.coord = coord
        self.grid = grid


ALL_ORIENTATIONS = (
    lambda x: x,
    lambda x: rotateRight(x),
    lambda x: rotateLeft(x),
    lambda x: rotate180(x),
    lambda x: flipHorizontal(x),
    lambda x: rotateLeft(flipHorizontal(x)),
    lambda x: rotateRight(flipHorizontal(x)),
    lambda x: flipVertical(x),
)  

DIRECTIONS = ["top", "down", "left", "right"]
TOP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def getSeaMonster():
    with open("day20/seaMonster.txt", "r") as file:
        return [list(line.rstrip("\n")) for line in file]

def readFile():
    with open("day20/sample.txt", "r") as file:
        tiles = dict()
        grid = []
        tileId = 0

        for line in file:
            if (line.startswith("Tile")):
                tileId = re.search("Tile (\d*):", line)[1]
            elif (line.startswith("#") or line.startswith(".")):
                grid.append(list(line.rstrip()))
            elif (line.rstrip() == ""):
                tiles[int(tileId)] = grid
                grid = []

        tiles[int(tileId)] = grid
    return tiles

def printTile(tileId, grid):
    rowSize = len(grid[0])
    colSize = len(grid)

    #print(tileId, ":")
    for y in range(colSize):
        for x in range(rowSize):
            print(grid[y][x], end="")
        print()
    print()

def printImage(imageGrid):
    dimension = len(imageGrid)
    size = len(imageGrid[0][0])

    yRow = []
    for yTile in range(dimension):
        for y in range(size):
            xCol = []
            for xTile in range(0, dimension, 1):
                print( "".join(imageGrid[yTile][xTile][y]), end="" )
                xCol += "".join(imageGrid[yTile][xTile][y])
                #print( "".join(imageGrid[yTile][xTile][y]) + "".join(imageGrid[yTile][xTile+1][y]) + "".join(imageGrid[yTile][xTile+2][y]), end="")

            # for xTile in range(0, dimension):
            #     xRow += imageGrid[yTile][xTile][y]
            yRow.append(xCol)
            print()
    return yRow

def isTileBorderAligned(sourceTile, targetTile, pos):
    size = len(sourceTile)
    if (pos == "top"):
        for i in range(size):
            if (sourceTile[0][i] != targetTile[size-1][i]):
                return False
    elif (pos == "down"):
        for i in range(size):
            if (sourceTile[size-1][i] != targetTile[0][i]):
                return False
    elif (pos == "right"):
        for i in range(size):
            if (sourceTile[i][size-1] != targetTile[i][0]):
                return False
    elif (pos == "left"):
        for i in range(size):
            if (sourceTile[i][0] != targetTile[i][size-1]):
                return False
    else:
        return False
    
    return True

def flipVertical(grid):
    size = len(grid)
    newGrid = deepcopy(grid)

    for y in range(size):
        for x in range(size):
            newGrid[size - y - 1][x] = grid[y][x]
    return newGrid

def flipHorizontal(grid):
    size = len(grid)
    newGrid = deepcopy(grid)

    for y in range(size):
        for x in range(size):
            newGrid[y][size - x - 1] = grid[y][x] 
    return newGrid

def rotateRight(grid):
    size = len(grid)
    newGrid = deepcopy(grid)

    for y in range(size):
        for x in range(size):
            newGrid[x][size - y - 1] = grid[y][x] 
    return newGrid

def rotateLeft(grid):
    size = len(grid)
    newGrid = deepcopy(grid)

    for y in range(size):
        for x in range(size):
            newGrid[size - x - 1][y] = grid[y][x] 
    return newGrid

def rotate180(grid):
    return rotateRight(rotateRight(grid))

def removeTileBordersInImage(grid, tileDimension):
    # remove cols
    imageRows = []
    for y in range(len(grid)):
        imageCols = []
        for x in range(0, len(grid), tileDimension):
            imageCols += grid[y][(x+1):(x+tileDimension-1)]
        imageRows.append(imageCols)

    grid = deepcopy(imageRows)
    imageRows = []
    
    # remove rows
    for y in range(0, len(grid)): 
        if ((y % tileDimension) == 0 or (y % tileDimension) == 9):
            continue
        imageRows.append(grid[y])
    grid = deepcopy(imageRows)

    return grid

def isTileAligned():
    return 0

def part1():
    tiles = readFile()
    tileDimension = len(tiles[list(tiles.keys())[0]])
    imageTileGrid = dict()
    sourceTileId = list(tiles.keys())[0]
    occupiedTiles = [(0,0)]
    imageTileMap = { (0,0): sourceTileId }

    imageTileGrid[sourceTileId] = ImageTile(sourceTileId, tiles[sourceTileId], (0,0))
    numTilesProcessed = 0

    while (len(imageTileGrid) != len(tiles)):
        found = False
        for sourceTileId in imageTileGrid.keys():
            sourceImageTile = imageTileGrid[sourceTileId]
            sourceTileGrid = sourceImageTile.grid
            sX, sY = sourceImageTile.coord
            allAdjCoord = [ (sX, sY + 1), (sX, sY - 1), (sX - 1, sY), (sX + 1, sY) ]

            for coordIndex in range(len(allAdjCoord)):
                if allAdjCoord[coordIndex] in occupiedTiles:
                    continue
                else:
                    for targetTileId, targetTileGrid in tiles.items():
                        if (targetTileId == sourceTileId or targetTileId in imageTileGrid):
                            continue
                        else:
                            for pos in range(4):
                                for targetOp in ALL_ORIENTATIONS:
                                    targetGrid = targetOp(targetTileGrid)

                                    if ( isTileBorderAligned( sourceTileGrid, targetGrid, DIRECTIONS[pos] ) ):
                                        print(coordIndex, sourceTileId, targetTileId, DIRECTIONS[pos], pos, allAdjCoord[pos])

                                        imageTileGrid[targetTileId] = ImageTile(targetTileId, targetGrid, allAdjCoord[pos])
                                        imageTileMap[allAdjCoord[pos]] = targetTileId
                                        occupiedTiles.append(allAdjCoord[pos])
                                        print("tiles processed:", numTilesProcessed)
                                        numTilesProcessed += 1
                                        found = True
                                        break
                                if found:
                                    break
                            if found:
                                break

            if found:
                break
    
    minX = min([ coord[0] for coord in occupiedTiles ])
    maxX = max([ coord[0] for coord in occupiedTiles ])
    minY = min([ coord[1] for coord in occupiedTiles ])
    maxY = max([ coord[1] for coord in occupiedTiles ])
    print(minX, maxX, minY, maxY)

    print( imageTileMap[(minX, minY)] *
            imageTileMap[(minX, maxY)] *
            imageTileMap[(maxX, minY)] *
            imageTileMap[(maxX, maxY)]
    )

    imageGrid = []
    for y in range(maxY, minY - 1, -1):
        imageCols = []
        for x in range(minX, maxX + 1, 1):
            gr = imageTileGrid[ imageTileMap[(x,y)] ].grid
            imageCols.append( gr )
        imageGrid.append(imageCols)
    
    imageGrid = printImage(imageGrid)
    print()

    #imageGrid = deepcopy(flipVertical(imageGrid))
    print()

    imageGrid = removeTileBordersInImage(imageGrid, tileDimension)
    
    seaMonster = getSeaMonster()
    originalImageGrid = deepcopy(imageGrid)
    newImageGrid = deepcopy(imageGrid)
    numSeaMonsters = -1
    found = False
    opIndex = 0

    for op in ALL_ORIENTATIONS:
        imageGrid = op(originalImageGrid)
        newImageGrid = deepcopy(imageGrid)

        numSeaMonsters = 0
        for y in range(len(imageGrid) - len(seaMonster)): # 24 - 3 = 21
            for x in range(len(imageGrid[0])- len(seaMonster[0])): # 24 - 19 = 5
                
                numPounds = 0
                for sY in range(len(seaMonster)):
                    for sX in range(len(seaMonster[0])):
                        #print(y, x, sY, sX)
                        if (seaMonster[sY][sX] == "#" and imageGrid[y + sY][x + sX] == "#"):
                            numPounds += 1

                if (numPounds == 15):
                    numSeaMonsters += 1
                    for sY in range(len(seaMonster)):
                        for sX in range(len(seaMonster[0])):
                            if (seaMonster[sY][sX] == "#"):
                                newImageGrid[y + sY][x + sX] = "O"
                    found = True
                    print(found, y,x)
                
        if (found):
            break

        print(opIndex)
        opIndex += 1
        


    count = 0
    for y in range(len(newImageGrid)):
        for x in range(len(newImageGrid[0])):
            if (newImageGrid[y][x] == "#"):
                count += 1
    print(count)
    


part1()


# def part2():



# part2()
