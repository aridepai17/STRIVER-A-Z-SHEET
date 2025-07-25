# BUBBLE SORT 

'''
Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
'''

def bubbleSort(nums):
  n = len(nums)
  
  for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
      if nums[j] > nums[j+1]:
        nums[j], nums[j+1] = nums[j+1], nums[j]
        swapped = True 
        
    if not swapped:
      break
    
  return nums

# Example 
nums1 = [7, 4, 1, 5, 3]
print(bubbleSort(nums1)) # Output: [1, 3, 4, 5, 7]

# Additional examples
nums2 = [64, 25, 12, 22, 11]
print(bubbleSort(nums2)) # Output: [11, 12, 22, 25, 64]

nums3 = [5, 4, 3, 2, 1]
print(bubbleSort(nums3)) # Output: [1, 2, 3, 4, 5]

nums4 = [1, 2, 3, 4, 5]
print(bubbleSort(nums4)) # Output: [1, 2, 3, 4, 5]

nums5 = [3, 3, 2, 1, 1]
print(bubbleSort(nums5)) # Output: [1, 1, 2, 3, 3]

nums6 = [10, -1, 2, 0, 5]
print(bubbleSort(nums6)) # Output: [-1, 0, 2, 5, 10]

nums7 = [7, 8, 9, 1, 2]
print(bubbleSort(nums7)) # Output: [1, 2, 7, 8, 9]

nums8 = [0, 0, 0, 0, 0]
print(bubbleSort(nums8)) # Output: [0, 0, 0, 0, 0]

nums9 = [1]
print(bubbleSort(nums9)) # Output: [1]

nums10 = []
print(bubbleSort(nums10)) # Output: []

nums11 = [2, 1]
print(bubbleSort(nums11)) # Output: [1, 2]