'''
Given a doubly linked list, implement a function to insert a new node with a given value at the tail (end) of the list. 
The function should return the head of the updated doubly linked list.
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insertAtTail(head, data):
    newNode = ListNode(data)
    
    if not head:
        return newNode
    
    current = head
    while current.next:
        current = current.next
        
    current.next = newNode
    newNode.prev = current
    
    return head

# Test Cases
head1 = [1, 2, 3, 4], data1 = 5
print(insertAtTail(head1, data1)) # Output: [1, 2, 3, 4, 5]

head2 = [], data2 = 10
print(insertAtTail(head2, data2)) # Output: [10]

head3 = [1], data3 = 2
print(insertAtTail(head3, data3)) # Output: [1, 2]

head4 = [1, 2], data4 = 3
print(insertAtTail(head4, data4)) # Output: [1, 2, 3]

head5 = [0], data5 = -1
print(insertAtTail(head5, data5)) # Output: [0, -1]

head6 = [5, 5], data6 = 5
print(insertAtTail(head6, data6)) # Output: [5, 5, 5]

head7 = ['a'], data7 = 'b'
print(insertAtTail(head7, data7)) # Output: ['a', 'b']

head8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], data8 = 11
print(insertAtTail(head8, data8)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

head9 = [-3, -2, -1], data9 = 0
print(insertAtTail(head9, data9)) # Output: [-3, -2, -1, 0]

head10 = [1, 2, 3, 4], data10 = 4
print(insertAtTail(head10, data10)) # Output: [1, 2, 3, 4, 4]