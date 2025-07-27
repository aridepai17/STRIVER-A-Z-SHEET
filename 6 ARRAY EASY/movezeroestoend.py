# MOVE ZEROES TO END 

'''
Given an integer array nums, move all the 0's to the end of the array. 
The relative order of the other elements must remain the same. 
This must be done in place, without making a copy of the array.
'''

def moveZeroes(nums):
    n = len(nums)
    left = 0
    for right in range(n):
        if nums[right] != 0:
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

# Examples 
nums1 = [0, 1, 0, 3, 12]
print(moveZeroes(nums1))  # Should print [1, 3, 12, 0, 0]

nums2 = [0, 0, 1, 2, 3]
print(moveZeroes(nums2))  # Should print [1, 2, 3, 0, 0]

nums3 = [1, 2, 3, 4, 5]
print(moveZeroes(nums3))  # Should print [1, 2, 3, 4, 5] (no zeros)

nums4 = [0]
print(moveZeroes(nums4))  # Should print [0] (single zero)

nums5 = []
print(moveZeroes(nums5))  # Should print [] (empty array)

nums6 = [0, 1, 0, 0, 2]
print(moveZeroes(nums6))  # Should print [1, 2, 0, 0, 0]

nums7 = [5, 0, 0, 3, 0, 2]
print(moveZeroes(nums7))  # Should print [5, 3, 2, 0, 0, 0]

nums8 = [0, 0, 0, 0, 0]
print(moveZeroes(nums8))  # Should print [0, 0, 0, 0, 0] (all zeros)

nums9 = [1, 0, 2, 0, 3]
print(moveZeroes(nums9))  # Should print [1, 2, 3, 0, 0]

nums10 = [4, 5, 0, 6, 0, 7, 0]
print(moveZeroes(nums10))  # Should print [4, 5, 6, 7, 0, 0, 0]