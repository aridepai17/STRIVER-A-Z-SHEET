# DELETE THE MIDDLE NODE OF SINGLY LINKED LIST

'''
You are given the head of a linked list. 
Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
where ⌊x⌋ denotes the largest integer less than or equal to x.
'''

# ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: Using Two Traversals

def deleteMiddleNode1(head):
    if head is None or head.next is None:
        return head
    
    current = head
    count = 0
    
    while current:
        count += 1
        current = current.next
        
    middle = count // 2
    
    current = head
    
    while current:
        middle -= 1
        if middle == 0:
            break
        current = current.next
        
    deleteNode = current.next
    current.next = current.next.next
    
    return head

# Time Complexity: O(n) + O(n / 2) = O(n)
# Space Complexity: O(1)

def deleteMiddleNode2(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head.next.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    slow.next = slow.next.next
    
    return head

# Time Complexity : O(n)
# Space Complexity: O(1)

# Examples
head1 = [1,3,4,7,1,2,6]
print(deleteMiddleNode2(head1)) # Output: [1,3,4,1,2,6]

head2 = [1,2,3,4,5,6]
print(deleteMiddleNode2(head2)) # Output: [1,2,3,5,6]

head3 = [1,2,3,4,5]
print(deleteMiddleNode2(head3)) # Output: [1,2,4,5]

head4 = [1,2]
print(deleteMiddleNode2(head4)) # Output: [1]

head5 = [1]
print(deleteMiddleNode2(head5)) # Output: None

head6 = []
print(deleteMiddleNode2(head6)) # Output: None

head7 = [1,2,3,4,5,6,7,8,9,10]
print(deleteMiddleNode2(head7)) # Output: [1,2,3,4,6,7,8,9,10]

head8 = [5,5,5,5,5]
print(deleteMiddleNode2(head8)) # Output: [5,5,5,5]

head9 = [-1,-2,-3,-4,-5]
print(deleteMiddleNode2(head9)) # Output: [-1,-2,-4,-5]

head10 = [0,1,-1,2,-2,3,-3]
print(deleteMiddleNode2(head10)) # Output: [0,1,-1,2,-2,-3]

head11 = [1,2,3]
print(deleteMiddleNode2(head11)) # Output: [1,3]