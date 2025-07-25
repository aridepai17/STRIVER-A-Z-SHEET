# INCREASING NUMBER TRIANGLE 

def increasingNumberTriangle(n):
  num = 1
  for i in range(1, n + 1):
    for j in range(i):
      print(num, end=" ")
      num += 1
    print()
    
# Example 
n1 = 1
print(f"Pattern for n={n1}:")
increasingNumberTriangle(n1)
# Output:
# 1

n2 = 2
print(f"Pattern for n={n2}:")
increasingNumberTriangle(n2)
# Output:
# 1
# 2 3

n3 = 3
print(f"Pattern for n={n3}:")
increasingNumberTriangle(n3)
# Output:
# 1
# 2 3
# 4 5 6

n4 = 4
print(f"Pattern for n={n4}:")
increasingNumberTriangle(n4)
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

n5 = 5
print(f"Pattern for n={n5}:")
increasingNumberTriangle(n5)
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n6 = 6
print(f"Pattern for n={n6}:")
increasingNumberTriangle(n6)
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21

n7 = 7
print(f"Pattern for n={n7}:")
increasingNumberTriangle(n7)
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28

n8 = 8
print(f"Pattern for n={n8}:")
increasingNumberTriangle(n8)
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36

n9 = 9
print(f"Pattern for n={n9}:")
increasingNumberTriangle(n9)
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36
# 37 38 39 40 41 42 43 44 45

n10 = 10
print(f"Pattern for n={n10}:")
increasingNumberTriangle(n10)
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36
# 37 38 39 40 41 42 43 44 45
# 46 47 48 49 50 51 52 53 54 55 