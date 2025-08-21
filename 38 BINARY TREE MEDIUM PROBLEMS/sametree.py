# SAME TREE

'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isSameTree(p, q):
    if not p or not q:
        return p == q
    
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Examples
p1 = [1,2,3], q1 = [1,2,3]
print(isSameTree(p1, q1)) # Output: True

# Additional examples
p2 = [1,2], q2 = [1,2]
print(isSameTree(p2, q2)) # Output: True

p3 = [1,2], q3 = [1,None,2]
print(isSameTree(p3, q3)) # Output: False

p4 = [1,2,3], q4 = [1,2,4]
print(isSameTree(p4, q4)) # Output: False

p5 = [], q5 = []
print(isSameTree(p5, q5)) # Output: True

p6 = [], q6 = [1]
print(isSameTree(p6, q6)) # Output: False

p7 = [1,None,2,3], q7 = [1,None,2,3]
print(isSameTree(p7, q7)) # Output: True

p8 = [1,None,2,3], q8 = [1,None,2]
print(isSameTree(p8, q8)) # Output: False

p9 = [1,2,3,4,5], q9 = [1,2,3,4,5]
print(isSameTree(p9, q9)) # Output: True

p10 = [1,2,3], q10 = [1,3,2]
print(isSameTree(p10, q10)) # Output: False