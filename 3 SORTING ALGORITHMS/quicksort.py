# QUICK SORT 

'''
Given an array of integers called nums, sort the array in non-decreasing order using the quick sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
'''

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[-1]
    left = []
    right = []
    
    for i in range(len(nums) - 1):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
            
    return quickSort(left) + [pivot] + quickSort(right)

# Examples
print(quickSort([5, 2, 9, 1, 5, 6]))          # Should print [1, 2, 5, 5, 6, 9]
print(quickSort([3, 0, 2, 5, -1, 4, 1]))      # Should print [-1, 0, 1, 2, 3, 4, 5]
print(quickSort([1]))                          # Should print [1]
print(quickSort([]))                           # Should print []
print(quickSort([10, 7, 8, 9, 1, 5]))         # Should print [1, 5, 7, 8, 9, 10]
print(quickSort([4, 3, 2, 1]))                 # Should print [1, 2, 3, 4]
print(quickSort([1, 2, 3, 4, 5]))              # Should print [1, 2, 3, 4, 5]
print(quickSort([2, 1]))                       # Should print [1, 2]
print(quickSort([5, 3, 8, 6, 2, 7, 4]))       # Should print [2, 3, 4, 5, 6, 7, 8]
print(quickSort([1, 1, 1, 1, 1]))              # Should print [1, 1, 1, 1, 1]