# FIND PEAK ELEMENT 

'''
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
'''

def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
            
    return left

# Examples
nums1 = [1,2,3,1]
print(findPeakElement(nums1)) # Output: 2

nums2 = [1,2,1,3,5,6,4]
print(findPeakElement(nums2)) # Output: 5

nums3 = [1,2,3,4,5]
print(findPeakElement(nums3)) # Output: 4

nums4 = [5,4,3,2,1]
print(findPeakElement(nums4)) # Output: 0

nums5 = [1,3,2,4,6,5]
print(findPeakElement(nums5)) # Output: 4

nums6 = [10,20,15,2,23,90,67]
print(findPeakElement(nums6)) # Output: 5

nums7 = [1,1,1,1,1]
print(findPeakElement(nums7)) # Output: 4

nums8 = [100,50,25,12,6]
print(findPeakElement(nums8)) # Output: 0

nums9 = [1,2,3,4,3,2,1]
print(findPeakElement(nums9)) # Output: 3

nums10 = [5,10,20,15,10,5]
print(findPeakElement(nums10)) # Output: 2