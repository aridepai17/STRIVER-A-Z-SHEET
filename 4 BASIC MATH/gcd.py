# GCD OF TWO NUMBERS 

'''
You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. 
Return the GCD of the two numbers.
The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.
'''

def GCD(a, b):
  while a > 0 and b > 0:
    if a > b:
      a = a % b
    else:
      b = b % a
  if a == 0:
    return b
  return a

# Example
n1 = 48
n2 = 18
print(f"GCD of {n1} and {n2}: {GCD(n1, n2)}")  # Output: 6

n3 = 56
n4 = 98
print(f"GCD of {n3} and {n4}: {GCD(n3, n4)}")  # Output: 14

n5 = 101
n6 = 10
print(f"GCD of {n5} and {n6}: {GCD(n5, n6)}")  # Output: 1

n7 = 100
n8 = 25
print(f"GCD of {n7} and {n8}: {GCD(n7, n8)}")  # Output: 25

n9 = 17
n10 = 34
print(f"GCD of {n9} and {n10}: {GCD(n9, n10)}")  # Output: 17

n11 = 0
n12 = 5
print(f"GCD of {n11} and {n12}: {GCD(n11, n12)}")  # Output: 5

n13 = 0
n14 = 0
print(f"GCD of {n13} and {n14}: {GCD(n13, n14)}")  # Output: 0

n15 = 12
n16 = 15
print(f"GCD of {n15} and {n16}: {GCD(n15, n16)}")  # Output: 3

n17 = 81
n18 = 27
print(f"GCD of {n17} and {n18}: {GCD(n17, n18)}")  # Output: 27

n19 = 14
n20 = 28
print(f"GCD of {n19} and {n20}: {GCD(n19, n20)}")  # Output: 14