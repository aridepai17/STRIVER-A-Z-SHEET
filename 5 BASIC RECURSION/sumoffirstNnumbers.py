# SUM OF FIRST N NUMBERS 

# Given an integer N, return the sum of first N natural numbers. 
# Try to solve this problem using recursion.

def numberSum(n):
  if n == 0:
    return 0
  return n + numberSum(n - 1)

# Examples
print(numberSum(1))   # Should print 1
print(numberSum(2))   # Should print 3 (1 + 2)
print(numberSum(3))   # Should print 6 (1 + 2 + 3)
print(numberSum(4))   # Should print 10 (1 + 2 + 3 + 4)
print(numberSum(5))   # Should print 15 (1 + 2 + 3 + 4 + 5)
print(numberSum(6))   # Should print 21 (1 + 2 + 3 + 4 + 5 + 6)
print(numberSum(7))   # Should print 28 (1 + 2 + 3 + 4 + 5 + 6 + 7)
print(numberSum(8))   # Should print 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
print(numberSum(9))   # Should print 45 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)
print(numberSum(10))  # Should print 55 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)