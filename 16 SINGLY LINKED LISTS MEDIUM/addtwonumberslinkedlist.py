# ADD TWO NUMBERS LINKED LIST

'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def addTwoNumbers(l1, l2):
    t1 = l1
    t2 = l2
    
    dummyNode = ListNode(-1)
    current = dummyNode
    carry = 0
    
    while t1 or t2:
        sum = carry
        
        if t1:
            sum = sum + t1.data
        if t2:
            sum = sum + t2.data
            
        newNode = ListNode(sum % 10)
        carry = sum // 10
        current.next = newNode
        current = newNode
        
        if t1:
            t1 = t1.next
        if t2:
            t2 = t2.next
            
    if carry:
        newNode = ListNode(carry)
        current.next = newNode
        
    return dummyNode.next

# Time Complexity: O(max(m, n)), where m and n are the lengths of the two input linked lists.
# Space Complexity: O(max(m, n)), for the output linked list.

# Test Cases
l1_1 = [2,4,3]; l2_1 = [5,6,4]
print(addTwoNumbers(l1_1, l2_1)) # Output: [7, 0, 8]

l1_2 = [0]; l2_2 = [0]
print(addTwoNumbers(l1_2, l2_2)) # Output: [0]

l1_3 = [9,9,9,9,9,9,9]; l2_3 = [9,9,9,9]
print(addTwoNumbers(l1_3, l2_3)) # Output: [8,9,9,9,0,0,0,1]

l1_4 = [1,8]; l2_4 = [0]
print(addTwoNumbers(l1_4, l2_4)) # Output: [1,8]

l1_5 = [5]; l2_5 = [5]
print(addTwoNumbers(l1_5, l2_5)) # Output: [0,1]

l1_6 = [1,2,3]; l2_6 = [4,5,6]
print(addTwoNumbers(l1_6, l2_6)) # Output: [5,7,9]

l1_7 = [9,9,9]; l2_7 = [1]
print(addTwoNumbers(l1_7, l2_7)) # Output: [0,0,0,1]

l1_8 = [2,4,9]; l2_8 = [5,6,4,9]
print(addTwoNumbers(l1_8, l2_8)) # Output: [7,0,4,0,1]

l1_9 = [0,1]; l2_9 = [0,1,2]
print(addTwoNumbers(l1_9, l2_9)) # Output: [0,2,2]

l1_10 = [1,0,0,1]; l2_10 = [9,9,9]
print(addTwoNumbers(l1_10, l2_10)) # Output: [0,0,0,2]