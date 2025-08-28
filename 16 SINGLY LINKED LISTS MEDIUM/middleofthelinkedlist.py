# MIDDLE OF SINGLY LINKED LIST

'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Manual solution using two traversals
def findMiddle(head):
    current = head
    count = 0
    
    while current is not None:
        count += 1
        current = current.next
        
    middleElement = (count // 2) + 1
    
    temp = head
    
    while temp is not None:
        middleElement -= 1
        if middleElement == 0:
            break
        temp = temp.next
        
    return temp

# Time Complexity: O(n) + O(n/2) = O(n)
# Space Complexity: O(1)

# Optimal Solution using Slow and Fast Pointers
def findMiddleElement(head):
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    return slow

# Time Complexity: O(n/2) = O(n)
# Space Complexity: O(1)

# Test Case 1
head1 = [1, 2, 3, 4, 5]
print(findMiddle(head1)) # Output: [3, 4, 5]

# Test Case 2
head2 = [1, 2, 3, 4, 5, 6]
print(findMiddle(head2)) # Output: [4, 5, 6]

# Test Case 3
head3 = []
print(findMiddle(head3)) # Output: []

# Test Case 4
head4 = [10]
print(findMiddle(head4)) # Output: [10]

# Test Case 5
head5 = [100, 200]
print(findMiddle(head5)) # Output: [200]

# Test Case 6
head6 = [1, 2, 3]
print(findMiddle(head6)) # Output: [2, 3]

# Test Case 7
head7 = [-1, -2, -3, -4]
print(findMiddle(head7)) # Output: [-3, -4]

# Test Case 8
head8 = [5, 5, 5, 5, 5]
print(findMiddle(head8)) # Output: [5, 5, 5]

# Test Case 9
head9 = [1, 2, 3, 4, 5, 6, 7]
print(findMiddle(head9)) # Output: [4, 5, 6, 7]

# Test Case 10
head10 = [1, 2, 3, 4, 5, 6, 7, 8]
print(findMiddle(head10)) # Output: [5, 6, 7, 8]