# INTEGER TO ROMAN

'''
You are given an integer, and your task is to convert it into a Roman numeral.

Seven different symbols represent Roman numerals with the following values:

Symbol   Value
I        1
V        5
X        10
L        50
C        100
D        500
M        1000

Roman numerals are formed by appending the conversions of decimal place values 
from highest to lowest, following these rules:

1. If the value does not start with 4 or 9:
- Select the symbol of the maximum value that can be subtracted from the number.
- Append that symbol to the result.
- Subtract its value from the number and continue.

2. If the value starts with 4 or 9:
- Use the subtractive form (one symbol placed before the next higher symbol).
- Examples:
4  -> IV   (1 before 5)
9  -> IX   (1 before 10)
40 -> XL   (10 before 50)
90 -> XC   (10 before 100)
400 -> CD  (100 before 500)
900 -> CM  (100 before 1000)

3. Only the symbols representing powers of 10 (I, X, C, M) 
can be repeated at most 3 times in succession.
- For example: III = 3, XXX = 30, CCC = 300, MMM = 3000
- Symbols for 5 (V), 50 (L), and 500 (D) cannot be repeated.
- If a symbol would need to appear 4 times, use the subtractive form instead.

Return the Roman numeral representation of the given integer.
'''

def intToRoman(num):
    roman = [
        ["M" , 1000],
        ["CM" , 900],
        ["D" , 500],
        ["CD" , 400],
        ["C" , 100],
        ["XC" , 90],
        ["L" , 50],
        ["XL" , 40],
        ["X" , 10],
        ["IX" , 9],
        ["V" , 5],
        ["IV" , 4],
        ["I" , 1]
    ]
    
    result = []
    
    for char, value in roman:
        while num >= value:
            result.append(char)
            num -= value
            
    return "".join(result)

# Examples
num1 = 3749
print(intToRoman(num1)) # Output: "MMMDCCXLIX" 

num2 = 4
print(intToRoman(num2)) # Output: "IV"

num3 = 9
print(intToRoman(num3)) # Output: "IX"

num4 = 58
print(intToRoman(num4)) # Output: "LVIII"

num5 = 1994
print(intToRoman(num5)) # Output: "MCMXCIV"

num6 = 3999
print(intToRoman(num6)) # Output: "MMMCMXCIX"

num7 = 40
print(intToRoman(num7)) # Output: "XL"

num8 = 90
print(intToRoman(num8)) # Output: "XC"

num9 = 400
print(intToRoman(num9)) # Output: "CD"

num10 = 900
print(intToRoman(num10)) # Output: "CM"

num11 = 2023
print(intToRoman(num11)) # Output: "MMXXIII" 