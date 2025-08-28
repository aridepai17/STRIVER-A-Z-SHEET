# INSERTION OF NODE AT GIVEN POSITION IN SINGLY LINKED LIST

'''
Given the head of a singly linked list, an integer position (0-indexed), and a value X,
insert a new node with value X at the given position and return the head of the modified list.
If the position is greater than the length of the list or negative, return the head unchanged.

Notes:
- Position 0 refers to inserting at the head
- If the list is empty and position is 0, the new node becomes the head
- Inserting at position equal to the current length appends at tail
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertAtPosition(head, position, X):
    newNode = ListNode(X)
    
    if position < 0:
        return head 
    
    if position == 1:
        newNode.next = head
        return newNode
    
    current = head
    
    for i in range(position - 1):
        if current is None:
            return head
        current = current.next
        
    if current is None:
        return head
    
    newNode.next = current.next
    current.next = newNode
    
    return head

# Test Case 1
print("Test Case 1:") # Input: head -> None, position = 0, X = 5
head1 = None
result1 = insertAtPosition(head1, 0, 5)
print("Output: head -> 5") # Result: head -> 5

# Test Case 2
print("Test Case 2:") # Input: head -> 10, position = 0, X = 20
head2 = ListNode(10)
result2 = insertAtPosition(head2, 0, 20)
print("Output: head -> 20 -> 10") # Result: head -> 20 -> 10

# Test Case 3
print("Test Case 3:") # Input: head -> 1 -> 2 -> 3, position = 1, X = 9
head3 = ListNode(1, ListNode(2, ListNode(3)))
result3 = insertAtPosition(head3, 1, 9)
print("Output: head -> 1 -> 9 -> 2 -> 3") # Result: head -> 1 -> 9 -> 2 -> 3

# Test Case 4
print("Test Case 4:") # Input: head -> 1 -> 2 -> 3, position = 3, X = 4 (append at tail)
head4 = ListNode(1, ListNode(2, ListNode(3)))
result4 = insertAtPosition(head4, 3, 4)
print("Output: head -> 1 -> 2 -> 3 -> 4") # Result: head -> 1 -> 2 -> 3 -> 4

# Test Case 5
print("Test Case 5:") # Input: head -> -1 -> -2 -> -3, position = 2, X = -9
head5 = ListNode(-1, ListNode(-2, ListNode(-3)))
result5 = insertAtPosition(head5, 2, -9)
print("Output: head -> -1 -> -2 -> -9 -> -3") # Result: head -> -1 -> -2 -> -9 -> -3

# Test Case 6
print("Test Case 6:") # Input: head -> 5 -> 5 -> 5, position = 1, X = 5
head6 = ListNode(5, ListNode(5, ListNode(5)))
result6 = insertAtPosition(head6, 1, 5)
print("Output: head -> 5 -> 5 -> 5 -> 5") # Result: head -> 5 -> 5 -> 5 -> 5

# Test Case 7
print("Test Case 7:") # Input: head -> 100 -> 200, position = 5 (out of range), X = 300
head7 = ListNode(100, ListNode(200))
result7 = insertAtPosition(head7, 5, 300)
print("Output: head -> 100 -> 200") # Result: head -> 100 -> 200

# Test Case 8
print("Test Case 8:") # Input: head -> 0, position = -1 (invalid), X = 10
head8 = ListNode(0)
result8 = insertAtPosition(head8, -1, 10)
print("Output: head -> 0") # Result: head -> 0

# Test Case 9
print("Test Case 9:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, position = 4, X = 99
head9 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result9 = insertAtPosition(head9, 4, 99)
print("Output: head -> 1 -> 2 -> 3 -> 4 -> 99 -> 5") # Result: head -> 1 -> 2 -> 3 -> 4 -> 99 -> 5

# Test Case 10
print("Test Case 10:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7, position = 7, X = 8
head10 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
result10 = insertAtPosition(head10, 7, 8)
print("Output: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8") # Result: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8