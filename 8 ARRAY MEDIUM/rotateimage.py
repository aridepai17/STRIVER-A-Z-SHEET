# ROTATE IMAGE 

'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
'''

def rotateImage(matrix):
    m, n = len(matrix), len(matrix[0])
    
    for i in range(m):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for row in matrix:
        row.reverse()
        
# Examples 
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateImage(matrix1)) # Output: [[7,4,1],[8,5,2],[9,6,3]]