import json

from collections import defaultdict

cwd = []
ds = defaultdict(int)


with open("input.txt") as file:
    for line in file:
        words = line.strip().split()

        if len(words) > 2:
            if words[2] == "..":
                cwd.pop()
            else:
                cwd.append(words[2])

        if words[0].isdigit():
            for i in range(0, len(cwd)):
                dir = "/".join(cwd[: i + 1])
                size = int(words[0])
                ds[dir] += size

MAX_SIZE = 100000
max_used = 70000000 - 30000000
total_used = ds["/"]
needs_to_free = total_used - max_used
p1 = 0
p2 = 1e9

for key in ds.keys():
    if ds[key] < MAX_SIZE:
        p1 += ds[key]
    if ds[key] >= needs_to_free:
        p2 = min(p2, ds[key])

print(p1)
print(p2)

# print(json.dumps(ds, indent=4))
