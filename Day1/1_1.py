from itertools import combinations
import math

f = open("data/1_1.txt", "r")
content = f.readlines()
content = [int(x.strip()) for x in content]
content.sort()
n = 2020
f.close()

def entry_sum1():
    
    for i in range(len(content)):
        firstValue = content[i]
        secondValue = n - firstValue
        if secondValue in content:
            break
    
    print("the found pair is: (" + str(firstValue) + ", " + str(secondValue) + ")")
    print("Which adds up to: " + str(firstValue*secondValue))

def entry_sum2():
    numOfValues = 3

    possible_comb = list(combinations(content, numOfValues))

    solution = [x for x in possible_comb if sum(x)==n]
    solutionList = [item for t in solution for item in t]
    print("the values adding up to 2020 is: " + str(solutionList))
    print("With a total product of: " + str((math.prod(solutionList))))
    
entry_sum1()
entry_sum2()