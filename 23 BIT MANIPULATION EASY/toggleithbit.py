# TOGGLE I-TH BIT

'''
For a given number n, if i-th bit (0-based indexing) is 0, then toggle it to 1 and if it is 1 then, toggle it to 0.
'''

def toggleBit(n, i):
    return n ^ (1 << i)

'''
Time Complexity: O(1)
Space Complexity: O(1)
'''

# Test Cases
n1 = 6, i1 = 1
print(toggleBit(n1, i1)) # Output: 4

n2 = 10, i2 = 2
print(toggleBit(n2, i2)) # Output: 14

n3 = 13, i3 = 3
print(toggleBit(n3, i3)) # Output: 5

n4 = 5, i4 = 0
print(toggleBit(n4, i4)) # Output: 4

n5 = 8, i5 = 0
print(toggleBit(n5, i5)) # Output: 9

n6 = 12, i6 = 5
print(toggleBit(n6, i6)) # Output: 44

n7 = 0, i7 = 4
print(toggleBit(n7, i7)) # Output: 16

n8 = 100, i8 = 4
print(toggleBit(n8, i8)) # Output: 116

n9 = 255, i9 = 7
print(toggleBit(n9, i9)) # Output: 127

n10 = 42, i10 = 5
print(toggleBit(n10, i10)) # Output: 10