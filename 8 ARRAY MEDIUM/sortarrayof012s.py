# SORT AN ARRAY OF 0'S, 1'S AND 2'S 

'''
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. 
he sorting must be done in-place, without making a copy of the original array.
'''

def sortZeroOneTwo(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            
# Examples
nums1 = [2, 0, 2, 1, 1, 0]
print(sortZeroOneTwo(nums1)) # Output: [0, 0, 1, 1, 2, 2]

# Additional examples
nums2 = [0, 1, 2, 0, 1, 2]  # Output: [0, 0, 1, 1, 2, 2]
print(sortZeroOneTwo(nums2)) # Output: [0, 0, 1, 1, 2, 2]

nums3 = [1, 0, 0, 1, 2, 2]  # Output: [0, 0, 1, 1, 2, 2]
print(sortZeroOneTwo(nums3)) # Output: [0, 0, 1, 1, 2, 2]

nums4 = [2, 2, 2, 2, 2]  # Output: [2, 2, 2, 2, 2]
print(sortZeroOneTwo(nums4)) # Output: [2, 2, 2, 2, 2]

nums5 = [0, 0, 0, 0, 0]  # Output: [0, 0, 0, 0, 0]
print(sortZeroOneTwo(nums5)) # Output: [0, 0, 0, 0, 0]

nums6 = [1, 1, 1, 1, 1]  # Output: [1, 1, 1, 1, 1]
print(sortZeroOneTwo(nums6)) # Output: [1, 1, 1, 1, 1]

nums7 = [0, 1, 2]  # Output: [0, 1, 2]
print(sortZeroOneTwo(nums7)) # Output: [0, 1, 2]

nums8 = [2, 1, 0]  # Output: [0, 1, 2]
print(sortZeroOneTwo(nums8)) # Output: [0, 1, 2]

nums9 = [1, 2, 0]  # Output: [0, 1, 2]
print(sortZeroOneTwo(nums9)) # Output: [0, 1, 2]

nums10 = [0, 2, 1, 0, 1, 2]  # Output: [0, 0, 1, 1, 2, 2]
print(sortZeroOneTwo(nums10)) # Output: [0, 0, 1, 1, 2, 2]