# https://www.geeksforgeeks.org/expression-evaluation/ 
# two stack solution

def readFile():
    with open("day18/input.txt", "r") as file:
        return [line.rstrip() for line in file]

def precedence(op, part):
    if (part == 1): # + and * are equal prec
        return 1 if (op == "+" or op == "*") else 0

    if (part == 2): # + higher prec than *
        if (op == "+"):     return 2
        elif (op == "*"):   return 1
        else:               return 0

def calculateOp(val1, val2, op):
    return val1 + val2 if op == "+" else val1 * val2

def evaluate(expr, part=1):
    values = []
    ops = []
    i = 0

    while (i < len(expr)):
        if (expr[i] == " "):
            i += 1
            continue
        elif (expr[i] == "("):
            ops.append("(")
        elif (expr[i].isdigit()):
            val = 0
            while (i < len(expr) and expr[i].isdigit()):
                val = (val * 10) + int(expr[i])
                i += 1
            values.append(val)
            i -= 1
        elif (expr[i] == ")"):
            while (len(ops) != 0 and ops[-1] != "("):
                values.append(calculateOp(values.pop(), values.pop(), ops.pop()))
            ops.pop() # get rid of opening brace
        else: # operator
            while (len(ops) != 0 and precedence(ops[-1], part) >= precedence(expr[i], part)): # if preivous prec greater, execute first
                values.append(calculateOp(values.pop(), values.pop(), ops.pop()))
            ops.append(expr[i])
        i += 1
    
    while (len(ops) != 0):
        values.append(calculateOp(values.pop(), values.pop(), ops.pop()))
    
    return values[-1]

expressions = readFile()

# part 1
print(sum([evaluate(line) for line in expressions]))
# part 2
print(sum([evaluate(line, 2) for line in expressions]))
