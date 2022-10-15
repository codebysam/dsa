#
# Given Sum Pair
# https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/
#


def find_pivot(nums, l):
    i = 0
    j = l - 1
    mid = (i + j) // 2
    while i < j:
        mid = (i + j) // 2
        if nums[mid] > nums[mid+1]:
            return mid
        
        if nums[i] < nums[mid]:
            i = mid
        else:
            j = mid
            
    return l - 1

def find_sum_pair(nums, target):
    l = len(nums)
    pivot = find_pivot(nums, l)
    i = (pivot + 1) % l
    j = pivot
    while i != j:
        s = nums[i] + nums[j]
        print(i, j, nums[i], nums[j], s)
        if s == target:
            return True
        
        if s < target:
            i = (i + 1) % l
        else:
            j = (l + j - 1) % l
        
    return False

if __name__ == "__main__":
    print(find_sum_pair([11, 15, 6, 8, 9, 10], 40))
    print(find_sum_pair([11, 15, 26, 38, 9, 10], 35))
    print(find_sum_pair([1, 2, 3, 4, 5, 6], 7))
    print(find_sum_pair([6, 1, 2, 3, 4, 5, 6], 10))
    
     