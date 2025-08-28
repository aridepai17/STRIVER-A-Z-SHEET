# REVERSE LINKED LIST IN-PLACE

'''
Given the head of a singly linked list, reverse the list in-place and return the reversed list.
Note: This should be done without using extra space (O(1) space complexity).
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseInPlace(head):
    current = head
    prev = None 
    
    while current is not None:
        front = current.next
        current.next = prev 
        prev = current
        current = front
        
    return prev

# Test Case 1
print("Test Case 1:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result1 = reverseInPlace(head1)
print("Output: head -> 5 -> 4 -> 3 -> 2 -> 1") # Result: head -> 5 -> 4 -> 3 -> 2 -> 1

# Test Case 2
print("Test Case 2:") # Input: head -> 1 -> 2
head2 = ListNode(1, ListNode(2))
result2 = reverseInPlace(head2)
print("Output: head -> 2 -> 1") # Result: head -> 2 -> 1

# Test Case 3
print("Test Case 3:") # Input: head -> None
head3 = None
result3 = reverseInPlace(head3)
print("Output: head -> None") # Result: head -> None

# Test Case 4
print("Test Case 4:") # Input: head -> 10
head4 = ListNode(10)
result4 = reverseInPlace(head4)
print("Output: head -> 10") # Result: head -> 10

# Test Case 5
print("Test Case 5:") # Input: head -> 1 -> 2 -> 3
head5 = ListNode(1, ListNode(2, ListNode(3)))
result5 = reverseInPlace(head5)
print("Output: head -> 3 -> 2 -> 1") # Result: head -> 3 -> 2 -> 1

# Test Case 6
print("Test Case 6:") # Input: head -> -1 -> -2 -> -3 -> -4
head6 = ListNode(-1, ListNode(-2, ListNode(-3, ListNode(-4))))
result6 = reverseInPlace(head6)
print("Output: head -> -4 -> -3 -> -2 -> -1") # Result: head -> -4 -> -3 -> -2 -> -1

# Test Case 7
print("Test Case 7:") # Input: head -> 5 -> 5 -> 5 -> 5
head7 = ListNode(5, ListNode(5, ListNode(5, ListNode(5))))
result7 = reverseInPlace(head7)
print("Output: head -> 5 -> 5 -> 5 -> 5") # Result: head -> 5 -> 5 -> 5 -> 5

# Test Case 8
print("Test Case 8:") # Input: head -> 100 -> 200 -> 300
head8 = ListNode(100, ListNode(200, ListNode(300)))
result8 = reverseInPlace(head8)
print("Output: head -> 300 -> 200 -> 100") # Result: head -> 300 -> 200 -> 100

# Test Case 9
print("Test Case 9:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
head9 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
result9 = reverseInPlace(head9)
print("Output: head -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1") # Result: head -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1

# Test Case 10
print("Test Case 10:") # Input: head -> 0 -> 1 -> 0 -> 1 -> 0
head10 = ListNode(0, ListNode(1, ListNode(0, ListNode(1, ListNode(0)))))
result10 = reverseInPlace(head10)
print("Output: head -> 0 -> 1 -> 0 -> 1 -> 0") # Result: head -> 0 -> 1 -> 0 -> 1 -> 0