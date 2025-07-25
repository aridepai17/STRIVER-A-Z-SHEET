# INVERTED NUMBERED RIGHT PYRAMID 

def invertedNumberedRightPyramid(n):
  for i in range(n, 0, -1):
    for j in range(1, i+1):
      print(j, end=" ")
    print()
    
# Example 
n1 = 1
print(f"Pattern for n={n1}:")
invertedNumberedRightPyramid(n1)
# Output:
# 1 

n2 = 2
print(f"Pattern for n={n2}:")
invertedNumberedRightPyramid(n2)
# Output:
# 1 2 
# 1

n3 = 3
print(f"Pattern for n={n3}:")
invertedNumberedRightPyramid(n3)
# Output:
# 1 2 3 
# 1 2 
# 1

n4 = 4
print(f"Pattern for n={n4}:")
invertedNumberedRightPyramid(n4)
# Output:
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1

n5 = 5
print(f"Pattern for n={n5}:")
invertedNumberedRightPyramid(n5)
# Output:
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1

n6 = 6
print(f"Pattern for n={n6}:")
invertedNumberedRightPyramid(n6)
# Output:
# 1 2 3 4 5 6 
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 
# 1 

n7 = 7
print(f"Pattern for n={n7}:")
invertedNumberedRightPyramid(n7)
# Output:
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 
# 1 2 3 4 5 
# 1 2 3 
# 1 2 
# 1 

n8 = 8
print(f"Pattern for n={n8}:")
invertedNumberedRightPyramid(n8)
# Output:
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 
# 1 2 3 4 
# 1 2 
# 1 

n9 = 9
print(f"Pattern for n={n9}:")
invertedNumberedRightPyramid(n9)
# Output:
# 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 
# 1 2 
# 1 

n10 = 10
print(f"Pattern for n={n10}:")
invertedNumberedRightPyramid(n10)
# Output:
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 
# 1 2 3 4 
# 1 2 
# 1 