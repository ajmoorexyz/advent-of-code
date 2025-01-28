# total = 0

# with open('input.txt') as file:
#     for line in file:
#         s = line.strip()
#         a, b = s[:len(s)//2], s[len(s)//2:]
#         match = [x for x in a if x in b][0]

#         if match.isupper():
#           total += ord(match) - 38
#         else:
#           total += ord(match) - 96

# print(total) # part 1

total = 0

with open('input.txt') as file:
    arr = []
    for line in file:
        if len(arr) < 3:
          arr.append(line.strip())
          if len(arr) == 3:
            a, b, c = arr[0], arr[1], arr[2]
            for i in a:
              if i in b and i in c:
                match = i

            if match.isupper():
              total += ord(match) - 38
            else:
              total += ord(match) - 96
            arr = []

print(total) # part 2
