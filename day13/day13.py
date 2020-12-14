import math

def readFile():
    with open("day13/input.txt", "r") as file: # add boundary for looping purposes
        earliestTs = int(file.readline().rstrip())
        busList = file.readline().split(",")
        return earliestTs, busList

def part1():
    earlistTs, busList = readFile()
    earliestBusTs = math.inf
    earliestBusId = 0
    busList = [bus for bus in busList if bus != "x"]

    for bus in busList: # find smallest difference between target timestamp and earliest bus timestamp
        busId = int(bus)
        busNearTs = math.ceil(earlistTs / busId ) * busId - earlistTs
        if (busNearTs <= earliestBusTs):
            earliestBusTs, earliestBusId = busNearTs, busId
    
    print(earliestBusId * earliestBusTs)

def part2():
    busList = readFile()[1]
    busSchedule = [ (int(busList[ts]), ts) for ts in range(len(busList)) if busList[ts] != "x" ] # list of bus id, subsequent minutes tuple
    ts = 0 # current timestamp
    tsIncrement = busSchedule[0][0] # increment is 1st bus id
    shifted = 1
    
    while(True):
        busId, tsDiff = busSchedule[shifted] # get current bus
        if ((ts + tsDiff) % busId == 0): # if current bus is aligned
            tsIncrement *= busId # new timestamp increment is sum of previous bus ids (least common multiple) 
            shifted += 1
        if len(busSchedule) == shifted:
            break
        ts += tsIncrement
        
    print(ts)

part1()
part2()