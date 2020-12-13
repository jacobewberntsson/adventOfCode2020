with open('data/12_1.txt') as f:
    content = f.read().split('\n')
    instructions = []
    for instr in content:
        instructions.append((instr[0], int(instr[1:])))

def manDist(pos):
    return abs(pos['E'] - pos['W']) + abs(pos['N'] - pos['S'])

def simpNav(instructions):
    turnAngle = 0
    turnAngles = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
    pos = {'E': 0, 'N': 0, 'W': 0, 'S': 0}

    for instr, value in instructions:
        if instr == 'R':
            value = -value
        if instr in 'LR':
            turnAngle = (turnAngle + value) % 360
        else:
            if instr == 'F':
                instr = turnAngles[turnAngle]
            pos[instr] += value
    return manDist(pos)

def wpNav(instrutions):
    x, y = 0, 0
    wx, wy = 10, 1
    d = {'E': (1, 0), 'N': (0, 1), 'W': (-1, 0), 'S': (0, -1)}
    sin = {0: 0, 90: 1, 180: 0, 270: -1, 360: 0}
    for instr, value in instructions:
        if instr == 'R':
            value = (-value) % 360
        if instr in 'LR':
            s, c = sin[value], sin[value + 90]
            wx, wy = round(wx * c - wy * s), round(wx * s + wy * c)
        elif instr == 'F':
            x, y = x + wx * value, y + wy * value
        else:
            xd, yd = d[instr]
            wx, wy = wx + xd * value, wy + yd * value
    return abs(x) + abs(y)

def main():
    part1 = simpNav(instructions)
    print("The Manhattan distance between that location and the ship's starting position is: " + str(part1))
    part2 = wpNav(instructions)
    print("The Manhattan distance between that location and the ship's starting position is: " + str(part2))

if __name__ == "__main__":
    main()