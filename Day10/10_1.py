with open("data/10_1.txt", "r") as f:
    adapters = sorted(map(int, f.read().splitlines()))


def joltDiff():
    adapterJolt = 0
    c1 = 0
    c2 = 0
    c3 = 0
    for adapter in adapters:
        if abs(adapter - adapterJolt) == 1:
            c1 += 1
            adapterJolt = adapter
        elif abs(adapter - adapterJolt) == 2:
            c2 += 1
            adapterJolt = adapter
        elif abs(adapter - adapterJolt) == 3:
            c3 += 1
            adapterJolt = adapter
        else:
            print("shit hit the fan")
    c3 += 1
    adapterJolt += 3
    return c1, c2, c3, adapterJolt

def distinctCounter():
    res = {0:1}
    for adapter in adapters:
        res[adapter] = 0
        if adapter - 1 in res:
            res[adapter] += res[adapter-1]
        if adapter - 2 in res:
            res[adapter] += res[adapter-2]
        if adapter - 3 in res:
            res[adapter] += res[adapter-3]
    return (res[max(adapters)])

def main():
    c1, c2, c3, adapterJolt = joltDiff()
    print("The number of 1*3 jolt differences are: " + str(c1 * c3))
    uniqueConnections = distinctCounter()
    print("The amount of unique connections are: " + str(uniqueConnections))


if __name__ == "__main__":
    main()