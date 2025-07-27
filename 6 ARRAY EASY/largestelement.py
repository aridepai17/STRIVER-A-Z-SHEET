# LARGEST ELEMENT 

# Given an array of integers nums, return the value of the largest element in the arrays 

def largestElement(nums):
    n = len(nums)
    largest = nums[0]
    
    for i in range(n):
        if largest < nums[i]:
            largest = nums[i]
    return largest 

# Examples
nums1 = [3, 3, 6, 1]          # Output: 6
print(largestElement(nums1))  # Should print 6

nums2 = [1, 2, 3, 4, 5]       # Output: 5
print(largestElement(nums2))  # Should print 5

nums3 = [-1, -2, -3, -4]      # Output: -1
print(largestElement(nums3))  # Should print -1

nums4 = [10, 20, 30, 40, 50]  # Output: 50
print(largestElement(nums4))  # Should print 50

nums5 = [5]                   # Output: 5
print(largestElement(nums5))  # Should print 5

nums6 = [0, 0, 0, 0]          # Output: 0
print(largestElement(nums6))  # Should print 0

nums7 = [100, 200, 150]       # Output: 200
print(largestElement(nums7))  # Should print 200

nums8 = [7, 5, 3, 9, 1]       # Output: 9
print(largestElement(nums8))  # Should print 9

nums9 = [2, 2, 2, 2, 2]       # Output: 2
print(largestElement(nums9))  # Should print 2