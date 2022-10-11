#
# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
#

def has_duplicate(nums):
    num_hash = {}
    flag = False
    for each_val in nums:
        if each_val in num_hash:
            return True
        num_hash[each_val] = True
    return flag
            
if __name__ == "__main__":
    print(has_duplicate([3,3]))
    print(has_duplicate([3,2,4]))