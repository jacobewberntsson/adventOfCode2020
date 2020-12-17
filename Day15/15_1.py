from collections import *

with open("data/15_small.txt", "r") as f:
    content = f.read().split(',')


def initNbrGame(spokenNbrs):
    nbrs = 0
    values = defaultdict(deque)
    for nbr in content:
        nbrs += 1
        values[int(nbr)] = 0
        for val in values:
            values[val] += 1
    return values, nbrs

def nbrGame(keyVal, spokenNbrs, turns):
    values = keyVal
    currNbr = 0
    newNbr = None
    turn = len(keyVal) + 1
    res = 0
    while spokenNbrs < turns:
        res = currNbr
        if currNbr in values:
            newNbr = values[currNbr]
            values[currNbr] = 0
            currNbr = newNbr
        else:
            values[currNbr] = 0
            currNbr = 0
        for val in values:
            values[val] += 1
        spokenNbrs += 1
        turn += 1
    return res




def main():
    spokenNbrs = 0
    keyVal, spokenNbrs = initNbrGame(spokenNbrs)
    res1 = nbrGame(keyVal, spokenNbrs, 2020)
    print(res1)

if __name__ == "__main__":
    main()