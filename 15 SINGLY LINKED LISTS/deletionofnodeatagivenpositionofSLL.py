# DELETION OF NODE AT A GIVEN POSITION OF SINGLY LINKED LIST

'''
Given the head of a singly linked list and an integer position (0-indexed),
delete the node at the given position and return the head of the modified list.
If the position is out of range or the list is empty, return the head unchanged.

Notes:
- Position 0 refers to the head of the list
- If the list has fewer nodes than the position, do nothing and return the original head
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteAtPosition(head, position):
    if head is None:
        return None
    
    if position == 0:
        newHead = head.next
        head.next = None
        return newHead
    
    current = head 
    
    for i in range(position - 1):
        if current is None or current.next is None:
            return head 
        current = current.next
        
    if current.next is not None:
        deleteNode = current.next
        current.next = deleteNode.next
        deleteNode.next = None
        
    return head
    
# Test Case 1
print("Test Case 1:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, position = 0
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result1 = deleteAtPosition(head1, 0)
print("Output: head -> 2 -> 3 -> 4 -> 5") # Result: head -> 2 -> 3 -> 4 -> 5

# Test Case 2
print("Test Case 2:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, position = 2
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result2 = deleteAtPosition(head2, 2)
print("Output: head -> 1 -> 2 -> 4 -> 5") # Result: head -> 1 -> 2 -> 4 -> 5

# Test Case 3
print("Test Case 3:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, position = 4
head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result3 = deleteAtPosition(head3, 4)
print("Output: head -> 1 -> 2 -> 3 -> 4") # Result: head -> 1 -> 2 -> 3 -> 4

# Test Case 4
print("Test Case 4:") # Input: head -> 10, position = 0
head4 = ListNode(10)
result4 = deleteAtPosition(head4, 0)
print("Output: head -> None") # Result: head -> None

# Test Case 5
print("Test Case 5:") # Input: head -> None, position = 0
head5 = None
result5 = deleteAtPosition(head5, 0)
print("Output: head -> None") # Result: head -> None

# Test Case 6
print("Test Case 6:") # Input: head -> 100 -> 200, position = 1
head6 = ListNode(100, ListNode(200))
result6 = deleteAtPosition(head6, 1)
print("Output: head -> 100") # Result: head -> 100

# Test Case 7
print("Test Case 7:") # Input: head -> -1 -> -2 -> -3 -> -4, position = 3
head7 = ListNode(-1, ListNode(-2, ListNode(-3, ListNode(-4))))
result7 = deleteAtPosition(head7, 3)
print("Output: head -> -1 -> -2 -> -3") # Result: head -> -1 -> -2 -> -3

# Test Case 8
print("Test Case 8:") # Input: head -> 5 -> 5 -> 5 -> 5, position = 2
head8 = ListNode(5, ListNode(5, ListNode(5, ListNode(5))))
result8 = deleteAtPosition(head8, 2)
print("Output: head -> 5 -> 5 -> 5") # Result: head -> 5 -> 5 -> 5

# Test Case 9
print("Test Case 9:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, position = 10 (out of range)
head9 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result9 = deleteAtPosition(head9, 10)
print("Output: head -> 1 -> 2 -> 3 -> 4 -> 5") # Result: head -> 1 -> 2 -> 3 -> 4 -> 5

# Test Case 10
print("Test Case 10:") # Input: head -> 0 -> 1 -> 2 -> 3, position = -1 (invalid)
head10 = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
result10 = deleteAtPosition(head10, -1)
print("Output: head -> 0 -> 1 -> 2 -> 3") # Result: head -> 0 -> 1 -> 2 -> 3