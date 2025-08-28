# INSERTION AT HEAD OF SINGLY LINKED LIST

'''
Given the head of a singly linked list and an integer X, 
insert a node with value X at the head of the linked list and return the head of the modified list.
The head is the first node of the linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertAtHead(self, head, X):
        newNode = ListNode(X)
        newNode.next = head 
        
        return newNode

# Test Case 1
print("Test Case 1:") # Input: head -> 1 -> 2 -> 3, X = 7
head1 = ListNode(1, ListNode(2, ListNode(3)))
result1 = Solution().insertAtHead(head1, 7)
print("Output: head -> 7 -> 1 -> 2 -> 3") # Result: head -> 7 -> 1 -> 2 -> 3

# Test Case 2
print("Test Case 2:") # Input: head -> None, X = 5
head2 = None
result2 = Solution().insertAtHead(head2, 5)
print("Output: head -> 5") # Result: head -> 5

# Test Case 3
print("Test Case 3:") # Input: head -> 10, X = 20
head3 = ListNode(10)
result3 = Solution().insertAtHead(head3, 20)
print("Output: head -> 20 -> 10") # Result: head -> 20 -> 10

# Test Case 4
print("Test Case 4:") # Input: head -> 100 -> 200, X = 300
head4 = ListNode(100, ListNode(200))
result4 = Solution().insertAtHead(head4, 300)
print("Output: head -> 300 -> 100 -> 200") # Result: head -> 300 -> 100 -> 200

# Test Case 5
print("Test Case 5:") # Input: head -> 1 -> 2 -> 3 -> 4 -> 5, X = 0
head5 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result5 = Solution().insertAtHead(head5, 0)
print("Output: head -> 0 -> 1 -> 2 -> 3 -> 4 -> 5") # Result: head -> 0 -> 1 -> 2 -> 3 -> 4 -> 5

# Test Case 6
print("Test Case 6:") # Input: head -> -1 -> -2 -> -3, X = -10
head6 = ListNode(-1, ListNode(-2, ListNode(-3)))
result6 = Solution().insertAtHead(head6, -10)
print("Output: head -> -10 -> -1 -> -2 -> -3") # Result: head -> -10 -> -1 -> -2 -> -3

# Test Case 7
print("Test Case 7:") # Input: head -> 5 -> 5 -> 5, X = 5
head7 = ListNode(5, ListNode(5, ListNode(5)))
result7 = Solution().insertAtHead(head7, 5)
print("Output: head -> 5 -> 5 -> 5 -> 5") # Result: head -> 5 -> 5 -> 5 -> 5

# Test Case 8
print("Test Case 8:") # Input: head -> 10 -> 20 -> 30 -> 40 -> 50, X = 5
head8 = ListNode(10, ListNode(20, ListNode(30, ListNode(40, ListNode(50)))))
result8 = Solution().insertAtHead(head8, 5)
print("Output: head -> 5 -> 10 -> 20 -> 30 -> 40 -> 50") # Result: head -> 5 -> 10 -> 20 -> 30 -> 40 -> 50

# Test Case 9
print("Test Case 9:") # Input: head -> 999 -> 888 -> 777, X = 1000
head9 = ListNode(999, ListNode(888, ListNode(777)))
result9 = Solution().insertAtHead(head9, 1000)
print("Output: head -> 1000 -> 999 -> 888 -> 777") # Result: head -> 1000 -> 999 -> 888 -> 777

# Test Case 10
print("Test Case 10:") # Input: head -> 1 -> 2 -> 3, X = 999999999
head10 = ListNode(1, ListNode(2, ListNode(3)))
result10 = Solution().insertAtHead(head10, 999999999)
print("Output: head -> 999999999 -> 1 -> 2 -> 3") # Result: head -> 999999999 -> 1 -> 2 -> 3