# ITERATIVE POST ORDER TRAVERSAL

'''
Given a binary tree, 
find the Postorder Traversal of it and return a list containing the 
postorder traversal of the given tree using 2 stacks.
'''

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def iterativePostOrderTraversal(root):
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    result = []
    
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
            
    while stack2:
        node = stack2.pop()
        result.append(node.val)
        
    return result
    
# Examples
root1 = [19, 10, 8, 11, 13] 
print(iterativePostOrderTraversal(root1)) # Output: [11, 13, 10, 8, 19]

root2 = [1]
print(iterativePostOrderTraversal(root2)) # Output: [1]

root3 = []
print(iterativePostOrderTraversal(root3)) # Output: []

root4 = [1, 2, None, 3, None, None, None, 4]
print(iterativePostOrderTraversal(root4)) # Output: [4, 3, 2, 1]

root5 = [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4]
print(iterativePostOrderTraversal(root5)) # Output: [4, 3, 2, 1]

root6 = [1, 2, 3, 4, 5, 6, 7]
print(iterativePostOrderTraversal(root6)) # Output: [4, 5, 2, 6, 7, 3, 1]

root7 = [1, 2, 3, None, 5, None, 7]
print(iterativePostOrderTraversal(root7)) # Output: [5, 2, 7, 3, 1]

root8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(iterativePostOrderTraversal(root8)) # Output: [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]

root9 = [-10, 9, 20, None, None, 15, 7]
print(iterativePostOrderTraversal(root9)) # Output: [9, 15, 7, 20, -10]

root10 = [0, 0, 0, 1, 2, 3, 4]
print(iterativePostOrderTraversal(root10)) # Output: [1, 2, 0, 3, 4, 0, 0]

root11 = [1, 2, 3, None, None, 4, 5, None, None, None, None, 6, 7]
print(iterativePostOrderTraversal(root11)) # Output: [2, 6, 7, 4, 5, 3, 1]

