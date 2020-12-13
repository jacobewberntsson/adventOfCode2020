import itertools

with open("data/11_1.txt", "r") as f:
    content = f.read().split("\n")


def gridCreator(content):
    rows = len(content)
    cols = len(content[0])
    grid = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(content[i][j])
        grid.append(col)
    return grid

def adjacentPositions(seats, row, col):
    rows = len(seats)
    cols = len(seats[0])
    countFree = 0
    countFloor = 0
    countOccu = 0
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            try:
                if r == 0 and c == 0:
                    continue
                elif row + r < 0 or row + r > rows or col + c < 0 or col + c > cols:
                    continue
                elif seats[row + r][col + c] == 'L':
                    countFree += 1
                elif seats[row + r][col + c] == '.':
                    countFloor += 1
                elif seats[row + r][col + c] == '#':
                    countOccu += 1
            except IndexError:
                continue
    return countFree, countFloor, countOccu

def adjacencyCHecker(seats, updatedGrid, flagSit):
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            adjacencyFree, adjacencyFloor, adjacencyOccupied = adjacentPositions(seats, row, col)

            if seats[row][col] == 'L' and adjacencyOccupied == 0 and flagSit:
                updatedGrid[row][col] = '#'
            elif seats[row][col] == '#' and adjacencyOccupied >= 4 and not flagSit:
                updatedGrid[row][col] = 'L'
    flagSit = not flagSit
    return updatedGrid, flagSit

def takenSeatsCounter(seats):
    takenSeats = 0
    for row in seats:
        for col in row:
            if col == '#':
                takenSeats += 1
    return takenSeats

def part1():
    grid = gridCreator(content)
    updatedGrid = gridCreator(content)
    flagSit = True
    keepGoing = True
    while keepGoing:
        updatedGrid, flagSit = adjacencyCHecker(grid, updatedGrid, flagSit)
        if updatedGrid == grid:
            keepGoing = False
        grid = gridCreator(updatedGrid)
    takenSeats = takenSeatsCounter(updatedGrid)
    return takenSeats

def part2(seats):
    new = []
    lines = list(seats)
    for row in range(len(lines)):
        new_row = []
        for col in range(len(lines[row])):
            direction = []
            for r in [-1, 0, 1]:
                for c in [-1, 0, 1]:
                    if r == c == 0:
                        continue
                    for i in range(1, len(lines)):
                        x = i * r
                        y = i * c
                        if 0 <= row + x < len(lines):
                            nextRow = row + x
                            if 0 <= col + y < len(lines[row]):
                                nextCol = col + y
                                if not lines[nextRow][nextCol] == '.':
                                    direction.append(lines[nextRow][nextCol])
                                    break

            if lines[row][col] == 'L' and not '#' in direction:
                new_row.append('#')

            elif lines[row][col] == '#' and direction.count('#') >= 5:
                new_row.append('L')
            else:
                new_row.append(lines[row][col])
        new.append(new_row)

    if list(itertools.chain.from_iterable(new)).count('#') == list(itertools.chain.from_iterable(lines)).count('#'):
        print(list(itertools.chain.from_iterable(new)).count('#'))
    else:
        part2(new)

def main():
    takenSeats1 = part1()
    print("Number of taken seats part 1:")
    print(takenSeats1)
    print("Number of taken seats part 2:")
    part2(content)

if __name__ == "__main__":
    main()