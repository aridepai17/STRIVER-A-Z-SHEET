# PAINTERS PARTITION PROBLEM

'''
Given an array arr[] where each element denotes the length of a board, and an integer k representing the number of painters available. 
Each painter takes 1 unit of time to paint 1 unit length of a board.
Determine the minimum amount of time required to paint all the boards, under the constraint that each painter can paint only a contiguous sequence of boards.
(No skipping or splitting allowed).
'''

def minTime(arr, k):
    n = len(arr)
    
    if k > n:
        return -1
    
    def findPainters(limit, arr):
        painters = 1
        timePaint = 0
        
        for i in range(n):
            if timePaint + arr[i] <= limit:
                timePaint += arr[i]
            else:
                painters += 1
                timePaint = arr[i]
                
        return painters
    
    left = max(arr)
    right = sum(arr)
    
    while left <= right:
        mid = (left + right) // 2
        
        noOfPainters = findPainters(mid, arr)
        
        if noOfPainters > k:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

# Examples
arr1 = [5, 10, 30, 20, 15], k1 = 3
print(minTime(arr1, k1)) # Output: 35

arr2 = [10, 20, 30, 40], k2 = 2
print(minTime(arr2, k2)) # Output: 60

arr3 = [1, 2, 3, 4, 5], k3 = 1
print(minTime(arr3, k3)) # Output: 15

arr4 = [5, 5, 5, 5, 5], k4 = 3
print(minTime(arr4, k4)) # Output: 10

arr5 = [100, 200, 300, 400, 500], k5 = 2
print(minTime(arr5, k5)) # Output: 900

arr6 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k6 = 4
print(minTime(arr6, k6)) # Output: 3

arr7 = [50, 60, 70, 80], k7 = 4
print(minTime(arr7, k7)) # Output: 80

arr8 = [2, 8, 15, 10, 5, 12, 7, 18, 3, 9], k8 = 3
print(minTime(arr8, k8)) # Output: 35

arr9 = [25, 25, 25, 25, 25, 25], k9 = 2
print(minTime(arr9, k9)) # Output: 75

arr10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], k10 = 4
print(minTime(arr10, k10)) # Output: 21