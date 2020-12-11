with open("data/11_small.txt", "r") as f:
    content = f.read().split("\n")


def gridCreator(content):
    rows = len(content)
    cols = len(content[0])
    grid = []
    for i in range(cols):
        col = []
        for j in range(rows):
            col.append(content[i][j])
        grid.append(col)
    return grid

def adjacentPositions(seats, row, col):
    # print(row, col)
    rows = len(seats)
    cols = len(seats[0])
    countFree = 0
    countFloor = 0
    countOccu = 0
    # print(seats[row][col])
    for r in [-1, 0, 1]:
        print("new row----------")
        for c in [-1, 0, 1]:
            if r == 0 and c == 0:
                print("home")
                continue
            elif row + r < 0 or row + r > rows or col + c < 0 or col + c > cols:
                print("out of bounds")
                continue
            elif seats[row + r][col + c] == 'L':
                print("seat")
                countFree += 1
            elif seats[row + r][col + c] == '.':
                print("floor")
                countFloor += 1
            elif seats[row + r][col + c] == '#':
                print("taken")
                countOccu += 1
    print(countFree, countFloor, countOccu)


    seat = seats[row][col]
    
    return

def adjacencyCHecker(seats):
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            adjacentPositions(seats, row, col)
            # adjacencyFree, adjacencyFloor, adjacencyOccupied = adjacentPositions(seats, row, col)
            # print(adjacencyFree, adjacencyFloor, adjacencyOccupied)
    return

def main():
    grid = gridCreator(content)
    adjacencyCHecker(grid)

if __name__ == "__main__":
    main()