# STRING TO INTEGER (ATOI)

'''
Implement the function myAtoi(string s), which converts a string into 
a 32-bit signed integer.

The algorithm works as follows:

1. Whitespace:
- Ignore any leading whitespace characters (' ').

2. Signedness:
- Check if the next character is either '-' or '+'.
- If present, this determines the sign of the integer.
- If neither is present, assume the integer is positive.

3. Conversion:
- Read the digits of the integer, ignoring leading zeros.
- Stop reading once a non-digit character is encountered 
    or the end of the string is reached.
- If no digits were read, return 0.

4. Rounding (Clamping to 32-bit range):
- The valid range is [-2^31, 2^31 - 1] 
    i.e., [-2147483648, 2147483647].
- If the integer is less than -2^31, return -2^31.
- If the integer is greater than 2^31 - 1, return 2^31 - 1.

Return the final integer as the result.
'''

def myAtoi(s):
    if not s:
        return 0
    
    s = s.strip()
    
    sign = 1
    result = 0
    
    if s[0] in ['-', '+']:
        if s[0] == '-':
            sign = -1
        s = s[1:]
        
    for char in s:
        if not char.isdigit():
            break
        result = result * 10 + int(char)
        
    result *= sign
    
    MIN = -2 ** 31 
    MAX = 2 ** 31 - 1
    
    if result > MAX:
        return MAX
    if result < MIN:
        return MIN 
    return result

# Examples
s1 = " -042"
print(myAtoi(s1)) # Output: -42

s2 = "42"
print(myAtoi(s2)) # Output: 42

s3 = "    +4193 with words"
print(myAtoi(s3)) # Output: 4193

s4 = "words and 987"
print(myAtoi(s4)) # Output: 0

s5 = "-91283472332"
print(myAtoi(s5)) # Output: -2147483648

s6 = "91283472332"
print(myAtoi(s6)) # Output: 2147483647

s7 = "+0000000000012345678"
print(myAtoi(s7)) # Output: 12345678

s8 = "-000"
print(myAtoi(s8)) # Output: 0

s9 = "+-12"
print(myAtoi(s9)) # Output: 0

s10 = "0032"
print(myAtoi(s10)) # Output: 32

s11 = "  -0012a42"
print(myAtoi(s11)) # Output: -12