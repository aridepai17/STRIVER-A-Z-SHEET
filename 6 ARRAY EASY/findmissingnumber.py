# FIND MISSING NUMBER 

'''
Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), 
return the only number missing from the array within this range.
'''

def missingNumber(nums):
    xor1 = 0
    xor2 = 0 
    n = len(nums)
    
    for i in range(n):
        xor1 ^= nums[i]
        xor2 ^= i
    
    xor2 ^= n
        
    return xor1 ^ xor2

# Alternate approach using n*(n+1)//2

def missingNumber(nums):
    n = len(nums)
    expectedSum  = n * (n + 1) // 2
    actualSum = sum(nums) 
    return expectedSum - actualSum

# Examples 
nums1 = [0, 2, 3, 1, 4]
print(missingNumber(nums1)) # Output: 5

nums2 = [0]  
print(missingNumber(nums2)) # Output: 1

nums3 = [1, 0]  
print(missingNumber(nums3)) # Output: 2

nums4 = [0, 1, 2, 3]  
print(missingNumber(nums4)) # Output: 4

nums5 = [0, 1, 3]  
print(missingNumber(nums5)) # Output: 2

nums6 = [1, 2, 3, 4, 5]  
print(missingNumber(nums6)) # Output: 0

nums7 = [0, 1, 2, 4, 5]  
print(missingNumber(nums7)) # Output: 3

nums8 = [0, 1, 3, 4, 5, 6]  
print(missingNumber(nums8)) # Output: 2

nums9 = [0, 1, 2, 3, 5]  
print(missingNumber(nums9)) # Output: 4

nums10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
print(missingNumber(nums10)) # Output: 10

nums11 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
print(missingNumber(nums11)) # Output: 0