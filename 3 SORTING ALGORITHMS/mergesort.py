# MERGE SORT 

'''
Given an array of integers, nums,sort the array in non-decreasing order using the merge sort algorithm. Return the sorted array.
A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.
'''

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = [ ]
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Examples 
print(mergeSort([5, 2, 9, 1, 5, 6]))          # Should print [1, 2, 5, 5, 6, 9]
print(mergeSort([3, 0, 2, 5, -1, 4, 1]))      # Should print [-1, 0, 1, 2, 3, 4, 5]
print(mergeSort([1]))                          # Should print [1]
print(mergeSort([]))                           # Should print []
print(mergeSort([10, 7, 8, 9, 1, 5]))         # Should print [1, 5, 7, 8, 9, 10]
print(mergeSort([4, 3, 2, 1]))                 # Should print [1, 2, 3, 4]
print(mergeSort([1, 2, 3, 4, 5]))              # Should print [1, 2, 3, 4, 5]
print(mergeSort([2, 1]))                       # Should print [1, 2]
print(mergeSort([5, 3, 8, 6, 2, 7, 4]))       # Should print [2, 3, 4, 5, 6, 7, 8]
print(mergeSort([1, 1, 1, 1, 1]))              # Should print [1, 1, 1, 1, 1] 