# SEARCH IN ROTATED SORTED ARRAY 1

'''
Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. 
The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.
'''

def searchinRotatedSortedArray1(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] >= target >= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Examples
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(searchinRotatedSortedArray1(nums1, target1)) # Output: 4

# Additional examples
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(searchinRotatedSortedArray1(nums2, target2)) # Output: -1

nums3 = [1, 3]
target3 = 3
print(searchinRotatedSortedArray1(nums3, target3)) # Output: 1

nums4 = [1]
target4 = 0
print(searchinRotatedSortedArray1(nums4, target4)) # Output: -1

nums5 = [5, 1, 3]
target5 = 5
print(searchinRotatedSortedArray1(nums5, target5)) # Output: 0

nums6 = [3, 5, 1]
target6 = 1
print(searchinRotatedSortedArray1(nums6, target6)) # Output: 2

nums7 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
target7 = 10
print(searchinRotatedSortedArray1(nums7, target7)) # Output: 8

nums8 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
target8 = 1
print(searchinRotatedSortedArray1(nums8, target8)) # Output: 5

nums9 = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target9 = 6
print(searchinRotatedSortedArray1(nums9, target9)) # Output: 5

nums10 = [1, 2, 3, 4, 5, 6, 7]
target10 = 4
print(searchinRotatedSortedArray1(nums10, target10)) # Output: 3