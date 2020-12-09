with open("data/9_1.txt", "r") as f:
    content = f.read().split("\n")

def sumChecker(value, lst):
    found = False
    nonSumValue = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            
            if int(lst[i]) + int(lst[j]) == int(value):
                found = True
            else:
                nonSumValue = value
    if not found:
        return nonSumValue
    return False

def premableChecker():
    premList = []
    premableLenght = 25

    for i, value in enumerate(content):
        if i < premableLenght:
            premList.append(value)
        else:
            if sumChecker(value, premList): return value
            premList.pop(0)
            premList.append(value)
    return False

def weaknessFinder(value):
    weakList = []
    for i in range(len(content)):
        weakList.append(int(content[i]))
        for j in range(i+1, len(content)):
            weakList.append(int(content[j]))
            if sum(weakList) == int(value):
                return weakList
        weakList = []
    return False
            
def main():
    premNum = premableChecker()
    weakList = weaknessFinder(premNum)
    encWeakness = max(weakList) + min(weakList)
    print(premNum)
    print(encWeakness)

if __name__ == "__main__":
    main()