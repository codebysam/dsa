#
# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# 

def generate_product_array_except_self(nums):
    l = len(nums)
    left_products = [1] * l
    right_products = [1] * l
    for i in range(1,l):
        left_products[i] = left_products[i-1] * nums[i-1]
    for i in range(l-2,-1,-1):
        right_products[i] = right_products[i+1] * nums[i+1]
    output = []
    for i in range(l):
        output.append(left_products[i] * right_products[i])
        
    return output
        
        
    

if __name__ == "__main__":
    print(generate_product_array_except_self([1,2,3,4]))
    print(generate_product_array_except_self([-1,1,0,-3,3]))