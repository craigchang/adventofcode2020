def readFile():
    with open("day6/input.txt", "r") as file:
        return [line.rstrip() for line in file] + [""] # added empty line for looping purposes

def part1():
    data = readFile()

    group = ""
    sumQuestions = 0

    for line in data:
        if line == "": # if blank line start new group
            sumQuestions += len(list(set(group)))
            group = ""
            continue
        group += line # aggregate questions for a group
    print(sumQuestions)

def part2():
    data = readFile()

    group = ""
    sumQuestions = 0
    lineCount = 0

    for line in data:
        if line == "": # if blank line start new group
            for l in list(set(group)):
                if lineCount == group.count(l):
                    sumQuestions += 1
            group = ""
            lineCount = 0
            continue
        group += line # aggregate questions for a group
        lineCount += 1
    print(sumQuestions)

part1()
part2()