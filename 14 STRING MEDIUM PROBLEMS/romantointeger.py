# ROMAN TO INTEGER

'''
Roman numerals are represented by seven different symbols:

Symbol   Value
----------------
I         1
V         5
X         10
L         50
C         100
D         500
M         1000

Examples:
- 2 is written as II (1 + 1).
- 12 is written as XII (10 + 1 + 1).
- 27 is written as XXVII (10 + 10 + 5 + 1 + 1).

Normally, numerals are written from largest to smallest left to right.
However, there are six special cases where subtraction is used:

- I before V (5) → 4
- I before X (10) → 9
- X before L (50) → 40
- X before C (100) → 90
- C before D (500) → 400
- C before M (1000) → 900

Task:
Given a Roman numeral string `s`, convert it into an integer.
'''

def romantoInt(s):
    roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    
    result = 0
    
    for char in range(len(s)):
        if char + 1 < len(s) and roman[s[char]] < roman[s[char + 1]]:
            result -= roman[s[char]]
        else:
            result += roman[s[char]]
            
    return result

# Examples
s1 = "III"
print(romantoInt(s1)) # Output: 3

s2 = "IV"
print(romantoInt(s2)) # Output: 4

s3 = "IX"
print(romantoInt(s3)) # Output: 9

s4 = "LVIII"
print(romantoInt(s4)) # Output: 58

s5 = "MCMXCIV"
print(romantoInt(s5)) # Output: 1994

s6 = "MMMCMXCIX"
print(romantoInt(s6)) # Output: 3999

s7 = "XL"
print(romantoInt(s7)) # Output: 40

s8 = "XC"
print(romantoInt(s8)) # Output: 90

s9 = "CD"
print(romantoInt(s9)) # Output: 400

s10 = "CM"
print(romantoInt(s10)) # Output: 900

s11 = "MMXXIII"
print(romantoInt(s11)) # Output: 2023