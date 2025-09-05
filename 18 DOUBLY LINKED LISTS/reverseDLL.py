# REVERSE DOUBLY LINKED LIST

# You are given the head of a doubly linked list. 
# You have to reverse the doubly linked list and return its head.

class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Solution 1: Using Stack Data Structure
def reverseDLL1(head):
    stack = []
    current = head
    
    while current:
        stack.append(current.data)
        current = current.next
        
    current = head
    
    while current:
        current.data = stack[-1]
        stack.pop()
        current = current.next
        
    return head

# Time Complexity: O(n)
# Space Complexity: O(n)

# Solution 2: In-Place One Pass Traversal
def reverseDLL2(head):
    if head.next is None:
        return head
    
    current = head
    
    while current:
        last = current.prev
        current.prev = current.next
        current.next = last
        current = current.prev
        
    return last.prev

# Time Complexity: O(n) because we traverse the list once.
# Space Complexity: O(1)

# Test Cases
head1 = [1,2,3,4,5]
print(reverseDLL2(head1)) # Output: [5, 4, 3, 2, 1]

# Test Case 2: Empty list
head2 = []
print(reverseDLL2(head2)) # Output: None

# Test Case 3: Single node list
head3 = [10]
print(reverseDLL2(head3)) # Output: [10]

# Test Case 4: Two nodes list
head4 = [1, 2]
print(reverseDLL2(head4)) # Output: [2, 1]

# Test Case 5: List with duplicate numbers
head5 = [5, 5, 5]
print(reverseDLL2(head5)) # Output: [5, 5, 5]

# Test Case 6: List with negative numbers
head6 = [-1, -2, -3]
print(reverseDLL2(head6)) # Output: [-3, -2, -1]

# Test Case 7: List with mixed positive/negative/zero
head7 = [-1, 0, 1]
print(reverseDLL2(head7)) # Output: [1, 0, -1]

# Test Case 8: Longer list
head8 = [10, 20, 30, 40, 50, 60]
print(reverseDLL2(head8)) # Output: [60, 50, 40, 30, 20, 10]

# Test Case 9: List with large values
head9 = [1000, 2000, 3000]
print(reverseDLL2(head9)) # Output: [3000, 2000, 1000]

# Test Case 10: Palindrome list
head10 = [1, 2, 1]
print(reverseDLL2(head10)) # Output: [1, 2, 1]
