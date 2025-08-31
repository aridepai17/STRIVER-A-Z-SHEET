# INTERSECTION OF TWO LINKED LISTS

'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return None.
The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: Using HashMap
def getIntersectionNode1(headA, headB):
    current1 = headA
    current2 = headB
    hashMap = {}
    
    while current1:
        hashMap[current1] = True
        current1 = current1.next
        
    while current2:
        if current2 in hashMap:
            return current2
        current2 = current2.next
        
    return None

# Time Complexity: O(m + n) where m and n are the lengths of the two linked lists
# Space Complexity: O(m) where m is the length of the first linked list

# Solution 2: Using Two Pointers 
def getIntersectionNode2(headA, headB):
    current1 = headA
    current2 = headB
    
    while current1 != current2:
        current1 = current1.next if current1 else headB
        current2 = current2.next if current2 else headA
        
    return current1

# Time Complexity: O(m + n) where m and n are the lengths of the two linked lists
# Space Complexity: O(1) - only using two pointers

# Test Cases
headA1 = [4,1,8,4,5]
headB1 = [5,6,1,8,4,5]
print(getIntersectionNode2(headA1, headB1)) # Output: ListNode(8)

headA2 = [1,9,1,2,4]
headB2 = [3,2,4]
print(getIntersectionNode2(headA2, headB2)) # Output: ListNode(2)

headA3 = [2,6,4]
headB3 = [1,5]
print(getIntersectionNode2(headA3, headB3)) # Output: None

headA4 = [1,2,3,4,5]
headB4 = [6,7,8,9,10]
print(getIntersectionNode2(headA4, headB4)) # Output: None

headA5 = [1,2,3,4,5]
headB5 = [1,2,3,4,5]
print(getIntersectionNode2(headA5, headB5)) # Output: ListNode(1)

headA6 = [1,2,3,4,5]
headB6 = [6,7,8,9,10,1,2,3,4,5]
print(getIntersectionNode2(headA6, headB6)) # Output: ListNode(1)

headA7 = [1,2,3,4,5]
headB7 = [6,7,8,9,10,11,12,13,14,15,1,2,3,4,5]
print(getIntersectionNode2(headA7, headB7)) # Output: ListNode(1)

headA8 = [1,2,3,4,5]
headB8 = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5]
print(getIntersectionNode2(headA8, headB8)) # Output: ListNode(1)

headA9 = [1,2,3,4,5]
headB9 = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,1,2,3,4,5]
print(getIntersectionNode2(headA9, headB9)) # Output: ListNode(1)

headA10 = [1,2,3,4,5]
headB10 = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,1,2,3,4,5]
print(getIntersectionNode2(headA10, headB10)) # Output: ListNode(1)