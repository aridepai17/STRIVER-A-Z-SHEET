# RECURSIVE INSERTION SORT 

'''
Given an array of integers nums, sort the array in non-decreasing order using the recursive Insertion Sort algorithm, and return the sorted array.
You must implement Insertion Sort using recursion only.
Do not use loops (like for or while) or built-in sorting functions (sort, Arrays.sort, etc.).
A sorted array in non-decreasing order is an array where each element is greater than or equal to all elements that come before it.
'''

def insertionSort(self, nums):
        def sortRecursive(n):
            if n <= 1:
                return 

            sortRecursive(n - 1)

            key = nums[n - 1]
            insertRecursive(nums, n - 2, key)

        def insertRecursive(arr, i, key):
            if i < 0 or arr[i] <= key:
                arr[i + 1] = key
                return 

            arr[i + 1] = arr[i]
            insertRecursive(arr, i - 1, key)

        sortRecursive(len(nums))
        return nums

# Examples 
print(insertionSort([5, 2, 9, 1, 5, 6]))          # Should print [1, 2, 5, 5, 6, 9]
print(insertionSort([3, 0, 2, 5, -1, 4, 1]))      # Should print [-1, 0, 1, 2, 3, 4, 5]
print(insertionSort([1]))                          # Should print [1]
print(insertionSort([]))                           # Should print []
print(insertionSort([10, 7, 8, 9, 1, 5]))         # Should print [1, 5, 7, 8, 9, 10]
print(insertionSort([4, 3, 2, 1]))                 # Should print [1, 2, 3, 4]
print(insertionSort([1, 2, 3, 4, 5]))              # Should print [1, 2, 3, 4, 5]
print(insertionSort([2, 1]))                       # Should print [1, 2]
print(insertionSort([5, 3, 8, 6, 2, 7, 4]))       # Should print [2, 3, 4, 5, 6, 7, 8]
print(insertionSort([1, 1, 1, 1, 1]))              # Should print [1, 1, 1, 1, 1]

