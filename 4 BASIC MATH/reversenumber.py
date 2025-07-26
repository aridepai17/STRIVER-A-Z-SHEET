# REVERSE A NUMBER 

# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.

def reverseNumber(n):
  rev = 0
  while n > 0:
    lastDigit = n % 10
    rev = (rev * 10) + lastDigit 
    n //= 10
  return rev 

# Examples 
n1 = 0
print(f"Reverse of {n1}: {reverseNumber(n1)}")  # Output: 0

n2 = 5
print(f"Reverse of {n2}: {reverseNumber(n2)}")  # Output: 5

n3 = 12
print(f"Reverse of {n3}: {reverseNumber(n3)}")  # Output: 21

n4 = 123
print(f"Reverse of {n4}: {reverseNumber(n4)}")  # Output: 321

n5 = 4567
print(f"Reverse of {n5}: {reverseNumber(n5)}")  # Output: 7654

n6 = 89012
print(f"Reverse of {n6}: {reverseNumber(n6)}")  # Output: 21098

n7 = 100
print(f"Reverse of {n7}: {reverseNumber(n7)}")  # Output: 1

n8 = 987654321
print(f"Reverse of {n8}: {reverseNumber(n8)}")  # Output: 123456789

n9 = 1000000000
print(f"Reverse of {n9}: {reverseNumber(n9)}")  # Output: 1

n10 = 1234567890
print(f"Reverse of {n10}: {reverseNumber(n10)}")  # Output: 987654321 