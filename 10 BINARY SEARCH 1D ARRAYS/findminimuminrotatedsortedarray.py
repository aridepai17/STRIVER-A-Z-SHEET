# FIND MINIMUM IN ROTATED SORTED ARRAY 

'''
Given an integer array nums of size N, 
sorted in ascending order with distinct values, 
and then rotated an unknown number of times (between 1 and N), 
find the minimum element in the array.
You must write an algorithm in O(log n) time.
'''

def findMin(nums):
    left = 0
    right = len(nums) - 1
    ans = float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[left] < nums[right]:
            ans = min(ans, nums[left])
            break
        
        if nums[left] <= nums[mid]:
            ans = min(ans, nums[left])
            left = mid + 1
        else:
            ans = min(ans, nums[mid])
            right = mid - 1

    return ans

# Examples
nums1 = [3, 4, 5, 1, 2]
print(findMin(nums1)) # Output: 1

# Additional examples
nums2 = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums2)) # Output: 0

nums3 = [1, 2, 3, 4, 5]
print(findMin(nums3)) # Output: 1

nums4 = [2, 3, 4, 5, 1]
print(findMin(nums4)) # Output: 1

nums5 = [5, 1, 2, 3, 4]
print(findMin(nums5)) # Output: 1

nums6 = [1]
print(findMin(nums6)) # Output: 1

nums7 = [2, 2, 2, 2, 2]
print(findMin(nums7)) # Output: 2

nums8 = [3, 3, 3, 1, 3]
print(findMin(nums8)) # Output: 1

nums9 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
print(findMin(nums9)) # Output: 1

nums10 = [10, 1, 10, 10, 10]
print(findMin(nums10)) # Output: 1