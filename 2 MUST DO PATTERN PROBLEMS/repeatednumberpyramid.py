# REPEATED NUMBER PYRAMID  

def RepeatedNumberPyramid(n):
  print(1)
  for i in range(2, n+1):
      print(str(i) * i)

# Examples
n1 = 1
print(f"Pattern for n={n1}:")
RepeatedNumberPyramid(n1)
# Output:
# 1 

n2 = 2
print(f"Pattern for n={n2}:")
RepeatedNumberPyramid(n2)
# Output:
# 1
# 22 

n3 = 3
print(f"Pattern for n={n3}:")
RepeatedNumberPyramid(n3)
# Output:
# 1
# 22
# 333 

n4 = 4
print(f"Pattern for n={n4}:")
RepeatedNumberPyramid(n4)
# Output:
# 1
# 22
# 333
# 4444 

n5 = 5
print(f"Pattern for n={n5}:")
RepeatedNumberPyramid(n5)
# Output:
# 1
# 22
# 333
# 4444
# 55555 

n6 = 6
print(f"Pattern for n={n6}:")
RepeatedNumberPyramid(n6)
# Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666 

n7 = 7
print(f"Pattern for n={n7}:")
RepeatedNumberPyramid(n7)
# Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777 

n8 = 8
print(f"Pattern for n={n8}:")
RepeatedNumberPyramid(n8)
# Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888 

n9 = 9
print(f"Pattern for n={n9}:")
RepeatedNumberPyramid(n9)
# Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999 

n10 = 10
print(f"Pattern for n={n10}:")
RepeatedNumberPyramid(n10)
# Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# 10101010101010101010 