with open("data/5_1.txt", "r") as f:
    content = f.read().splitlines()

def rowCheck(rowList):
    lower = 0
    upper = 128
    rowPos = None
    powOf = 7
    for row in rowList:
        powOf -= 1
        if row == 'F':
            upper = upper - (2 ** powOf)
        elif row == 'B':
            lower = lower + (2 ** powOf)
    rowPos = lower
    return rowPos

def colCheck(colList):
    colPos = None
    lower = 0
    upper = 8
    powOf = 3
    for col in colList:
        powOf -= 1
        if col == 'L':
            upper = upper - (2 ** powOf)
        elif col == 'R':
            lower = lower + (2 ** powOf)
    colPos = lower
    return colPos

def seatID(row, col):
    return row*8 + col

def seatFinder():
    seatId = []
    for boardingPass in content:
        row = rowCheck(boardingPass[:7])
        col = colCheck(boardingPass[7:])
        seat = seatID(row, col)
        seatId.append(seat)
    print("Max seatID: " + str(max(seatId)))
    seatId = sorted(seatId)
    possibleIds = [i for i in range(min(seatId), max(seatId)+1)]
    mySeatID = set(possibleIds).difference(seatId)
    print("Your seatID is: " + str(mySeatID))


seatFinder()
