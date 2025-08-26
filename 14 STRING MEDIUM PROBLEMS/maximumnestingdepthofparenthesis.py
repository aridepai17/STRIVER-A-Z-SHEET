# MAXIMUM NESTING DEPTH OF THE PARENTHESES

'''
Given a valid parentheses string s, return the nesting depth of s. 
The nesting depth is the maximum number of nested parentheses.
'''

def maxDepth(s):
    currentDepth = 0
    maximumDepth = 0
    
    for char in s:
        if char == '(':
            currentDepth += 1
            maximumDepth = max(maximumDepth, currentDepth)
        elif char == ')':
            currentDepth -= 1
    
    return maximumDepth

# Examples
s1 = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s1)) # Output: 3

s2 = "(1)+((2))+(((3)))"
print(maxDepth(s2)) # Output: 3

s3 = "1+(2*3)/(2-1)"
print(maxDepth(s3)) # Output: 1

s4 = "1"
print(maxDepth(s4)) # Output: 0

s5 = "()"
print(maxDepth(s5)) # Output: 1

s6 = "(()())"
print(maxDepth(s6)) # Output: 2

s7 = "((()))"
print(maxDepth(s7)) # Output: 3

s8 = "()()()"
print(maxDepth(s8)) # Output: 1

s9 = "((((()))))"
print(maxDepth(s9)) # Output: 5

s10 = "(a(b(c)d)e)"
print(maxDepth(s10)) # Output: 3

s11 = "((a+b)*(c-d))"
print(maxDepth(s11)) # Output: 2