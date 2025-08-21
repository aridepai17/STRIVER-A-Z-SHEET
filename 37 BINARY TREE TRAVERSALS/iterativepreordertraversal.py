# ITERATIVE PREORDER TRAVERSAL

'''
Given the root of a Binary Tree, 
write a function that returns an array containing the 
preorder traversal of the tree using an iterative approach 
with a stack.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def iterativePreOrder(root):
    preorder = []
    
    if not root:
        return []
    
    stack = []
    stack.append(root)
    
    while stack:
        node = stack.pop()
        
        preorder.append(node.val)
        
        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)
            
    return preorder

# Examples
root1 = [1, None, 2, 3]
print(iterativePreOrder(root1)) # Output: [1, 2, 3]

root2 = [1]
print(iterativePreOrder(root2)) # Output: [1]

root3 = []
print(iterativePreOrder(root3)) # Output: []

root4 = [1, 2, None, 3, None, None, None, 4]
print(iterativePreOrder(root4)) # Output: [1, 2, 3, 4]

root5 = [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4]
print(iterativePreOrder(root5)) # Output: [1, 2, 3, 4]

root6 = [1, 2, 3, 4, 5, 6, 7]
print(iterativePreOrder(root6)) # Output: [1, 2, 4, 5, 3, 6, 7]

root7 = [1, 2, 3, None, 5, None, 7]
print(iterativePreOrder(root7)) # Output: [1, 2, 5, 3, 7]

root8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(iterativePreOrder(root8)) # Output: [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]

root9 = [-10, 9, 20, None, None, 15, 7]
print(iterativePreOrder(root9)) # Output: [-10, 9, 20, 15, 7]

root10 = [0, 0, 0, 1, 2, 3, 4]
print(iterativePreOrder(root10)) # Output: [0, 0, 1, 2, 0, 3, 4]

root11 = [1, 2, 3, None, None, 4, 5, None, None, None, None, 6, 7]
print(iterativePreOrder(root11)) # Output: [1, 2, 3, 4, 6, 7, 5]