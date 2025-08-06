# PASCALS TRIANGLE 2 

'''
iven two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.
'''

def nCr(n, r):
    result = 1 
    
    for i in range(r):
        result *= (n - i)
        result  //= (i + 1)
        
    return result 

def pascalsTriangle2(r, c):
    return nCr(r-1, c-1)

# Examples
r1 = 4
c1 = 2
print(pascalsTriangle2(r1, c1)) # Output: 3 

# Additional examples
r2 = 1
c2 = 1
print(pascalsTriangle2(r2, c2)) # Output: 1

r3 = 2
c3 = 1
print(pascalsTriangle2(r3, c3)) # Output: 1

r4 = 2
c4 = 2
print(pascalsTriangle2(r4, c4)) # Output: 1

r5 = 3
c5 = 1
print(pascalsTriangle2(r5, c5)) # Output: 1

r6 = 3
c6 = 2
print(pascalsTriangle2(r6, c6)) # Output: 2

r7 = 3
c7 = 3
print(pascalsTriangle2(r7, c7)) # Output: 1

r8 = 5
c8 = 3
print(pascalsTriangle2(r8, c8)) # Output: 6

r9 = 5
c9 = 4
print(pascalsTriangle2(r9, c9)) # Output: 4

r10 = 6
c10 = 3
print(pascalsTriangle2(r10, c10)) # Output: 10

r11 = 6
c11 = 4
print(pascalsTriangle2(r11, c11)) # Output: 15 