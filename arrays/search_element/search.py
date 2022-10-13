#
# Search an Element in a Sorted and Pivoted Array
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
# 

def search_element(arr, k):
    # This is a general search algorithm
    # Time complexity O(n)
    for i, val in enumerate(arr):
        if val == k:
            return i
    return -1

def find_pivot(arr, l):
    # This function will return the pivot in case of a rotated sorted array 
    low = 0
    high = l - 1
    
    while low < high:
        mid = (high + low) // 2
        if arr[mid] > arr[mid + 1]:
            return mid
        
        if arr[low] < arr[mid]:
            low = mid
        else:
            high = mid
    return l - 1

def binary_search(arr, k, l, h):
    # Searching element in a sorted array
    # Time Complexity O(n/2)
    while l <= h:
        mid = (l+h) // 2
        if arr[mid] == k:
            return mid
        
        if arr[mid] < k:
            l = mid + 1
        else:
            h = mid - 1
    return -1

def search_in_pivotted_array(arr, k):
    l = len(arr)
    if l <= 0:
        return -1
    
    pivot = find_pivot(arr, l)
    print(f"PIVOT: {pivot}")
    if k < arr[0]:
        return binary_search(arr, k, pivot+1, l - 1)
    else:
        return binary_search(arr, k, 0, pivot)
            
        

if __name__ == "__main__":
    print(search_element([5, 6, 7, 8, 9, 10, 1, 2, 3], 3))
    print(search_in_pivotted_array([5, 6, 7, 8, 9, 10, 1, 2, 3], 1))
    print(search_in_pivotted_array([7,0,1,2,4,5,6], 7))