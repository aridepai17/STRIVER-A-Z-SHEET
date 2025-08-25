# SEARCH IN 2D MATRIX II

'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.
'''

def searchMatrix2(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    
    row = 0
    col = m - 1
    
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
            
    return False

# Examples
matrix1 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target1 = 5
print(searchMatrix2(matrix1, target1)) # Output: True
    
matrix2 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target2 = 20
print(searchMatrix2(matrix2, target2)) # Output: False

matrix3 = [[1,2,3,4,5]], target3 = 4
print(searchMatrix2(matrix3, target3)) # Output: True

matrix4 = [[1,2,3,4,5]], target4 = 6
print(searchMatrix2(matrix4, target4)) # Output: False

matrix5 = [[1],[2],[3],[4],[5]], target5 = 3
print(searchMatrix2(matrix5, target5)) # Output: True

matrix6 = [[1],[2],[3],[4],[5]], target6 = 0
print(searchMatrix2(matrix6, target6)) # Output: False

matrix7 = [[-10,-5,0],[-3,1,4],[2,6,9]], target7 = -3
print(searchMatrix2(matrix7, target7)) # Output: True

matrix8 = [[-10,-5,0],[-3,1,4],[2,6,9]], target8 = 5
print(searchMatrix2(matrix8, target8)) # Output: False

matrix9 = [[1,4,7],[8,11,15],[18,21,23]], target9 = 23
print(searchMatrix2(matrix9, target9)) # Output: True

matrix10 = [[1,4,7],[8,11,15],[18,21,23]], target10 = 2
print(searchMatrix2(matrix10, target10)) # Output: False

matrix11 = [[5]], target11 = 5
print(searchMatrix2(matrix11, target11)) # Output: True
    