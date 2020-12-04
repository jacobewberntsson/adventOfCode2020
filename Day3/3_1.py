f = open("data/3_1.txt", "r")
f.readline()
content = f.readlines()
content = [line.strip().split(",") for line in content]
f.close()

def slopeTraverse(idxX, idxY):
    nextIdx = 0
    countTree = 0
    countOpenSquares = 0

    for i, line in enumerate(content):
        i = i+1
        if i % idxY == 0:
            info = ''.join(line)
            nextIdx += idxX
            nextIdx = nextIdx % len(info)
            if info[nextIdx] == '#':
                countTree +=1
            else:
                countOpenSquares += 1

    print("Open squares: " + str(countOpenSquares))
    print("Trees: " + str(countTree))
    return countTree

_11 = slopeTraverse(1,1)
_31 = slopeTraverse(3,1)
_51 = slopeTraverse(5,1)
_71 = slopeTraverse(7,1)
_12 = slopeTraverse(1,2)


res = _11*_31*_51*_71*_12
print("The product of the trees in the slopes are: " + str(res))