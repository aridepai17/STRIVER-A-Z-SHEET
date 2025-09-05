'''
Given a doubly linked list, implement a function to insert a new node with a given value at a specified position (0-indexed) in the list. 
If the position is 0, insert at the head. If the position is equal to the length of the list, insert at the tail. 
The function should return the head of the updated doubly linked list.
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insertAtPosition(head, data, position):
    newNode = ListNode(data)
    
    if position == 0:
        newNode.next = head
        if head:
            head.prev = newNode
        return newNode
    
    current = head
    index = 0
    
    while current and index < position - 1:
        current = current.next
        index += 1
        
    if not current:
        return None
    
    if current.next is None:
        current.next = newNode
        newNode.prev = current
        return head
    
    nextNode = current.next
    current.next = newNode
    newNode.prev = current
    newNode.next = nextNode
    nextNode.prev = newNode
    
    return head

# Test Cases (to be added by user)
head1 = [1, 2, 3], position1 = 3, value1 = 4
print(insertAtPosition(head1, position1, value1)) # Output:[1, 2, 3, 4]

head2 = [], position2 = 0, value2 = 1
print(insertAtPosition(head2, position2, value2)) # Output: [1]

head3 = [1], position3 = 0, value3 = 0
print(insertAtPosition(head3, position3, value3)) # Output: [0, 1]

head4 = [1], position4 = 1, value4 = 2
print(insertAtPosition(head4, position4, value4)) # Output: [1, 2]

head5 = [1, 3], position5 = 1, value5 = 2
print(insertAtPosition(head5, position5, value5)) # Output: [1, 2, 3]

head6 = [1, 2, 4], position6 = 2, value6 = 3
print(insertAtPosition(head6, position6, value6)) # Output: [1, 2, 3, 4]

head7 = [1, 2, 3], position7 = 1, value7 = 10
print(insertAtPosition(head7, position7, value7)) # Output: [1, 10, 2, 3]

head8 = [1, 2, 3], position8 = 0, value8 = -1
print(insertAtPosition(head8, position8, value8)) # Output: [-1, 1, 2, 3]

head9 = [1, 2, 3], position9 = 2, value9 = 99
print(insertAtPosition(head9, position9, value9)) # Output: [1, 2, 99, 3]

head10 = [1, 2, 3, 4, 5], position10 = 5, value10 = 6
print(insertAtPosition(head10, position10, value10)) # Output: [1, 2, 3, 4, 5, 6]