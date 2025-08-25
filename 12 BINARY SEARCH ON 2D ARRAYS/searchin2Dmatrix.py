# SEARCH IN 2D MATRIX 

'''
You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
- Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

def search2DMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    
    left = 0
    right = n * m - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        row = mid // m 
        col = mid % m 
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

# Examples
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target1 = 3
print(search2DMatrix(matrix1, target1)) # Output: True

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target2 = 13
print(search2DMatrix(matrix2, target2)) # Output: False

matrix3 = [[1,2,3,4,5]], target3 = 4
print(search2DMatrix(matrix3, target3)) # Output: True

matrix4 = [[1,2,3,4,5]], target4 = 6
print(search2DMatrix(matrix4, target4)) # Output: False

matrix5 = [[1],[3],[5],[7]], target5 = 3
print(search2DMatrix(matrix5, target5)) # Output: True

matrix6 = [[1],[3],[5],[7]], target6 = 2
print(search2DMatrix(matrix6, target6)) # Output: False

matrix7 = [[1,5,9,13,17],[21,25,29,33,37],[41,45,49,53,57]], target7 = 49
print(search2DMatrix(matrix7, target7)) # Output: True

matrix8 = [[1,5,9,13,17],[21,25,29,33,37],[41,45,49,53,57]], target8 = 20
print(search2DMatrix(matrix8, target8)) # Output: False

matrix9 = [[-10,-5,-2,-1],[0,3,6,9],[12,15,18,21]], target9 = -2
print(search2DMatrix(matrix9, target9)) # Output: True

matrix10 = [[-10,-5,-2,-1],[0,3,6,9],[12,15,18,21]], target10 = 4
print(search2DMatrix(matrix10, target10)) # Output: False

matrix11 = [[1,4,7],[10,13,16],[19,22,25]], target11 = 25
print(search2DMatrix(matrix11, target11)) # Output: True