# ALPHA TRIANGLE 

def alphaTriangle(n):
  startChar = ord("A") + n - 1
  
  for i in range(1, n+1):
    for j in range(i):
      print(chr(startChar - j), end=" ")
    print()
    
# Example 
n1 = 1
print(f"Pattern for n={n1}:")
alphaTriangle(n1)
# Output:
# A

n2 = 2
print(f"Pattern for n={n2}:")
alphaTriangle(n2)
# Output:
# B
# A B

n3 = 3
print(f"Pattern for n={n3}:")
alphaTriangle(n3)
# Output:
# C
# B C
# A B C

n4 = 4
print(f"Pattern for n={n4}:")
alphaTriangle(n4)
# Output:
# D
# C D
# B C D
# A B C D

n5 = 5
print(f"Pattern for n={n5}:")
alphaTriangle(n5)
# Output:
# E
# D E
# C D E
# B C D E
# A B C D E

n6 = 6
print(f"Pattern for n={n6}:")
alphaTriangle(n6)
# Output:
# F
# E F
# D E F
# C D E F
# B C D E F
# A B C D E F

n7 = 7
print(f"Pattern for n={n7}:")
alphaTriangle(n7)
# Output:
# G
# F G
# E F G
# D E F G
# C D E F G
# B C D E F G
# A B C D E F G

n8 = 8
print(f"Pattern for n={n8}:")
alphaTriangle(n8)
# Output:
# H
# G H
# F G H
# E F G H
# D E F G H
# C D E F G H
# B C D E F G H
# A B C D E F G H

n9 = 9
print(f"Pattern for n={n9}:")
alphaTriangle(n9)
# Output:
# I
# H I
# G H I
# F G H I
# E F G H I
# D E F G H I
# C D E F G H I
# B C D E F G H I
# A B C D E F G H I

n10 = 10
print(f"Pattern for n={n10}:")
alphaTriangle(n10)
# Output:
# J
# I J
# H I J
# G H I J
# F G H I J
# E F G H I J
# D E F G H I J
# C D E F G H I J
# B C D E F G H I J
# A B C D E F G H I J 