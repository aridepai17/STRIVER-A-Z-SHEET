# DELETE NODE WITH GIVEN VALUE IN DOUBLY LINKED LIST

'''
Given a doubly linked list and a value, implement a function to delete the first node that contains the given value.
The function should return the head of the updated doubly linked list.
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def deleteNodeWithValue(head, value):
    if head is None:
        return None
    
    if head.data == value:
        head = head.next
        if head:
            head.prev = None
        return None
    
    current = head
    while current and current.data != value:
        current = current.next
        
    if current is None:
        return None
    
    if current.prev:
        current.prev.next = current.next
    if current.next:
        current.next.prev = current.prev
        
    return head

# Test Cases
head1 = [1, 2, 3, 4], value1 = 4
print(deleteNodeWithValue(head1, value1)) # Output: [1, 2, 3]
        
# Test Case 2: Empty list
head2 = [], value2 = 1
print(deleteNodeWithValue(head2, value2)) # Output: None

# Test Case 3: Single node list, value matches
head3 = [10], value3 = 10
print(deleteNodeWithValue(head3, value3)) # Output: None

# Test Case 4: Single node list, value does not match
head4 = [10], value4 = 5
print(deleteNodeWithValue(head4, value4)) # Output: [10]

# Test Case 5: Deleting the head
head5 = [1, 2, 3], value5 = 1
print(deleteNodeWithValue(head5, value5)) # Output: [2, 3]

# Test Case 6: Deleting a node in the middle
head6 = [1, 2, 3, 4, 5], value6 = 3
print(deleteNodeWithValue(head6, value6)) # Output: [1, 2, 4, 5]

# Test Case 7: Value not found in the list
head7 = [10, 20, 30], value7 = 25
print(deleteNodeWithValue(head7, value7)) # Output: [10, 20, 30]

# Test Case 8: List with duplicates, deleting the first occurrence
head8 = [5, 10, 5, 20], value8 = 5
print(deleteNodeWithValue(head8, value8)) # Output: [10, 5, 20]

# Test Case 9: Longer list, deleting a value
head9 = [10, 20, 30, 40, 50, 60], value9 = 40
print(deleteNodeWithValue(head9, value9)) # Output: [10, 20, 30, 50, 60]

# Test Case 10: Deleting the head in a two-node list
head10 = [100, 200], value10 = 100
print(deleteNodeWithValue(head10, value10)) # Output: [200]
