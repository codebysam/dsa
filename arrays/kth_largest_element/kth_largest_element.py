#
# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# #

def find_kth_largest(nums, k):
    nums.sort(reverse=True)
    if k <= len(nums):
        return nums[k-1]
    else:
        return 0

if __name__ == "__main__":
    print(find_kth_largest([3,2,1,5,6,4],2))