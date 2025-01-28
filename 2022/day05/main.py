with open('input.txt') as file:
    stacks, instructions = file.read().split('\n\n')

    arr = []

    for i in stacks.split('\n'):
        arr.append(i)

    arr.reverse()

    stack_numbers, stacks = arr[0].replace(' ', ''), arr[1:]

    number_of_stacks = len(stack_numbers)

    rows_of_stacks = {}

    for row in stacks:
      n = 1
      offset = 0
      while n < number_of_stacks:
        if n not in rows_of_stacks.keys():
          rows_of_stacks[n] = []
        crate = row[offset:offset+4].strip()
        if crate:
          rows_of_stacks[n].append(crate[1:2])
        offset += 4
        n += 1
      last_crate = row[(n * 4) -4:]
      if n not in rows_of_stacks.keys():
          rows_of_stacks[n] = []
      if last_crate:
          rows_of_stacks[n].append(last_crate[1:2])
      n = 0
      offset = 0

    # print(rows_of_stacks)

    instructions = instructions.split('\n')

    for instruction in instructions:
      instruction = instruction.replace('move ', '').replace(' from', '').replace(' to', '').split(' ')
      number_of_crates = int(instruction[0])
      from_stack = int(instruction[1])
      to_stack = int(instruction[2])

      # part 1
      # for i in range(number_of_crates):
      #   rows_of_stacks[to_stack].append(rows_of_stacks[from_stack].pop())

      # part 2
      rows_of_stacks[to_stack].extend(rows_of_stacks[from_stack][len(rows_of_stacks[from_stack]) - number_of_crates:])
      rows_of_stacks[from_stack] = rows_of_stacks[from_stack][:len(rows_of_stacks[from_stack]) - number_of_crates]

    # answer builder
    str = ''
    for i in range(1, number_of_stacks + 1):
      str += rows_of_stacks[i][-1]

    # answer
    print(str)
