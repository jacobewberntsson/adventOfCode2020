with open("data/8_1.txt", "r") as f:
    content = f.read().split('\n')

def dataHandler():
    return [(pair.split(' ')) for pair in content]

def instructorLoop(pairs):
    countLoop = 0
    lstIdx = 0
    oprIdx = 0
    argIdx = 1
    loop = set()
    terminateCount = 0

    while lstIdx not in loop and lstIdx < len(pairs):
        tmp = lstIdx
        if pairs[lstIdx][oprIdx] == "nop":
            tmp += 1

        elif pairs[lstIdx][oprIdx] == "acc":
            tmp += 1
            sign = pairs[lstIdx][argIdx][0]
            nbr = int(pairs[lstIdx][argIdx][1:])
            if sign == "+":
                countLoop += nbr
            else:
                countLoop -= nbr

        elif pairs[lstIdx][oprIdx] == "jmp":
            sign = pairs[lstIdx][argIdx][0]
            nbr = int(pairs[lstIdx][argIdx][1:])
            if sign == "+":
                tmp += nbr
            else:
                tmp -= nbr

        else:
            print("something went wrong")

        loop.add(lstIdx)
        lstIdx = tmp
        if lstIdx > len(pairs) - 1:
            terminateCount = countLoop

    return countLoop, terminateCount

def terminator(pairs):
    countLst = []
    for i, pair in enumerate(pairs):
        tmpLst = pairs
        if pair[0] == "nop":
            tmpLst[i][0] = "jmp"
        elif pair[0] == "jmp":
            tmpLst[i][0] = "nop"
        tmp = instructorLoop(tmpLst)[1]

        if tmpLst[i][0] == "nop":
            tmpLst[i][0] = "jmp"
        elif tmpLst[i][0] == "jmp":
            tmpLst[i][0] = "nop"
        countLst.append(tmp)
    return (max(countLst))
    
def accCounter():
    pairs = dataHandler()
    accCountLoop = instructorLoop(pairs)[0]
    accCountTerminate = terminator(pairs)
    return accCountLoop, accCountTerminate

print(accCounter())