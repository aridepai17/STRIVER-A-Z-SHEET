# FIND HOW MANY TIMES THE ARRAY IS ROTATED 

'''
Given an integer array nums of size n, sorted in ascending order with distinct values. 
The array has been right rotated an unknown number of times, between 0 and n-1 (including). 
Determine the number of rotations performed on the array.
'''

def findKRotation(nums):
    left = 0
    right = len(nums) - 1
    minIndex = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[left] < nums[right]:
            if nums[left] < nums[minIndex]:
                minIndex = left
            break
        
        if nums[left] <= nums[mid]:
            if nums[left] < nums[minIndex]:
                minIndex = left
            left = mid + 1
        else:
            if nums[mid] < nums[minIndex]:
                minIndex = mid
            right = mid - 1

    return minIndex


# Examples 
nums1 = [4, 5, 6, 7, 0, 1, 2, 3]
print(findKRotation(nums1)) # Output: 4

# Additional examples
nums2 = [1, 2, 3, 4, 5]
print(findKRotation(nums2)) # Output: 0

nums3 = [3, 4, 5, 1, 2]
print(findKRotation(nums3)) # Output: 3

nums4 = [2, 3, 4, 5, 1]
print(findKRotation(nums4)) # Output: 4

nums5 = [5, 1, 2, 3, 4]
print(findKRotation(nums5)) # Output: 1

nums6 = [1]
print(findKRotation(nums6)) # Output: 0

nums7 = [2, 2, 2, 2, 2]
print(findKRotation(nums7)) # Output: 0

nums8 = [3, 3, 3, 1, 3]
print(findKRotation(nums8)) # Output: 3

nums9 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
print(findKRotation(nums9)) # Output: 5

nums10 = [10, 1, 10, 10, 10]
print(findKRotation(nums10)) # Output: 1