# opponent = {
#   'A': 'rock',
#   'B': 'paper',
#   'C': 'scissors',
# }

# me = {
#   'X' : ('rock', 1),
#   'Y' : ('paper', 2),
#   'Z' : ('scissors', 3),
# }

# my_score = 0

# with open('input.txt') as file:
#     for line in file:
#         a, b = line.strip().split(' ')
#         # draw
#         if opponent[a] == me[b][0]:
#             my_score += 3
#         # win
#         elif opponent[a] == 'rock' and me[b][0] == 'paper':
#             my_score += 6
#         # win
#         elif opponent[a] == 'paper' and me[b][0] == 'scissors':
#             my_score += 6
#         # win
#         elif opponent[a] == 'scissors' and me[b][0] == 'rock':
#             my_score += 6
#         my_score += me[b][1]

# print(my_score) # part 1

default = {
  'A' : ('rock', 1),
  'B' : ('paper', 2),
  'C' : ('scissors', 3),
}

me = {
  'X' : 'lose',
  'Y' : 'draw',
  'Z' : 'win',
}

my_score = 0

with open('input.txt') as file:
    for line in file:
        a, b = line.strip().split(' ')
        if me[b] == 'lose':
            if default[a][0] == 'rock':
                my_score += default['C'][1] # scissors loses to rock
            elif default[a][0] == 'paper':
                my_score += default['A'][1] # rock loses to paper
            elif default[a][0] == 'scissors':
                my_score += default['B'][1] # paper loses to scissors
        elif me[b] == 'draw':
            my_score += default[a][1]
            my_score += 3
        elif me[b] == 'win':
            if default[a][0] == 'rock':
                my_score += default['B'][1] # paper wins to rock
            elif default[a][0] == 'paper':
                my_score += default['C'][1] # scissors wins to paper
            elif default[a][0] == 'scissors':
                my_score += default['A'][1] # rock wins to scissors
            my_score += 6


print(my_score)
