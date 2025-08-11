# FLOOR AND CEIL IN SORTED ARRAY

'''
Given a sorted array nums and an integer x. 
Find the floor and ceil of x in nums. 
The floor of x is the largest element in the array which is smaller than or equal to x. 
The ceiling of x is the smallest element in the array greater than or equal to x. 
If no floor or ceil exists, output -1.
'''

def getFloorandCeil(nums, x):
    left = 0
    right = len(nums) - 1
    floorVal = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= x:
            floorVal = nums[mid]
            left = mid + 1
        else:
            right = mid - 1
            
    left = 0
    right = len(nums) - 1
    ceilVal = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= x:
            ceilVal = nums[mid]
            right = mid - 1
        else:
            left = mid + 1
    
    return floorVal, ceilVal

# Examples
nums1 = [3, 4, 4, 7, 8, 10]
x1 = 5
print(getFloorandCeil(nums1, x1)) # Output: 4 7

# Additional examples
nums2 = [1, 2, 3, 4, 5]
x2 = 3
print(getFloorandCeil(nums2, x2)) # Output: 3 3

nums3 = [1, 2, 3, 4, 5]
x3 = 0
print(getFloorandCeil(nums3, x3)) # Output: -1 1

nums4 = [1, 2, 3, 4, 5]
x4 = 6
print(getFloorandCeil(nums4, x4)) # Output: 5 -1

nums5 = [10, 20, 30, 40, 50]
x5 = 25
print(getFloorandCeil(nums5, x5)) # Output: 20 30

nums6 = [5, 10, 15, 20]
x6 = 15
print(getFloorandCeil(nums6, x6)) # Output: 15 15

nums7 = [1, 3, 5, 7, 9]
x7 = 8
print(getFloorandCeil(nums7, x7)) # Output: 7 9

nums8 = [1, 2, 3, 4, 5]
x8 = 2.5
print(getFloorandCeil(nums8, x8)) # Output: 2 3

nums9 = [1, 2, 3, 4, 5]
x9 = 1
print(getFloorandCeil(nums9, x9)) # Output: 1 1

nums10 = [1, 2, 3, 4, 5]
x10 = 4.5
print(getFloorandCeil(nums10, x10)) # Output: 4 5