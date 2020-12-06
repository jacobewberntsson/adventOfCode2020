with open("data/6_1.txt", "r") as f:
    content = [line.split() for line in f.read().split("\n\n")]

def yesCounterUnique():
    nbrOfYes = 0
    for group in content:
        uniqueAnswers = set()
        for answers in group:
            for answer in answers:
                uniqueAnswers.add(answer)
        nbrOfYes += len(uniqueAnswers)
    print("Number of unique yes'ses: " + str(nbrOfYes))

def yesCounterAll():
    nbrOfYes = 0
    for group in content:
        for i, answers in enumerate(group):
            if i == 0:
                ans = set(answers)
            else:
                ans = ans.intersection(set(answers))
        nbrOfYes += len(ans)
    print("Number of questions where the group answered yes: " + str(nbrOfYes))

yesCounterUnique()
yesCounterAll()