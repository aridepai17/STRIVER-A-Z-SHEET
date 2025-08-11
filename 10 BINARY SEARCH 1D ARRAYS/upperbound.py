# UPPER BOUND

'''
Given a sorted array of nums and an integer x, write a program to find the upper bound of x.
The upper bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than a given key i.e. x.
If no such index is found, return the size of the array.
'''

def upperBound(nums, x):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > x:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ans

# Examples 
nums1 = [1, 2, 2, 3]
x1 = 2
print(upperBound(nums1, x1)) # Output: 3 

# Additional examples
nums2 = [1, 3, 5, 7, 9]
x2 = 4
print(upperBound(nums2, x2)) # Output: 3

nums3 = [1, 2, 3, 4, 5]
x3 = 5
print(upperBound(nums3, x3)) # Output: 5

nums4 = [1, 1, 1, 1, 1]
x4 = 1
print(upperBound(nums4, x4)) # Output: 5

nums5 = [2, 4, 6, 8, 10]
x5 = 5
print(upperBound(nums5, x5)) # Output: 3

nums6 = [10, 20, 30, 40, 50]
x6 = 25
print(upperBound(nums6, x6)) # Output: 2

nums7 = [1, 2, 3, 4, 5, 6]
x7 = 0
print(upperBound(nums7, x7)) # Output: 0

nums8 = [1, 2, 3, 4, 5]
x8 = 6
print(upperBound(nums8, x8)) # Output: 5

nums9 = [5, 10, 15, 20]
x9 = 15
print(upperBound(nums9, x9)) # Output: 3

nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x10 = 8
print(upperBound(nums10, x10)) # Output: 8 