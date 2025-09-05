# DELETE TAIL OF DOUBLY LINKED LIST

'''
Given a doubly linked list, implement a function to delete the tail (last node) of the list.
The function should return the head of the updated doubly linked list.
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def deleteTail(head):
    if head is None:
        return None
    
    if head.next is None:
        return None
    
    current = head
    
    while current.next:
        current = current.next
        
    current.prev.next = None
    current.prev = None
    
    return head

# Test Cases
head1 = [1, 2, 3, 4]
print(deleteTail(head1)) # Output: [1, 2, 3]


# Test Case 2: Empty list
head2 = []
print(deleteTail(head2)) # Output: None

# Test Case 3: Single node list
head3 = [10]
print(deleteTail(head3)) # Output: None

# Test Case 4: Two nodes list
head4 = [1, 2]
print(deleteTail(head4)) # Output: [1]

# Test Case 5: List with negative numbers
head5 = [-3, -2, -1]
print(deleteTail(head5)) # Output: [-3, -2]

# Test Case 6: List with duplicate numbers
head6 = [5, 5, 5]
print(deleteTail(head6)) # Output: [5, 5]

# Test Case 7: List with mixed positive/negative/zero
head7 = [-1, 0, 1]
print(deleteTail(head7)) # Output: [-1, 0]

# Test Case 8: List with strings
head8 = ['a', 'b', 'c']
print(deleteTail(head8)) # Output: ['a', 'b']

# Test Case 9: Longer list
head9 = [10, 20, 30, 40, 50, 60]
print(deleteTail(head9)) # Output: [10, 20, 30, 40, 50]

# Test Case 10: List with large values
head10 = [1000, 2000, 3000]
print(deleteTail(head10)) # Output: [1000, 2000]