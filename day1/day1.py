def readFile():
    with open("day1/input.txt", "r") as file:
        data = [int(x) for x in file]
    return data

def part1():
    data = readFile()

    for i in data:
        for j in data:
            if (i + j == 2020):
                return i * j

def part2():
    data = readFile()

    for i in data:
        for j in data:
            for k in data:
                if (i + j + k == 2020):
                    return i * j * k


print(part1())
print(part2())