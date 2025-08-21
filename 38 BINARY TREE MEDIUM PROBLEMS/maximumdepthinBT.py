# MAXIMUM DEPTH OF BINARY TREE

'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def maxDepth(root):
    if not root:
        return 0
    
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)
    
    return max(leftDepth, rightDepth) + 1

# Examples
root1 = [3, 9, 20, None, None, 15, 7]
print(maxDepth(root1)) # Output: 3

# Additional examples
root2 = [1, None, 2]
print(maxDepth(root2)) # Output: 2

root3 = []
print(maxDepth(root3)) # Output: 0

root4 = [1]
print(maxDepth(root4)) # Output: 1

root5 = [1, 2, 3, 4, 5]
print(maxDepth(root5)) # Output: 3

root6 = [1, 2, None, 3, 4, None, None, 5]
print(maxDepth(root6)) # Output: 4

root7 = [1, None, 2, None, None, None, 3]
print(maxDepth(root7)) # Output: 3

root8 = [1, 2, 3, None, None, 4, 5, None, None, None, None, 6]
print(maxDepth(root8)) # Output: 4

root9 = [10, 5, 15, 2, 7, 12, 18, 1, 3, 6, 8, 11, 13, 16, 19]
print(maxDepth(root9)) # Output: 4

root10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(maxDepth(root10)) # Output: 4