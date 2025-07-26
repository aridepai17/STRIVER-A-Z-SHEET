# RECURSIVE BUBBLE SORT 

'''
Given an array of integers nums, sort the array in non-decreasing order using the recursive Bubble Sort algorithm, and return the sorted array.
You must implement Bubble Sort using recursion only.
Do not use built-in sorting functions (sort, sorted, Arrays.sort, etc.).
A sorted array in non-decreasing order is an array where each element is greater than or equal to the previous one.
'''

def bubbleSort(nums):
    def sortRecursive(n):
        if n == 1:
            return 
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        sortRecursive(n - 1)
        
    sortRecursive(len(nums))
    return nums

# Examples 
print(bubbleSort([5, 2, 9, 1, 5, 6]))          # Should print [1, 2, 5, 5, 6, 9]
print(bubbleSort([3, 0, 2, 5, -1, 4, 1]))      # Should print [-1, 0, 1, 2, 3, 4, 5]
print(bubbleSort([1]))                          # Should print [1]
print(bubbleSort([]))                           # Should print []
print(bubbleSort([10, 7, 8, 9, 1, 5]))         # Should print [1, 5, 7, 8, 9, 10]
print(bubbleSort([4, 3, 2, 1]))                 # Should print [1, 2, 3, 4]
print(bubbleSort([1, 2, 3, 4, 5]))              # Should print [1, 2, 3, 4, 5]
print(bubbleSort([2, 1]))                       # Should print [1, 2]
print(bubbleSort([5, 3, 8, 6, 2, 7, 4]))       # Should print [2, 3, 4, 5, 6, 7, 8]
print(bubbleSort([1, 1, 1, 1, 1]))              # Should print [1, 1, 1, 1, 1]