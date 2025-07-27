# LINEAR SEARCH 

# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array.
# If not found in the array, return -1.

def linearSearch(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1

# Examples
nums1 = [2, 7, 11, 15]
target1 = 9
print(linearSearch(nums1, target1))  # Should print -1 (not found)

nums2 = [1, 2, 3, 4, 5]
target2 = 3
print(linearSearch(nums2, target2))  # Should print 2 (found at index 2)

nums3 = [5, 5, 5, 5]
target3 = 5
print(linearSearch(nums3, target3))  # Should print 0 (first occurrence)

nums4 = [10, 20, 30, 40, 50]
target4 = 40
print(linearSearch(nums4, target4))  # Should print 3 (found at index 3)

nums5 = [1, 2, 3, 4, 5]
target5 = 6
print(linearSearch(nums5, target5))  # Should print -1 (not found)

nums6 = [0, 0, 0, 0]
target6 = 0
print(linearSearch(nums6, target6))  # Should print 0 (first occurrence)

nums7 = [100, 200, 300, 400]
target7 = 300
print(linearSearch(nums7, target7))  # Should print 2 (found at index 2)

nums8 = [7, 5, 3, 9, 1]
target8 = 1
print(linearSearch(nums8, target8))  # Should print 4 (found at index 4)

nums9 = [2, 4, 6, 8, 10]
target9 = 5
print(linearSearch(nums9, target9))  # Should print -1 (not found)

nums10 = [1, 3, 5, 7, 9]
target10 = 1
print(linearSearch(nums10, target10))  # Should print 0 (found at index 0)