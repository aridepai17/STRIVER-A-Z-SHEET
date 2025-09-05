# DELETE NODE AT SPECIFIED POSITION IN DOUBLY LINKED LIST

'''
Given a doubly linked list, implement a function to delete a node at a specified position (0-indexed) in the list. 
The function should return the head of the updated doubly linked list.
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def deleteAtPosition(head, position):
    if head is None:
        return None
    
    if position == 0:
        newHead = head.next
        if newHead:
            newHead.prev = None
        return newHead
    
    current = head
    index = 0
    
    while current and index < position:
        current = current.next
        index += 1
    
    if current is None:
        return head
    
    current.prev.next = current.next
    if current.next:
        current.next.prev = current.prev
        
    return head

# Test Cases
head1 = [1, 2, 3, 4, 5], position1 = 1
print(deleteAtPosition(head1, position1)) # Output: [1, 3, 4, 5]

# Test Case 2: Empty list
head2 = [], position2 = 0
print(deleteAtPosition(head2, position2)) # Output: None

# Test Case 3: Single node list, deleting the only node
head3 = [10], position3 = 0
print(deleteAtPosition(head3, position3)) # Output: None

# Test Case 4: Deleting the head
head4 = [1, 2, 3], position4 = 0
print(deleteAtPosition(head4, position4)) # Output: [2, 3]

# Test Case 5: Deleting the tail
head5 = [1, 2, 3], position5 = 2
print(deleteAtPosition(head5, position5)) # Output: [1, 2]

# Test Case 6: Position out of bounds (greater than length)
head6 = [1, 2, 3], position6 = 5
print(deleteAtPosition(head6, position6)) # Output: [1, 2, 3]

# Test Case 7: List with two nodes, deleting tail
head7 = [1, 2], position7 = 1
print(deleteAtPosition(head7, position7)) # Output: [1]

# Test Case 8: List with duplicate numbers
head8 = [5, 5, 5], position8 = 1
print(deleteAtPosition(head8, position8)) # Output: [5, 5]

# Test Case 9: Longer list
head9 = [10, 20, 30, 40, 50, 60], position9 = 3
print(deleteAtPosition(head9, position9)) # Output: [10, 20, 30, 50, 60]

# Test Case 10: List with large values
head10 = [1000, 2000, 3000], position10 = 1
print(deleteAtPosition(head10, position10)) # Output: [1000, 3000]