# SWAP TWO NUMBERS

'''
You are given two numbers a and b. Your task is to swap the given two numbers.
Note: Try to do it without a temporary variable.
'''

def swaptwoNumbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    
    return a, b

'''
Time Complexity: O(1)
The bitwise XOR operations are constant time operations. The function performs a fixed number of these operations regardless of the input values.

Space Complexity: O(1)
The function uses a constant amount of extra space to store the variables. No additional space that scales with the input is required.
'''

# Test Cases
a1 = 13, b1 = 9
print(swaptwoNumbers(a1, b1)) # Output: 9 13

a2, b2 = 5, 10
print(swaptwoNumbers(a2, b2)) # Output: 10 5

a3, b3 = 0, 7
print(swaptwoNumbers(a3, b3)) # Output: 7 0

a4, b4 = 100, 100
print(swaptwoNumbers(a4, b4)) # Output: 100 100

a5, b5 = -5, 10
print(swaptwoNumbers(a5, b5)) # Output: 10 -5

a6, b6 = -15, -25
print(swaptwoNumbers(a6, b6)) # Output: -25 -15

a7, b7 = 12345, 67890
print(swaptwoNumbers(a7, b7)) # Output: 67890 12345

a8, b8 = 1, 0
print(swaptwoNumbers(a8, b8)) # Output: 0 1

a9, b9 = 1024, 512
print(swaptwoNumbers(a9, b9)) # Output: 512 1024

a10, b10 = 42, 24
print(swaptwoNumbers(a10, b10)) # Output: 24 42