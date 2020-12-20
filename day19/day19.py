import re

def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

def readFile():
    with open("day19/sample.txt", "r") as file:
        messagesDict = dict()
        received = []
        for line in file:
            if (line.rstrip() == ""): break
            splits = line.split(": ")
            messagesDict[splits[0]] = splits[1].rstrip()
        received = [ line.rstrip() for line in file.readlines() ]
    return messagesDict, received

def calculate(m, mDict):
    if ( re.search("\"[a|b]\"", m) ): # if letter
        return m.replace("\"", "")
    elif ( m.isnumeric() ) : # if number
        return calculate(mDict[m], mDict)
    elif ( not re.search("\|", m) ): # no pipe
        rules = [ calculate(mDict[r], mDict) for r in m.split(" ") ]
        prev = rules.pop(0)

        for rule in rules: # evaluate rules together
            if (type(prev) is list and type(rule) is list): # combine two lists
                prev = [ p + r for p in prev for r in rule ]
            elif (type(rule) is list): # append letter to list
                prev = [ prev + r for r in rule ]
            elif (type(prev) is list): # prepend letter to list
                prev = [ p + rule for p in prev ]
            else: # combine letters
                prev += rule
        return prev
    elif ( re.search("\|", m) ): # with pipe 
        splits = m.split(" | ")
        #output = [ calculate(s, mDict) for s in splits ]

        output = []
        for s in splits:
            if (m == "42 | 42 8" and s == "42 8"):
                break
            else:
                output.append(calculate(s, mDict))

        final = []
        for f in output: # addresses nested lists
            final += f if type(f) is list else [f]
        return final
    return ""

def part1():
    messagesDict, received = readFile()
    messages = calculate(messagesDict["0"], messagesDict)
    print( sum( 1 for m in messages if (m in received) ) )

def part2():
    messagesDict, received = readFile()
    # messages = calculate(messagesDict["0"], messagesDict)
    # print( sum( 1 for m in messages if (m in received) ) )

    # test8 = calculate(messagesDict["8"], messagesDict) # 8: 42
    # print("8", len(test8))
    # for i in range(len(test8)):
    #     print(i, test8[i])

    # test32 = calculate(messagesDict["31"], messagesDict) # 31: 14 17 | 1 13
    # print("31", len(test32))
    # for i in range(len(test32)):
    #     print(i, test32[i])

    # test2 = calculate(messagesDict["11"], messagesDict) # 42 31
    # print(len(test2))
    # for i in range(len(test2)):
    #     print(i, test2[i])

    messagesDict["8"] = "42 | 42 8"
    messagesDict["11"] = "42 31 | 42 11 31"

    test1 = calculate(messagesDict["8"], messagesDict) # 42

    print(len(test1)) 

    # test2 = calculate(messagesDict["11"], messagesDict) # 42, 31
    # print(len(test2))

    # messages = calculate(messagesDict["0"], messagesDict)
    # print( sum( 1 for m in messages if (m in received) ) )

#part1()
part2()


# print(principal_period("aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"))