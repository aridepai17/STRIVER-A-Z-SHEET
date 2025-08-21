# LEVEL ORDER TRAVERSAL

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def levelOrder(root):
    result = []
    
    queue = collections.deque()
    queue.append(root)
    
    while queue:
        queueLength = len(queue)
        level = []
        
        for i in range(queueLength):
            node = queue.popleft()
            
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
                
        if level:
            result.append(level)
            
    return result

# Examples
root1 = [3, 9, 20, None, None, 15, 7]
print(levelOrder(root1)) # Output: [[3], [9, 20], [15, 7]]

root2 = [1]
print(levelOrder(root2)) # Output: [[1]]

root3 = []
print(levelOrder(root3)) # Output: []

root4 = [1, 2, None, 3, None, None, None, 4]
print(levelOrder(root4)) # Output: [[1], [2], [3], [4]]

root5 = [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4]
print(levelOrder(root5)) # Output: [[1], [2], [3], [4]]

root6 = [1, 2, 3, 4, 5, 6, 7]
print(levelOrder(root6)) # Output: [[1], [2, 3], [4, 5, 6, 7]]

root7 = [1, 2, 3, None, 5, None, 7]
print(levelOrder(root7)) # Output: [[1], [2, 3], [5, 7]]

root8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(levelOrder(root8)) # Output: [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]]

root9 = [-10, 9, 20, None, None, 15, 7]
print(levelOrder(root9)) # Output: [[-10], [9, 20], [15, 7]]

root10 = [0, 0, 0, 1, 2, 3, 4]
print(levelOrder(root10)) # Output: [[0], [0, 0], [1, 2, 3, 4]]