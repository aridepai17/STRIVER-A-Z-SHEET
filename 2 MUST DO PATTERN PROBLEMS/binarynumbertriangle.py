# BINARY NUMBER TRIANGLE PATTERN 

def binaryNumberTriangle(n):
  num = 1
  for i in range(n):
    for j in range(1, num+1):
      print((i+j) & 1, end=" ")
    print()
    num += 1
    
# Examples

# Example
n1 = 1
print(f"Pattern for n={n1}:")
binaryNumberTriangle(n1)
# Output:
# 1

n2 = 2
print(f"Pattern for n={n2}:")
binaryNumberTriangle(n2)
# Output:
# 1
# 0 1

n3 = 3
print(f"Pattern for n={n3}:")
binaryNumberTriangle(n3)
# Output:
# 1
# 0 1
# 1 0 1

n4 = 4
print(f"Pattern for n={n4}:")
binaryNumberTriangle(n4)
# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1

n5 = 5
print(f"Pattern for n={n5}:")
binaryNumberTriangle(n5)
# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

n6 = 6
print(f"Pattern for n={n6}:")
binaryNumberTriangle(n6)
# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# 0 1 0 1 0 1

n7 = 7
print(f"Pattern for n={n7}:")
binaryNumberTriangle(n7)
# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# 0 1 0 1 0 1
# 1 0 1 0 1 0 1

n8 = 8
print(f"Pattern for n={n8}:")
binaryNumberTriangle(n8)
# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# 0 1 0 1 0 1
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1

n9 = 9
print(f"Pattern for n={n9}:")
binaryNumberTriangle(n9)
# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# 0 1 0 1 0 1
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0 1

n10 = 10
print(f"Pattern for n={n10}:")
binaryNumberTriangle(n10)
# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# 0 1 0 1 0 1
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1 0 1
