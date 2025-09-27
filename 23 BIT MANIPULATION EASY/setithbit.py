# SET I-TH BIT

'''
Given a number n and a value i. From the right, set the ith bit in the binary representation of n. 
The position of the Least Significant Bit(or last bit) is 0, the second last bit is 1 and so on. 
'''

def setIthBit(n, i):
    return n | ( 1 << i )

'''
Time Complexity: O(1)
Space Complexity: O(1)
'''

# Test Cases
n1 = 10, i1 = 2
print(setIthBit(n1, i1)) # Output: 14

n2, i2 = 13, 2
print(setIthBit(n2, i2)) # Output: 13

n3, i3 = 8, 0
print(setIthBit(n3, i3)) # Output: 9

n4, i4 = 5, 0
print(setIthBit(n4, i4)) # Output: 5

n5, i5 = 0, 3
print(setIthBit(n5, i5)) # Output: 8

n6, i6 = 9, 4
print(setIthBit(n6, i6)) # Output: 25

n7, i7 = 100, 1
print(setIthBit(n7, i7)) # Output: 102

n8, i8 = 42, 4
print(setIthBit(n8, i8)) # Output: 58

n9, i9 = 21, 1
print(setIthBit(n9, i9)) # Output: 23

n10, i10 = 15, 4
print(setIthBit(n10, i10)) # Output: 31