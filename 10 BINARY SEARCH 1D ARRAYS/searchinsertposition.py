# SEARCH INSERT POSITION 

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

def searchInsertPosition(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return mid + 1

# Examples
nums1 = [1, 3, 5, 6]
target1 = 5
print(searchInsertPosition(nums1, target1)) # Output: 2

# Additional examples
nums2 = [1, 3, 5, 6]
target2 = 2
print(searchInsertPosition(nums2, target2)) # Output: 1

nums3 = [1, 3, 5, 6]
target3 = 7
print(searchInsertPosition(nums3, target3)) # Output: 4

nums4 = [1, 3, 5, 6]
target4 = 0
print(searchInsertPosition(nums4, target4)) # Output: 0

nums5 = [1, 2, 3, 4, 5]
target5 = 3
print(searchInsertPosition(nums5, target5)) # Output: 2

nums6 = [10, 20, 30, 40, 50]
target6 = 25
print(searchInsertPosition(nums6, target6)) # Output: 2

nums7 = [1, 2, 3, 4, 5]
target7 = 6
print(searchInsertPosition(nums7, target7)) # Output: 5

nums8 = [5, 10, 15, 20]
target8 = 15
print(searchInsertPosition(nums8, target8)) # Output: 2

nums9 = [1, 2, 3, 4, 5, 6]
target9 = 4
print(searchInsertPosition(nums9, target9)) # Output: 3

nums10 = [1, 2, 3, 4, 5]
target10 = 1
print(searchInsertPosition(nums10, target10)) # Output: 0