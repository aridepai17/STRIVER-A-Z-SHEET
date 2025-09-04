# REVERSE LINKED LIST IN A GROUP OF GIVEN SIZE K

'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''

def reverseKGroup(head, k):
    current = head
    prevNode = None
    
    while current:
        kNode = findKthNode(current, k)
        if kNode is None:
            if prevNode:
                prevNode.next = current
            break
        
        nextNode = kNode.next
        kNode.next = None
        
        newHead = reverseLL(current)
        if current == head:
            head = newHead
        else:
            prevNode.next = newHead
            
        prevNode = current
        current = nextNode
        
    return head

def findKthNode(current, k):
    while current and k > 1:
        k -= 1
        current = current.next
    return current

def reverseLL(head):
    current = head
    prev = None
    
    while current:
        front = current.next
        current.next = prev
        prev = current
        current = front
        
    return prev

# Test Cases
head1 = [1,2,3,4,5]; k1 = 2
print(reverseKGroup(head1, k1)) # Output: [2,1,4,3,5]

head2 = [1,2,3,4,5]; k2 = 3
print(reverseKGroup(head2, k2)) # Output: [3,2,1,4,5]

head3 = [1,2,3,4,5,6]; k3 = 2
print(reverseKGroup(head3, k3)) # Output: [2,1,4,3,6,5]

head4 = [1,2,3,4,5,6]; k4 = 3
print(reverseKGroup(head4, k4)) # Output: [3,2,1,6,5,4]

head5 = [1,2,3,4,5,6,7,8]; k5 = 4
print(reverseKGroup(head5, k5)) # Output: [4,3,2,1,8,7,6,5]

head6 = [1,2,3,4,5,6,7,8,9]; k6 = 3
print(reverseKGroup(head6, k6)) # Output: [3,2,1,6,5,4,9,8,7]

head7 = [1,2,3]; k7 = 1
print(reverseKGroup(head7, k7)) # Output: [1,2,3]

head8 = [1]; k8 = 1
print(reverseKGroup(head8, k8)) # Output: [1]

head9 = [1,2]; k9 = 2
print(reverseKGroup(head9, k9)) # Output: [2,1]

head10 = [1,2,3,4,5]; k10 = 5
print(reverseKGroup(head10, k10)) # Output: [5,4,3,2,1]