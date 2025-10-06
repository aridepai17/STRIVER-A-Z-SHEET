# FIND XOR OF NUMBERS FROM L TO R

'''
You are given two integers L and R, your task is to find the XOR of elements of the range [L, R].
'''

def findXOR(l, r):
    if l > r:
        return 0
    
    def xorUpto(n):
        if n < 0:
            return 0
        
        remainder = n % 4
        
        if remainder == 0:
            return n
        elif remainder == 1:
            return 1
        elif remainder == 2:
            return n + 1
        else:
            return 0
        
        
    xorR = xorUpto(r)
    xorL = xorUpto(l - 1)
    
    return xorR ^ xorL

'''
Time Complexity: O(1)
The function `xorUpto(n)` calculates the XOR sum from 0 to n in constant time. It uses a mathematical property based on the remainder of n when divided by 4. All operations inside `xorUpto` (modulo, comparison, addition) are constant time operations.
The `findXOR` function makes two calls to `xorUpto` and performs one XOR operation, all of which are O(1).
Therefore, the overall time complexity of the `findXOR` function is O(1).

Space Complexity: O(1)
The algorithm uses a fixed amount of memory to store variables (`remainder`, `xorR`, `xorL`). The space required does not scale with the input values `l` and `r`.
Therefore, the space complexity is O(1).
'''

# Test Cases
l1 = 4, r1 = 8
print(findXOR(l1, r1)) # Output: 8

l2, r2 = 1, 5
print(findXOR(l2, r2)) # Output: 1

l3, r3 = 10, 10
print(findXOR(l3, r3)) # Output: 10

l4, r4 = 0, 3
print(findXOR(l4, r4)) # Output: 0

l5, r5 = 15, 20
print(findXOR(l5, r5)) # Output: 27

l6, r6 = 10, 5
print(findXOR(l6, r6)) # Output: 0

l7, r7 = 5, 10
print(findXOR(l7, r7)) # Output: 15

l8, r8 = 0, 0
print(findXOR(l8, r8)) # Output: 0

l9, r9 = 1, 10
print(findXOR(l9, r9)) # Output: 11

l10, r10 = 100, 200
print(findXOR(l10, r10)) # Output: 200