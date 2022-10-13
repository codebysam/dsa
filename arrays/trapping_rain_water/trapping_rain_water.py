#
# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
#

def find_collected_water(height):
    l = len(height)
    left_bar_arr = [0] * l
    right_bar_arr = [0] * l
    collected_water = 0
    left_bar_arr[0] = height[0]
    for i in range(1, l):
        left_bar_arr[i] = max(left_bar_arr[i-1], height[i])
    right_bar_arr[l-1] = height[l-1]
    for i in range(l-2, -1, -1):
        right_bar_arr[i] = max(right_bar_arr[i + 1], height[i])
    for i in range(0, l):
        collected_water += min(left_bar_arr[i], right_bar_arr[i]) - height[i]
    
    return collected_water
        
            
                

if __name__ == "__main__":
    print(find_collected_water([0,1,0,3,1,0,1,2,2,1,2,1]))
    print(find_collected_water([0,1,0,2,1,0,1]))
    print(find_collected_water([4,2,0,3,2,5]))
    print(find_collected_water([4,2,3]))