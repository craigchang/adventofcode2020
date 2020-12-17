from functools import reduce
import math

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

def getFieldRange(start1, end1, start2, end2):
    return lambda x: ((int(start1) <= x and x <= int(end1)) or (int(start2) <= x and x <= int(end2)))

def readFile(filename=""):
    with open(filename, "r") as file: # add boundary for looping purposes
        yourTickets = []
        nearbyTickets = []
        fieldRangeDict = dict()

        for line in file:
            if line.rstrip() == "": 
                continue
            if (line.startswith("your ticket:")):
                yourTickets = [ int(i) for i in file.readline().rstrip().split(",") ]
            elif (line.startswith("nearby tickets:")):
                nearbyTickets = [ [ int(i) for i in nt.rstrip().split(",") ] for nt in file.readlines() ]
            else: # read fields
                splits = line.rstrip().split(": ")
                field = splits[0]
                ranges = splits[1].split(" or ")
                start1, end1  = ranges[0].split("-")
                start2, end2  = ranges[1].split("-")
                fieldRangeDict[field] = getFieldRange(start1, end1, start2, end2)

        return yourTickets, nearbyTickets, fieldRangeDict

def part1(filename=""):
    yourTickets, nearbyTickets, fieldRangeDict = readFile(filename)
    validTicketList = []
    invalidTicketValueList = []

    for ticket in nearbyTickets:
        validTicket = True
        for ticketValue in ticket:
            rangeResults = [ isInRange(ticketValue) for key, isInRange in fieldRangeDict.items() ]
            if (not (True in rangeResults)):
                invalidTicketValueList.append(ticketValue)
                validTicket = False
        if (validTicket):
            validTicketList.append(ticket)

    print(sum(invalidTicketValueList))

    return validTicketList

def part2(filename="", validTicketsList=[]):
    yourTickets, nearbyTickets, fieldRangeDict = readFile(filename)
    
    if (len(validTicketsList) != 0): # from part 1
        nearbyTickets = validTicketsList.copy()
    
    nearbyTickets.append(yourTickets) # append your tickets

    numsPerTicket = len(nearbyTickets[0])   # numbers per ticket
    numTickets = len(nearbyTickets)         # number of tickets

    fieldIndexDict = dict() # holds which field belongs to which position

    # since 1st iter fields can has multiple positions, use process of elimination until each fields has 1 unique pos 
    while(len(fieldIndexDict.keys()) != numsPerTicket): 
        for field, isInRange in fieldRangeDict.items(): # for each field from file
            if (field in fieldIndexDict):
                continue
            validFields = []
            for colIndex in range(numsPerTicket): # check each column
                if (colIndex in fieldIndexDict.values()):
                    continue
                colValues = [ nearbyTickets[row][colIndex] for row in range(numTickets) ] # get all column values
                validValues = [ ticketValue for ticketValue in colValues if isInRange(ticketValue) ] # check each col value if in range

                if (len(validValues) == numTickets): # if all values in field range
                    validFields.append(colIndex)

            if (len(validFields) == 1): # if field only matches one position
                fieldIndexDict[field] = validFields[0]
            
    print(reduce((lambda  x,y: x * y), [yourTickets[index] for field, index in fieldIndexDict.items() if field.startswith("departure")]))

# testing
#part1(filename="day16/sample.txt")
#part2(filename="day16/sample2.txt")

#part1(filename="day16/input.txt")
part2("day16/input.txt", part1(filename="day16/input.txt"))