# CHECK IF ARRAY IS SORTED 2

# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

def isSorted(nums):
    n = len(nums)
    
    for i in range(1, n):
        if nums[i - 1] > nums[i]:
            return False
    return True 

# Examples
nums1 = [1, 2, 3, 4, 5]
print(isSorted(nums1))  # Should print True

nums2 = [5, 4, 3, 2, 1]
print(isSorted(nums2))  # Should print False

nums3 = [1, 2, 2, 3, 4]
print(isSorted(nums3))  # Should print True

nums4 = [1]
print(isSorted(nums4))  # Should print True (single element)

nums5 = []
print(isSorted(nums5))  # Should print True (empty array)

nums6 = [1, 3, 2, 4]
print(isSorted(nums6))  # Should print False

nums7 = [0, 0, 0, 0]
print(isSorted(nums7))  # Should print True (all elements are equal)

nums8 = [10, 20, 30, 40, 50]
print(isSorted(nums8))  # Should print True

nums9 = [1, 2, 3, 2, 5]
print(isSorted(nums9))  # Should print False

nums10 = [2, 2, 3, 3, 4]
print(isSorted(nums10))  # Should print True