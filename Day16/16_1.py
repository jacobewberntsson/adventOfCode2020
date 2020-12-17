import re
from collections import defaultdict

with open("data/16_1.txt", "r") as f:
    content = [line.strip() for line in f]

rules = defaultdict(list)
validRanges = set()
for line in content[:20]:
    rulename = re.match(r"(\w+( \w+)?):", line).group(1)
    for r in re.findall(r"\d+\-\d+", line):
        rules[rulename].append(tuple(int(x) for x in r.split("-")))
        validRanges.add(tuple(int(x) for x in r.split("-")))

errorRate = 0
validTickets = []
for line in content[25:]:
    values = [int(x) for x in line.split(",")]
    for v in values:
        valid = False
        for low, high in validRanges:
            if low <= v <= high:
                valid = True
                break
        if not valid:
            errorRate += v
            break
    if valid:
        validTickets.append(values)

possible_fields = {i: set(rules.keys()) for i in range(len(validTickets[0]))}
for ticket in validTickets:
    for i, value in enumerate(ticket):
        for field in rules:
            possible = False
            for low, high in rules[field]:
                if low <= value <= high:
                    possible = True
                    break
            if not possible:
                possible_fields[i].discard(field)

for i in sorted(possible_fields, key=lambda k: len(possible_fields[k])):
    this_field = next(iter(possible_fields[i]))
    for j in possible_fields:
        if i != j:
            possible_fields[j].discard(this_field)

my_ticket = [int(x) for x in content[22].split(",")]
ans = 1
for i in possible_fields:
    if possible_fields[i].pop().startswith("departure"):
        ans *= my_ticket[i]

print(errorRate)
print(ans)