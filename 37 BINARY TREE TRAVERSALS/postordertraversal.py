# POSTORDER TRAVERSAL

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    result = []
    traverse(root, result)
    return result

def traverse(node, result):
    if not node:
        return
    
    traverse(node.left, result)
    traverse(node.right, result)
    result.append(node.val)
        
# Examples
root1 = [1, None, 2, 3]
print(postorderTraversal(root1)) # Output: [3, 2, 1]

root2 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
print(postorderTraversal(root2)) # Output: [6, 7, 4, 5, 2, 9, 8, 3, 1]

root3 = [1, 2, 3, 4, 5, 6, 7]
print(postorderTraversal(root3)) # Output: [4, 5, 2, 6, 7, 3, 1]

root4 = [1, None, 2, None, 3]
print(postorderTraversal(root4)) # Output: [3, 2, 1]

root5 = [1, 2, None, 3]
print(postorderTraversal(root5)) # Output: [3, 2, 1]

root6 = [1]
print(postorderTraversal(root6)) # Output: [1]

root7 = []
print(postorderTraversal(root7)) # Output: []

root8 = [1, 1, 2, 2, None, None, 1]
print(postorderTraversal(root8)) # Output: [2, 1, 2, 1, 1]

root9 = [-1, 2, -3, 4, None, None, -5]
print(postorderTraversal(root9)) # Output: [4, 2, -5, -3, -1]

root10 = [1, 2, 3, 4, 5, None, 6, 7, 8, None, 9, 10]
print(postorderTraversal(root10)) # Output: [7, 8, 4, 9, 5, 2, 10, 6, 3, 1]