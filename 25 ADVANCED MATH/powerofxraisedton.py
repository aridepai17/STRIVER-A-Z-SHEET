# POWER OF X RAISED TO N TIMES

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
        
    result = 1.0
    
    while n > 0:
        if n % 2 == 1:
            result *= x
            n -= 1
        else:
            x *= x
            n //= 2
            
    return result

'''
# Time Complexity: O(log n)
# The algorithm uses a method similar to binary exponentiation (or exponentiation by squaring).
# In each iteration of the while loop, the power 'n' is either reduced by 1 (if odd) or halved (if even).
# An odd 'n' becomes even in the next step, which is then guaranteed to be halved.
# This means that 'n' is roughly halved every two iterations, leading to a logarithmic number of loop executions with respect to n.
# The operations inside the loop are constant time.

# Space Complexity: O(1)
# The algorithm uses a fixed number of variables (x, n, result) to store values.
# The memory usage does not scale with the input size 'n', so the space complexity is constant.
'''

# Test Cases
x1 = 2.00000, n1 = 10
print(myPow(x1, n1)) # Output: 1024.00000

x2, n2 = 2.10000, 3
print(myPow(x2, n2)) # Output: 9.26100

x3, n3 = 2.00000, -2
print(myPow(x3, n3)) # Output: 0.25000

x4, n4 = 1.00000, 12345
print(myPow(x4, n4)) # Output: 1.00000

x5, n5 = 3.00000, 0
print(myPow(x5, n5)) # Output: 1.00000

x6, n6 = -2.00000, 3
print(myPow(x6, n6)) # Output: -8.00000

x7, n7 = -2.00000, 4
print(myPow(x7, n7)) # Output: 16.00000

x8, n8 = 0.00000, 5
print(myPow(x8, n8)) # Output: 0.0

x9, n9 = 5.00000, 1
print(myPow(x9, n9)) # Output: 5.00000

x10, n10 = 0.5, 4
print(myPow(x10, n10)) # Output: 0.0625