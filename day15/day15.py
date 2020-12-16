def findNum(nums=[], limit=2020):
    numsDict = dict() # keeps track of num of occurances

    # initialize starting numbers
    for i in range(len(nums)):
        if nums[i] not in numsDict:
            numsDict[nums[i]] = i

    turn = len(nums) - 1 # start from end of starting numbers

    while(turn != limit):
        previousNumber = nums[turn]
        
        if (previousNumber in numsDict): # if found
            prevTurn = numsDict[previousNumber]
            if (prevTurn == turn): # if previous number from previous turn and only first time
                nums.append(0)
            elif (prevTurn != turn): # if previous number from prev turn and more than one occurance
                numsDict[previousNumber] = turn
                nums.append(turn - prevTurn)
        else: # if not found in dict
            numsDict[previousNumber] = turn
            nums.append(0)

        turn += 1
    
    print(nums[limit - 1])
    
findNum([1,17,0,10,18,11,6])
findNum([1,17,0,10,18,11,6], 30000000)
