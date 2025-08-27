# LONGEST PALINDROMIC SUBSTRING

'''
Given a string s, return the longest palindromic substring in s.
A string is palindromic if it reads the same forward and backward.
'''

def longestPalindrome(s):
    result = ""
    resultLength = 0
    
    for i in range(len(s)):
        # Odd Length strings
        
        left = i
        right = i
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > resultLength:
                result = s[left : right + 1]
                resultLength = right - left + 1
            left -= 1
            right += 1
            
        # Even length strings
        
        left = i
        right = i + 1
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > resultLength:
                result = s[left : right + 1]
                resultLength = right - left + 1
            left -= 1
            right += 1
            
    return result

# Examples
s1 = "babad"
print(longestPalindrome(s1)) # Output: "bab"

s2 = "cbbd"
print(longestPalindrome(s2)) # Output: "bb"

s3 = "a"
print(longestPalindrome(s3)) # Output: "a"

s4 = "ac"
print(longestPalindrome(s4)) # Output: "a"

s5 = "racecar"
print(longestPalindrome(s5)) # Output: "racecar"

s6 = "forgeeksskeegfor"
print(longestPalindrome(s6)) # Output: "geeksskeeg"

s7 = "abacdfgdcaba"
print(longestPalindrome(s7)) # Output: "aba"

s8 = "aaaa"
print(longestPalindrome(s8)) # Output: "aaaa"

s9 = "abcda"
print(longestPalindrome(s9)) # Output: "a"

s10 = "bananas"
print(longestPalindrome(s10)) # Output: "anana"

s11 = ""
print(longestPalindrome(s11)) # Output: ""