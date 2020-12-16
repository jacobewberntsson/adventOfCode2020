with open("data/14_example.txt", "r") as f:
    content = f.read().splitlines()

def sumOfValues():
    mem = {}
    for line in content:
        if line.startswith("mask"):
            mask = line[7:]
        else:
            res = []
            currPointer = line[4:].replace("]", "").split(" = ")
            currMem, currValue = int(currPointer[0]), format(int(currPointer[1]), "036b")

            for i, bit in enumerate(mask):
                if bit != "X":
                    res.append(bit)
                else:
                    res.append(currValue[i])
            mem[currMem] = int(''.join(res), 2)
    return sum(mem.values())

def main():
    res1 = sumOfValues()
    print(res1)


if __name__ == "__main__":
    main()