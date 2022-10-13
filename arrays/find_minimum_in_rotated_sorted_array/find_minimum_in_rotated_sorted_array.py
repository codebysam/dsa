#
# Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#

def find_rotated_index(nums, l):
    low = 0
    high = l - 1
    
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid+1]:
            return mid
        
        if nums[mid] > nums[low]:
            low = mid
        else:
            high = mid
            
    return -1
            
def find_min(nums):
    l = len(nums)
    pivot = find_rotated_index(nums, l)
    return nums[pivot + 1]
            
if __name__ == "__main__":
    print(find_min([0,1,2,4,5,6,7]))
    print(find_min([7,0,1,2,4,5,6]))
    print(find_min([4,5,6,7,0,1,2]))
    print(find_min([4,5,6,7,0,1,2]))
    print(find_min([4,5,6,7,0]))
            