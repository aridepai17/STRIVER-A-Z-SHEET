# ODD EVEN LINKED LIST

'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.
'''

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Solution 1: Using List
def oddevenList1(head):
    if head is None or head.next is None:
        return head
    
    arr = []
    current = head
    
    while current is not None and current.next is not None:
        arr.append(current.data)
        current = current.next.next
    
    if current:
        arr.append(current.data)
        
    current = head.next
    
    while current is not None and current.next is not None:
        arr.append(current.data)
        current = current.next.next
        
    if current:
        arr.append(current.data)
        
    i = 0
    current = head
    
    while current is not None:
        current.data = arr[i]
        i += 1
        current = current.next
        
    return head

# Time Complexity: O(n)
# Space Complexity: O(n)

# Solution 2: Using Two Pointers approach

def oddevenList2(head):
    if head is None or head.next is None:
        return head
    
    odd = head
    even = head.next
    evenHead = head.next
    
    while even is not None and even.next is not None:
        odd.next = odd.next.next
        even.next = even.next.next
        
        odd = odd.next
        even = even.next
        
    odd.next = evenHead
    
    return head

# Time Complexity: O(n)
# Space Complexity: O(1)

# Examples
head1 = [1,2,3,4,5]
print(oddevenList2(head1)) # Output: [1, 3, 5, 2, 4]

head2 = [2,1,3,5,6,4,7]
print(oddevenList2(head2)) # Output: [2, 3, 6, 7, 1, 5, 4]

head3 = [1]
print(oddevenList2(head3)) # Output: [1]

head4 = [1,2]
print(oddevenList2(head4)) # Output: [1, 2]

head5 = [1,2,3]
print(oddevenList2(head5)) # Output: [1, 3, 2]

head6 = []
print(oddevenList2(head6)) # Output: []

head7 = [10,20,30,40,50,60]
print(oddevenList2(head7)) # Output: [10, 30, 50, 20, 40, 60]

head8 = [5,5,5,5,5]
print(oddevenList2(head8)) # Output: [5, 5, 5, 5, 5]

head9 = [-1,-2,-3,-4,-5,-6]
print(oddevenList2(head9)) # Output: [-1, -3, -5, -2, -4, -6]

head10 = [0,1,0,1,0,1]
print(oddevenList2(head10)) # Output: [0, 0, 0, 1, 1, 1]