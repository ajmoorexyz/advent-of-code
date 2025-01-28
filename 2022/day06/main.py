with open('input.txt') as file:
    index = 0
    char_arr = []
    for char in file.read():
        if len(set(char_arr)) == 4: # vs 14
            break
        else:
            if len (char_arr) == 4: # vs 14
                char_arr.remove(char_arr[0])
                char_arr.append(char)
            else:
                char_arr.append(char)
        index += 1
    print(index)
