def readFile():
    with open("day22/input.txt", "r") as file:
        p1 = []
        p2 = []
        for line in file:
            if line.startswith("\n"):
                break
            elif not line.startswith("Player 1:"):
                p1.append(int(line))
        for line in file:
            if line.startswith("\n"):
                break
            elif not line.startswith("Player 2:"):
                p2.append(int(line))
        return p1, p2

def calculateScore(pwon):
    score = 0
    if len(pwon) > 0:
        pwon = pwon[::-1]
        for i in range(1, len(pwon) + 1):
            score += (i * pwon[i-1])
    return score

def playGame(p1, p2):
    turn = 1

    while(len(p1) != 0 and len(p2) != 0):
        v1, v2 = p1.pop(0), p2.pop(0)
        if (v1 > v2):
            p1 += [v1,v2]
        else:
            p2 += [v2,v1]
        turn += 1

    return p1 if len(p1) > 0 else p2

def part1():
    p1, p2 = readFile()
    pwon = playGame(p1, p2)
    print(calculateScore(pwon))

def playGame2(p1, p2):
    turn = 0
    historyList = []

    while(len(p1) != 0 and len(p2) != 0): 
        turn += 1

        if ([p1,p2] in historyList): # if players hands the same as previous rounds
            return "1"

        historyList.append([p1.copy(),p2.copy()])
        v1, v2 = p1.pop(0), p2.pop(0)

        if (len(p1) + 1 > v1 and len(p2) + 1 > v2):
            if (playGame2(p1[0:v1].copy(), p2[0:v2].copy()) == "1"):
                p1 += [v1,v2]
            else:
                p2 += [v2,v1]
        else:
            if (v1 > v2):
                p1 += [v1,v2]
            else:
                p2 += [v2,v1]

    return "1" if len(p1) > 0 else "2"

def part2():
    p1, p2 = readFile()
    player = playGame2(p1, p2)
    pwon = p1 if player == "1" else p2
    print(calculateScore(pwon))

part1()
part2()