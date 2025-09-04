# ROTATE LINKED LIST

# Given the head of a linked list, rotate the list to the right by k places.

def rotateRight(head, k):
    if head is None or head.next is None or k == 0:
        return head
    
    current = head
    tail = head
    length = 1
    
    while tail.next:
        length += 1
        tail = tail.next
        
    if k % length == 0:
        return head
    
    k = k % length
    
    tail.next = current
    newLastNode = findNthNode(current, length - k)
    current = newLastNode.next
    newLastNode.next = None
    
    return current

def findNthNode(current, n):
    count = 0
    
    while current:
        count += 1
        if count == n:
            return current
        current = current.next
        
    return current

# Test Cases
head1 = [1,2,3,4,5]; k1 = 2
print(rotateRight(head1, k1)) # Output: [4,5,1,2,3]

head2 = [0,1,2]; k2 = 4
print(rotateRight(head2, k2)) # Output: [2,0,1]

head3 = [1,2]; k3 = 0
print(rotateRight(head3, k3)) # Output: [1,2]

head4 = [1]; k4 = 99
print(rotateRight(head4, k4)) # Output: [1]

head5 = [1,2,3,4,5]; k5 = 5
print(rotateRight(head5, k5)) # Output: [1,2,3,4,5]

head6 = [1,2,3,4,5]; k6 = 1
print(rotateRight(head6, k6)) # Output: [5,1,2,3,4]

head7 = [1,2,3,4,5,6]; k7 = 3
print(rotateRight(head7, k7)) # Output: [4,5,6,1,2,3]

head8 = [1,2,3,4,5,6,7,8,9,10]; k8 = 7
print(rotateRight(head8, k8)) # Output: [4,5,6,7,8,9,10,1,2,3]

head9 = [1,2,3]; k9 = 3
print(rotateRight(head9, k9)) # Output: [1,2,3]

head10 = [10,20,30,40,50]; k10 = 12
print(rotateRight(head10, k10)) # Output: [40,50,10,20,30]