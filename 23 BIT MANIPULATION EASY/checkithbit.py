# CHECK I-TH BIT IS SET OR NOT

'''
Given two positive integer n and  i, check if the ith index bit of n is set or not.
Note: A bit is called set if it is 1. 
'''
# Solution 1: Using Left Shift Operator
def checkithBit(n, i):
    if (n & (1 << i) != 0):
        return True
    else:
        return False

'''
Time Complexity: O(1)
Space Complexity: O(1)
'''

# Solution 2: Using Right Shift Operator
def checkithBit2(n, i):
    if ((n >> i) & 1 != 0):
        return True
    else:
        return False

'''
Time Complexity: O(1)
Space Complexity: 
'''

# Test Cases
n1 = 4, i1 = 0
print(checkithBit(n1, i1)) # Output: False

n2, i2 = 5, 0
print(checkithBit(n2, i2)) # Output: True

n3, i3 = 13, 2
print(checkithBit(n3, i3)) # Output: True

n4, i4 = 13, 1
print(checkithBit(n4, i4)) # Output: False

n5, i5 = 8, 3
print(checkithBit(n5, i5)) # Output: True

n6, i6 = 8, 2
print(checkithBit(n6, i6)) # Output: False

n7, i7 = 0, 0
print(checkithBit(n7, i7)) # Output: False

n8, i8 = 1, 0
print(checkithBit(n8, i8)) # Output: True

n9, i9 = 1024, 10
print(checkithBit(n9, i9)) # Output: True

n10, i10 = 1023, 5
print(checkithBit(n10, i10)) # Output: True

