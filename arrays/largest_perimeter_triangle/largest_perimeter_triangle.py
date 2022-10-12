#
# Largest Perimeter Triangle
# https://leetcode.com/problems/largest-perimeter-triangle/submissions/
# 

def find_largest_perimeter_triangle_brute_force(nums):
    l = len(nums)
    sum_max_triplets = 0
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if nums[i] > nums[j] and nums[i] > nums[k]:
                    if nums[j] + nums[k] > nums[i]:
                        sum_max_triplets = max(nums[i] + nums[j] + nums[k], sum_max_triplets)
                elif nums[j] > nums[i] and nums[j] > nums[k]:
                    if nums[i] + nums[k] > nums[j]:
                        sum_max_triplets = max(nums[i] + nums[j] + nums[k], sum_max_triplets)
                else:
                    if nums[i] + nums[j] > nums[k]:
                        sum_max_triplets = max(nums[i] + nums[j] + nums[k], sum_max_triplets)
                            
    return sum_max_triplets
    
    
def find_largest_perimeter_triangle_efficient(nums):
    sum_max_triplets = 0
    n = len(nums)
    nums.sort(reverse = True)
    for i in range(0, n - 2):
        if nums[i] < (nums[i + 1] + nums[i + 2]):
            sum_max_triplets = max(sum_max_triplets, nums[i] + nums[i + 1] + nums[i + 2])
            break
 
    return sum_max_triplets

if __name__ == "__main__":
    print(find_largest_perimeter_triangle_brute_force([33, 6, 20, 1, 8, 12, 5, 55, 4, 9]))
    print(find_largest_perimeter_triangle_efficient([33, 6, 20, 1, 8, 12, 5, 55, 4, 9]))