# ITERATIVE POSTORDER TRAVERSAL USING 1 STACK

'''
Given a binary tree, 
find the Postorder Traversal of it and return a list containing the 
postorder traversal of the given tree using 1 stack.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def postorderTraversalusing1Stack(root):
    if not root:
        return []
    
    result = []
    stack = []
    current = root
    lastVisited = None 
    
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            peekNode = stack[-1]
            if peekNode.right and lastVisited != peekNode.right:
                current = peekNode.right
            else:
                lastVisited = stack.pop()
                result.append(lastVisited.val)
                
    return result


# Examples
root1 = [1, None, 2, 3]
print(postorderTraversalusing1Stack(root1))  # Output: [3, 2, 1]

root2 = [42]
print(postorderTraversalusing1Stack(root2))  # Output: [42]

root3 = [1, 2, 3]
print(postorderTraversalusing1Stack(root3))  # Output: [2, 3, 1]

root4 = [1, 2, None, 3]
print(postorderTraversalusing1Stack(root4))  # Output: [3, 2, 1]

root5 = [1, None, 2, None, None, 3]
print(postorderTraversalusing1Stack(root5))  # Output: [3, 2, 1]

root6 = [1, 2, 3, 4, 5, 6, 7]
print(postorderTraversalusing1Stack(root6))  # Output: [4, 5, 2, 6, 7, 3, 1]

root7 = [1, 2, 3, None, 4, None, 5]
print(postorderTraversalusing1Stack(root7))  # Output: [4, 2, 5, 3, 1]

root8 = [1, None, 2, 3, 4]
print(postorderTraversalusing1Stack(root8))  # Output: [3, 4, 2, 1]

root9 = [10, 5, 15, 2, 7, 12]
print(postorderTraversalusing1Stack(root9))  # Output: [2, 7, 5, 12, 15, 10]

root10 = [3, 1, 4, None, 2]
print(postorderTraversalusing1Stack(root10))  # Output: [2, 1, 4, 3]