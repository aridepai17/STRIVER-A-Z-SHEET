# FACTORIAL OF A NUMBER 

# Given a number, find its factorial.

def factorial(n):
  if n == 0 or n == 1:
    return 1 
  return n * factorial(n - 1)

# Examples 
print(factorial(0))   # Should print 1 (0! = 1)
print(factorial(1))   # Should print 1 (1! = 1)
print(factorial(2))   # Should print 2 (2! = 2)
print(factorial(3))   # Should print 6 (3! = 6)
print(factorial(4))   # Should print 24 (4! = 24)
print(factorial(5))   # Should print 120 (5! = 120)
print(factorial(6))   # Should print 720 (6! = 720)
print(factorial(7))   # Should print 5040 (7! = 5040)
print(factorial(8))   # Should print 40320 (8! = 40320)
print(factorial(9))   # Should print 362880 (9! = 362880) 