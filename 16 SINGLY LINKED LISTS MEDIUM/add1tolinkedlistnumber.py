# ADD 1 TO LINKED LIST NUMBER 

'''
You are given a linked list where each element in the list is a node and have an integer data. 
You need to add 1 to the number formed by concatinating all the list node numbers together and return the head of the modified linked list. 

Note: The head represents the first element of the given array.

Constraints:
1 <= len(list) <= 10^5
0 <= list[i] <= 9
'''

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Solution 1: Iterative Method
def addOne1(head):
    head = reverseLL(head)
    
    current = head
    carry = 1
    
    while current:
        current.data = current.data + carry
        if current.data < 10:
            carry = 0
            break
        else:
            current.data = 0
            carry = 1
        current = current.next
        
    if carry == 1:
        newNode = ListNode(1)
        head = reverseLL(head)
        newNode.next = head
        return newNode 
    
    head = reverseLL(head)
    return head

def reverseLL(head):
    current = head
    prev = None
    
    while current:
        front = current.next
        current.next = prev
        prev = current
        current = front
        
    return prev

# Time Complexity: O(3n) => O(n) where n is the number of nodes in the linked list and 3 is number of times it has been traversed.
# Space Complexity: O(1) - only using a constant number of variables.

# Solution 2: Recursive Method
def addOne2(head):
    carry = recursiveCarry(head)
    
    if carry == 1:
        newNode = ListNode(1)
        newNode.next = head
        return newNode
    
    return head

def recursiveCarry(node):
    if node == None:
        return 1
    
    carry = recursiveCarry(node.next)
    node.data = node.data + carry
    
    if node.data < 10:
        return 0
    node.data = 0
    return 1

# Time Complexity: O(n) where n is the number of nodes in the linked list
# Space Complexity: O(n) due to recursion stack space

# Test Cases
head1 = [4, 5, 6]
print(addOne2(head1)) # Output: [4, 5, 7]

head2 = [1, 2, 3]
print(addOne2(head2)) # Output: [1, 2, 4]

head3 = [9, 9, 9]
print(addOne2(head3)) # Output: [1, 0, 0, 0]

head4 = [0]
print(addOne2(head4)) # Output: [1]

head5 = [1, 0, 0, 0]
print(addOne2(head5)) # Output: [1, 0, 0, 1]

head6 = [9]
print(addOne2(head6)) # Output: [1, 0]

head7 = [1, 9, 9]
print(addOne2(head7)) # Output: [2, 0, 0]

head8 = [5, 6, 7, 8]
print(addOne2(head8)) # Output: [5, 6, 7, 9]

head9 = [9, 8, 7, 6]
print(addOne2(head9)) # Output: [9, 8, 7, 7]

head10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(addOne2(head10)) # Output: [1, 2, 3, 4, 5, 6, 7, 9, 0]