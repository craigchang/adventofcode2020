def readFile():
    with open("day25/input.txt", "r") as file:
        return int(file.readline()), int(file.readline())

def findLoopSize(pubKey):
    val = 1
    loop = 0
    while val != pubKey:
        val = (val * 7) % 20201227
        loop += 1
    return loop, val

def calcEncryptionKey(subjectNum, loop):
    encryptKey = 1
    for l in range(loop):
        encryptKey = (encryptKey * subjectNum) % 20201227
    return encryptKey

cardPubKey, doorPubKey = readFile()

cardLoop, cardSubjectNum = findLoopSize(cardPubKey)
doorLoop, doorSubjectNum = findLoopSize(doorPubKey)

cEncrypt = calcEncryptionKey(cardSubjectNum, doorLoop)
print(cEncrypt)
dEncrypt = calcEncryptionKey(doorSubjectNum, cardLoop)
print(dEncrypt)
