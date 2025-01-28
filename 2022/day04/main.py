# total = 0

# def create_array(str):
#   arr = []
#   a, b = str.split('-')[0], str.split('-')[1]
#   for i in range(int(a), int(b)+1):
#     arr.append(i)
#   return arr


# with open('input.txt') as file:
#     for line in file:
#       a, b = line.strip().split(',')[0], line.strip().split(',')[1]
#       a_arr, b_arr = create_array(a), create_array(b)
#       if set(a_arr).issubset(b_arr) or set(b_arr).issubset(a_arr):
#         total += 1

# print(total) # part 1


total = 0

def create_array(str):
  arr = []
  a, b = str.split('-')[0], str.split('-')[1]
  for i in range(int(a), int(b)+1):
    arr.append(i)
  return arr


with open('input.txt') as file:
    for line in file:
      a, b = line.strip().split(',')[0], line.strip().split(',')[1]
      a_arr, b_arr = create_array(a), create_array(b)
      intersection = list(set(a_arr) & set(b_arr))
      print(intersection)
      if len(intersection) > 0:
        total += 1

print(total) # part 2
