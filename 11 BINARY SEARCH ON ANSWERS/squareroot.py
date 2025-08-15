# FIND SQUARE ROOT 

'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
You must do it in O(log n) time.
'''

def mySqrt(x):
    left = 1
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

# Examples
x1 = 4
print(mySqrt(x1))  # Output: 2

x2 = 8
print(mySqrt(x2)) # Output: 2

# Additional examples
x3 = 0
print(mySqrt(x3))  # Output: 0

x4 = 1
print(mySqrt(x4))  # Output: 1

x5 = 2
print(mySqrt(x5))  # Output: 1

x6 = 9
print(mySqrt(x6))  # Output: 3

x7 = 16
print(mySqrt(x7))  # Output: 4

x8 = 25
print(mySqrt(x8))  # Output: 5

x9 = 100
print(mySqrt(x9))  # Output: 10

x10 = 144
print(mySqrt(x10))  # Output: 12

x11 = 1000
print(mySqrt(x11))  # Output: 31

x12 = 2147483647
print(mySqrt(x12))  # Output: 46340