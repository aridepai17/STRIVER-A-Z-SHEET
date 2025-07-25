# REVERSE LETTER TRIANGLE 

def reverseLetterTriangle(n):
  ch = ord("A")
  
  for i in range(n, 0, -1):
    for j in range(i):
      print(chr(ch + j), end=" ")
    print()
    
# Example 
n1 = 1
print(f"Pattern for n={n1}:")
reverseLetterTriangle(n1)
# Output:
# A

n2 = 2
print(f"Pattern for n={n2}:")
reverseLetterTriangle(n2)
# Output:
# A B
# A

n3 = 3
print(f"Pattern for n={n3}:")
reverseLetterTriangle(n3)
# Output:
# A B C
# A B
# A

n4 = 4
print(f"Pattern for n={n4}:")
reverseLetterTriangle(n4)
# Output:
# A B C D
# A B C
# A B
# A

n5 = 5
print(f"Pattern for n={n5}:")
reverseLetterTriangle(n5)
# Output:
# A B C D E
# A B C D
# A B C
# A B
# A

n6 = 6
print(f"Pattern for n={n6}:")
reverseLetterTriangle(n6)
# Output:
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A

n7 = 7
print(f"Pattern for n={n7}:")
reverseLetterTriangle(n7)
# Output:
# A B C D E F G
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A

n8 = 8
print(f"Pattern for n={n8}:")
reverseLetterTriangle(n8)
# Output:
# A B C D E F G H
# A B C D E F G
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A

n9 = 9
print(f"Pattern for n={n9}:")
reverseLetterTriangle(n9)
# Output:
# A B C D E F G H I
# A B C D E F G H
# A B C D E F G
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A

n10 = 10
print(f"Pattern for n={n10}:")
reverseLetterTriangle(n10)
# Output:
# A B C D E F G H I J
# A B C D E F G H I
# A B C D E F G H
# A B C D E F G
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A