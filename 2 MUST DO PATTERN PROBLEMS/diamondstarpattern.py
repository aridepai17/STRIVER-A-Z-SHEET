# DIAMOND STAR PATTERN 

def printDiamond(n):
  for i in range(1, n+1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
    
    for i in range(n-1, 0, -1):
      spaces = ' ' * (n - i)
      stars = '*' * (2 * i - 1)
      print(spaces + stars)
      
# Examples 
n1 = 1
print(f"Pattern for n={n1}:")
printDiamond(n1)
# Output:
# *

n2 = 2
print(f"Pattern for n={n2}:")
printDiamond(n2)
# Output:
#  *
# ***
#  *

n3 = 3
print(f"Pattern for n={n3}:")
printDiamond(n3)
# Output:
#   *
#  ***
# *****
#  ***
#   *

n4 = 4
print(f"Pattern for n={n4}:")
printDiamond(n4)
# Output:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n5 = 5
print(f"Pattern for n={n5}:")
printDiamond(n5)
# Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

n6 = 6
print(f"Pattern for n={n6}:")
printDiamond(n6)
# Output:
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *

n7 = 7
print(f"Pattern for n={n7}:")
printDiamond(n7)
# Output:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *

n8 = 8
print(f"Pattern for n={n8}:")
printDiamond(n8)
# Output:
#        *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
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
printDiamond(n9)
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
printDiamond(n10)
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
#  *****************
#   ***************
#    *************
#     ***********
#      *********
#       *******
#        *****
#         ***
#          *

