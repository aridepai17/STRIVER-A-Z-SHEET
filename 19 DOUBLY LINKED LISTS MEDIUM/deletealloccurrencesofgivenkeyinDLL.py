# DELETE ALL OCCURRENCES OF GIVEN KEY IN DOUBLE LINKED LIST

'''
Given a doubly linked list and a key, your task is to delete all occurrences of the given key in the doubly linked list. 
The function should return the head of the modified list.
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def deleteAllOccurrences(head, key):
    current = head
    
    while current:
        nextNode = current.next
        if current.data == key:
            if current == head:
                head = nextNode
                if head:
                    head.prev = None
            else:
                if current.prev:
                    current.prev.next = nextNode
                if nextNode:
                    nextNode.prev = current.prev
                    
        current = nextNode
        
    return head

'''
Time Complexity: O(n), where n is the number of nodes in the doubly linked list.
We traverse the list once.
    
Space Complexity: O(1).
We are not using any extra space.
'''

# Test Cases
head1 = [1, 2, 2, 3], key1 = 3
print(deleteAllOccurrences(head1, key1)) # Output: [1, 2, 2]

head2 = [2, 5, 2, 8, 2], key2 = 2
print(deleteAllOccurrences(head2, key2)) # Output: [5, 8]

head3 = [3, 3, 3, 3], key3 = 3
print(deleteAllOccurrences(head3, key3)) # Output: []

head4 = [10, 20, 30], key4 = 40
print(deleteAllOccurrences(head4, key4)) # Output: [10, 20, 30]

head5 = [], key5 = 5
print(deleteAllOccurrences(head5, key5)) # Output: []

head6 = [6], key6 = 6
print(deleteAllOccurrences(head6, key6)) # Output: []

head7 = [7], key7 = 8
print(deleteAllOccurrences(head7, key7)) # Output: [7]

head8 = [1, 2, 3, 4, 5], key8 = 5
print(deleteAllOccurrences(head8, key8)) # Output: [1, 2, 3, 4]

head9 = [9, 8, 7, 9, 6, 9], key9 = 9
print(deleteAllOccurrences(head9, key9)) # Output: [8, 7, 6]

head10 = [1, 1, 2, 3, 3, 3, 4, 5, 5], key10 = 3
print(deleteAllOccurrences(head10, key10)) # Output: [1, 1, 2, 4, 5, 5]