with open("data/13_1.txt", "r") as f:
    content = f.read().split('\n')


timestamp, busIDs = content
current_time, busses = int(timestamp), [int(bus) for bus in busIDs.split(",") if bus != 'x']
next_bus, next_bus_id = min((bus * (current_time // bus + 1), bus) for bus in busses)
res = (next_bus - current_time) * next_bus_id
print("Part 1: " + str(res))


reqs = [(int(bus_id), offset) for offset, bus_id in enumerate(busIDs.split(',')) if bus_id != 'x']
delta, time = 1, 10000

for bus, offset in reqs:
    while (time + offset) % bus != 0:
        time += delta
    delta *= bus

print("Part 2: " + str(time))