# REMOVE DUPLICATES FROM SORTED DOUBLY LINKED LIST

'''
Given a sorted doubly linked list, remove all the duplicate nodes from the list.
The final list should contain each element only once.
The function should return the head of the updated doubly linked list.
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def removeDuplicates(head):
    current = head 
    
    while current and current.next:
        nextNode = current.next
        while nextNode and nextNode.data == current.data:
            nextNode = nextNode.next
        current.next = nextNode
        if nextNode:
            nextNode.prev = current
        current = nextNode
        
    return head

# Time Complexity: O(n), where n is the number of nodes in the doubly linked list.
# We traverse the list once.

# Space Complexity: O(1)
# We are not using any extra space. The modifications are done in-place.

# Test Cases
head1 = [1, 1, 2, 2, 3, 4]
print(removeDuplicates(head1)) # Output: [1, 2, 3, 4]

# Test Case 2: Empty list
head2 = []
print(removeDuplicates(head2)) # Output: []

# Test Case 3: Single node list
head3 = [10]
print(removeDuplicates(head3)) # Output: [10]

# Test Case 4: No duplicates
head4 = [1, 2, 3, 4, 5]
print(removeDuplicates(head4)) # Output: [1, 2, 3, 4, 5]

# Test Case 5: All elements are duplicates
head5 = [5, 5, 5, 5, 5]
print(removeDuplicates(head5)) # Output: [5]

# Test Case 6: Duplicates at the beginning
head6 = [1, 1, 2, 3, 4]
print(removeDuplicates(head6)) # Output: [1, 2, 3, 4]

# Test Case 7: Duplicates at the end
head7 = [1, 2, 3, 4, 4, 4]
print(removeDuplicates(head7)) # Output: [1, 2, 3, 4]

# Test Case 8: Duplicates in the middle
head8 = [1, 2, 2, 2, 3, 4]
print(removeDuplicates(head8)) # Output: [1, 2, 3, 4]

# Test Case 9: List with negative numbers and duplicates
head9 = [-3, -3, -1, 0, 0, 2, 2, 2]
print(removeDuplicates(head9)) # Output: [-3, -1, 0, 2]

# Test Case 10: Longer list with multiple groups of duplicates
head10 = [1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6]
print(removeDuplicates(head10)) # Output: [1, 2, 3, 4, 5, 6]
