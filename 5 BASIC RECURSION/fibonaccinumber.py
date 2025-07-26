# FIBONACCI NUMBER

'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''

def fib(n):
  if n <= 1:
    return n
  return fib(n - 1) + fib(n - 2) 

# Examples
print(fib(0))   # Should print 0
print(fib(1))   # Should print 1
print(fib(2))   # Should print 1 (F(2) = F(1) + F(0))
print(fib(3))   # Should print 2 (F(3) = F(2) + F(1))
print(fib(4))   # Should print 3 (F(4) = F(3) + F(2))
print(fib(5))   # Should print 5 (F(5) = F(4) + F(3))
print(fib(6))   # Should print 8 (F(6) = F(5) + F(4))
print(fib(7))   # Should print 13 (F(7) = F(6) + F(5))
print(fib(8))   # Should print 21 (F(8) = F(7) + F(6))
print(fib(9))   # Should print 34 (F(9) = F(8) + F(7)) 

