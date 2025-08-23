# SPLIT ARRAY LARGEST SUM

'''
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.
'''

def splitArray(nums, k):
    n = len(nums)
    
    if k > n:
        return -1
    
    def findSubarrays(limit, nums):
        subarrays = 1
        subarraySum = 0
        
        for i in range(n):
            if subarraySum + nums[i] <= limit:
                subarraySum += nums[i]
            else:
                subarrays += 1
                subarraySum = nums[i]
                
        return subarrays
                
    left = max(nums)
    right = sum(nums)
    
    while left <= right:
        mid = (left + right) // 2
        
        noOfSubarrays = findSubarrays(mid, nums)
        
        if noOfSubarrays > k:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

# Examples
nums1 = [7,2,5,10,8], k1 = 2
print(splitArray(nums1, k1)) # Output: 18

nums2 = [1,2,3,4,5], k2 = 2
print(splitArray(nums2, k2)) # Output: 9

nums3 = [1,4,4], k3 = 3
print(splitArray(nums3, k3)) # Output: 4

nums4 = [10,20,30,40], k4 = 1
print(splitArray(nums4, k4)) # Output: 100

nums5 = [1,2,3,4,5,6,7,8,9,10], k5 = 5
print(splitArray(nums5, k5)) # Output: 15

nums6 = [100,200,300,400,500], k6 = 3
print(splitArray(nums6, k6)) # Output: 700

nums7 = [5,5,5,5,5], k7 = 2
print(splitArray(nums7, k7)) # Output: 15

nums8 = [1,1,1,1,1,1,1,1,1,1], k8 = 4
print(splitArray(nums8, k8)) # Output: 3

nums9 = [50,60,70,80], k9 = 4
print(splitArray(nums9, k9)) # Output: 80

nums10 = [2,8,15,10,5,12,7,18,3,9,11,4,6,13,16], k10 = 4
print(splitArray(nums10, k10)) # Output: 45