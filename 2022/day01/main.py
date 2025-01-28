elves = []
elf_calorie_count = 0

with open('input.txt') as file:
    for line in file:
        if len(line) > 1:
          elf_calorie_count += int(line)
        else:
          elves.append(elf_calorie_count)
          elf_calorie_count = 0

print(max(elves)) # part1
print(sum(sorted(elves)[-3:])) # part2
