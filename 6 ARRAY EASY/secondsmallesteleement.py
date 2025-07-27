# SECOND SMALLEST ELEMENT 

'''
Given an array of integers nums, return the second-largest element in the array. 
If the second-largest element does not exist, return -1.
'''

def secondSmallestElement(nums):
    n = len(nums)
    if n < 2:
        return -1 
    
    smallest = float('inf')
    secondSmallest = float('inf')
    
    for i in range(n):
        if nums[i] < smallest:
            secondSmallest = smallest
            smallest = nums[i]
        elif nums[i] < secondSmallest and nums[i] != smallest:
            secondSmallest = nums[i]
            
    return secondSmallest 

# Examples
nums1 = [8, 8, 7, 6, 5]
print(secondSmallestElement(nums1))  # Should print 6

nums2 = [1, 2, 3, 4, 5]
print(secondSmallestElement(nums2))  # Should print 2

nums3 = [5, 5, 5, 5]
print(secondSmallestElement(nums3))  # Should print -1 (no second smallest)

nums4 = [10, 20, 30, 40, 50]
print(secondSmallestElement(nums4))  # Should print 20

nums5 = [3]
print(secondSmallestElement(nums5))  # Should print -1 (not enough elements)

nums6 = [0, 0, 0, 0]
print(secondSmallestElement(nums6))  # Should print -1 (no second smallest)

nums7 = [100, 200, 150]
print(secondSmallestElement(nums7))  # Should print 150

nums8 = [7, 5, 3, 9, 1]
print(secondSmallestElement(nums8))  # Should print 3

nums9 = [2, 2, 2, 2, 2]
print(secondSmallestElement(nums9))  # Should print -1 (no second smallest)

nums10 = [1, 3, 2, 4, 4]
print(secondSmallestElement(nums10))  # Should print 2

