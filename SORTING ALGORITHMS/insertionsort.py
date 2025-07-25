# INSERTION SORT 

'''
Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
'''

def insertionSort(nums):
  n = len(nums)
  
  for i in range(1, n):
    key = nums[i]
    j = i - 1
    
    while j >= 0 and nums[j] > key:
      nums[j + 1] = nums[j]
      j -= 1
      
    nums[j + 1] = key
    
  return nums

# Example 
arr1 = [7, 4, 1, 5, 3]
print(insertionSort(arr1)) # Output: [1, 3, 4, 5, 7]

# Additional examples
arr2 = [64, 25, 12, 22, 11]
print(insertionSort(arr2)) # Output: [11, 12, 22, 25, 64]

arr3 = [5, 4, 3, 2, 1]
print(insertionSort(arr3)) # Output: [1, 2, 3, 4, 5]

arr4 = [1, 2, 3, 4, 5]
print(insertionSort(arr4)) # Output: [1, 2, 3, 4, 5]

arr5 = [3, 3, 2, 1, 1]
print(insertionSort(arr5)) # Output: [1, 1, 2, 3, 3]

arr6 = [10, -1, 2, 0, 5]
print(insertionSort(arr6)) # Output: [-1, 0, 2, 5, 10]

arr7 = [7, 8, 9, 1, 2]
print(insertionSort(arr7)) # Output: [1, 2, 7, 8, 9]

arr8 = [0, 0, 0, 0, 0]
print(insertionSort(arr8)) # Output: [0, 0, 0, 0, 0]

arr9 = [1]
print(insertionSort(arr9)) # Output: [1]

arr10 = []
print(insertionSort(arr10)) # Output: []

arr11 = [2, 1]
print(insertionSort(arr11)) # Output: [1, 2]
