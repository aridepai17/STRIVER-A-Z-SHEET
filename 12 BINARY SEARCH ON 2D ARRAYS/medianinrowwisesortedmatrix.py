# MEDIAN IN ROW WISE SORTED MATRIX

'''
Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and columns is always odd. 
Return the median of the matrix.
'''
def median(mat):
    n = len(mat)
    m = len(mat[0])
    
    medianPosition = (n * m) // 2 + 1
    
    left = 0
    right = 2000
    
    while left <= right:
        mid = (left + right) // 2
        
        countofElements = countLessthanorEqual(mat, mid)
        
        if countofElements < medianPosition:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
    
def countLessthanorEqual(mat, value):
    count = 0
    
    for row in mat:
        count += upperBound(row, value)
        
    return count
    
def upperBound(row, target):
    left = 0
    right = len(row) - 1
    ans = len(row)
    
    while left <= right:
        mid = (left + right) // 2
        
        if row[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ans
    
# Examples
mat1 = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
print(median(mat1)) # Output: 5

mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(median(mat2)) # Output: 5

mat3 = [[1, 10, 20], [2, 12, 30], [3, 13, 40]]
print(median(mat3)) # Output: 12

mat4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(median(mat4)) # Output: 1

mat5 = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
print(median(mat5)) # Output: 9

mat6 = [[-5, -3, -1], [-2, 0, 2], [3, 4, 5]]
print(median(mat6)) # Output: 0

mat7 = [[1, 2, 2], [2, 3, 3], [3, 4, 4]]
print(median(mat7)) # Output: 3

mat8 = [[1, 5, 9], [10, 11, 12], [13, 14, 15]]
print(median(mat8)) # Output: 11

mat9 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(median(mat9)) # Output: 4

mat10 = [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
print(median(mat10)) # Output: 11

mat11 = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
print(median(mat11)) # Output: 500