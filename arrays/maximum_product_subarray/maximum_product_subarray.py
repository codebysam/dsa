#
# Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# #

def find_max_prod_subarray(nums):
    n = len(nums)
    max_ending_here = nums[0]
    min_ending_here = nums[0]
    max_so_far = nums[0]
    for i in range(1, n):
        temp = max(nums[i], nums[i] * max_ending_here, nums[i] * min_ending_here)
        min_ending_here = min(nums[i], nums[i] * max_ending_here, nums[i] * min_ending_here)
        max_ending_here = temp
        max_so_far = max(max_so_far, max_ending_here)
      
    return max_so_far

            
if __name__ == "__main__":
    print(find_max_prod_subarray([-1, -7, 2, 3, -2, 4]))
    print(find_max_prod_subarray([-3, -2, -5, 1]))
    print(find_max_prod_subarray([0,2]))
    print(find_max_prod_subarray([-2]))
    print(find_max_prod_subarray([-3,0,1,2,3,-2]))