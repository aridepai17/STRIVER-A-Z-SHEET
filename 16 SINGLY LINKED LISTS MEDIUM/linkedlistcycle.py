# LINKED LIST CYCLE 

'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: Using Hash Set
def hasCycle1(head, pos):
    current = head
    hashMap = {}
    
    while current is not None:
        if current in hashMap:
            return True
        hashMap[current] = 1
        current = current.next
        
    return False

# Time Complexity: O(n) - where n is the number of nodes in the linked list
# Space Complexity: O(n) - we store each node in the hash set


# Solution 2: Slow and Fast pointers (Floyd's Cycle-Finding Algorithm)
def hasCycle2(head, pos):
    if head is None or head.next is None:
        return False
    
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False

# Time Complexity: O(n) - where n is the number of nodes in the linked list
# Space Complexity: O(1) - we only use two pointers regardless of the list size

# Examples
head = [3,2,0,-4], pos = 1
print(hasCycle2(head, pos)) # Output: True

head = [1,2], pos = 0
print(hasCycle2(head, pos)) # Output: True

head = [1,2,3,4,5], pos = -1
print(hasCycle2(head, pos)) # Output: False

head = [], pos = -1
print(hasCycle2(head, pos)) # Output: False

head = [1], pos = -1
print(hasCycle2(head, pos)) # Output: False

head = [1], pos = 0
print(hasCycle2(head, pos)) # Output: True

head = [1,2], pos = 1
print(hasCycle2(head, pos)) # Output: True

head = [1,2,3,4,5,6,7,8,9,10], pos = 5
print(hasCycle2(head, pos)) # Output: True

head = [1,2,3,4,5,6,7,8,9,10], pos = -1
print(hasCycle2(head, pos)) # Output: False

head = [1,2,3,4,5], pos = 4
print(hasCycle2(head, pos)) # Output: True

head = [-1,-2,-3,-4,-5], pos = 2
print(hasCycle2(head, pos)) # Output: True