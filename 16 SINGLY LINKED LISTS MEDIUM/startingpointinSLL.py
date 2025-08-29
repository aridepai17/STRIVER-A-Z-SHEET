# STARTING POINT IN SINGLY LINKED LIST

'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: Using HashMap data structure
def detectCycle1(head):
    hashMap = {}
    current = head
    
    while current is not None:
        if current in hashMap:
            return current
        hashMap[current] = True
        current = current.next
        
    return None
    
# Time Complexity: O(n)
# Space Complexity: O(n)

# Solution 2: Using Slow and Fast pointers
def detectCycle2(head):
    slow = head
    fast = head 
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None

    slow = head
    
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow

# Time Complexity: O(n)
# Space Complexity: O(1)

# Examples
head = [3,2,0,-4], pos = 1
print(detectCycle2(head)) # Output: ListNode(2)

head = [1,2], pos = 0
print(detectCycle2(head)) # Output: ListNode(1)

head = [1,2,3,4,5], pos = -1
print(detectCycle2(head)) # Output: None

head = [], pos = -1
print(detectCycle2(head)) # Output: None

head = [1], pos = -1
print(detectCycle2(head)) # Output: None

head = [1], pos = 0
print(detectCycle2(head)) # Output: ListNode(1)

head = [1,2], pos = 1
print(detectCycle2(head)) # Output: ListNode(2)

head = [1,2,3,4,5,6,7,8,9,10], pos = 5
print(detectCycle2(head)) # Output: ListNode(6)

head = [1,2,3,4,5,6,7,8,9,10], pos = -1
print(detectCycle2(head)) # Output: None

head = [1,2,3,4,5], pos = 4
print(detectCycle2(head)) # Output: ListNode(5)

head = [-1,-2,-3,-4,-5], pos = 2
print(detectCycle2(head)) # Output: ListNode(-3)

head = [1,2,3,4,5,6,7,8,9,10,11,12], pos = 8
print(detectCycle2(head)) # Output: ListNode(9)

head = [1,2,3,4,5,6,7,8,9,10,11,12], pos = -1
print(detectCycle2(head)) # Output: None

head = [0,0,0,0,0], pos = 1
print(detectCycle2(head)) # Output: ListNode(0)

head = [1000,2000,3000,4000,5000], pos = 3
print(detectCycle2(head)) # Output: ListNode(4000)

head = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], pos = 10
print(detectCycle2(head)) # Output: ListNode(11)

head = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], pos = -1
print(detectCycle2(head)) # Output: None

head = [1,1,1,1,1], pos = 2
print(detectCycle2(head)) # Output: ListNode(1)

head = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], pos = 15
print(detectCycle2(head)) # Output: ListNode(16)

head = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], pos = -1
print(detectCycle2(head)) # Output: None