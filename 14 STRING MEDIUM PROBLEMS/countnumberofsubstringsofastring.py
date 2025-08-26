# COUNT NUMBER OF SUBSTRINGS OF A STRING

'''
Given a string `s`, your task is to determine the total number of 
**non-empty substrings** that can be formed from the string.

A substring is defined as a contiguous sequence of characters within the string.
'''

def countSubstrings(s):
    n = len(s)
    
    return (n * (n + 1)) // 2

# Examples
s1 = "abcde"
print(countSubstrings(s1)) # Output: 15

s2 = ""
print(countSubstrings(s2)) # Output: 0

s3 = "a"
print(countSubstrings(s3)) # Output: 1

s4 = "aa"
print(countSubstrings(s4)) # Output: 3

s5 = "aba"
print(countSubstrings(s5)) # Output: 6

s6 = "abcdef"
print(countSubstrings(s6)) # Output: 21

s7 = "aaaa"
print(countSubstrings(s7)) # Output: 10

s8 = "abcabc"
print(countSubstrings(s8)) # Output: 21

s9 = "xyz"
print(countSubstrings(s9)) # Output: 6

s10 = "hello"
print(countSubstrings(s10)) # Output: 15

s11 = "1234567890"
print(countSubstrings(s11)) # Output: 55