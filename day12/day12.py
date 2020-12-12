import re
import math

DIR = ("E", "S", "W", "N")
SHIPDIR = { "E": 0, "S": 1, "W": 2, "N": 3}

def readFile():
    with open("day12/input.txt", "r") as file: # add boundary for looping purposes
        directions = []
        for line in file:
            action, val = re.findall("([A-Z])(\\d+)", line.rstrip())[0]
            directions.append((action, int(val)))
        return directions

def turnShip(action, index, degrees):
    if (action == "L"):
        return (index - int(degrees / 90) + 4) % 4
    elif (action == "R"):
        return (index + int(degrees / 90)) % 4

def move(action, units, x, y):
    if (action == "N"):
        y += int(units)
    elif (action == "S"):
        y -= int(units)
    elif (action == "E"):
        x += int(units)
    elif (action == "W"):
        x -= int(units)
    return x,y

def part1():
    lines = readFile()
    shipDir = DIR[0] # initialize to east
    shipX = 0
    shipY = 0

    for action, val in lines:
        if (action == "N" or action == "S" or action == "E" or action == "W"):
            shipX, shipY = move(action, val, shipX, shipY)
        elif (action == "F"):
            shipX, shipY = move(shipDir, val, shipX, shipY)
        elif (action == "L" or action == "R"):
            shipDir = DIR[ turnShip(action, SHIPDIR[shipDir], val) ]

    print(abs(shipX) + abs(shipY))

def part2():
    lines = readFile()
    shipX = 0
    shipY = 0
    waypointX = 10
    waypointY = 1

    for action, val in lines:
        if (action == "N" or action == "S" or action == "E" or action == "W"):
            waypointX, waypointY = move(action, val, waypointX, waypointY)
        elif (action == "F"):
            diffX, diffY = (waypointX - shipX, waypointY - shipY)
            shipX, shipY = (shipX + val * diffX, shipY + val * diffY)
            waypointX, waypointY = (shipX + diffX, shipY + diffY)
        elif (action == "L" or action == "R"):
            diffX, diffY = (waypointX - shipX, waypointY - shipY) # diffs between waypoint and ship
            if (action == "L" and val == 90 or action == "R" and val == 270): 
                waypointX, waypointY = (shipX - diffY, shipY + diffX)
            elif (action == "L" and val == 270 or action == "R" and val == 90):
                waypointX, waypointY = (shipX + diffY, shipY - diffX)
            else: # val == 180
                waypointX, waypointY = (shipX - diffX, shipY - diffY)

    print(abs(shipX) + abs(shipY))

part1()
part2()
