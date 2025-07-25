# ALPHA HILL PATTERN 

def alphaHill(n):
  for i in range(n):
    print(" " * (n - i - 1), end="")
    
    for j in range(i + 1):
      print(chr(ord("A") + j), end=" ")
      
    for j in range(i - 1, -1 , -1):
      print(chr(ord("A") + j), end=" ")
      
    print()
    
# Example 
n1 = 1
print(f"Pattern for n={n1}:")
alphaHill(n1)
# Output:
# A

n2 = 2
print(f"Pattern for n={n2}:")
alphaHill(n2)
# Output:
#  A
# A B A

n3 = 3
print(f"Pattern for n={n3}:")
alphaHill(n3)
# Output:
#   A
#  A B A
# A B C A B

n4 = 4
print(f"Pattern for n={n4}:")
alphaHill(n4)
# Output:
#    A
#   A B A
#  A B C A B
# A B C D A B C

n5 = 5
print(f"Pattern for n={n5}:")
alphaHill(n5)
# Output:
#     A
#    A B A
#   A B C A B
#  A B C D A B C
# A B C D E A B C D

n6 = 6
print(f"Pattern for n={n6}:")
alphaHill(n6)
# Output:
#      A
#     A B A
#    A B C A B
#   A B C D A B C
#  A B C D E A B C D
# A B C D E F A B C D E

n7 = 7
print(f"Pattern for n={n7}:")
alphaHill(n7)
# Output:
#       A
#      A B A
#     A B C A B
#    A B C D A B C
#   A B C D E A B C D
#  A B C D E F A B C D E
# A B C D E F G A B C D E F

n8 = 8
print(f"Pattern for n={n8}:")
alphaHill(n8)
# Output:
#        A
#       A B A
#      A B C A B
#     A B C D A B C
#    A B C D E A B C D
#   A B C D E F A B C D E
#  A B C D E F G A B C D E F
# A B C D E F G H A B C D E F G

n9 = 9
print(f"Pattern for n={n9}:")
alphaHill(n9)
# Output:
#         A
#        A B A
#       A B C A B
#      A B C D A B C
#     A B C D E A B C D
#    A B C D E F A B C D E
#   A B C D E F G A B C D E F
#  A B C D E F G H A B C D E F G
# A B C D E F G H I A B C D E F G H

n10 = 10
print(f"Pattern for n={n10}:")
alphaHill(n10)
# Output:
#          A
#         A B A
#        A B C A B
#       A B C D A B C
#      A B C D E A B C D
#     A B C D E F A B C D E
#    A B C D E F G A B C D E F
#   A B C D E F G H A B C D E F G
#  A B C D E F G H I A B C D E F G H
# A B C D E F G H I J A B C D E F G H I 
    