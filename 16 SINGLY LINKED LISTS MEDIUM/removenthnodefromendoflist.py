# REMOVE NTH NODE FROM END OF LIST

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: Using Two Traversals
def removeNthFromEnd1(head, n):
    count = 0
    current = head
    
    while current:
        count += 1
        current = current.next
        
    if count == n:
        newHead = head.next
        return newHead
    
    result = count - n
    current = head
    
    while current:
        result -= 1
        if result == 0:
            break
        current = current.next
        
    deleteNode = current.next
    current.next = deleteNode.next
    
    return head

# Time Complexity: O(len) + O(len - n) => O(n)
# Space Complexity: O(1)

# Solution 2: Two pointers approach
def removeNthFromEnd2(head, n):
    fast = head
    slow = head
    
    for i in range(n):
        fast = fast.next
        
    if fast is None:
        return head.next
    
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
        
    deleteNode = slow.next
    slow.next = deleteNode.next
    
    return head

# Time Complexity: O(n)
# Space Complexity: O(1)

# Examples
head1 = [1,2,3,4,5], n1 = 2
print(removeNthFromEnd2(head1, n1)) # Output: [1, 2, 3, 5]

head2 = [1], n2 = 1
print(removeNthFromEnd2(head2, n2)) # Output: []

head3 = [1,2], n3 = 1
print(removeNthFromEnd2(head3, n3)) # Output: [1]

head4 = [1,2,3,4,5], n4 = 1
print(removeNthFromEnd2(head4, n4)) # Output: [1, 2, 3, 4]

head5 = [1,2,3,4,5], n5 = 5
print(removeNthFromEnd2(head5, n5)) # Output: [2, 3, 4, 5]

head6 = [1,2,3,4,5,6,7,8,9,10], n6 = 3
print(removeNthFromEnd2(head6, n6)) # Output: [1, 2, 3, 4, 5, 6, 7, 9, 10]

head7 = [1,2,3,4,5,6,7,8,9,10], n7 = 10
print(removeNthFromEnd2(head7, n7)) # Output: [2, 3, 4, 5, 6, 7, 8, 9, 10]

head8 = [1,2,3,4,5,6,7,8,9,10], n8 = 1
print(removeNthFromEnd2(head8, n8)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

head9 = [1,1,1,1,1], n9 = 3
print(removeNthFromEnd2(head9, n9)) # Output: [1, 1, 1, 1]

head10 = [-1,-2,-3,-4,-5], n10 = 2
print(removeNthFromEnd2(head10, n10)) # Output: [-1, -2, -3, -5]
        