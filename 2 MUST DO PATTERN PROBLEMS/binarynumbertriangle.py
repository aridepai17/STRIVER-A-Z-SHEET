# BINARY NUMBER TRIANGLE PATTERN 

def binaryNumberTriangle(n):
  for i in range(1, n+1):
    for j in range(1, i+1):
      print((i + j) % 2, end= " ")
    print()
    
# Examples 
n1 = 1
print(f"Pattern for n={n1}:")
binaryNumberTriangle(n1)
# Output:
# 0

n2 = 2
print(f"Pattern for n={n2}:")
binaryNumberTriangle(n2)
# Output:
# 0
# 1 0

n3 = 3
print(f"Pattern for n={n3}:")
binaryNumberTriangle(n3)
# Output:
# 0
# 1 0
# 0 1 0

n4 = 4
print(f"Pattern for n={n4}:")
binaryNumberTriangle(n4)
# Output:
# 0
# 1 0
# 0 1 0
# 1 0 1 0

n5 = 5
print(f"Pattern for n={n5}:")
binaryNumberTriangle(n5)
# Output:
# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0

n6 = 6
print(f"Pattern for n={n6}:")
binaryNumberTriangle(n6)
# Output:
# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0
# 1 0 1 0 1 0

n7 = 7
print(f"Pattern for n={n7}:")
binaryNumberTriangle(n7)
# Output:
# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0
# 1 0 1 0 1 0
# 0 1 0 1 0 1 0

n8 = 8
print(f"Pattern for n={n8}:")
binaryNumberTriangle(n8)
# Output:
# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0
# 1 0 1 0 1 0
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1 0

n9 = 9
print(f"Pattern for n={n9}:")
binaryNumberTriangle(n9)
# Output:
# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0
# 1 0 1 0 1 0
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1 0

n10 = 10
print(f"Pattern for n={n10}:")
binaryNumberTriangle(n10)
# Output:
# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0
# 1 0 1 0 1 0
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1 0 1 0 