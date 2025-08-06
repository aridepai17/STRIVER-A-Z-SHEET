# PASCALS TRIANGLE 1

'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above.
'''

def pascalsTriangle1(numRows):
    triangle = []
    
    for i in range(numRows):
        rows  = []
        for j in range(i + 1):
            if j == 0 or j == i:
                rows.append(1)
            else:
                rows.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        triangle.append(rows)
    
    return triangle

# Examples
numRows1 = 5
print(pascalsTriangle1(numRows1)) # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Additional examples
numRows2 = 1
print(pascalsTriangle1(numRows2)) # Output: [[1]]

numRows3 = 2
print(pascalsTriangle1(numRows3)) # Output: [[1],[1,1]]

numRows4 = 3
print(pascalsTriangle1(numRows4)) # Output: [[1],[1,1],[1,2,1]]

numRows5 = 4
print(pascalsTriangle1(numRows5)) # Output: [[1],[1,1],[1,2,1],[1,3,3,1]]

numRows6 = 6
print(pascalsTriangle1(numRows6)) # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]

numRows7 = 7
print(pascalsTriangle1(numRows7)) # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1]]

numRows8 = 8
print(pascalsTriangle1(numRows8)) # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1]]

numRows9 = 9
print(pascalsTriangle1(numRows9)) # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1]]

numRows10 = 10
print(pascalsTriangle1(numRows10)) # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1]]
