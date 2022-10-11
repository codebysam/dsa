#
# Chocolate Distribution Problem
# https://www.geeksforgeeks.org/chocolate-distribution-problem/
#
from sys import maxsize

def sort_array(arr, l):
    
    for i in range(l):
        for j in range(l):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

def find_min_diff_pairs(nums, n):
    l = len(nums)
    sort_array(nums, l)
    i = 0
    min_diff = maxsize
    while i + n - 1 < l:
        if min_diff > nums[i + n - 1] - nums[i]:
            min_diff = nums[i + n - 1] - nums[i]
        i = i + 1
    return min_diff
    
    
if __name__ == "__main__":
    print(find_min_diff_pairs([7, 3, 2, 4, 9, 12, 56], 3))
    print(find_min_diff_pairs([3, 4, 1, 9, 56, 7, 9, 12], 5))