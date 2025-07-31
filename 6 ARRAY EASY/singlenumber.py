# SINGLE NUMBER 

'''
Given an array of nums of n integers.
Every integer in the array appears twice except one integer. 
Find the number that appeared once in the array.
'''

def singleNumber(nums):
    xor = 0
    
    for num in nums:
        xor ^= num
        
    return xor

# Alternate approach using hashmaps

def singleNumber(nums):
    hashmap = {}
    
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1
        
    for key, value in hashmap.items():
        if value == 1:
            return key
        
# Examples
nums1 = [1, 2, 2, 4, 3, 1, 4]
print(singleNumber(nums1)) # Output: 3

# Additional examples
nums2 = [2, 2, 1]  # Output: 1
print(singleNumber(nums2)) # Output: 1

nums3 = [4, 1, 2, 1, 2]  # Output: 4
print(singleNumber(nums3)) # Output: 4

nums4 = [1]  # Output: 1
print(singleNumber(nums4)) # Output: 1

nums5 = [5, 5, 6, 6, 7, 7, 8]  # Output: 8
print(singleNumber(nums5)) # Output: 8

nums6 = [10, 10, 20, 20, 30]  # Output: 30
print(singleNumber(nums6)) # Output: 30

nums7 = [0, 1, 0, 1, 2]  # Output: 2
print(singleNumber(nums7)) # Output: 2

nums8 = [3, 3, 7, 7, 8, 8, 9]  # Output: 9
print(singleNumber(nums8)) # Output: 9

nums9 = [6, 6, 2, 2, 3, 3, 4]  # Output: 4
print(singleNumber(nums9)) # Output: 4

nums10 = [1, 1, 2, 2, 3, 3, 4, 4, 5]  # Output: 5
print(singleNumber(nums10)) # Output: 5