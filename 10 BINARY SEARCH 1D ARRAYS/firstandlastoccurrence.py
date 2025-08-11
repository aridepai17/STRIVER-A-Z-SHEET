# FIRST AND LAST OCCURRENCE 

'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found in the array, 
return [-1, -1].
'''

def firstandlastOccurrence(nums, target):
    left = 0
    right = len(nums) - 1
    last = -1
    first = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            if nums[mid] == target:
                last = mid
            left = mid + 1
        else:
            right = mid - 1
            
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            if nums[mid] == target:
                first = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return first, last


# Examples
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(firstandlastOccurrence(nums1, target1)) # Output: [3, 4]

# Additional examples
nums2 = [1, 2, 2, 3, 4, 5]
target2 = 2
print(firstandlastOccurrence(nums2, target2)) # Output: [1, 2]

nums3 = [1, 2, 3, 4, 5]
target3 = 6
print(firstandlastOccurrence(nums3, target3)) # Output: [-1, -1]

nums4 = [1, 1, 1, 1, 1]
target4 = 1
print(firstandlastOccurrence(nums4, target4)) # Output: [0, 4]

nums5 = [10, 20, 30, 40, 50]
target5 = 25
print(firstandlastOccurrence(nums5, target5)) # Output: [-1, -1]

nums6 = [1, 3, 5, 7, 9]
target6 = 3
print(firstandlastOccurrence(nums6, target6)) # Output: [1, 1]

nums7 = [1, 2, 3, 4, 5]
target7 = 1
print(firstandlastOccurrence(nums7, target7)) # Output: [0, 0]

nums8 = [1, 2, 3, 4, 5]
target8 = 5
print(firstandlastOccurrence(nums8, target8)) # Output: [4, 4]

nums9 = [1, 2, 2, 3, 4, 5]
target9 = 3
print(firstandlastOccurrence(nums9, target9)) # Output: [3, 3]

nums10 = [5, 5, 5, 5, 5]
target10 = 5
print(firstandlastOccurrence(nums10, target10)) # Output: [0, 4]