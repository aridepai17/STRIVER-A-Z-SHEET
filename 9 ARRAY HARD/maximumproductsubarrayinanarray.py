# MAXIMUM PRODUCT SUBARRAY IN AN ARRAY 

'''
Given an integer array nums. 
Find the subarray with the largest product, and return the product of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

def maxProductSubarray(nums):
    maxProd = nums[0]
    minProd = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        current = nums[i]
        
        tempMax = max(current, maxProd * current, minProd * current)
        minProd = min(current, maxProd * current, minProd * current)
        maxProd = tempMax
        result = max(result, maxProd)
        
    return result

# Examples 
nums1 = [4, 5, 3, 7, 1, 2]
print(maxProductSubarray(nums1)) # Output: 840

# Additional examples
nums2 = [2, 3, -2, 4]
print(maxProductSubarray(nums2)) # Output: 6

nums3 = [-2, 0, -1]
print(maxProductSubarray(nums3)) # Output: 0

nums4 = [-2, 3, -4]
print(maxProductSubarray(nums4)) # Output: 24

nums5 = [1, 2, 3, 0, 4, 5]
print(maxProductSubarray(nums5)) # Output: 20

nums6 = [0, 2, 0, 3]
print(maxProductSubarray(nums6)) # Output: 3

nums7 = [2, -5, -2, -4, 3]
print(maxProductSubarray(nums7)) # Output: 24

nums8 = [-1, -3, -10, 0, 60]
print(maxProductSubarray(nums8)) # Output: 60

nums9 = [1, -2, -3, 0, 7]
print(maxProductSubarray(nums9)) # Output: 7

nums10 = [3, -1, 4]
print(maxProductSubarray(nums10)) # Output: 12