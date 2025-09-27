# BINARY STRING TO DECIMAL

'''
Given a string `s` which represents a binary number, your task is to convert this binary string into its equivalent decimal integer.
The binary string will consist only of '0's and '1's.
'''

def binarystringtoDecimal(s):
    n = len(s)
    total = 0
    powerof2 = 1
    
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            total += powerof2
        powerof2 *= 2
        
    return total

'''
Time Complexity: O(n)
The function iterates through the input string `s` once from right to left. Let `n` be the length of the string.
The loop runs `n` times. Inside the loop, all operations (character access, comparison, addition, multiplication) are performed in constant time.
Therefore, the total time complexity is directly proportional to the length of the string, making it O(n).

Space Complexity: O(1)
The function uses a fixed number of variables (`n`, `total`, `powerof2`, `i`) to store values.
The amount of memory required for these variables does not change with the size of the input string.
Thus, the space complexity is constant, O(1).
'''

# Test Cases
s1 = '101'
print(binarystringtoDecimal(s1)) # Output: 5

s2 = '0'
print(binarystringtoDecimal(s2)) # Output: 0

s3 = '1'
print(binarystringtoDecimal(s3)) # Output: 1

s4 = '10'
print(binarystringtoDecimal(s4)) # Output: 2

s5 = '111'
print(binarystringtoDecimal(s5)) # Output: 7

s6 = '1010'
print(binarystringtoDecimal(s6)) # Output: 10

s7 = '10000'
print(binarystringtoDecimal(s7)) # Output: 16

s8 = '1111'
print(binarystringtoDecimal(s8)) # Output: 15

s9 = '1100100'
print(binarystringtoDecimal(s9)) # Output: 100

s10 = '11111111'
print(binarystringtoDecimal(s10)) # Output: 255