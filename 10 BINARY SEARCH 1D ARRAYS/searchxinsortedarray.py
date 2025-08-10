# SEARCH X IN SORTED ARRAY 

'''
Given a sorted array of integers nums with 0-based indexing, find the index of a specified target integer. 
If the target is found in the array, return its index. If the target is not found, return -1.
You must do the search in O(log n) time.
'''

def search(nums, target):
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
            
    return - 1

# Examples 
nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
print(search(nums1, target1)) # Output: 4

# Additional examples
nums2 = [1, 2, 3, 4, 5]
target2 = 3
print(search(nums2, target2)) # Output: 2

nums3 = [1, 2, 3, 4, 5]
target3 = 6
print(search(nums3, target3)) # Output: -1

nums4 = [2, 4, 6, 8, 10]
target4 = 2
print(search(nums4, target4)) # Output: 0

nums5 = [2, 4, 6, 8, 10]
target5 = 10
print(search(nums5, target5)) # Output: 4

nums6 = [5, 6, 7, 8, 9]
target6 = 5
print(search(nums6, target6)) # Output: 0

nums7 = [1, 3, 5, 7, 9]
target7 = 1
print(search(nums7, target7)) # Output: 0

nums8 = [1, 3, 5, 7, 9]
target8 = 9
print(search(nums8, target8)) # Output: 4

nums9 = [10, 20, 30, 40, 50]
target9 = 25
print(search(nums9, target9)) # Output: -1

nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target10 = 8
print(search(nums10, target10)) # Output: 7