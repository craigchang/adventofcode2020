import re

def part1():
    valid = 0
    with open("day2/input.txt", "r") as file:
        for line in file:
            data = re.split("-|:\\s|\\s", line.rstrip())
            count = len(re.findall(data[2], data[3]))
            if (int(data[0]) <= count and count <= int(data[1])):
                valid += 1
    print(valid)

def part2():
    valid = 0
    with open("day2/input.txt", "r") as file:
        for line in file:
            data = re.split("-|:\\s|\\s", line.rstrip())
            if ((data[3][int(data[0])-1] == data[2]) != 
                (data[3][int(data[1])-1] == data[2])) : 
                valid += 1

    print(valid)

part1()
part2()