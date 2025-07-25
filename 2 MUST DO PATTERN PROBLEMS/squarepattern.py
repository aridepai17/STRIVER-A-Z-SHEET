# PATTERN 1 

'''
Geek is very fond of patterns. Once, his teacher gave him a square pattern to solve. He gave Geek an integer n and asked him to build a pattern.
Help Geek to build a square pattern with the help of *  such that each * is space-separated in each line.
'''

def printSquare(n):
  for i in range(n):
    print("* " * n)
    
# Example
n1 = 3
print(printSquare(n1))  # Output: 
# * * * 
# * * * 
# * * * 

# Additional examples
n2 = 1
print(printSquare(n2))  # Output: 
# * 

n3 = 2
print(printSquare(n3))  # Output: 
# * * 
# * * 

n4 = 4
print(printSquare(n4))  # Output: 
# * * * * 
# * * * * 
# * * * * 
# * * * * 

n5 = 5
print(printSquare(n5))  # Output: 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

n6 = 6
print(printSquare(n6))  # Output: 
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 

n7 = 7
print(printSquare(n7))  # Output: 
# * * * * * * * 
# * * * * * * * 
# * * * * * * * 
# * * * * * * * 
# * * * * * * * 
# * * * * * * * 
# * * * * * * * 

n8 = 8
print(printSquare(n8))  # Output: 
# * * * * * * * * 
# * * * * * * * * 
# * * * * * * * * 
# * * * * * * * * 
# * * * * * * * * 
# * * * * * * * * 
# * * * * * * * * 
# * * * * * * * * 

n9 = 9
print(printSquare(n9))  # Output: 
# * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * 