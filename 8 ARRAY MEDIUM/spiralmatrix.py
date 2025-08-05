# SPIRAL MATRIX 

'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

def spiralMatrix(matrix):
    result = []
    if not matrix:
        return result 
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
            
        if left <= right:
            for row in range(bottom, top - 1 , -1):
                result.append(matrix[row][left])
            left += 1
            
    return result

# Examples 
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralMatrix(matrix1)) # Output: [1,2,3,6,9,8,7,4,5]

# New examples
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiralMatrix(matrix2)) # Output: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

matrix3 = [[1]]
print(spiralMatrix(matrix3)) # Output: [1]

matrix4 = [[1,2],[3,4]]
print(spiralMatrix(matrix4)) # Output: [1,2,4,3]

matrix5 = [[1,2,3],[4,5,6]]
print(spiralMatrix(matrix5)) # Output: [1,2,3,6,5,4]

matrix6 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(spiralMatrix(matrix6)) # Output: [1,2,3,6,9,12,11,10,7,4,5,8]

matrix7 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print(spiralMatrix(matrix7)) # Output: [1,2,3,4,5,10,15,14,13,12,11,6,7,8,9]

matrix8 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
print(spiralMatrix(matrix8)) # Output: [1,2,3,6,9,12,15,14,13,10,7,4,5,8,11]

matrix9 = [[1,2,3,4],[5,6,7,8]]
print(spiralMatrix(matrix9)) # Output: [1,2,3,4,8,7,6,5]

matrix10 = [[1,2],[3,4],[5,6],[7,8]]
print(spiralMatrix(matrix10)) # Output: [1,2,4,6,8,7,5,3]