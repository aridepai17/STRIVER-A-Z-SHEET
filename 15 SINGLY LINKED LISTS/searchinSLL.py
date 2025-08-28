# SEARCH IN SINGLY LINKED LIST 

'''
You are given the head of a singly linked list and an integer key.
Return true if the key exists in the linked list, otherwise return false.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def searchKey(head, key):
    current = head 
    
    while current:
        if current.val == key:
            return True
        current = current.next 
        
    return False

# Test Case 1
print("Test Case 1:") # Input: head -> 1 -> 2 -> 3 -> 4, key = 3
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(searchKey(head1, 3)) # Output: True

# Test Case 2
print("Test Case 2:") # Input: head -> 1 -> 2 -> 3 -> 4, key = 5
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(searchKey(head2, 5)) # Output: False

# Test Case 3
print("Test Case 3:") # Input: head -> None, key = 10
head3 = None
print(searchKey(head3, 10)) # Output: False

# Test Case 4
print("Test Case 4:") # Input: head -> 10, key = 10
head4 = ListNode(10)
print(searchKey(head4, 10)) # Output: True

# Test Case 5
print("Test Case 5:") # Input: head -> 10, key = 20
head5 = ListNode(10)
print(searchKey(head5, 20)) # Output: False

# Test Case 6
print("Test Case 6:") # Input: head -> 5 -> 5 -> 5 -> 5, key = 5
head6 = ListNode(5, ListNode(5, ListNode(5, ListNode(5))))
print(searchKey(head6, 5)) # Output: True

# Test Case 7
print("Test Case 7:") # Input: head -> -1 -> -2 -> -3 -> -4, key = -3
head7 = ListNode(-1, ListNode(-2, ListNode(-3, ListNode(-4))))
print(searchKey(head7, -3)) # Output: True

# Test Case 8
print("Test Case 8:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, key = 1
head8 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(searchKey(head8, 1)) # Output: True

# Test Case 9
print("Test Case 9:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, key = 5
head9 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(searchKey(head9, 5)) # Output: True

# Test Case 10
print("Test Case 10:") # Input: head -> 999 -> 888 -> 777, key = 666
head10 = ListNode(999, ListNode(888, ListNode(777)))
print(searchKey(head10, 666)) # Output: False