# COPY LIST WITH RANDOM POINTER

'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
'''

class ListNode:
    def __init__(self, x: int, next: 'ListNode' = None, random: 'ListNode'= None):
        self.val = int(x)
        self.next = next
        self.random = random
        
# Solution 1: Using HashMap
def copyRandomList1(head):
    if not head:
        return None
    
    current = head
    hashMap = {}
    
    while current:
        newNode = ListNode(current.val)
        hashMap[current] = newNode
        current = current.next
        
    current = head
    
    while current:
        copyNode = hashMap[current]
        copyNode.next = hashMap.get(current.next)
        copyNode.random = hashMap.get(current.random)
        current = current.next
        
    return hashMap[head]

# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list twice: once to create the mapping and once to set next and random pointers.
# Space Complexity: O(n), for the extra space used by the hashMap to store the mapping from original nodes to their copies.

# Solution 2: Using DummyNode and No Extra Space
def copyRandomList2(head):
    if not head:
        return None
    
    current = head
    
    while current:
        copyNode = ListNode(current.val)
        copyNode.next = current.next
        current.next = copyNode
        current = current.next.next
        
    current = head
    
    while current:
        copyNode = current.next
        if current.random:
            copyNode.random = current.random.next
        else:
            copyNode.random = None
        current = current.next.next

    dummyNode = ListNode(-1)
    result = dummyNode
    current = head
    
    while current:
        result.next = current.next
        current.next = current.next.next
        result = result.next
        current = current.next
        
    return dummyNode.next

# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list three times: once to interleave nodes, once to assign random pointers, and once to separate the lists.
# Space Complexity: O(1), since we do not use any extra space that grows with the input size (excluding the space for the new nodes themselves).

# Test Cases
# Test Case 1: Example from the problem
head1 = [[7,None],[13,0],[11,4],[10,2],[1,0]]
print(copyRandomList2(head1)) # Output: [[7,None],[13,0],[11,4],[10,2],[1,0]]

# Test Case 2: Empty list
head2 = []
print(copyRandomList2(head2)) # Output: []

# Test Case 3: Single node, random points to itself
head3 = [[1,0]]
print(copyRandomList2(head3)) # Output: [[1,0]]

# Test Case 4: Two nodes, randoms are None
head4 = [[1,None],[2,None]]
print(copyRandomList2(head4)) # Output: [[1,None],[2,None]]

# Test Case 5: Two nodes, randoms point to each other
head5 = [[1,1],[2,0]]
print(copyRandomList2(head5)) # Output: [[1,1],[2,0]]

# Test Case 6: Three nodes, all randoms are None
head6 = [[1,None],[2,None],[3,None]]
print(copyRandomList2(head6)) # Output: [[1,None],[2,None],[3,None]]

# Test Case 7: Three nodes, randoms form a cycle
head7 = [[1,1],[2,2],[3,0]]
print(copyRandomList2(head7)) # Output: [[1,1],[2,2],[3,0]]

# Test Case 8: Four nodes, randoms alternate between None and valid
head8 = [[1,None],[2,0],[3,None],[4,2]]
print(copyRandomList2(head8)) # Output: [[1,None],[2,0],[3,None],[4,2]]

# Test Case 9: Five nodes, all randoms point to the last node
head9 = [[1,4],[2,4],[3,4],[4,4],[5,4]]
print(copyRandomList2(head9)) # Output: [[1,4],[2,4],[3,4],[4,4],[5,4]]

# Test Case 10: Five nodes, randoms point backwards (reverse order)
head10 = [[1,None],[2,0],[3,1],[4,2],[5,3]]
print(copyRandomList2(head10)) # Output: [[1,None],[2,0],[3,1],[4,2],[5,3]]