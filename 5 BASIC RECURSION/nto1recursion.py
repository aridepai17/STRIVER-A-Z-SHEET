# PRINT N TO 1 USING RECURSION 

'''
Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.
You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in decreasing order from n to 1
'''

def printDescending(n):
  if n == 0:
    return 
  print(n)
  printDescending(n - 1)
  
# Examples 
printDescending(1)   # Should print 1
printDescending(2)   # Should print 2, 1
printDescending(3)   # Should print 3, 2, 1
printDescending(4)   # Should print 4, 3, 2, 1
printDescending(5)   # Should print 5, 4, 3, 2, 1
printDescending(6)   # Should print 6, 5, 4, 3, 2, 1
printDescending(7)   # Should print 7, 6, 5, 4, 3, 2, 1
printDescending(8)   # Should print 8, 7, 6, 5, 4, 3, 2, 1
printDescending(9)   # Should print 9, 8, 7, 6, 5, 4, 3, 2, 1
printDescending(10)  # Should print 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 