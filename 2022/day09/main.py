from os import environ

file = "input.txt"

if "DEMO" in environ:
    file = "demo.txt"

instructions = []

hx = hy = 0
tx = ty = 0

directions = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

with open(file, "r") as f:
    for line in f:
        words = line.strip().split()
        instructions.append((words[0], int(words[1])))


def touching():
    global hx, hy, tx, ty

    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
        return True


def move(dx, dy):
    global hx, hy, tx, ty

    hx += dx
    hy += dy

    if not touching():
        sign_x = 0 if hx == tx else (hx - tx) // abs(hx - tx)
        sign_y = 0 if hy == ty else (hy - ty) // abs(hy - ty)

        tx += sign_x
        ty += sign_y


tail_positions_visited = set()
tail_positions_visited.add((tx, ty))

for instruction in instructions:
    d, amount = instruction[0], instruction[1]

    dx, dy = directions[d]

    for _ in range(amount):
        move(dx, dy)
        tail_positions_visited.add((tx, ty))

# Keep track of the number of tail positions visited.
p1: int = len(tail_positions_visited)

print(p1)
