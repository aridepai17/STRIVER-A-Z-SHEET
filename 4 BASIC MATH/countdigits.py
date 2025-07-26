# COUNT ALL DIGITS OF A NUMBER 

'''
You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.
'''

def countDigit(n):
  count = 0
  while n > 0:
    count += 1
    n //= 10
  return count

# Examples
n1 = 0
print(f"Number of digits in {n1}: {countDigit(n1)}")  # Output: 1

n2 = 5
print(f"Number of digits in {n2}: {countDigit(n2)}")  # Output: 1

n3 = 12
print(f"Number of digits in {n3}: {countDigit(n3)}")  # Output: 2

n4 = 123
print(f"Number of digits in {n4}: {countDigit(n4)}")  # Output: 3

n5 = 4567
print(f"Number of digits in {n5}: {countDigit(n5)}")  # Output: 4

n6 = 89012
print(f"Number of digits in {n6}: {countDigit(n6)}")  # Output: 5

n7 = 1234567
print(f"Number of digits in {n7}: {countDigit(n7)}")  # Output: 7

n8 = 987654321
print(f"Number of digits in {n8}: {countDigit(n8)}")  # Output: 9

n9 = 1000000000
print(f"Number of digits in {n9}: {countDigit(n9)}")  # Output: 10

n10 = 9999999999
print(f"Number of digits in {n10}: {countDigit(n10)}")  # Output: 10