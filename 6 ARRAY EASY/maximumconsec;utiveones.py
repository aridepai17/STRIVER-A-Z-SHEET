# MAXIMUM CONSECUTIVE ONES 

'''
iven a binary array nums, return the maximum number of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.
'''

def findMaxConsecutiveOnes(nums):
    count = 0
    maxCount = 0
    
    for num in nums:
        if num == 1:
            count += 1
            maxCount = max(maxCount, count)
        else:
            count = 0
    
    return maxCount

# Examples
nums1 = [1, 1, 0, 0, 1, 1, 1, 0]
print(findMaxConsecutiveOnes(nums1))  # Output: 3

# Additional examples
nums2 = [1, 1, 1, 1, 0, 0, 0]  # Output: 4
print(findMaxConsecutiveOnes(nums2))  # Output: 4

nums3 = [0, 0, 0, 0]  # Output: 0
print(findMaxConsecutiveOnes(nums3))  # Output: 0

nums4 = [1, 0, 1, 1, 1, 0, 1]  # Output: 3
print(findMaxConsecutiveOnes(nums4))  # Output: 3

nums5 = [1, 1, 0, 1, 1, 1, 1]  # Output: 4
print(findMaxConsecutiveOnes(nums5))  # Output: 4

nums6 = [0, 1, 1, 1, 0, 1, 1]  # Output: 3
print(findMaxConsecutiveOnes(nums6))  # Output: 3

nums7 = [1, 1, 1, 0, 1, 1]  # Output: 3
print(findMaxConsecutiveOnes(nums7))  # Output: 3

nums8 = [1, 0, 0, 1, 0, 1, 1, 1]  # Output: 3
print(findMaxConsecutiveOnes(nums8))  # Output: 3

nums9 = [1, 1, 1, 1, 1]  # Output: 5
print(findMaxConsecutiveOnes(nums9))  # Output: 5

nums10 = [0, 1, 0, 1, 0, 1, 0]  # Output: 1
print(findMaxConsecutiveOnes(nums10))  # Output: 1