# LENGTH OF LOOP IN SINGLY LINKED LIST

'''
Given the head of a singly linked list, find the length of the loop in the linked list if it exists. 
Return the length of the loop if it exists; otherwise, return 0.
A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index (0-based) of the node from where the loop starts.
Note that pos is not passed as a parameter.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

# Solution 1: Using a HashMap
def lengthOfLoop(head):
    current = head
    hashMap = {}
    count = 1
    
    while current is not None:
        if current in hashMap:
            return count - hashMap[current]
        hashMap[current] = count
        count += 1
        current = current.next
        
    return 0
        
# Time Complexity: O(n) * O( 2 * log n) = O(n)
# Space Complexity: O(n)

# Solution 2: Slow and Fast Pointers
def lengthofLoop2(head):
    slow = head
    fast = head 
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return findLength(slow, fast)
        
    return 0

def findLength(slow, fast):
    count = 1
    fast = fast.next
    
    while slow != fast:
        count += 1
        fast = fast.next
        
    return count

# Time Complexity: O(n) - traverse until pointers meet (<= n steps) + count cycle length (<= n)
# Space Complexity: O(1) - uses a constant number of pointers

# Examples
head1 = [3,2,0,-4]
pos1 = 1
print(lengthOfLoop(head1, pos1)) # Output: 3

head2 = [1,2]
pos2 = 0
print(lengthOfLoop(head2, pos2)) # Output: 2

head3 = [1,2,3,4,5]
pos3 = -1
print(lengthOfLoop(head3, pos3)) # Output: 0

head4 = []
pos4 = -1
print(lengthOfLoop(head4, pos4)) # Output: 0

head5 = [1]
pos5 = -1
print(lengthOfLoop(head5, pos5)) # Output: 0

head6 = [1]
pos6 = 0
print(lengthOfLoop(head6, pos6)) # Output: 1

head7 = [1,2]
pos7 = 1
print(lengthOfLoop(head7, pos7)) # Output: 1

head8 = [1,2,3,4,5,6,7,8,9,10]
pos8 = 5
print(lengthOfLoop(head8, pos8)) # Output: 5

head9 = [1,2,3,4,5,6,7,8,9,10]
pos9 = -1
print(lengthOfLoop(head9, pos9)) # Output: 0

head10 = [1,2,3,4,5]
pos10 = 4
print(lengthOfLoop(head10, pos10)) # Output: 1

head11 = [-1,-2,-3,-4,-5]
pos11 = 2
print(lengthOfLoop(head11, pos11)) # Output: 3

head12 = [0,0,0,0,0]
pos12 = 1
print(lengthOfLoop(head12, pos12)) # Output: 4

head13 = [1000,2000,3000,4000,5000]
pos13 = 3
print(lengthOfLoop(head13, pos13)) # Output: 2

head14 = [1,2,3,4,5,6,7,8,9,10,11,12]
pos14 = 8
print(lengthOfLoop(head14, pos14)) # Output: 4

head15 = [1,2,3,4,5,6,7,8,9,10,11,12]
pos15 = -1
print(lengthOfLoop(head15, pos15)) # Output: 0

head16 = [1,1,1,1,1]
pos16 = 2
print(lengthOfLoop(head16, pos16)) # Output: 3

head17 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pos17 = 10
print(lengthOfLoop(head17, pos17)) # Output: 5

head18 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pos18 = -1
print(lengthOfLoop(head18, pos18)) # Output: 0

head19 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pos19 = 15
print(lengthOfLoop(head19, pos19)) # Output: 5

head20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pos20 = -1
print(lengthOfLoop(head20, pos20)) # Output: 0