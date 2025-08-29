# PALINDROME LINKED LIST

'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
A palindrome is a sequence that reads the same forward and backward.
'''

# Solution 1: Using Stack Data Structure
def isPalindrome1(head):
    stack = []
    current = head
    
    while current is not None:
        stack.append(current.val)
        current = current.next
        
    current = head
    
    while current is not None:
        if current != stack[-1]:
            return False
        stack.pop()
        current = current.next
        
    return True

# Time Complexity: O(n)
# Space Complexity: O(n)

# Solution 2: Using Slow and Fast Pointers
def isPalindrome2(head):
    slow = head
    fast = head
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    newHead = reverseList(slow.next)
    
    first = head
    second = newHead
    
    while second is not None:
        if first.val != second.val:
            reverseList(newHead)
            return False
        
        first = first.next
        second = second.next
        
    reverseList(newHead)
    return True

# Time Complexity: O(n)
# Space Complexity: O(1)

def reverseList(current):
    prev = None
    
    while current is not None:
        front = current.next
        current.next = prev
        prev = current
        current = front
        
    return prev

# Examples
head1 = [1,2,2,1]
print(isPalindrome2(head1)) # Output: True

head2 = [1,2]
print(isPalindrome2(head2)) # Output: False

head3 = [1]
print(isPalindrome2(head3)) # Output: True

head4 = []
print(isPalindrome2(head4)) # Output: True

head5 = [1,2,3,2,1]
print(isPalindrome2(head5)) # Output: True

head6 = [1,2,3,4,5]
print(isPalindrome2(head6)) # Output: False

head7 = [1,1,1,1]
print(isPalindrome2(head7)) # Output: True

head8 = [1,2,1,2]
print(isPalindrome2(head8)) # Output: False

head9 = [2,2]
print(isPalindrome2(head9)) # Output: True

head10 = [0,0,0]
print(isPalindrome2(head10)) # Output: True

head11 = [1,0,1,0,1]
print(isPalindrome2(head11)) # Output: True

head12 = [10,20,20,10]
print(isPalindrome2(head12)) # Output: True

head13 = [-1,-2,-2,-1]
print(isPalindrome2(head13)) # Output: True

head14 = [-1,0,-1]
print(isPalindrome2(head14)) # Output: True

head15 = [1,2,3,3,2,1]
print(isPalindrome2(head15)) # Output: True