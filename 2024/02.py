from typing import List

from aocd import get_data

data = get_data(day=2, year=2024).split("\n")


# ######### WITHOUT HELP #########


# def is_safe(ints: List[int]) -> bool:
#     for i in range(1, len(ints)):
#         # if ints[i] > ints[i - 1] + 3 or ints[i] == ints[i - 1] or ints[i] < ints[i - 1]:
#         if ints[i] > ints[i - 1] + 3 or ints[i] <= ints[i - 1]:
#             return False
#     return True


# first try
# def convert_string_to_ints(string: str) -> List[int]:
#     ints: List[int] = []
#     for ch in string.split(" "):
#         ints.append(int(ch))
#     return ints


# the pythonic way
# def convert_string_to_ints(string: str) -> List[int]:
#     return [int(ch) for ch in string.split(" ")]


# --- PART ONE ---
# no_of_safe_reports = 0

# for d in data:
#     ints = convert_string_to_ints(d)
#     if is_safe(ints) or is_safe(ints[::-1]):
#         no_of_safe_reports += 1

# print(no_of_safe_reports)

# --- PART TWO ---

###############################################################################
# I got shut down pretty good here
# While all the testcases passed, return the number safe reports was wrong
###############################################################################

# no_of_safe_reports_including_dampener = 0


# this produces a number too high
# def is_safe_with_dampener(ints: List[int]) -> bool:
#     # base case
#     # print(len(ints))
#     if len(ints) < 5:
#         return False
#     for i in range(1, len(ints) - 1):
#         if ints[i] > ints[i - 1] + 3 or ints[i] <= ints[i - 1]:
#             return is_safe_with_dampener(
#                 ints[:i] + ints[i + 1 :]
#             )  # return is key to recursion
#     return True

# if not 1 <= ints[i + 1] - ints[i] <= 3:
#     break  # this combo is unsafe


# this answer is too low
# def is_safe_with_dampener(ints: List[int]) -> bool:
#     # base case
#     # print(len(ints))
#     if len(ints) < 5:
#         return False
#     for i in range(1, len(ints) - 1):
#         if ints[i] > ints[i - 1] + 3 or ints[i] <= ints[i - 1]:
#             if ints != sorted(ints):
#                 return False
#             if len(set(ints)) != len(ints):
#                 return False
#             return is_safe(ints[:i] + ints[i + 1 :])  # return is key to recursion
#     return True


# 649 - not right
# def is_safe_with_dampener(ints: List[int]) -> bool:
#     # print(len(ints))
#     # print(ints)
#     # base case
#     if len(ints) < 4:
#         return False
#     for i in range(1, len(ints)):
#         # if ints[i] < ints[i - 1]:
#         #     return is_safe_with_dampener(
#         #         ints[: i - 1] + ints[i:]
#         #     )  # return is key to recursion
#         if ints[i] > ints[i - 1] + 3 or ints[i] <= ints[i - 1]:
#             return is_safe_with_dampener(
#                 ints[: i - 1] + ints[i:] # clue #1
#             )  # return is key to recursion
#     return True


# 653
# def is_safe_with_dampener(ints: List[int]) -> bool:
#     safe = False

#     if is_safe(ints):
#         safe = True

#     if not safe:
#         for i in range(len(ints) - 1):
#             ints = ints[:i] + ints[i + 1 :] clue #2
#             if is_safe(ints) or is_safe(ints[::-1]):
#                 safe = True
#                 break

#     return safe


# for d in data[0:20]:
#     ints = convert_string_to_ints(d)
#     if is_safe_with_dampener(ints) or is_safe_with_dampener(ints[::-1]):
#         no_of_safe_reports_including_dampener += 1

# print(data[0:10])
# print(no_of_safe_reports_including_dampener)

# assert is_safe_with_dampener([7, 6, 4, 2, 1][::-1]) is True
# assert is_safe_with_dampener([1, 2, 7, 8, 9]) is False
# assert is_safe_with_dampener([9, 7, 6, 2, 1][::-1]) is False
# assert is_safe_with_dampener([1, 3, 2, 4, 5]) is True
# assert is_safe_with_dampener([8, 6, 4, 4, 1][::-1]) is True
# assert is_safe_with_dampener([1, 3, 6, 7, 9]) is True

# 566 - correct answer

###############################################################################
# I turned to GitHub for help
# https://github.com/mebeim/aoc/blob/master/2024/solutions/day02.py
###############################################################################


def convert_string_to_ints(string: str) -> List[int]:
    return [int(ch) for ch in string.split(" ")]


# # this isn't working
# def within_tolerance(i: int, j: int) -> bool:
#     return 1 <= j - i <= 3


def safe(ints: List[int], allow_removal=False) -> bool:
    for i in range(len(ints) - 1):
        if not 1 <= ints[i + 1] - ints[i] <= 3:
            break
    else:
        return True

    if not allow_removal:
        return False

    # i is still in scope, lets use it
    # either i or i + 1 are potential dampeners

    # i case
    # arr = [0, 1, 2, 3, 4] for i = 2 -> arr = [1, 3, 4]
    rest = ints[i - 1 : i] + ints[i + 1 :]

    for j in range(len(rest) - 1):
        if not 1 <= rest[j + 1] - rest[j] <= 3:
            # if not within_tolerance(rest[j], rest[j] + 1):
            # remember, we can only remove 1 list entry
            # if j > 0 lets move onto i + 1
            if j > 0:
                return False
            break  # move onto i + 1
    else:
        return True

    # i + 1 case
    # arr = [0, 1, 2, 3, 4] for i = 2 -> arr = [2, 4]
    rest = ints[i : i + 1] + ints[i + 2 :]

    for j in range(len(rest) - 1):
        if not 1 <= rest[j + 1] - rest[j] <= 3:
            # if not within_tolerance(rest[j], rest[j] + 1):
            return False
    else:
        return True


safe_reports = safe_reports_w_removal = 0

for d in data:
    ints = convert_string_to_ints(d)

    if safe(ints) or safe(ints[::-1]):
        safe_reports += 1
        continue  # skip to the next iteration; e.g. no need for a dampener

    if safe(ints, True) or safe(ints[::-1], True):
        safe_reports_w_removal += 1


print("part1: ", safe_reports)
print("part2: ", safe_reports + safe_reports_w_removal)
