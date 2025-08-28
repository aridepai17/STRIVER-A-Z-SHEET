# DELETION OF NODE BY VALUE IN SINGLY LINKED LIST

'''
Given the head of a singly linked list and a value X,
delete the first occurrence of X in the linked list and return the head of the modified list.
If X is not present or the list is empty, return the head unchanged.

Notes:
- If X is at the head, the new head should be head.next
- Only the first occurrence of X should be deleted
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteByValue(head, X):
    if head is None:
        return None
    
    if head.val == X:
        newHead = head.next
        head.next = None
        return newHead
    
    current = head 
    
    while current.next is not None:
        if current.next.val == X:
            deleteNode = current.next
            current.next = deleteNode.next
            deleteNode.next = None          
            return head

        current = current.next
        
    return head

# Test Case 1
print("Test Case 1:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, X = 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result1 = deleteByValue(head1, 1)
print("Output: head -> 2 -> 3 -> 4 -> 5") # Result: head -> 2 -> 3 -> 4 -> 5

# Test Case 2
print("Test Case 2:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, X = 3
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result2 = deleteByValue(head2, 3)
print("Output: head -> 1 -> 2 -> 4 -> 5") # Result: head -> 1 -> 2 -> 4 -> 5

# Test Case 3
print("Test Case 3:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, X = 5
head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result3 = deleteByValue(head3, 5)
print("Output: head -> 1 -> 2 -> 3 -> 4") # Result: head -> 1 -> 2 -> 3 -> 4

# Test Case 4
print("Test Case 4:") # Input: head -> 10, X = 10
head4 = ListNode(10)
result4 = deleteByValue(head4, 10)
print("Output: head -> None") # Result: head -> None

# Test Case 5
print("Test Case 5:") # Input: head -> None, X = 1
head5 = None
result5 = deleteByValue(head5, 1)
print("Output: head -> None") # Result: head -> None

# Test Case 6
print("Test Case 6:") # Input: head -> 100 -> 200 -> 300, X = 400 (not found)
head6 = ListNode(100, ListNode(200, ListNode(300)))
result6 = deleteByValue(head6, 400)
print("Output: head -> 100 -> 200 -> 300") # Result: head -> 100 -> 200 -> 300

# Test Case 7
print("Test Case 7:") # Input: head -> -1 -> -2 -> -3 -> -4, X = -3
head7 = ListNode(-1, ListNode(-2, ListNode(-3, ListNode(-4))))
result7 = deleteByValue(head7, -3)
print("Output: head -> -1 -> -2 -> -4") # Result: head -> -1 -> -2 -> -4

# Test Case 8
print("Test Case 8:") # Input: head -> 5 -> 5 -> 5 -> 5, X = 5 (delete first only)
head8 = ListNode(5, ListNode(5, ListNode(5, ListNode(5))))
result8 = deleteByValue(head8, 5)
print("Output: head -> 5 -> 5 -> 5") # Result: head -> 5 -> 5 -> 5

# Test Case 9
print("Test Case 9:") # Input: head -> 0 -> 1 -> 0 -> 2 -> 0, X = 0 (delete first only)
head9 = ListNode(0, ListNode(1, ListNode(0, ListNode(2, ListNode(0)))))
result9 = deleteByValue(head9, 0)
print("Output: head -> 1 -> 0 -> 2 -> 0") # Result: head -> 1 -> 0 -> 2 -> 0

# Test Case 10
print("Test Case 10:") # Input: head -> 9 -> 8 -> 7 -> 6 -> 5, X = 6
head10 = ListNode(9, ListNode(8, ListNode(7, ListNode(6, ListNode(5)))))
result10 = deleteByValue(head10, 6)
print("Output: head -> 9 -> 8 -> 7 -> 5") # Result: head -> 9 -> 8 -> 7 -> 5