# DELETE HEAD OF DOUBLY LINKED LIST

"""
Given a doubly linked list, implement a function to delete the head (first node) of the list.
The function should return the head of the updated doubly linked list.
"""

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def deleteHead(head):
    if head is None:
        return None
    
    if head.next is None:
        return None
    
    newHead = head.next
    newHead.prev = None
    head.next = None 
    
    return newHead

# Test Cases
head1 = [1, 2, 3, 4]
print(deleteHead(head1)) # Output: [2, 3, 4]

# Test Case 2: Empty list
head2 = []
print(deleteHead(head2)) # Output: None

# Test Case 3: Single node list
head3 = [10]
print(deleteHead(head3)) # Output: None

# Test Case 4: Two nodes list
head4 = [1, 2]
print(deleteHead(head4)) # Output: [2]

# Test Case 5: List with negative numbers
head5 = [-3, -2, -1]
print(deleteHead(head5)) # Output: [-2, -1]

# Test Case 6: List with duplicate numbers
head6 = [5, 5, 5]
print(deleteHead(head6)) # Output: [5, 5]

# Test Case 7: List with mixed positive/negative/zero
head7 = [-1, 0, 1]
print(deleteHead(head7)) # Output: [0, 1]

# Test Case 8: List with strings
head8 = ['a', 'b', 'c']
print(deleteHead(head8)) # Output: ['b', 'c']

# Test Case 9: Longer list
head9 = [10, 20, 30, 40, 50, 60]
print(deleteHead(head9)) # Output: [20, 30, 40, 50, 60]

# Test Case 10: List with large values
head10 = [1000, 2000, 3000]
print(deleteHead(head10)) # Output: [2000, 3000]