# INORDER TRAVERSAL

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    traverse(root, result)
    return result

def traverse(node, result):
    if not node:
        return
    
    traverse(node.left, result)
    result.append(node.val)
    traverse(node.right, result)


# Examples
root1 = [1, None, 2, 3]
print(inorderTraversal(root1)) # Output: [1, 3, 2]

root2 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
print(inorderTraversal(root2)) # Output: [4, 6, 7, 2, 5, 1, 3, 8, 9]

root3 = [1, 2, 3, 4, 5, 6, 7]
print(inorderTraversal(root3)) # Output: [4, 2, 5, 1, 6, 3, 7]

root4 = [1, None, 2, None, 3]
print(inorderTraversal(root4)) # Output: [1, 2, 3]

root5 = [1, 2, None, 3]
print(inorderTraversal(root5)) # Output: [3, 2, 1]

root6 = [1]
print(inorderTraversal(root6)) # Output: [1]

root7 = []
print(inorderTraversal(root7)) # Output: []

root8 = [1, 1, 2, 2, None, None, 1]
print(inorderTraversal(root8)) # Output: [2, 1, 2, 1, 1]

root9 = [-1, 2, -3, 4, None, None, -5]
print(inorderTraversal(root9)) # Output: [4, 2, -1, -3, -5]

root10 = [1, 2, 3, 4, 5, None, 6, 7, 8, None, 9, 10]
print(inorderTraversal(root10)) # Output: [7, 4, 8, 2, 5, 9, 1, 3, 6, 10]