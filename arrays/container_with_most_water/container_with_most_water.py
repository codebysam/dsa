#
# 
# 
#

from sys import maxsize

def find_container_with_max_water(height):
    print("#################################")
    l = len(height)
    
    left_bars = [0] * l
    left_bars[0] = height[0]
    right_bars = [0] * l
    right_bars[l-1] = height[l-1]
    
    height_maps = {}
    height_maps[left_bars[0]] = 0
    height_maps[right_bars[l-1]] = 0
    
    for i in range(1,l):
        left_bars[i] = max(left_bars[i-1], height[i])
        height_maps[left_bars[i]] = 0
    for i in range(l-2, -1, -1):
        right_bars[i] = max(right_bars[i+1], height[i])
        height_maps[right_bars[i]] = 0
    
    print(height)
    print(height_maps)
    
    max_collected_water = -maxsize - 1
    for h in height_maps:
        collected_water = 0
        i = 0
        while i < l: 
            if height[i] >= h: break
            i += 1
            
        j = l - 1
        while j > -1: 
            if height[j] >= h: break
            j -= 1
        collected_water = h * (j - i)
        print(h, i, j, collected_water)
        max_collected_water = max(max_collected_water, collected_water)
        
    return max_collected_water

        
        
    
if __name__ == "__main__":
    print(find_container_with_max_water([5,2,3,1,8,6,2,5,4,8,3,7]))
    print(find_container_with_max_water([1,1]))
    print(find_container_with_max_water([1,1,2]))
        