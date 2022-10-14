#
# 3Sum 
# https://leetcode.com/problems/3sum/
#

def find_triplets_with_target_sum(nums):
    target = 0
    l = len(nums)
    nums.sort()
    results = []
    for i in range(l-1):
        low = i + 1
        high = l - 1
        while (low < high):
            s = nums[i] + nums[low] + nums[high]
            if s == target:
                temp = [nums[i], nums[low], nums[high]]
                if temp not in results:
                    results.append(temp)
            if s > target:
                high = high - 1
            else:
                low = low + 1
        
    return results

def find_duplets_with_target_sum(nums):
    target = 3
    nums.sort()
    l = 0
    h = len(nums) - 1
    results = []
    while (l < h):
        s = nums[l] + nums[h]
        if s == target:
            results.append([nums[l], nums[h]])
        
        if s < target:
            l = l + 1
        else:
            h = h - 1
            
    return results
            
    
if __name__ == "__main__":
    print(find_triplets_with_target_sum([-1,0,1,2,-1,-4]))
    print(find_triplets_with_target_sum([0,1,1]))
    print(find_duplets_with_target_sum([0,1,-2,7, -4, 3, 2]))