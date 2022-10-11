#
# Write a program to reverse an array or string
# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
#

def reverse_arr(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i = i + 1
        j = j - 1

if __name__ == "__main__":
    arr1 = [7, 5, 21, 3, 4, 1, 19, 5]
    print(f"Array items before reversing: {arr1}")
    reverse_arr(arr1)
    print(f"Array items after reversing: {arr1}")