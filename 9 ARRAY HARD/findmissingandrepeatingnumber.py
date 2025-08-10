# FIND MISSING AND REPEATING NUMBER 

'''
Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, 
except for A, which appears twice and B which is missing.
Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
Note: You are not allowed to modify the original array.
'''

def findMissingRepeatingNumbers(nums):
    n = len(nums)
    
    actualSum = sum(nums)
    actualSquareSum = sum(x * x for x in nums)
    
    expectedSum = n * (n + 1) // 2
    expectedSquareSum = n * (n + 1) * (2 * n + 1) // 6
    
    diff1 = actualSum - expectedSum 
    diff2 = actualSquareSum - expectedSquareSum
    
    absSum = diff2 // diff1 
    
    A = (diff1 + absSum) // 2
    B = absSum - A 
    
    return [A, B]

# Examples 
nums1 = [3, 5, 4, 1, 1]
print(findMissingRepeatingNumbers(nums1)) # Output: [1, 2]

# Additional examples
nums2 = [1, 2, 2, 4]
print(findMissingRepeatingNumbers(nums2)) # Output: [2, 3]

nums3 = [2, 3, 3, 1]
print(findMissingRepeatingNumbers(nums3)) # Output: [3, 4]

nums4 = [1, 1]
print(findMissingRepeatingNumbers(nums4)) # Output: [1, 2]

nums5 = [5, 3, 4, 2, 2]
print(findMissingRepeatingNumbers(nums5)) # Output: [2, 1]

nums6 = [1, 2, 3, 4, 5, 5]
print(findMissingRepeatingNumbers(nums6)) # Output: [5, 6]

nums7 = [6, 1, 2, 3, 4, 4, 5]
print(findMissingRepeatingNumbers(nums7)) # Output: [4, 7]

nums8 = [1, 2, 3, 3, 5]
print(findMissingRepeatingNumbers(nums8)) # Output: [3, 4]

nums9 = [1, 2, 2, 3, 4, 5, 6]
print(findMissingRepeatingNumbers(nums9)) # Output: [2, 7]

nums10 = [1, 1, 1, 1, 1]
print(findMissingRepeatingNumbers(nums10)) # Output: [1, 2]
    
    