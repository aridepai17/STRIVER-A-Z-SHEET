# PEAK ELEMENT IN 2D MATRIX

'''
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
'''

def findPeakGrid(mat):
    def maxElement(mat, n, col):
        maxValue = -1
        index = -1
        
        for i in range(n):
            if mat[i][col] > maxValue:
                maxValue = mat[i][col]
                index = i
                
        return index
    
    n = len(mat)
    m = len(mat[0])
    
    left = 0
    right = m - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        row = maxElement(mat, n, mid)
        
        leftNeighbor = mat[row][mid - 1] if mid - 1 >= 0 else -1
        rightNeighbor = mat[row][mid + 1] if mid + 1 < m else -1
        
        if mat[row][mid] > leftNeighbor and mat[row][mid] > rightNeighbor:
            return [row, mid]
        elif mat[row][mid] < leftNeighbor:
            right = mid - 1
        else:
            left = mid + 1
            
    return [-1, -1]

# Examples
mat1 = [[1,4],[3,2]]
print(findPeakGrid(mat1)) # Output: [0, 1]

mat2 = [[10,20,15],[21,30,14],[7,16,32]]
print(findPeakGrid(mat2)) # Output: [2, 2]

mat3 = [[1,2,3,6,5],[16,41,23,22,6],[15,17,24,21,7],[14,18,19,20,10],[13,14,11,10,9]]
print(findPeakGrid(mat3)) # Output: [1, 1]

mat4 = [[3,4,5],[3,2,6],[2,2,1]]
print(findPeakGrid(mat4)) # Output: [1, 2]

mat5 = [[1,2,1],[2,3,2],[1,2,1]]
print(findPeakGrid(mat5)) # Output: [1, 1]

mat6 = [[1]]
print(findPeakGrid(mat6)) # Output: [0, 0]

mat7 = [[1,3,5,7],[2,4,6,8]]
print(findPeakGrid(mat7)) # Output: [1, 3]

mat8 = [[10,9,8],[7,6,5],[4,3,2]]
print(findPeakGrid(mat8)) # Output: [0, 0]

mat9 = [[1,2,3],[6,5,4],[7,8,9]]
print(findPeakGrid(mat9)) # Output: [2, 2]

mat10 = [[5,10,5],[4,11,6],[3,9,7]]
print(findPeakGrid(mat10)) # Output: [1, 1]

mat11 = [[1,2,1,3,5],[3,2,1,4,6],[5,3,2,1,0]]
print(findPeakGrid(mat11)) # Output: [2, 0]