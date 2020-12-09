def readFile():
    with open("day9/input.txt", "r") as file:
        return [int(x) for x in file]

def notTwoSum(nums, num, start, preamble):
    vals = {}
    for i in range(start, preamble + start):
        if (num - nums[i] in vals):
            return None
        else:
            vals[nums[i]] = i
    return num

def part1(preamble):
    nums = readFile()
    start = 0

    for num in nums[preamble:]:
        if (notTwoSum(nums, num, start, preamble) is not None): # notTwoSum returns None if pair not found
            return num
        start += 1

def part2(preamble, val):
    nums = readFile()
    start = 0
    numList = []

    while(True):
        numList = []
        numSum = 0
        for i in range(start, len(nums)):
            numSum += nums[i]
            numList.append(nums[i])
            if (numSum == val):
                return min(numList) + max(numList)
        start += 1
            
preamble = 25
print( part1(preamble) )
print( part2(preamble, part1(preamble)) )