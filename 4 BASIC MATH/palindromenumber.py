# PALINDROME NUMBER 

'''
You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
A palindrome number is a number which reads the same both left to right and right to left.
'''

def isPalindrome(n):
  rev = 0
  dup = n
  while n > 0:
    lastDigit = n % 10
    rev = (rev * 10) + lastDigit 
    n //= 10
  return rev == dup

# Examples
n1 = 0
print(f"Is {n1} a palindrome? {isPalindrome(n1)}")  # Output: True

n2 = 5
print(f"Is {n2} a palindrome? {isPalindrome(n2)}")  # Output: True

n3 = 121
print(f"Is {n3} a palindrome? {isPalindrome(n3)}")  # Output: True

n4 = 12321
print(f"Is {n4} a palindrome? {isPalindrome(n4)}")  # Output: True

n5 = 123
print(f"Is {n5} a palindrome? {isPalindrome(n5)}")  # Output: False

n6 = 1221
print(f"Is {n6} a palindrome? {isPalindrome(n6)}")  # Output: True

n7 = 1234321
print(f"Is {n7} a palindrome? {isPalindrome(n7)}")  # Output: True

n8 = 123456
print(f"Is {n8} a palindrome? {isPalindrome(n8)}")  # Output: False

n9 = 1001
print(f"Is {n9} a palindrome? {isPalindrome(n9)}")  # Output: True

n10 = 12345678987654321
print(f"Is {n10} a palindrome? {isPalindrome(n10)}")  # Output: True