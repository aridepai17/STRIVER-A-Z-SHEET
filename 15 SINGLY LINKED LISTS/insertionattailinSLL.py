# INSERTION AT TAIL IN SINGLY LINKED LIST

'''
Given the head of a singly linked list and a value X,
insert a new node with value X at the tail (end) of the linked list and return the head.
If the linked list is empty, the new node becomes the head.

Notes:
- Insertion at tail appends the new node after the current last node
- Return the head of the modified list
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertAtTail(head, X):
    newNode = ListNode(X)
    
    if head is None:
        return newNode
    
    current = head
    
    while current.next is not None:
        current = current.next
        
    current.next = newNode
    
    return head

# Test Case 1
print("Test Case 1:") # Input: head -> None, X = 5
head1 = None
result1 = insertAtTail(head1, 5)
print("Output: head -> 5") # Result: head -> 5

# Test Case 2
print("Test Case 2:") # Input: head -> 10, X = 20
head2 = ListNode(10)
result2 = insertAtTail(head2, 20)
print("Output: head -> 10 -> 20") # Result: head -> 10 -> 20

# Test Case 3
print("Test Case 3:") # Input: head -> 1 -> 2 -> 3, X = 4
head3 = ListNode(1, ListNode(2, ListNode(3)))
result3 = insertAtTail(head3, 4)
print("Output: head -> 1 -> 2 -> 3 -> 4") # Result: head -> 1 -> 2 -> 3 -> 4

# Test Case 4
print("Test Case 4:") # Input: head -> -1 -> -2 -> -3, X = -4
head4 = ListNode(-1, ListNode(-2, ListNode(-3)))
result4 = insertAtTail(head4, -4)
print("Output: head -> -1 -> -2 -> -3 -> -4") # Result: head -> -1 -> -2 -> -3 -> -4

# Test Case 5
print("Test Case 5:") # Input: head -> 5 -> 5 -> 5, X = 5
head5 = ListNode(5, ListNode(5, ListNode(5)))
result5 = insertAtTail(head5, 5)
print("Output: head -> 5 -> 5 -> 5 -> 5") # Result: head -> 5 -> 5 -> 5 -> 5

# Test Case 6
print("Test Case 6:") # Input: head -> 0, X = 0
head6 = ListNode(0)
result6 = insertAtTail(head6, 0)
print("Output: head -> 0 -> 0") # Result: head -> 0 -> 0

# Test Case 7
print("Test Case 7:") # Input: head -> 100 -> 200, X = 300
head7 = ListNode(100, ListNode(200))
result7 = insertAtTail(head7, 300)
print("Output: head -> 100 -> 200 -> 300") # Result: head -> 100 -> 200 -> 300

# Test Case 8
print("Test Case 8:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, X = 6
head8 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result8 = insertAtTail(head8, 6)
print("Output: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6") # Result: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

# Test Case 9
print("Test Case 9:") # Input: head -> 999 -> 888 -> 777, X = 1000
head9 = ListNode(999, ListNode(888, ListNode(777)))
result9 = insertAtTail(head9, 1000)
print("Output: head -> 999 -> 888 -> 777 -> 1000") # Result: head -> 999 -> 888 -> 777 -> 1000

# Test Case 10
print("Test Case 10:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9, X = 10
head10 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
result10 = insertAtTail(head10, 10)
print("Output: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10") # Result: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10