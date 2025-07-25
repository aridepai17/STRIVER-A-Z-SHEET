# RIGHT ANGLED NUMBER PYRAMID 

def RightAngledNumberPyramid(n):
  for i in range(1, n+1):
    for j in range(1, i+1):
      print(j, end=" ")
    print()
    
# Examples
n1 = 1
print(f"Pattern for n={n1}:")
RightAngledNumberPyramid(n1)
# Output:
# 1 

n2 = 2
print(f"Pattern for n={n2}:")
RightAngledNumberPyramid(n2)
# Output:
# 1 
# 1 2 

n3 = 3
print(f"Pattern for n={n3}:")
RightAngledNumberPyramid(n3)
# Output:
# 1 
# 1 2 
# 1 2 3 

n4 = 4
print(f"Pattern for n={n4}:")
RightAngledNumberPyramid(n4)
# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 

n5 = 5
print(f"Pattern for n={n5}:")
RightAngledNumberPyramid(n5)
# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

n6 = 6
print(f"Pattern for n={n6}:")
RightAngledNumberPyramid(n6)
# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 

n7 = 7
print(f"Pattern for n={n7}:")
RightAngledNumberPyramid(n7)
# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 

n8 = 8
print(f"Pattern for n={n8}:")
RightAngledNumberPyramid(n8)
# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 

n9 = 9
print(f"Pattern for n={n9}:")
RightAngledNumberPyramid(n9)
# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 8 9 

n10 = 10
print(f"Pattern for n={n10}:")
RightAngledNumberPyramid(n10)
# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 9 10 