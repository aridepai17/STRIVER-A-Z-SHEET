# INCREASING LETTER TRIANGLE 

def increasingLetterTriangle(n):
  ch = ord("A")
  
  for i in range(1, n+1):
    for j in range(i):
      print(chr(ch + j), end=" ")
    print()
    
# Example 
n1 = 1
print(f"Pattern for n={n1}:")
increasingLetterTriangle(n1)
# Output:
# A

n2 = 2
print(f"Pattern for n={n2}:")
increasingLetterTriangle(n2)
# Output:
# A
# A B

n3 = 3
print(f"Pattern for n={n3}:")
increasingLetterTriangle(n3)
# Output:
# A
# A B
# A B C

n4 = 4
print(f"Pattern for n={n4}:")
increasingLetterTriangle(n4)
# Output:
# A
# A B
# A B C
# A B C D

n5 = 5
print(f"Pattern for n={n5}:")
increasingLetterTriangle(n5)
# Output:
# A
# A B
# A B C
# A B C D
# A B C D E

n6 = 6
print(f"Pattern for n={n6}:")
increasingLetterTriangle(n6)
# Output:
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F

n7 = 7
print(f"Pattern for n={n7}:")
increasingLetterTriangle(n7)
# Output:
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F
# A B C D E F G

n8 = 8
print(f"Pattern for n={n8}:")
increasingLetterTriangle(n8)
# Output:
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F
# A B C D E F G
# A B C D E F G H

n9 = 9
print(f"Pattern for n={n9}:")
increasingLetterTriangle(n9)
# Output:
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F
# A B C D E F G
# A B C D E F G H
# A B C D E F G H I

n10 = 10
print(f"Pattern for n={n10}:")
increasingLetterTriangle(n10)
# Output:
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F
# A B C D E F G
# A B C D E F G H
# A B C D E F G H I
# A B C D E F G H I J
