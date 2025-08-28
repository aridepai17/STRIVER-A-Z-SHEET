# LENGTH OF SINGLY LINKED LIST

'''
You are given the head of a singly linked list. 
Your task is to return the number of nodes in the linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getLength(head):
    count = 0
    current = head
    
    while current:
        count += 1
        current = current.next
        
    return count

# Test Case 1
print("Test Case 1:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(getLength(head1)) # Output: 5

# Test Case 2
print("Test Case 2:") # Input: head -> None
head2 = None
print(getLength(head2)) # Output: 0

# Test Case 3
print("Test Case 3:") # Input: head -> 10
head3 = ListNode(10)
print(getLength(head3)) # Output: 1

# Test Case 4
print("Test Case 4:") # Input: head -> 100 -> 200
head4 = ListNode(100, ListNode(200))
print(getLength(head4)) # Output: 2

# Test Case 5
print("Test Case 5:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
head5 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
print(getLength(head5)) # Output: 10

# Test Case 6
print("Test Case 6:") # Input: head -> -1 -> -2 -> -3 -> -4
head6 = ListNode(-1, ListNode(-2, ListNode(-3, ListNode(-4))))
print(getLength(head6)) # Output: 4

# Test Case 7
print("Test Case 7:") # Input: head -> 5 -> 5 -> 5 -> 5 -> 5
head7 = ListNode(5, ListNode(5, ListNode(5, ListNode(5, ListNode(5)))))
print(getLength(head7)) # Output: 5

# Test Case 8
print("Test Case 8:") # Input: head -> 999 -> 888 -> 777
head8 = ListNode(999, ListNode(888, ListNode(777)))
print(getLength(head8)) # Output: 3

# Test Case 9
print("Test Case 9:") # Input: head -> 0
head9 = ListNode(0)
print(getLength(head9)) # Output: 1

# Test Case 10
print("Test Case 10:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15
head10 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10, ListNode(11, ListNode(12, ListNode(13, ListNode(14, ListNode(15)))))))))))))))
print(getLength(head10)) # Output: 15