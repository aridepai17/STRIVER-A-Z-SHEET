# SELECTION SORT 

'''
Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.
'''

def selectionSort(nums):
  n = len(nums)
  
  for i in range(n):
    minIndex = i 
    
    for j in range(i + 1, n):
      if nums[j] < nums[minIndex]:
        minIndex = j
        
    nums[i], nums[minIndex] = nums[minIndex], nums[i]
  
  return nums

# Example 

arr1 = [3, 4, 5, 1, 7]
print(selectionSort(arr1)) # Output: [1, 3, 4, 5, 7]

# Additional examples
arr2 = [64, 25, 12, 22, 11]
print(selectionSort(arr2)) # Output: [11, 12, 22, 25, 64]

arr3 = [5, 4, 3, 2, 1]
print(selectionSort(arr3)) # Output: [1, 2, 3, 4, 5]

arr4 = [1, 2, 3, 4, 5]
print(selectionSort(arr4)) # Output: [1, 2, 3, 4, 5]

arr5 = [3, 3, 2, 1, 1]
print(selectionSort(arr5)) # Output: [1, 1, 2, 3, 3]

arr6 = [10, -1, 2, 0, 5]
print(selectionSort(arr6)) # Output: [-1, 0, 2, 5, 10]

arr7 = [7, 8, 9, 1, 2]
print(selectionSort(arr7)) # Output: [1, 2, 7, 8, 9]

arr8 = [0, 0, 0, 0, 0]
print(selectionSort(arr8)) # Output: [0, 0, 0, 0, 0]

arr9 = [1]
print(selectionSort(arr9)) # Output: [1]

arr10 = []
print(selectionSort(arr10)) # Output: []

arr11 = [2, 1]
print(selectionSort(arr11)) # Output: [1, 2]