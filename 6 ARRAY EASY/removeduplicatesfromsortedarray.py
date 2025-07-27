# REMOVE DUPLICATES FROM SORTED ARRAY

'''
Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once. Return the number of unique elements in the array.
If the number of unique elements be k, then,
Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
The remaining elements, as well as the size of the array does not matter in terms of correctness.
An array sorted in non-decreasing order is an array where every element to the right of an element is either equal to or greater in value than that element.
'''

def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Examples
nums1 = [1, 1, 2]
print(removeDuplicates(nums1))  # Should print 2

nums2 = [0, 0, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums2))  # Should print 5

nums3 = [1, 2, 3, 4, 5]
print(removeDuplicates(nums3))  # Should print 5

nums4 = [1, 1, 1, 1, 1]
print(removeDuplicates(nums4))  # Should print 1

nums5 = []
print(removeDuplicates(nums5))  # Should print 0

nums6 = [2, 2, 2, 2, 3, 3, 4]
print(removeDuplicates(nums6))  # Should print 4

nums7 = [5, 5, 5, 5, 5, 5]
print(removeDuplicates(nums7))  # Should print 1

nums8 = [1, 2, 2, 3, 4, 4, 5]
print(removeDuplicates(nums8))  # Should print 5

nums9 = [10, 20, 20, 30, 30, 30, 40]
print(removeDuplicates(nums9))  # Should print 4

nums10 = [1, 2, 3, 3, 3, 4, 5, 5]
print(removeDuplicates(nums10))  # Should print 5

