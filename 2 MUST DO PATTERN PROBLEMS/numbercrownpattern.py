# NUMBER CROWN PATTERN 

def numberCrown(n):
  for i in range(1, n+1):
    for j in range(1, i+1):
      print(j, end=" ")
      
    spaces = 2 * (n - i)
    print(" " * spaces, end="")
    
    for j in range(i, 0, -1):
      print(j, end=" ")
    
    print()
    
# Example
n1 = 1
print(f"Pattern for n={n1}:")
numberCrown(n1)
# Output:
# 1 1

n2 = 2
print(f"Pattern for n={n2}:")
numberCrown(n2)
# Output:
# 1     1
# 1 2 2 1

n3 = 3
print(f"Pattern for n={n3}:")
numberCrown(n3)
# Output:
# 1         1
# 1 2     2 1
# 1 2 3 3 2 1

n4 = 4
print(f"Pattern for n={n4}:")
numberCrown(n4)
# Output:
# 1             1
# 1 2         2 1
# 1 2 3     3 2 1
# 1 2 3 4 4 3 2 1

n5 = 5
print(f"Pattern for n={n5}:")
numberCrown(n5)
# Output:
# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1

n6 = 6
print(f"Pattern for n={n6}:")
numberCrown(n6)
# Output:
# 1                     1
# 1 2                 2 1
# 1 2 3             3 2 1
# 1 2 3 4         4 3 2 1
# 1 2 3 4 5     5 4 3 2 1
# 1 2 3 4 5 6 6 5 4 3 2 1

n7 = 7
print(f"Pattern for n={n7}:")
numberCrown(n7)
# Output:
# 1                         1
# 1 2                     2 1
# 1 2 3                 3 2 1
# 1 2 3 4             4 3 2 1
# 1 2 3 4 5         5 4 3 2 1
# 1 2 3 4 5 6     6 5 4 3 2 1
# 1 2 3 4 5 6 7 7 6 5 4 3 2 1

n8 = 8
print(f"Pattern for n={n8}:")
numberCrown(n8)
# Output:
# 1                             1
# 1 2                         2 1
# 1 2 3                     3 2 1
# 1 2 3 4                 4 3 2 1
# 1 2 3 4 5             5 4 3 2 1
# 1 2 3 4 5 6         6 5 4 3 2 1
# 1 2 3 4 5 6 7     7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 8 7 6 5 4 3 2 1

n9 = 9
print(f"Pattern for n={n9}:")
numberCrown(n9)
# Output:
# 1                                 1
# 1 2                             2 1
# 1 2 3                         3 2 1
# 1 2 3 4                     4 3 2 1
# 1 2 3 4 5                 5 4 3 2 1
# 1 2 3 4 5 6             6 5 4 3 2 1
# 1 2 3 4 5 6 7         7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8     8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 9 8 7 6 5 4 3 2 1

n10 = 10
print(f"Pattern for n={n10}:")
numberCrown(n10)
# Output:
# 1                                     1
# 1 2                                 2 1
# 1 2 3                             3 2 1
# 1 2 3 4                         4 3 2 1
# 1 2 3 4 5                     5 4 3 2 1
# 1 2 3 4 5 6                 6 5 4 3 2 1
# 1 2 3 4 5 6 7             7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8         8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9     9 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 10 10 9 8 7 6 5 4 3 2 1
