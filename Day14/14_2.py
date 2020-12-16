with open("data/14_1.txt", "r") as fi:
    file = fi.read().splitlines()

memory = {}

for line in file:
    line = line.split()

    if line[0] == "mask":
        mask = line[2]

    else:
        result = []
        ind, value = format(int(line[0][4:-1]), '036b'), int(line[2])

        for index, bit in enumerate(mask):
            if bit == "0":
                result.append(ind[index])
            else:
                result.append(bit)
                
        possible = []

        index = [index for index, bit in enumerate(result) if bit == "X"]

        for num in range(2**len(index)):
            tmp = result.copy()

            for idx, val in enumerate(format(num, f"0{len(index)}b")):
                tmp[index[idx]] = val

            possible.append(''.join(tmp))

        for possibility in possible:
            memory[int(possibility, 2)] = value

res2 = sum(memory.values())

print(res2)