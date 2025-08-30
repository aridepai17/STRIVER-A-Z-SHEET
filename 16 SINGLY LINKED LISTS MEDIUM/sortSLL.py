# SORT SINGLY LINKED LIST

# Given the head of a linked list, return the list after sorting it in ascending order.

# ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: Using extra array
def sortList1(head):
    if head is None or head.next is None:
        return head
    
    current = head
    arr = []
    
    while current:
        arr.append(current.val)
        current = current.next
        
    arr.sort()
    
    current = head
    i = 0
    
    while current:
        current.val = arr[i]
        current = current.next
        i += 1
        
    return head

# Time Complexity : O(n) + O(n log n) + O(n) => O(n log n)
# Space Complexity: O(n)

# Solution 2: Using Merge Sort and Recursion
def sortList2(head):
    if head is None or head.next is None:
        return head
    
    middle = findMiddle(head)
    
    leftHead = head
    rightHead = middle.next
    middle.next = None
    
    leftHead = sortList2(leftHead)
    rightHead = sortList2(rightHead)
    
    return merge(leftHead, rightHead)

def findMiddle(head):
    slow = head
    fast = head.next.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

def merge(leftHead, rightHead):
    current = ListNode(0)
    tail = current
    
    while leftHead and rightHead:
        if leftHead.val <= rightHead.val:
            tail.next = leftHead
            leftHead = leftHead.next
        else:
            tail.next = rightHead
            rightHead = rightHead.next
        tail = tail.next
        
    if leftHead:
        tail.next = leftHead
    if rightHead:
        tail.next = rightHead
        
    return current.next

# Test Cases
head1 = [-1,5,3,4,0]
print(sortList2(head1)) # Output: [-1, 0, 3, 4, 5]

head2 = [4,2,1,3]
print(sortList2(head2)) # Output: [1, 2, 3, 4]

head3 = [-1,-2,-3,-4,-5]
print(sortList2(head3)) # Output: [-5, -4, -3, -2, -1]

head4 = [1]
print(sortList2(head4)) # Output: [1]

head5 = []
print(sortList2(head5)) # Output: None

head6 = [5,5,5,5,5]
print(sortList2(head6)) # Output: [5, 5, 5, 5, 5]

head7 = [9,8,7,6,5,4,3,2,1]
print(sortList2(head7)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

head8 = [0,0,0,1,1,1]
print(sortList2(head8)) # Output: [0, 0, 0, 1, 1, 1]

head9 = [100,-100,50,-50,25,-25]
print(sortList2(head9)) # Output: [-100, -50, -25, 25, 50, 100]

head10 = [1,2,3,4,5]
print(sortList2(head10)) # Output: [1, 2, 3, 4, 5]

head11 = [3,1,4,1,5,9,2,6]
print(sortList2(head11)) # Output: [1, 1, 2, 3, 4, 5, 6, 9]