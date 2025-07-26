# PRINT 1 TO N USING RECURSION

'''
Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion.
You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in increasing order from 1 to n.
'''

def printNumbers(n):
  if n == 0:
    return 
  printNumbers(n - 1)
  print(n)
  
# Examples
printNumbers(1)   # Should print 1
printNumbers(2)   # Should print 1, 2
printNumbers(3)   # Should print 1, 2, 3
printNumbers(4)   # Should print 1, 2, 3, 4
printNumbers(5)   # Should print 1, 2, 3, 4, 5
printNumbers(6)   # Should print 1, 2, 3, 4, 5, 6
printNumbers(7)   # Should print 1, 2, 3, 4, 5, 6, 7
printNumbers(8)   # Should print 1, 2, 3, 4, 5, 6, 7, 8
printNumbers(9)   # Should print 1, 2, 3, 4, 5, 6, 7, 8, 9
printNumbers(10)  # Should print 1, 2, 3, 4, 5, 6, 7, 8, 9, 10