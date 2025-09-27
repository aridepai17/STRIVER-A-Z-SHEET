# REPLACE I-TH BIT

'''
Given two numbers n and i, change the ith (1-based indexing) bit from the left of the binary representation 
of the number n to '0' if it is  '1', else return the number N itself.
'''

def replaceIthBit(n, i):
    length = n.bit_length()
    
    if i <= 0 or i > length:
        return n
    
    position = length - i
    
    mask = ~ ( 1 << position )
    
    return n & mask

'''
Time Complexity: O(1)
The function performs a fixed number of operations, including `bit_length()`, arithmetic calculations, and bitwise manipulations (left shift, NOT, AND). These operations are all considered to have constant time complexity, regardless of the size of the input number `n`.

Space Complexity: O(1)
The function uses a few variables (`length`, `position`, `mask`) to store intermediate results. The amount of memory used does not depend on the size of the input `n`, so the space complexity is constant.
'''

# Test Cases
n1 = 13, i1 = 2
print(replaceIthBit(n1, i1)) # Output: 9

n2 = 10, i2 = 1
print(replaceIthBit(n2, i2)) # Output: 2

n3 = 10, i3 = 2
print(replaceIthBit(n3, i3)) # Output: 10

n4 = 0, i4 = 1
print(replaceIthBit(n4, i4)) # Output: 0

n5 = 1, i5 = 1
print(replaceIthBit(n5, i5)) # Output: 0

n6 = 100, i6 = 1
print(replaceIthBit(n6, i6)) # Output: 36

n7 = 100, i7 = 3
print(replaceIthBit(n7, i7)) # Output: 100

n8 = 13, i8 = 5
print(replaceIthBit(n8, i8)) # Output: 13

n9 = 13, i9 = 0
print(replaceIthBit(n9, i9)) # Output: 13

n10 = 255, i10 = 8
print(replaceIthBit(n10, i10)) # Output: 254