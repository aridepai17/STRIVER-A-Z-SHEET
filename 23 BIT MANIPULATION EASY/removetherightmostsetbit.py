# REMOVE THE RIGHTMOST SET BIT

'''
Given an integer n, turn remove turn off the rightmost set bit in it. 
'''

def removerightmostSetBit(n):
    return n & (n - 1)

'''
Time Complexity: O(1)
Space Complexity: O(1)
'''

# Test Cases
n1 = 12
print(removerightmostSetBit(n1)) # Output: 6

n2 = 10
print(removerightmostSetBit(n2)) # Output: 8

n3 = 7
print(removerightmostSetBit(n3)) # Output: 6

n4 = 8
print(removerightmostSetBit(n4)) # Output: 0

n5 = 0
print(removerightmostSetBit(n5)) # Output: 0

n6 = 1
print(removerightmostSetBit(n6)) # Output: 0

n7 = 100
print(removerightmostSetBit(n7)) # Output: 96

n8 = 255
print(removerightmostSetBit(n8)) # Output: 254

n9 = 42
print(removerightmostSetBit(n9)) # Output: 40

n10 = 13
print(removerightmostSetBit(n10)) # Output: 12