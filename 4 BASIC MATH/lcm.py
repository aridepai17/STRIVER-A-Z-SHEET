# LCM OF TWO NUMBERS 

'''
You are given two positive integers a and b. Find the Least Common Multiple of the two numbers.
LCM is the shortest possible number that is divisible by both a and b.
'''

def findLCM(a, b):
    x, y = a, b
    
    while y != 0:
        x, y = y, x % y
        
    gcd = x
    
    return (a * b) // gcd 

# Examples 

a1 = 15; b1 = 20
print(findLCM(a1, b1)) # Output: 60

# Additional examples
a2 = 12; b2 = 15
print(findLCM(a2, b2)) # Output: 60

a3 = 7; b3 = 5
print(findLCM(a3, b3)) # Output: 35

a4 = 9; b4 = 6
print(findLCM(a4, b4)) # Output: 18

a5 = 8; b5 = 12
print(findLCM(a5, b5)) # Output: 24

a6 = 14; b6 = 35
print(findLCM(a6, b6)) # Output: 70

a7 = 21; b7 = 14
print(findLCM(a7, b7)) # Output: 42

a8 = 10; b8 = 25
print(findLCM(a8, b8)) # Output: 50

a9 = 18; b9 = 24
print(findLCM(a9, b9)) # Output: 72

a10 = 5; b10 = 3
print(findLCM(a10, b10)) # Output: 15

a11 = 11; b11 = 22
print(findLCM(a11, b11)) # Output: 22