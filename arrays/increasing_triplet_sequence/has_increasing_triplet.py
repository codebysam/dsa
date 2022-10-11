#
# Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/
# 

def has_increasing_triplet(nums):
    n = len(nums)
    min_ind = 0
    max_ind = n-1

    # Create an array which contains the index of the element smaller than current
    # and is on the left of the element in the input array
    smaller = [-1] * n
    for i in range(1, n):
        if (nums[i] <= nums[min_ind]):
            min_ind = i
            smaller[i] = -1
        else:
            smaller[i] = min_ind
    
    # Create an array which contains the index of the element greater than current
    # and is on the right of the element in the input array
    greater = [-1] * n
    for i in range(n-2, -1, -1):
        if (nums[i] >= nums[max_ind]):
            max_ind = i
            greater[i] = -1
        else:
            greater[i] = max_ind
    
    # If there is a number in the array which has smaller element in left 
    # and greater element in right then the pair exists
    for i in range(0, n):
        if smaller[i] != -1 and greater[i] != -1:
            return True
    
    return False
    
    
if __name__ == "__main__":
    print(has_increasing_triplet([1,2,3,4,5]))