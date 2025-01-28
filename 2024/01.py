# from utils import load_file

# load_file()

from aocd import get_data

data = get_data(day=1, year=2024).split("\n")

l, r = [], []

for d in data:
    arr = d.split("  ")  # split on two spaces
    l.append(int(arr[0]))  # cast str to int
    r.append(int(arr[1]))

l.sort()
r.sort()

# part 1
distance = 0

for i, j in zip(l, r):
    distance += abs(i - j)

# part 2
similarity = 0

for i in l:
    similarity += i * r.count(i)


print(similarity)
