# PRINT ALL DIVISORS 

'''
You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.
A number which completely divides another number is called it's divisor.
'''

import math 

def findDivisors(n):
  divisors = []
  sqrtN = int(math.sqrt(n))
  
  for i in range(1, sqrtN + 1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n // i)
        
  return divisors

# Examples 
n1 = 1
print(f"Divisors of {n1}: {findDivisors(n1)}")  # Output: [1]

n2 = 2
print(f"Divisors of {n2}: {findDivisors(n2)}")  # Output: [1, 2]

n3 = 3
print(f"Divisors of {n3}: {findDivisors(n3)}")  # Output: [1, 3]

n4 = 4
print(f"Divisors of {n4}: {findDivisors(n4)}")  # Output: [1, 2, 4]

n5 = 5
print(f"Divisors of {n5}: {findDivisors(n5)}")  # Output: [1, 5]

n6 = 12
print(f"Divisors of {n6}: {findDivisors(n6)}")  # Output: [1, 2, 3, 4, 6, 12]

n7 = 15
print(f"Divisors of {n7}: {findDivisors(n7)}")  # Output: [1, 3, 5, 15]

n8 = 28
print(f"Divisors of {n8}: {findDivisors(n8)}")  # Output: [1, 2, 4, 7, 14, 28]

n9 = 30
print(f"Divisors of {n9}: {findDivisors(n9)}")  # Output: [1, 2, 3, 5, 6, 10, 15, 30]

n10 = 36
print(f"Divisors of {n10}: {findDivisors(n10)}")  # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
      