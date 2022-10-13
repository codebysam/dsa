#
# Next Permutation
# https://leetcode.com/problems/next-permutation/
# 
            

from operator import index


def find_next_permutation(nums):
    # print("\n\n\n")
    # import itertools
    # p_list = list(itertools.permutations(nums))
    # p_list.sort()
    # # print(p_list)
    
    l = len(nums)
    if l <= 1:
        return nums
    elif nums[l-2] < nums[l-1]:
        nums[l-2], nums[l-1] = nums[l-1], nums[l-2]
    else:
        left_max = nums[l-2]
        ind = l-3
        p1 = -1
        while ind >= 0:
            if nums[ind] >= left_max:
                left_max = nums[ind]
            else:
                p1 = ind
                break
            ind = ind - 1
        if p1 == -1:
            nums.sort()
            return nums
        
        temp_arr = nums[p1+1:l]
        temp_arr.sort()
        j = p1+1
        swapped = False
        while j < l:
            nums[j] = temp_arr[j-(p1+1)]
            if not swapped and nums[j] > nums[p1]:
                nums[j], nums[p1] = nums[p1], nums[j]
                swapped = True
            j = j + 1
                
    return nums
        
    
if __name__ == "__main__":
    print(find_next_permutation([2,2,7,5,4,3,2,2,1]))