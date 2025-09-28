# POWER OF 2

'''
Given a non-negative integer n. You have to check if it is a power of 2 or not. 
'''

def isPowerofTwo(n):
    if n == 0:
        return False
    if n & (n - 1) == 0:
        return True
    else:
        return False

'''
Time Complexity: O(1)
Space Complexity: O(1)
'''

# Test Cases
n1 = 8
print(isPowerofTwo(n1)) # Output: True

n2 = 1
print(isPowerofTwo(n2)) # Output: True

n3 = 0
print(isPowerofTwo(n3)) # Output: False

n4 = 16
print(isPowerofTwo(n4)) # Output: True

n5 = 10
print(isPowerofTwo(n5)) # Output: False

n6 = 1024
print(isPowerofTwo(n6)) # Output: True

n7 = 1023
print(isPowerofTwo(n7)) # Output: False

n8 = 6
print(isPowerofTwo(n8)) # Output: False

n9 = 7
print(isPowerofTwo(n9)) # Output: False

n10 = 2
print(isPowerofTwo(n10)) # Output: True