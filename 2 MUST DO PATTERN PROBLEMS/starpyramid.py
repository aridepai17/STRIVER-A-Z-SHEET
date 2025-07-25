# STAR PYRAMID 

def starPyramid(n):
  for i in range(1, n+1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
    
# Examples 
n1 = 1
print(f"Pattern for n={n1}:")
starPyramid(n1)
# Output:
# *

n2 = 2
print(f"Pattern for n={n2}:")
starPyramid(n2)
# Output:
#  *
# ***

n3 = 3
print(f"Pattern for n={n3}:")
starPyramid(n3)
# Output:
#   *
#  ***
# *****

n4 = 4
print(f"Pattern for n={n4}:")
starPyramid(n4)
# Output:
#    *
#   ***
#  *****
# *******

n5 = 5
print(f"Pattern for n={n5}:")
starPyramid(n5)
# Output:
#     *
#    ***
#   *****
#  *******
# *********

n6 = 6
print(f"Pattern for n={n6}:")
starPyramid(n6)
# Output:
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

n7 = 7
print(f"Pattern for n={n7}:")
starPyramid(n7)
# Output:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************

n8 = 8
print(f"Pattern for n={n8}:")
starPyramid(n8)
# Output:
#        *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************

n9 = 9
print(f"Pattern for n={n9}:")
starPyramid(n9)
# Output:
#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************

n10 = 10
print(f"Pattern for n={n10}:")
starPyramid(n10)
# Output:
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# ******************* 