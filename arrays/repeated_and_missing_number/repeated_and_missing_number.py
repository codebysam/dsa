#
# Missing Number
# https://leetcode.com/problems/missing-number/
#
# Repeat and Missing Number Array
# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# 

def list_sum(nums):
    sum = 0
    for i in nums:
        sum = sum + i
    return sum

def find_missing_number(nums):
    l = len(nums)
    expected_sum = (l * (l + 1)) // 2
    s = list_sum(nums)
    return expected_sum - s

def find_repeated_and_missing_number(nums):
    h_map = {}
    repeated_val = 0
    for i in nums:
        if i in h_map:
            repeated_val = i
        h_map[i] = True
    
    l = len(nums)
    s = list_sum(nums)
    expected_sum = (l * (l + 1)) // 2
    return [repeated_val, expected_sum + repeated_val - s]

if __name__ == "__main__":
    print(find_missing_number([3,0,1]))
    print(find_repeated_and_missing_number([3, 1, 2, 5, 3]))
    print(find_repeated_and_missing_number([4, 1, 2, 5, 3]))