# LARGEST ODD NUMBER IN STRING

'''
You are given a string num, representing a large integer. 
Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.
'''

def largestOddNumber(s):
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 == 1:
            return s[:i+1]
    return ""

# Example
s1 = "504"
print(largestOddNumber(s1)) # Output: "5"

# Additional examples
s2 = "4206"
print(largestOddNumber(s2)) # Output: ""

s3 = "35427"
print(largestOddNumber(s3)) # Output: "35427"

s4 = "123456"
print(largestOddNumber(s4)) # Output: "12345"

s5 = "2468"
print(largestOddNumber(s5)) # Output: ""

s6 = "13579"
print(largestOddNumber(s6)) # Output: "13579"

s7 = "1000"
print(largestOddNumber(s7)) # Output: "1"

s8 = "9999"
print(largestOddNumber(s8)) # Output: "9999"

s9 = "246135"
print(largestOddNumber(s9)) # Output: "246135"

s10 = "0000"
print(largestOddNumber(s10)) # Output: ""