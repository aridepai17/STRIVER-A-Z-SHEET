# LONGEST SUBARRAY WITH SUM K INCLUDING NEGATIVES 

'''
Given an array nums of size n and an integer k, find the length of the longest subarray that sums to k.
If no such sub-array exists, then return 0.
'''

def longestSubarraywithSumK(nums, k):
    prefixSumMap = {}
    Sum = 0
    maxLen = 0
    
    n = len(nums)
    
    for i in range(n):
        Sum += nums[i]
        
        if Sum == k:
            maxLen = max(maxLen, i + 1)
        
        rem = Sum - k
    
        if rem in prefixSumMap:
            length = i - prefixSumMap[rem]
            maxLen = max(maxLen, length)
        
        if Sum not in prefixSumMap:
            prefixSumMap[Sum] = i
        
    return maxLen 

# Examples
nums1 = [1, 2, 1, 0, 1]
k1 = 4
print(longestSubarraywithSumK(nums1, k1)) # Output: 4

# Additional examples
nums2 = [1, -1, 5, -2, 3]
k2 = 3  # Output: 4 (subarray [1, -1, 5, -2])
print(longestSubarraywithSumK(nums2, k2)) # Output: 4

nums3 = [2, -1, 2, 1, -1, 2]
k3 = 3  # Output: 5 (subarray [2, -1, 2, 1, -1])
print(longestSubarraywithSumK(nums3, k3)) # Output: 5

nums4 = [-2, -1, 2, 1]
k4 = 1  # Output: 2 (subarray [-1, 2])
print(longestSubarraywithSumK(nums4, k4)) # Output: 2

nums5 = [1, 2, 3, -2, 5]
k5 = 6  # Output: 4 (subarray [1, 2, 3])
print(longestSubarraywithSumK(nums5, k5)) # Output: 3

nums6 = [0, 0, 0, 0]
k6 = 0  # Output: 4 (entire array)
print(longestSubarraywithSumK(nums6, k6)) # Output: 4

nums7 = [1, 2, 3, 4, 5]
k7 = 10  # Output: 4 (subarray [2, 3, 4, 5])
print(longestSubarraywithSumK(nums7, k7)) # Output: 4

nums8 = [1, -2, 3, 4, -1, 2]
k8 = 6  # Output: 4 (subarray [3, 4, -1])
print(longestSubarraywithSumK(nums8, k8)) # Output: 4

nums9 = [5, 1, 3, -2, 4]
k9 = 6  # Output: 3 (subarray [1, 3, -2])
print(longestSubarraywithSumK(nums9, k9)) # Output: 3

nums10 = [1, 2, 3, -3, 4]
k10 = 4  # Output: 4 (subarray [1, 2, 3, -3, 4])
print(longestSubarraywithSumK(nums10, k10)) # Output: 4
    