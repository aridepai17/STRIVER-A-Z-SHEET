# KTH MISSING POSITIVE NUMBER

'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.
'''

def findKthPositive(arr, k):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        missing = arr[mid] - (mid + 1)
        
        if missing >= k:
            right = mid - 1
        else:
            left = mid + 1
    
    return left + k


# Examples

arr = [2,3,4,7,11]
k = 5
print(findKthPositive(arr, k)) # Output: 9

# Additional examples
arr = [1,2,3,4]
k = 2
print(findKthPositive(arr, k)) # Output: 6

arr = [2]
k = 1
print(findKthPositive(arr, k)) # Output: 1

arr = [2]
k = 2
print(findKthPositive(arr, k)) # Output: 3

arr = [1,10]
k = 1
print(findKthPositive(arr, k)) # Output: 2

arr = [1,10]
k = 9
print(findKthPositive(arr, k)) # Output: 11

arr = [5,6,7]
k = 1
print(findKthPositive(arr, k)) # Output: 1

arr = [5,6,7]
k = 4
print(findKthPositive(arr, k)) # Output: 4

arr = [1,2,3,4,5]
k = 5
print(findKthPositive(arr, k)) # Output: 10

arr = [3,4,5,6,7,8]
k = 2
print(findKthPositive(arr, k)) # Output: 2

arr = [1,3,5,7,9]
k = 3
print(findKthPositive(arr, k)) # Output: 6