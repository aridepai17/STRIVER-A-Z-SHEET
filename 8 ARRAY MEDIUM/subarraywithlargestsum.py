# SUBARRAY WITH LARGEST SUM 

'''
Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

def maxSubArraySum(nums):
    Sum = 0
    maxSum = float('-inf')
    
    for num in nums:
        Sum += num 
        
        if Sum > maxSum:
            maxSum = Sum 
            
        if Sum < 0:
            Sum = 0
            
    return maxSum 

# Examples 
nums1 = [2, 3, 5, -2, 7, -4]
print(maxSubArraySum(nums1)) # Output: 15

# Additional examples
nums2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Output: 6 (subarray [4, -1, 2, 1])
print(maxSubArraySum(nums2)) # Output: 6

nums3 = [1]  # Output: 1
print(maxSubArraySum(nums3)) # Output: 1

nums4 = [5, 4, -1, 7, 8]  # Output: 23 (subarray [5, 4, -1, 7, 8])
print(maxSubArraySum(nums4)) # Output: 23

nums5 = [-1, -2, -3, -4]  # Output: -1 (subarray [-1])
print(maxSubArraySum(nums5)) # Output: -1

nums6 = [2, -1, 2, 1, -5, 4]  # Output: 4 (subarray [2, -1, 2, 1])
print(maxSubArraySum(nums6)) # Output: 4

nums7 = [3, -2, 5, -1]  # Output: 6 (subarray [3, -2, 5])
print(maxSubArraySum(nums7)) # Output: 6

nums8 = [1, 2, 3, 4, 5]  # Output: 15 (entire array)
print(maxSubArraySum(nums8)) # Output: 15

nums9 = [-2, -3, 4, -1, -2, 1, 5, -3]  # Output: 7 (subarray [4, -1, -2, 1, 5])
print(maxSubArraySum(nums9)) # Output: 7

nums10 = [0, -1, -2, -3]  # Output: 0 (subarray [0])
print(maxSubArraySum(nums10)) # Output: 0
