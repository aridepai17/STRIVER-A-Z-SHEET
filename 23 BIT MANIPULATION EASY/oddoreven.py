# ODD OR EVEN

'''
Given a positive integer n, determine whether it is odd or even.
Return true if the number is even and false if the number is odd.
'''

def oddorEven(n):
    if n & 1:
        return False
    else:
        return True
    
'''
Time Complexity: O(1)
The function performs a single bitwise AND operation (`n & 1`), which is a constant-time operation, regardless of the size of the input number `n`. The conditional check and return statement also take constant time.

Space Complexity: O(1)
The function uses a constant amount of memory. It does not allocate any additional space that depends on the size of the input `n`.
'''

# Test Cases
n1 = 15
print(oddorEven(n1)) # Output: False

n2 = 10
print(oddorEven(n2)) # Output: True

n3 = 0
print(oddorEven(n3)) # Output: True

n4 = 1
print(oddorEven(n4)) # Output: False

n5 = 2
print(oddorEven(n5)) # Output: True

n6 = 100
print(oddorEven(n6)) # Output: True

n7 = 99
print(oddorEven(n7)) # Output: False

n8 = 42
print(oddorEven(n8)) # Output: True

n9 = 255
print(oddorEven(n9)) # Output: False

n10 = 1024
print(oddorEven(n10)) # Output: True