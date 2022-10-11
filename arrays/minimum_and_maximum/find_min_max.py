#
# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
# Maximum and minimum of an array using minimum number of comparisons
#

def find_min_max(arr):
    if len(arr) == 0:
        return None, None
    min_val = arr[0]
    max_val = arr[0]
    for value in arr:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
            
    return min_val, max_val

if __name__ == "__main__":
    arr = [7, 5, 21, 3, 4, 1, 19]
    min_value, max_value = find_min_max(arr)
    print(f"Array items: {arr}")
    print(f"Minimum: {min_value}")
    print(f"Maximum: {max_value}")