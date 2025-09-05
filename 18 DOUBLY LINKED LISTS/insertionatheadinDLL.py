'''
Given a doubly linked list, implement a function to insert a new node with a given value at the head (beginning) of the list. 
The function should return the new head of the doubly linked list.
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insertAtHead(head, data):
    newHead = ListNode(data)
    if head:
        head.prev = newHead
    return newHead

# Test Case 1: Insert into empty list
head1 = [None]
head1 = insertAtHead(head1, 10)
print(insertAtHead(head1))  # Expected: [10]

# Test Case 2: Insert at head when list has one node
head2 = [20]
head2 = insertAtHead(head2, 15)
print(insertAtHead(head2))  # Expected: [15, 20]

# Test Case 3: Insert at head when list has multiple nodes
head3 = [30, 40, 50]
head3 = insertAtHead(head3, 25)
print(insertAtHead(head3))  # Expected: [25, 30, 40, 50]

# Test Case 4: Insert negative value at head
head4 = [5, 10]
head4 = insertAtHead(head4, -1)
print(insertAtHead(head4))  # Expected: [-1, 5, 10]

# Test Case 5: Insert at head repeatedly
head5 = None
head5 = insertAtHead(head5, 3)
head5 = insertAtHead(head5, 2)
head5 = insertAtHead(head5, 1)
# Expected: [1, 2, 3]

# Test Case 6: Insert at head with all negative values
head6 = None
head6 = insertAtHead(head6, -4)
head6 = insertAtHead(head6, -3)
head6 = insertAtHead(head6, -2)
head6 = insertAtHead(head6, -1)
# Expected: [-1, -2, -3, -4]

# Test Case 7: Insert at head with duplicate values
head7 = None
head7 = insertAtHead(head7, 5)
head7 = insertAtHead(head7, 5)
head7 = insertAtHead(head7, 5)
head7 = insertAtHead(head7, 5)
# Expected: [5, 5, 5, 5]

# Test Case 8: Insert at head with a large value
head8 = None
head8 = insertAtHead(head8, 3)
head8 = insertAtHead(head8, 2)
head8 = insertAtHead(head8, 1)
head8 = insertAtHead(head8, 99999)
# Expected: [99999, 1, 2, 3]

# Test Case 9: Insert at head with a string value (if allowed)
head9 = None
head9 = insertAtHead(head9, 'c')
head9 = insertAtHead(head9, 'b')
head9 = insertAtHead(head9, 'a')
# Expected: ['a', 'b', 'c']

# Test Case 10: Insert at head with a long list
head10 = None
for val in range(20, 0, -1):
    head10 = insertAtHead(head10, val)
# Expected: [1, 2, ..., 20]