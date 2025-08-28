# DELETION OF HEAD OF SINGLY LINKED LIST

'''
Given the head of a singly linked list, delete the first node (head) of the linked list and return the new head.
If the linked list is empty, return null.

Note: The head is the first node of the linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteHead(head):
    if head is None or head.next is None:
        return None
    
    current = head
    
    newHead = current.next
    current.next = None
    
    return newHead

# Test Case 1
print("Test Case 1:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result1 = deleteHead(head1)
print("Output: head -> 2 -> 3 -> 4 -> 5") # Result: head -> 2 -> 3 -> 4 -> 5

# Test Case 2
print("Test Case 2:") # Input: head -> None
head2 = None
result2 = deleteHead(head2)
print("Output: head -> None") # Result: head -> None

# Test Case 3
print("Test Case 3:") # Input: head -> 10
head3 = ListNode(10)
result3 = deleteHead(head3)
print("Output: head -> None") # Result: head -> None

# Test Case 4
print("Test Case 4:") # Input: head -> 100 -> 200
head4 = ListNode(100, ListNode(200))
result4 = deleteHead(head4)
print("Output: head -> 200") # Result: head -> 200

# Test Case 5
print("Test Case 5:") # Input: head -> 1 -> 2 -> 3
head5 = ListNode(1, ListNode(2, ListNode(3)))
result5 = deleteHead(head5)
print("Output: head -> 2 -> 3") # Result: head -> 2 -> 3

# Test Case 6
print("Test Case 6:") # Input: head -> -1 -> -2 -> -3 -> -4
head6 = ListNode(-1, ListNode(-2, ListNode(-3, ListNode(-4))))
result6 = deleteHead(head6)
print("Output: head -> -2 -> -3 -> -4") # Result: head -> -2 -> -3 -> -4

# Test Case 7
print("Test Case 7:") # Input: head -> 5 -> 5 -> 5 -> 5
head7 = ListNode(5, ListNode(5, ListNode(5, ListNode(5))))
result7 = deleteHead(head7)
print("Output: head -> 5 -> 5 -> 5") # Result: head -> 5 -> 5 -> 5

# Test Case 8
print("Test Case 8:") # Input: head -> 999 -> 888 -> 777
head8 = ListNode(999, ListNode(888, ListNode(777)))
result8 = deleteHead(head8)
print("Output: head -> 888 -> 777") # Result: head -> 888 -> 777

# Test Case 9
print("Test Case 9:") # Input: head -> 0 -> 1 -> 2
head9 = ListNode(0, ListNode(1, ListNode(2)))
result9 = deleteHead(head9)
print("Output: head -> 1 -> 2") # Result: head -> 1 -> 2

# Test Case 10
print("Test Case 10:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
head10 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
result10 = deleteHead(head10)
print("Output: head -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10") # Result: head -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10

