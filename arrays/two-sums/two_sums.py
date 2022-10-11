#
# Two Sum
# https://leetcode.com/problems/two-sum/
#

def two_sum(nums, target):
        num_hash = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in num_hash and num_hash[diff] != i:
                if i < num_hash[diff]:
                    return [i, num_hash[diff]]
                else:
                    return [num_hash[diff], i]
            num_hash[nums[i]] = i
            
if __name__ == "__main__":
    print(two_sum([3,3], 6))
    print(two_sum([3,2,4], 6))