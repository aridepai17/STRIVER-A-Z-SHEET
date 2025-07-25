# CONCENTRIC NUMBER PATTERN 

def concentricNumberPattern(n):
  size = 2 * n - 1
  for i in range(size):
    for j in range(size): 
      minDist = min(i, j, size - i - 1, size - j - 1)
      print(n - minDist, end = " ")
    print()
    
# Example 
n1 = 1
print(f"Pattern for n={n1}:")
concentricNumberPattern(n1)
# Output:
# 1

n2 = 2
print(f"Pattern for n={n2}:")
concentricNumberPattern(n2)
# Output:
# 2 2
# 2 1 2
# 2 2

n3 = 3
print(f"Pattern for n={n3}:")
concentricNumberPattern(n3)
# Output:
# 3 3 3
# 3 2 3
# 3 3 3

n4 = 4
print(f"Pattern for n={n4}:")
concentricNumberPattern(n4)
# Output:
# 4 4 4 4 4
# 4 3 3 3 4
# 4 3 2 3 4
# 4 3 3 3 4
# 4 4 4 4 4

n5 = 5
print(f"Pattern for n={n5}:")
concentricNumberPattern(n5)
# Output:
# 5 5 5 5 5 5 5
# 5 4 4 4 4 4 5
# 5 4 3 3 3 4 5
# 5 4 3 2 3 4 5
# 5 4 3 3 3 4 5
# 5 4 4 4 4 4 5
# 5 5 5 5 5 5 5

n6 = 6
print(f"Pattern for n={n6}:")
concentricNumberPattern(n6)
# Output:
# 6 6 6 6 6 6 6 6 6
# 6 5 5 5 5 5 5 5 6
# 6 5 4 4 4 4 5 5 6
# 6 5 4 3 3 4 5 5 6
# 6 5 4 4 4 4 5 5 6
# 6 5 5 5 5 5 5 5 6
# 6 6 6 6 6 6 6 6 6

n7 = 7
print(f"Pattern for n={n7}:")
concentricNumberPattern(n7)
# Output:
# 7 7 7 7 7 7 7 7 7 7 7
# 7 6 6 6 6 6 6 6 6 6 7
# 7 6 5 5 5 5 5 5 5 6 7
# 7 6 5 4 4 4 4 5 5 6 7
# 7 6 5 4 3 3 4 5 5 6 7
# 7 6 5 4 4 4 4 5 5 6 7
# 7 6 5 5 5 5 5 5 6 6 7
# 7 6 6 6 6 6 6 6 6 6 7
# 7 7 7 7 7 7 7 7 7 7 7

n8 = 8
print(f"Pattern for n={n8}:")
concentricNumberPattern(n8)
# Output:
# 8 8 8 8 8 8 8 8 8 8 8 8 8
# 8 7 7 7 7 7 7 7 7 7 7 7 8
# 8 7 6 6 6 6 6 6 6 6 7 8
# 8 7 6 5 5 5 5 5 6 7 8
# 8 7 6 5 4 4 4 5 6 7 8
# 8 7 6 5 4 3 4 5 6 7 8
# 8 7 6 5 4 4 4 5 6 7 8
# 8 7 6 6 6 6 6 6 7 8
# 8 7 7 7 7 7 7 7 7 8
# 8 8 8 8 8 8 8 8 8 8 8 8 8

n9 = 9
print(f"Pattern for n={n9}:")
concentricNumberPattern(n9)
# Output:
# 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
# 9 8 8 8 8 8 8 8 8 8 8 8 8 9
# 9 8 7 7 7 7 7 7 7 7 7 8 9
# 9 8 7 6 6 6 6 6 7 8 9
# 9 8 7 6 5 5 5 6 7 8 9
# 9 8 7 6 5 4 5 6 7 8 9
# 9 8 7 6 5 5 5 6 7 8 9
# 9 8 7 7 7 7 7 8 9
# 9 8 8 8 8 8 8 9
# 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9

n10 = 10
print(f"Pattern for n={n10}:")
concentricNumberPattern(n10)
# Output:
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
# 10 9 9 9 9 9 9 9 9 9 9 9 9 9 10
# 10 9 8 8 8 8 8 8 8 8 8 9 10
# 10 9 8 7 7 7 7 7 8 9 10
# 10 9 8 7 6 6 6 7 8 9 10
# 10 9 8 7 6 5 6 7 8 9 10
# 10 9 8 7 6 6 6 7 8 9 10
# 10 9 8 8 8 8 8 9 10
# 10 9 9 9 9 9 9 10
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 