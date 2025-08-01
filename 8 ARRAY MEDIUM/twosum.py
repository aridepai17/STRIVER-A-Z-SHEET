# TWO SUM 

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

def twoSum(nums, target):
    hashMap = {}
    n = len(nums)
    
    for i in range(n):
        complement = target - nums[i]
        
        if complement in hashMap:
            return [hashMap[complement], i]
        
        hashMap[nums[i]] = i
        
    return []

# Examples 
nums1 = [2, 7, 11, 15]
target1 = 13
print(twoSum(nums1, target1)) # Output: [0, 2]

# Additional examples
nums2 = [1, 2, 3, 4, 5]
target2 = 5  # Output: [0, 3] or [1, 2]
print(twoSum(nums2, target2)) # Output: [0, 3] or [1, 2]

nums3 = [3, 2, 4]
target3 = 6  # Output: [1, 2]
print(twoSum(nums3, target3)) # Output: [1, 2]

nums4 = [3, 3]
target4 = 6  # Output: [0, 1]
print(twoSum(nums4, target4)) # Output: [0, 1]

nums5 = [1, 5, 3, 7]
target5 = 8  # Output: [1, 3]
print(twoSum(nums5, target5)) # Output: [1, 3]

nums6 = [0, 4, 3, 0]
target6 = 0  # Output: [0, 3]
print(twoSum(nums6, target6)) # Output: [0, 3]

nums7 = [-1, -2, -3, -4, -5]
target7 = -8  # Output: [2, 4]
print(twoSum(nums7, target7)) # Output: [2, 4]

nums8 = [1, 2, 3, 4, 5, 6]
target8 = 10  # Output: [3, 4]
print(twoSum(nums8, target8)) # Output: [3, 4]

nums9 = [5, 5, 11, 1]
target9 = 10  # Output: [0, 1]
print(twoSum(nums9, target9)) # Output: [0, 1]

nums10 = [2, 1, 5, 3]
target10 = 6  # Output: [0, 2] or [1, 3]
print(twoSum(nums10, target10)) # Output: [0, 2] or [1, 3]