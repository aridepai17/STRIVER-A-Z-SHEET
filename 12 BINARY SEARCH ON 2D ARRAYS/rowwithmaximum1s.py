# ROW WITH MAXIMUM 1s

'''
You are given a 2D binary array arr[][] consisting of only 1s and 0s. 
Each row of the array is sorted in non-decreasing order. 
Your task is to find and return the index of the first row that contains the maximum number of 1s. 
If no such row exists, return -1.

Note:
- The array follows 0-based indexing.
- The number of rows and columns in the array are denoted by n and m respectively.
'''

def rowwithMax1s(arr):
    def firstOccurrence(row, target):
        left = 0
        right = len(row) - 1
        firstIndex = len(row)
        
        while left <= right:
            mid = (left + right) // 2
            
            if row[mid] == target:
                firstIndex = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return firstIndex
    
    n = len(arr)
    m = len(arr[0])
    
    resultIndex = -1
    maxCount = 0
    
    for i in range(n):
        firstOneIndex = firstOccurrence(arr[i], 1)
        currentCount = m - firstOneIndex
        
        if currentCount > maxCount:
            maxCount = currentCount 
            resultIndex = i 
            
    return resultIndex

# Examples
arr1 = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
print(rowwithMax1s(arr1)) # Output: 2

arr2 = [[0,0,0,0], [0,0,0,1], [0,0,1,1], [0,1,1,1]]
print(rowwithMax1s(arr2)) # Output: 3

arr3 = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
print(rowwithMax1s(arr3)) # Output: 0

arr4 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
print(rowwithMax1s(arr4)) # Output: -1

arr5 = [[0,0,0,1], [0,0,1,1], [0,1,1,1], [1,1,1,1]]
print(rowwithMax1s(arr5)) # Output: 3

arr6 = [[1,1,1,1], [0,1,1,1], [0,0,1,1], [0,0,0,1]]
print(rowwithMax1s(arr6)) # Output: 0

arr7 = [[0,0,1,1], [0,0,1,1], [0,0,1,1], [0,0,1,1]]
print(rowwithMax1s(arr7)) # Output: 0

arr8 = [[0,1,1,1,1], [0,0,1,1,1], [1,1,1,1,1], [0,0,0,0,1]]
print(rowwithMax1s(arr8)) # Output: 2

arr9 = [[1,1,1,1,1,1], [0,1,1,1,1,1], [0,0,1,1,1,1], [0,0,0,1,1,1]]
print(rowwithMax1s(arr9)) # Output: 0

arr10 = [[0,0,0,0,0,1], [0,0,0,0,1,1], [0,0,0,1,1,1], [0,0,1,1,1,1], [0,1,1,1,1,1]]
print(rowwithMax1s(arr10)) # Output: 4

arr11 = [[1,1,1,1,1,1,1], [0,0,0,0,0,0,1], [0,0,0,0,0,1,1], [0,0,0,0,1,1,1]]
print(rowwithMax1s(arr11)) # Output: 0