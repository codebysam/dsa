#
# Largest Sum Contiguous Subarray (Kadane’s Algorithm)
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
#

from sys import maxsize

def find_max_subarray(arr):
    max_till_index = 0
    overall_max = -maxsize - 1
    start = 0
    end = 0
    p1 = 0
    
    for i in range(len(arr)):
        max_till_index = max_till_index + arr[i]
        if overall_max < max_till_index:
            overall_max = max_till_index
            start = p1
            end = i
            
        if max_till_index < 0:
            max_till_index = 0
            p1 = i + 1
    print(f"Starting index: {start} Ending index: {end}")    
    return overall_max


if __name__ == "__main__":
    max_val = find_max_subarray([-2, -3, 4, -1, -2, 3, 5, -3])
    print(f"Maximum sum of a contiguous sub array: {max_val}")
    
    