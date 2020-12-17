with open("data/15_1.txt", "r") as f:
    content = f.read().split(',')
    content = {int(i):index for index,i in enumerate(content,start=1)}

def part2(turns):
    turn = len(content)+1
    currNbr = 0
    values = [int(i) for i in content]

    while turn < turns:
        values.append(currNbr)
        if currNbr in content.keys():
            newNbr = turn - content[currNbr]
            content[currNbr] = turn
            currNbr = newNbr
        else:
            content[currNbr] = turn
            currNbr = 0
        turn += 1

    print(currNbr)


def main():
    part2(30000000)

if __name__ == '__main__':
    main()