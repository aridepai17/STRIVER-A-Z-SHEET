# FIND ALL PAIRS WITH GIVEN SUM IN DOUBLY LINKED LIST

'''
Given a sorted doubly linked list of distinct elements, the task is to find all pairs of nodes whose sum is equal to a given value 'target'.
The function should return a list of tuples, where each tuple contains a pair of values that sum up to the target.
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
# Solution 1: Using Brute Force Approach
def findPairsWithSum(head, target):
    current1 = head
    pairs = []
    
    while current1:
        current2 = current1.next
        while current2 and current1.data + current2.data <= target:
            if current1.data + current2.data == target:
                pairs.append([current1.data, current2.data])
            current2 = current2.next
        current1 = current1.next
        
    return pairs

# Time Complexity: O(n^2), where n is the number of nodes in the doubly linked list.
# The nested loops result in a quadratic time complexity as each node is compared with every other node that comes after it.

# Space Complexity: O(1) auxiliary space.
# The space used by the 'pairs' list is not considered auxiliary space as it is part of the output.

# Solution 2: Using Two-Pointer Approach
def findPairsWithSum2(head, target):
    left = head
    right = findTail(head)
    pairs = []
    
    while left.data < right.data:
        if left.data + right.data == target:
            pairs.append([left.data, right.data])
            left = left.next
            right = right.prev
        elif left.data + right.data < target:
            left = left.next
        else:
            right = right.prev
            
    return pairs

def findTail(head):
    current = head
    while current.next:
        current = current.next
        
    return current

# Time Complexity: O(n), where n is the number of nodes in the doubly linked list.
# The list is traversed once to find the tail and then the two pointers traverse the list once.

# Space Complexity: O(1) auxiliary space.
# The space used by the 'pairs' list is not considered auxiliary space as it is part of the output.

# Test Cases
head1 = [1, 2, 3, 4, 5, 6, 7, 8], target1 = 5
print(findPairsWithSum(head1, target1)) # Output: [[1, 4], [2, 3]]

# Test Case 2: No pairs found
head2 = [1, 2, 3, 9], target2 = 7
print(findPairsWithSum(head2, target2)) # Output: []

# Test Case 3: Empty list
head3 = [], target3 = 10
print(findPairsWithSum(head3, target3)) # Output: []

# Test Case 4: Single node list
head4 = [5], target4 = 10
print(findPairsWithSum(head4, target4)) # Output: []

# Test Case 5: Multiple pairs
head5 = [1, 2, 3, 4, 5, 6], target5 = 7
print(findPairsWithSum(head5, target5)) # Output: [[1, 6], [2, 5], [3, 4]]

# Test Case 6: Target is sum of first and last elements
head6 = [2, 5, 8, 11, 15], target6 = 17
print(findPairsWithSum(head6, target6)) # Output: [[2, 15]]

# Test Case 7: List with negative numbers
head7 = [-5, -2, 0, 3, 4, 6], target7 = 1
print(findPairsWithSum(head7, target7)) # Output: [[-5, 6], [-2, 3]]

# Test Case 8: Target is zero
head8 = [-3, -1, 1, 2, 3], target8 = 0
print(findPairsWithSum(head8, target8)) # Output: [[-3, 3], [-1, 1]]

# Test Case 9: Target smaller than any possible sum
head9 = [10, 20, 30, 40], target9 = 25
print(findPairsWithSum(head9, target9)) # Output: []

# Test Case 10: Target larger than any possible sum
head10 = [1, 2, 3, 4], target10 = 10
print(findPairsWithSum(head10, target10)) # Output: []

# Test Case 11: Two node list, pair found
head11 = [3, 7], target11 = 10
print(findPairsWithSum(head11, target11)) # Output: [[3, 7]]
