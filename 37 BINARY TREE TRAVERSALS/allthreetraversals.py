# ALL THREE TRAVERSALS IN ONE STACK

# Given a binary tree with root node. Return the In-order,Pre-order and Post-order traversal of the binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
        

def treeTraversals(root):
    if not root:
        return []
    
    preorderList = []
    inorderList = []
    postorderList = []
    
    stack = [(root, 1)]
    
    while stack:
        currentNode, state = stack.pop()
        
        if state == 1:
            preorderList.append(currentNode.data)
            stack.append((currentNode, 2))
            if currentNode.left:
                stack.append((currentNode.left, 1))
                
        elif state == 2:
            inorderList.append(currentNode.data)
            stack.append((currentNode, 3))
            if currentNode.right:
                stack.append((currentNode.right, 1))
                
        else:
            postorderList.append(currentNode.data)
            
    return preorderList, inorderList, postorderList

# Examples
root1 = [1, 3, 4, 5, 2, 7, 6 ]
print(treeTraversals(root1)) # Output: [ [5, 3, 2, 1, 7, 4, 6] , [1, 3, 5, 2, 4, 7, 6] , [5, 2, 3, 7, 6, 4, 1] ]

# Additional examples
root2 = [42]
print(treeTraversals(root2)) # Output: [ [42] , [42] , [42] ]

root3 = [1, 2, 3]
print(treeTraversals(root3)) # Output: [ [2, 1, 3] , [1, 2, 3] , [2, 3, 1] ]

root4 = [1, 2, None, 3]
print(treeTraversals(root4)) # Output: [ [3, 2, 1] , [1, 2, 3] , [3, 2, 1] ]

root5 = [1, None, 2, None, None, 3]
print(treeTraversals(root5)) # Output: [ [1, 3, 2] , [1, 2, 3] , [3, 2, 1] ]

root6 = [1, 2, 3, 4, 5, 6, 7]
print(treeTraversals(root6)) # Output: [ [4, 2, 5, 1, 6, 3, 7] , [1, 2, 4, 5, 3, 6, 7] , [4, 5, 2, 6, 7, 3, 1] ]

root7 = [1, 2, 3, 4, None, None, 5]
print(treeTraversals(root7)) # Output: [ [4, 2, 1, 3, 5] , [1, 2, 4, 3, 5] , [4, 2, 5, 3, 1] ]

root8 = [1, None, 2, 3, 4]
print(treeTraversals(root8)) # Output: [ [1, 3, 2, 4] , [1, 2, 3, 4] , [3, 4, 2, 1] ]

root9 = [10, 5, 15, 2, 7, 12]
print(treeTraversals(root9)) # Output: [ [2, 5, 7, 10, 12, 15] , [10, 5, 2, 7, 15, 12] , [2, 7, 5, 12, 15, 10] ]

root10 = [3, 1, 4, None, 2]
print(treeTraversals(root10)) # Output: [ [1, 2, 3, 4] , [3, 1, 2, 4] , [2, 1, 4, 3] ]