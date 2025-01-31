from typing import List

from aocd import get_data

data = get_data(day=2, year=2024).split("\n")


def is_safe(nums: List[int]) -> bool:
    for i in range(1, len(nums)):
        # if nums[i] > nums[i - 1] + 3 or nums[i] == nums[i - 1] or nums[i] < nums[i - 1]:
        if nums[i] > nums[i - 1] + 3 or nums[i] <= nums[i - 1]:
            return False
    return True


# first try
# def convert_string_to_nums(string: str) -> List[int]:
#     nums: List[int] = []
#     for ch in string.split(" "):
#         nums.append(int(ch))
#     return nums


# the pythonic way
def convert_string_to_nums(string: str) -> List[int]:
    return [int(ch) for ch in string.split(" ")]


# --- PART ONE ---
# no_of_safe_reports = 0

# for d in data:
#     nums = convert_string_to_nums(d)
#     if is_safe(nums) or is_safe(nums[::-1]):
#         no_of_safe_reports += 1

# print(no_of_safe_reports)

# --- PART TWO ---

no_of_safe_reports_including_dampener = 0


# this produces a number too high
# def is_safe_with_dampener(nums: List[int]) -> bool:
#     # base case
#     # print(len(nums))
#     if len(nums) < 5:
#         return False
#     for i in range(1, len(nums) - 1):
#         if nums[i] > nums[i - 1] + 3 or nums[i] <= nums[i - 1]:
#             return is_safe_with_dampener(
#                 nums[:i] + nums[i + 1 :]
#             )  # return is key to recursion
#     return True


# this answer is too low
# def is_safe_with_dampener(nums: List[int]) -> bool:
#     # base case
#     # print(len(nums))
#     if len(nums) < 5:
#         return False
#     for i in range(1, len(nums) - 1):
#         if nums[i] > nums[i - 1] + 3 or nums[i] <= nums[i - 1]:
#             if nums != sorted(nums):
#                 return False
#             if len(set(nums)) != len(nums):
#                 return False
#             return is_safe(nums[:i] + nums[i + 1 :])  # return is key to recursion
#     return True


def is_safe_with_dampener(nums: List[int]) -> bool:
    # base case
    # print(nums)
    if len(nums) < 4:
        return False
    for i in range(1, len(nums) - 1):
        if nums[i] < nums[i - 1]:
            return is_safe_with_dampener(
                nums[: i - 1] + nums[i:]
            )  # return is key to recursion
        if nums[i] > nums[i - 1] + 3 or nums[i] <= nums[i - 1]:
            return is_safe_with_dampener(
                nums[:i] + nums[i + 1 :]
            )  # return is key to recursion
    return True


for d in data:
    nums = convert_string_to_nums(d)
    if is_safe_with_dampener(nums) or is_safe_with_dampener(nums[::-1]):
        no_of_safe_reports_including_dampener += 1

print(no_of_safe_reports_including_dampener)


assert is_safe_with_dampener([7, 6, 4, 2, 1][::-1]) is True
assert is_safe_with_dampener([1, 2, 7, 8, 9]) is False
assert is_safe_with_dampener([9, 7, 6, 2, 1][::-1]) is False
assert is_safe_with_dampener([1, 3, 2, 4, 5]) is True
assert is_safe_with_dampener([8, 6, 4, 4, 1][::-1]) is True
assert is_safe_with_dampener([1, 3, 6, 7, 9]) is True
