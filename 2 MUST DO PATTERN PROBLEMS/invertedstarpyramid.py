# INVERTED STAR PYRAMID 

def invertedStarPyramid(n):
  for i in range(n, 0, -1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

# Examples
n1 = 1
print(f"Pattern for n={n1}:")
invertedStarPyramid(n1)
# Output:
# *

n2 = 2
print(f"Pattern for n={n2}:")
invertedStarPyramid(n2)
# Output:
# ***
#  *

n3 = 3
print(f"Pattern for n={n3}:")
invertedStarPyramid(n3)
# Output:
# *****
#  ***
#   *

n4 = 4
print(f"Pattern for n={n4}:")
invertedStarPyramid(n4)
# Output:
# *******
#  *****
#   ***
#    *

n5 = 5
print(f"Pattern for n={n5}:")
invertedStarPyramid(n5)
# Output:
# *********
#  *******
#   *****
#    ***
#     *

n6 = 6
print(f"Pattern for n={n6}:")
invertedStarPyramid(n6)
# Output:
# ***********
#  *********
#   *******
#    *****
#     ***
#      *

n7 = 7
print(f"Pattern for n={n7}:")
invertedStarPyramid(n7)
# Output:
# *************
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *

n8 = 8
print(f"Pattern for n={n8}:")
invertedStarPyramid(n8)
# Output:
# ***************
#  *************
#   ***********
#    *********
#     *******
#      *****
#       ***
#        *

n9 = 9
print(f"Pattern for n={n9}:")
invertedStarPyramid(n9)
# Output:
# *****************
#  ***************
#   *************
#    ***********
#     *********
#      *******
#       *****
#        ***
#         *

n10 = 10
print(f"Pattern for n={n10}:")
invertedStarPyramid(n10)
# Output:
# *******************
#  *****************
#   ***************
#    *************
#     ***********
#      *********
#       *******
#        *****
#         ***
#          *
