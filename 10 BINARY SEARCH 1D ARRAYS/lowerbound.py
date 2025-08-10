# LOWER BOUND 

'''
Given a sorted array of nums and an integer x, write a program to find the lower bound of x.
The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
If no such index is found, return the size of the array.
'''

def lowerBound(nums, x):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= x:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ans

# Examples
nums1 = [1, 2, 2, 3]
x1 = 2
print(lowerBound(nums1, x1)) # Output: 1

# Additional examples
nums2 = [1, 2, 3, 4, 5]
x2 = 3
print(lowerBound(nums2, x2)) # Output: 2

nums3 = [1, 2, 3, 4, 5]
x3 = 6
print(lowerBound(nums3, x3)) # Output: 5

nums4 = [2, 4, 6, 8, 10]
x4 = 5
print(lowerBound(nums4, x4)) # Output: 3

nums5 = [2, 4, 6, 8, 10]
x5 = 10
print(lowerBound(nums5, x5)) # Output: 4

nums6 = [5, 6, 7, 8, 9]
x6 = 5
print(lowerBound(nums6, x6)) # Output: 0

nums7 = [1, 3, 5, 7, 9]
x7 = 1
print(lowerBound(nums7, x7)) # Output: 0

nums8 = [1, 3, 5, 7, 9]
x8 = 9
print(lowerBound(nums8, x8)) # Output: 4

nums9 = [10, 20, 30, 40, 50]
x9 = 25
print(lowerBound(nums9, x9)) # Output: 2

nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x10 = 8
print(lowerBound(nums10, x10)) # Output: 7