from collections import defaultdict
from os import environ

file = "input.txt"

cwd = []

if "DEMO" in environ:
    file = "demo.txt"

fs = defaultdict(int)

with open(file, "r") as f:
    for line in f:
        words = line.strip().split()

        if len(words) == 3:
            if words[2] == "..":
                cwd.pop()
            else:
                cwd.append(words[2])

        if words[0].isnumeric():
            for i in range(len(cwd)):
                fs["/".join(cwd[: i + 1])] += int(words[0])


p1 = 0
MAX_SIZE = 1e5

for key in fs.keys():
    if fs[key] < MAX_SIZE:
        p1 += fs[key]

print(p1)

p2 = 1e9

# setup for part 2
DISK_SIZE = 7e7
MIN_AMOUNT_OF_FREE_DISK = 3e7
MAX_USED = DISK_SIZE - MIN_AMOUNT_OF_FREE_DISK
DISK_USED = fs["/"]
DISK_TO_FREE = DISK_USED - MAX_USED

for key in fs.keys():
    if fs[key] > DISK_TO_FREE:
        p2 = min(p2, fs[key])

print(p2)


# print(json.dumps(fs))
