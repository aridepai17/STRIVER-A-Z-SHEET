# REVERSE AN ARRAY 

# Given an array of n elements. The task to reverse the given array.
# The reversal of an array should be inplace.

def reverseArray(arr, n):
  def helper(start, end):
    if start >= end:
      return 
    arr[start], arr[end] = arr[end], arr[start]
    helper(start + 1, end - 1)
    
  helper(0, n-1)
  
  
# Examples 
arr1 = [1, 2, 3, 4, 5]
reverseArray(arr1, len(arr1))
print(arr1)  # Should print [5, 4, 3, 2, 1]

arr2 = [10, 20, 30, 40]
reverseArray(arr2, len(arr2))
print(arr2)  # Should print [40, 30, 20, 10]

arr3 = ['a', 'b', 'c', 'd']
reverseArray(arr3, len(arr3))
print(arr3)  # Should print ['d', 'c', 'b', 'a']

arr4 = [1]
reverseArray(arr4, len(arr4))
print(arr4)  # Should print [1]

arr5 = []
reverseArray(arr5, len(arr5))
print(arr5)  # Should print []

arr6 = [1, 2]
reverseArray(arr6, len(arr6))
print(arr6)  # Should print [2, 1]

arr7 = [5, 4, 3, 2, 1]
reverseArray(arr7, len(arr7))
print(arr7)  # Should print [1, 2, 3, 4, 5]

arr8 = [100, 200, 300]
reverseArray(arr8, len(arr8))
print(arr8)  # Should print [300, 200, 100]

arr9 = [1, 3, 5, 7, 9]
reverseArray(arr9, len(arr9))
print(arr9)  # Should print [9, 7, 5, 3, 1]

arr10 = [2, 4, 6, 8, 10, 12]
reverseArray(arr10, len(arr10))
print(arr10)  # Should print [12, 10, 8, 6, 4, 2]
  
  