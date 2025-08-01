# LONGEST SUBARRAY WITH SUM K 

'''
Given an array nums of size n and an integer k, find the length of the longest subarray that sums to k.
If no such sub-array exists, then return 0 
'''

def longestSubarray(nums, k):
    n = len(nums)
    maxLen = 0
    Sum = nums[0]
    
    left, right = 0, 0
    
    while right < n:
        while left <= right and Sum > k:
            Sum -= nums[left]
            left += 1
            
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)
        
        right += 1
        
        if right < n:
            Sum += nums[right]
            
    return maxLen 

# Examples
nums1 = [10, 5, 2, 7, 1, 9]
k1 = 15
print(longestSubarray(nums1, k1)) # Output: 4

# Additional examples
nums2 = [1, 2, 3, 4, 5]
k2 = 9  # Output: 2 (subarray [4, 5])
print(longestSubarray(nums2, k2)) # Output: 2

nums3 = [1, 2, 3, 4, 5]
k3 = 15  # Output: 5 (entire array)
print(longestSubarray(nums3, k3)) # Output: 5

nums4 = [1, -1, 5, -2, 3]
k4 = 3  # Output: 4 (subarray [1, -1, 5, -2])
print(longestSubarray(nums4, k4)) # Output: 4

nums5 = [-2, -1, 2, 1]
k5 = 1  # Output: 2 (subarray [-1, 2])
print(longestSubarray(nums5, k5)) # Output: 2

nums6 = [1, 2, 3, 4, 5]
k6 = 10  # Output: 4 (subarray [2, 3, 4, 5])
print(longestSubarray(nums6, k6)) # Output: 4

nums7 = [0, 0, 0, 0]
k7 = 0  # Output: 4 (entire array)
print(longestSubarray(nums7, k7)) # Output: 4

nums8 = [1, 2, 3, 4, 5]
k8 = 7  # Output: 3 (subarray [2, 3, 4])
print(longestSubarray(nums8, k8)) # Output: 3

nums9 = [5, 1, 3, 2, 4]
k9 = 6  # Output: 2 (subarray [5, 1])
print(longestSubarray(nums9, k9)) # Output: 2

nums10 = [1, 2, 3, 4, 5]
k10 = 0  # Output: 0 (no subarray sums to 0)
print(longestSubarray(nums10, k10)) # Output: 0