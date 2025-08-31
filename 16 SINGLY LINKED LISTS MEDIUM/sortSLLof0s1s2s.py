# SORT LINKED LIST OF 0s, 1s and 2s

'''
Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only. 
Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.
'''

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Solution 1: Using Two Traversals
def segregateList1(head):
    current = head
    count0 = 0
    count1 = 0
    count2 = 0
    
    while current:
        if current.data == 0:
            count0 += 1
        elif current.data == 1:
            count1 += 1
        else:
            count2 += 1
        current = current.next
            
    current = head
    
    while current:
        if count0:
            current.data = 0
            count0 -= 1
        elif count1:
            current.data = 1
            count1 -= 1
        else:
            current.data = 2
            count2 -= 1
        current = current.next
            
    return head

# Time Complexity: O(n)
# Space Complexity: O(1)

# Solution 2: One Pass using Three Dummy Nodes
def segregateList2(head):
    zeroHead = ListNode(-1)
    oneHead = ListNode(-1)
    twoHead = ListNode(-1)
    
    zero = zeroHead
    one = oneHead
    two = twoHead
    
    current = head
    
    while current:
        if current.data == 0:
            zero.next = current
            zero = current
        elif current.data == 1:
            one.next = current
            one = current
        else:
            two.next = current
            two = current
        current = current.next
        
    zero.next = oneHead.next if oneHead.next else twoHead.next
    one.next = twoHead.next
    two.next = None
    
    newHead = zeroHead.next
    
    return newHead

# Test Cases
head1 = [1, 2, 2, 1, 2, 0, 2, 2]
print(segregateList2(head1)) # Output: [0, 1, 1, 2, 2, 2, 2, 2]

head2 = [2, 2, 0, 1]
print(segregateList2(head2)) # Output: [0, 1, 2, 2]

head3 = [2, 1, 0]
print(segregateList2(head3)) # Output: [0, 1, 2]

head4 = [0, 0, 0]
print(segregateList2(head4)) # Output: [0, 0, 0]

head5 = [1, 1, 1]
print(segregateList2(head5)) # Output: [1, 1, 1]

head6 = [2, 2, 2]
print(segregateList2(head6)) # Output: [2, 2, 2]

head7 = [0, 1, 2, 0, 1, 2]
print(segregateList2(head7)) # Output: [0, 0, 1, 1, 2, 2]

head8 = [1, 0, 2, 1, 0, 2, 1, 0, 2]
print(segregateList2(head8)) # Output: [0, 0, 0, 1, 1, 1, 2, 2, 2]

head9 = [2, 1, 0, 2, 1, 0, 2, 1, 0]
print(segregateList2(head9)) # Output: [0, 0, 0, 1, 1, 1, 2, 2, 2]

head10 = [0]
print(segregateList2(head10)) # Output: [0]