# LARGEST SUBARRAY WITH SUM 0

'''
Given an array arr[] containing both positive and negative integers, the task is to find the length of the longest subarray with a sum equals to 0.
Note: A subarray is a contiguous part of an array, formed by selecting one or more consecutive elements while maintaining their original order.
'''

def maxLengthofSubarray(nums):
    hashMap = {}
    Sum = 0
    maxLength = 0
    n = len(nums)
    
    for i in range(n):
        Sum += nums[i]
        
        if Sum == 0:
            maxLength = i + 1
        else:
            if Sum in hashMap:
                maxLength = max(maxLength,  i - hashMap[Sum])
            else:
                hashMap[Sum] = i
                
    return maxLength

# Examples
nums1 = [15, -2, 2, -8, 1, 7, 10, 23]
print(maxLengthofSubarray(nums1)) # Output: 5

# Additional examples
nums2 = [1, 2, -2, 1]
print(maxLengthofSubarray(nums2)) # Output: 3

nums3 = [0, 0, 0, 0]
print(maxLengthofSubarray(nums3)) # Output: 4

nums4 = [1, -1, 2, -2, 3, -3]
print(maxLengthofSubarray(nums4)) # Output: 6

nums5 = [4, -1, -2, 1, 4, -4]
print(maxLengthofSubarray(nums5)) # Output: 5

nums6 = [1, 2, 3, -3, -2, -1]
print(maxLengthofSubarray(nums6)) # Output: 6

nums7 = [5, 1, -1, -5, 2, 3, -2]
print(maxLengthofSubarray(nums7)) # Output: 7

nums8 = [1, 2, 3, 4, -10]
print(maxLengthofSubarray(nums8)) # Output: 4

nums9 = [-1, -1, 1, 1]
print(maxLengthofSubarray(nums9)) # Output: 4

nums10 = [2, -2, 3, -3, 4, -4]
print(maxLengthofSubarray(nums10)) # Output: 6

nums11 = [1, 2, 3, 4, 5]
print(maxLengthofSubarray(nums11)) # Output: 0
