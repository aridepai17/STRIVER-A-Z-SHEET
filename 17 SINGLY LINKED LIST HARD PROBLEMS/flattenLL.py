# FLATTEN LINKED LIST

'''
Given a linked list containing n head nodes where every node in the linked list contains two pointers:
(i) next points to the next node in the list.
(ii) bottom points to a sub-linked list where the current node is the head.
Each of the sub-linked lists nodes and the head nodes are sorted in ascending order based on their data. 
Flatten the linked list such that all the nodes appear in a single level while maintaining the sorted order.
'''

class ListNode:
    def __init__(self, data=0, next=None, bottom=None):
        self.data = data
        self.next = next
        self.bottom = bottom

# Solution 1: Brute Force Solution
def flatten(head):
    arr = []
    current = head
    
    while current:
        t2 = current
        while t2:
            arr.append(t2.data)
            t2 = t2.bottom
        current = current.next
        
    arr.sort()
    
    head = convert(arr)
    
    return head

def convert(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        newNode = ListNode(arr[i])
        current.bottom = newNode
        current = current.bottom
        
    return head

# Time Complexity: O(N log N), where N is the total number of nodes in all lists (collecting all nodes and sorting them)
# Space Complexity: O(N), for storing all node values in the array and for the new flattened list

# Solution 2: Using DummyNode and Recursion
def flatten(head):
    if head is None or head.next is None:
        return head
    
    mergeHead = flatten(head.next)
    
    return merge(head, mergeHead)

def merge(list1, list2):
    dummyNode = ListNode(-1)
    result = dummyNode
    
    while list1 and list2:
        if list1.data < list2.data:
            result.bottom = list1
            result = list1
            list1 = list1.bottom
        else:
            result.bottom = list2
            result = list2
            list2 = list2.bottom
        result.next = None
        
    if list1:
        result.bottom = list1
    if list2:
        result.bottom = list2
        
    return dummyNode.bottom

# Time Complexity: O(N log k), where N is the total number of nodes and k is the number of head nodes (lists).
#   - Each merge operation takes O(N) time, and we merge k lists recursively (like merge k sorted lists).
# Space Complexity: O(1) auxiliary (ignoring recursion stack), but O(k) due to recursion stack depth.

# Test Cases
# Each test case is represented as a list of lists, where each sublist is a bottom chain for a head node.
# Output is the flattened list in sorted order.

# Test Case 1
# Input: [[5, 7, 8, 30], [10, 20], [19, 22, 50], [28, 35, 40, 45]]
# Output: [5, 7, 8, 10, 19, 20, 22, 28, 30, 35, 40, 45, 50]

# Test Case 2
# Input: [[1, 3, 5], [2, 4, 6]]
# Output: [1, 2, 3, 4, 5, 6]

# Test Case 3
# Input: [[1], [2], [3], [4]]
# Output: [1, 2, 3, 4]

# Test Case 4
# Input: [[1, 2, 3, 4]]
# Output: [1, 2, 3, 4]

# Test Case 5
# Input: [[10, 20, 30], [5, 15, 25], [1, 2, 3]]
# Output: [1, 2, 3, 5, 10, 15, 20, 25, 30]

# Test Case 6
# Input: [[1], [], [2, 3], [4, 5, 6]]
# Output: [1, 2, 3, 4, 5, 6]

# Test Case 7
# Input: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Test Case 8
# Input: [[1], [1], [1]]
# Output: [1, 1, 1]

# Test Case 9
# Input: [[]]
# Output: []

# Test Case 10
# Input: [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]