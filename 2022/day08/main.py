from os import environ

file = "input.txt"

if "DEMO" in environ:
    file = "demo.txt"

grid = []

with open(file, "r") as f:
    for line in f:
        row = line.strip()
        grid.append(row)

rows = len(grid)
cols = len(grid[0])

p1 = 0
for row in range(rows):
    for col in range(cols):
        ct = grid[row][col]  # current tree
        # look in each direction
        # if we find a tree, increment p1
        if (
            all(ct > grid[row_above][col] for row_above in range(row))
            or all(ct > grid[row_below][col] for row_below in range(row + 1, rows))
            or all(ct > grid[row][col_left] for col_left in range(col))
            or all(ct > grid[row][col_right] for col_right in range(col + 1, cols))
        ):
            p1 += 1

print(p1)


p2 = 0
for row in range(rows):
    for col in range(cols):
        up = down = left = right = 0
        ct = grid[row][col]
        for row_above in range(row - 1, -1, -1):
            up += 1
            if grid[row_above][col] >= ct:
                break
        for row_below in range(row + 1, rows):
            down += 1
            if grid[row_below][col] >= ct:
                break
        for col_left in range(col - 1, -1, -1):
            left += 1
            if grid[row][col_left] >= ct:
                break
        for col_right in range(col + 1, cols):
            right += 1
            if grid[row][col_right] >= ct:
                break
        p2 = max(p2, up * down * left * right)

print(p2)
