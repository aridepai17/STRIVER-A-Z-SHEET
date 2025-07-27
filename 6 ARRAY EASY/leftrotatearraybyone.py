# LEFT ROTATE ARRAY BY ONE 

'''
Given an integer array nums, rotate the array to the left by one.
Note: There is no need to return anything, just modify the given array.
'''

def rotateArrayByOne(nums):
    n = len(nums)
    temp = nums[0]
    
    for i in range(1, n):
        nums[i - 1] = nums[i]
    nums[n - 1] = temp 
    
    return nums

# Examples
nums1 = [1, 2, 3, 4, 5]
print(rotateArrayByOne(nums1))  # Should print [2, 3, 4, 5, 1]

nums2 = [5, 6, 7, 8, 9]
print(rotateArrayByOne(nums2))  # Should print [6, 7, 8, 9, 5]

nums3 = [10]
print(rotateArrayByOne(nums3))  # Should print [10] (single element)

nums4 = []
print(rotateArrayByOne(nums4))  # Should print [] (empty array)

nums5 = [1, 2]
print(rotateArrayByOne(nums5))  # Should print [2, 1]

nums6 = [3, 3, 3, 3]
print(rotateArrayByOne(nums6))  # Should print [3, 3, 3, 3] (all elements are the same)

nums7 = [1, 2, 3]
print(rotateArrayByOne(nums7))  # Should print [2, 3, 1]

nums8 = [4, 5, 6, 7, 8, 9]
print(rotateArrayByOne(nums8))  # Should print [5, 6, 7, 8, 9, 4]

nums9 = [0, 1, 2, 3, 4]
print(rotateArrayByOne(nums9))  # Should print [1, 2, 3, 4, 0]

nums10 = [9, 8, 7, 6, 5]
print(rotateArrayByOne(nums10))  # Should print [8, 7, 6, 5, 9]