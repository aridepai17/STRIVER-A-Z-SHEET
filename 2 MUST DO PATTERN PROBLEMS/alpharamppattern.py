# ALPHA RAMP PATTERN 

def alphaRampPattern(n):
  for i in range(n):
    ch = chr(ord('A') + i)
    for j in range(i + 1):
      print(ch, end=" ")
    print()
    
# Example 
n1 = 1
print(f"Pattern for n={n1}:")
alphaRampPattern(n1)
# Output:
# A

n2 = 2
print(f"Pattern for n={n2}:")
alphaRampPattern(n2)
# Output:
# A
# B B

n3 = 3
print(f"Pattern for n={n3}:")
alphaRampPattern(n3)
# Output:
# A
# B B
# C C C

n4 = 4
print(f"Pattern for n={n4}:")
alphaRampPattern(n4)
# Output:
# A
# B B
# C C C
# D D D D

n5 = 5
print(f"Pattern for n={n5}:")
alphaRampPattern(n5)
# Output:
# A
# B B
# C C C
# D D D D
# E E E E E

n6 = 6
print(f"Pattern for n={n6}:")
alphaRampPattern(n6)
# Output:
# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F

n7 = 7
print(f"Pattern for n={n7}:")
alphaRampPattern(n7)
# Output:
# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F
# G G G G G G G

n8 = 8
print(f"Pattern for n={n8}:")
alphaRampPattern(n8)
# Output:
# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F
# G G G G G G G
# H H H H H H H H

n9 = 9
print(f"Pattern for n={n9}:")
alphaRampPattern(n9)
# Output:
# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F
# G G G G G G G
# H H H H H H H H
# I I I I I I I I I

n10 = 10
print(f"Pattern for n={n10}:")
alphaRampPattern(n10)
# Output:
# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F
# G G G G G G G
# H H H H H H H H
# I I I I I I I I I
# J J J J J J J J J J 