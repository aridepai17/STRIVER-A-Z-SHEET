# SECOND LARGEST ELEMENT 

# Given an array of integers nums, return the second-largest element in the array. 
# If the second-largest element does not exist, return - 1

def secondLargestElement(nums):
    n = len(nums)
    if n < 2:
        return -1 
    
    large = float('-inf')
    secondLargest = float('-inf')
    
    for i in range(n):
        if nums[i] > large:
            secondLargest = large
            large = nums[i]
        elif nums[i] > secondLargest and nums[i] != large:
            secondLargest = nums[i]
            
    return secondLargest 


# Examples 
nums1 = [8, 8, 7, 6, 4]
print(secondLargestElement(nums1))  # Should print 7

nums2 = [1, 2, 3, 4, 5]
print(secondLargestElement(nums2))  # Should print 4

nums3 = [5, 5, 5, 5]
print(secondLargestElement(nums3))  # Should print -1 (no second largest)

nums4 = [10, 20, 30, 40, 50]
print(secondLargestElement(nums4))  # Should print 40

nums5 = [3]
print(secondLargestElement(nums5))  # Should print -1 (not enough elements)

nums6 = [0, 0, 0, 0]
print(secondLargestElement(nums6))  # Should print -1 (no second largest)

nums7 = [100, 200, 150]
print(secondLargestElement(nums7))  # Should print 150

nums8 = [7, 5, 3, 9, 1]
print(secondLargestElement(nums8))  # Should print 7

nums9 = [2, 2, 2, 2, 2]
print(secondLargestElement(nums9))  # Should print -1 (no second largest)

nums10 = [1, 3, 2, 4, 4]
print(secondLargestElement(nums10))  # Should print 3