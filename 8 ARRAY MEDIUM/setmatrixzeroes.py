# SET MATRIX ZEROES 

'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
'''

def setMatrixZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    firstRowhasZero = False 
    firstColhasZero = False 
    
    for j in range(n):
        if matrix[0][j] == 0:
            firstRowhasZero = True
            break 
        
    for i in range(m):
        if matrix[i][0] == 0:
            firstColhasZero = True
            break 
        
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
                
    for i in range(1, m):
        for j in range(1, n):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
                
    if firstColhasZero:
        for i in range(m):
            matrix[i][0] = 0
            
    if firstRowhasZero:
        for j in range(n):
            matrix[0][j] = 0
            
# Example 
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
print(setMatrixZeroes(matrix1)) # Output: [[1,0,1],[0,0,0],[1,0,1]]

# New examples
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setMatrixZeroes(matrix2)) # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
print(setMatrixZeroes(matrix3)) # Output: [[1,2,3],[4,5,6],[7,8,9]]

matrix4 = [[1,0,3],[4,5,6],[7,8,0]]
print(setMatrixZeroes(matrix4)) # Output: [[0,0,0],[4,5,0],[0,8,0]]

matrix5 = [[1,2,3],[0,5,6],[7,8,9]]
print(setMatrixZeroes(matrix5)) # Output: [[0,2,3],[0,5,6],[0,8,9]]

matrix6 = [[0]]
print(setMatrixZeroes(matrix6)) # Output: [[0]]

matrix7 = [[1,1,1],[1,1,1],[1,1,1]]
print(setMatrixZeroes(matrix7)) # Output: [[1,1,1],[1,1,1],[1,1,1]]

matrix8 = [[1,2,0],[4,5,6],[7,8,9]]
print(setMatrixZeroes(matrix8)) # Output: [[0,0,0],[4,5,6],[7,8,9]]

matrix9 = [[1,2,3],[4,0,6],[7,8,9]]
print(setMatrixZeroes(matrix9)) # Output: [[1,0,3],[0,0,0],[7,0,9]]

matrix10 = [[1,2,3],[4,5,6],[0,0,0]]
print(setMatrixZeroes(matrix10)) # Output: [[0,0,0],[0,0,0],[0,0,0]]