# PASCALS TRIANGLE 3 

'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
'''

def pascalTriangle3(rowIndex):
    row = [1]
    value = 1
    
    for i in range(1, rowIndex + 1):
        value *= (rowIndex - i + 1)
        value //= i
        row.append(value)
        
    return row

# Examples
rowIndex1 = 3 
print(pascalTriangle3(rowIndex1)) # Output: [1,3,3,1]

# Additional examples
rowIndex2 = 0
print(pascalTriangle3(rowIndex2)) # Output: [1]

rowIndex3 = 1
print(pascalTriangle3(rowIndex3)) # Output: [1, 1]

rowIndex4 = 2
print(pascalTriangle3(rowIndex4)) # Output: [1, 2, 1]

rowIndex5 = 4
print(pascalTriangle3(rowIndex5)) # Output: [1, 4, 6, 4, 1]

rowIndex6 = 5
print(pascalTriangle3(rowIndex6)) # Output: [1, 5, 10, 10, 5, 1]

rowIndex7 = 6
print(pascalTriangle3(rowIndex7)) # Output: [1, 6, 15, 20, 15, 6, 1]

rowIndex8 = 7
print(pascalTriangle3(rowIndex8)) # Output: [1, 7, 21, 35, 35, 21, 7, 1]

rowIndex9 = 8
print(pascalTriangle3(rowIndex9)) # Output: [1, 8, 28, 56, 70, 56, 28, 8, 1]

rowIndex10 = 9
print(pascalTriangle3(rowIndex10)) # Output: [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]