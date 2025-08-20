# PREORDER TRAVERSAL

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def preorderTraversal(root):
    result = []
    traverse(root, result)
    return result

def traverse(node, result):
    if not node:
        return
    
    result.append(node.val)
    traverse(node.left, result)
    traverse(node.right, result)
        
# Examples
root1 = [1, None, 2, 3]
print(preorderTraversal(root1)) # Output: [1, 2, 3]

root2 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
print(preorderTraversal(root2)) # Output: [1, 2, 4, 6, 7, 5, 3, 8, 9]

root3 = [1, 2, 3, 4, 5, 6, 7]
print(preorderTraversal(root3)) # Output: [1, 2, 4, 5, 3, 6, 7]

root4 = [1, None, 2, None, 3]
print(preorderTraversal(root4)) # Output: [1, 2, 3]

root5 = [1, 2, None, 3]
print(preorderTraversal(root5)) # Output: [1, 2, 3]

root6 = [1]
print(preorderTraversal(root6)) # Output: [1]

root7 = []
print(preorderTraversal(root7)) # Output: []

root8 = [1, 1, 2, 2, None, None, 1]
print(preorderTraversal(root8)) # Output: [1, 1, 2, 2, 1]

root9 = [-1, 2, -3, 4, None, None, -5]
print(preorderTraversal(root9)) # Output: [-1, 2, 4, -3, -5]

root10 = [1, 2, 3, 4, 5, None, 6, 7, 8, None, 9, 10]
print(preorderTraversal(root10)) # Output: [1, 2, 4, 7, 8, 5, 9, 3, 6, 10]