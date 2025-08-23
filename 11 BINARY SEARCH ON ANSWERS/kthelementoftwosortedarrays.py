# KTH ELEMENT OF TWO SORTED ARRAYS

# Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.

def kthElementofTwoSortedArrays(a, b, k):
    n1 = len(a)
    n2 = len(b)
    
    if n1 > n2:
        return kthElementofTwoSortedArrays(b, a, k)
    
    left = k
    
    n = n1 + n2
    
    low = max(0, k - n1)
    high = min(k, n1)
    
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        
        if mid1 < n1:
            r1 = a[mid1]
        if mid2 < n2:
            r2 = b[mid2]
            
        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]  
            
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
            
# Examples
a1 = [2, 3, 6, 7, 9], b1 = [1, 4, 8, 10], k1 = 5
print(kthElementofTwoSortedArrays(a1, b1, k1)) # Output: 6

a2 = [1, 3, 5, 7, 9], b2 = [2, 4, 6, 8, 10], k2 = 7
print(kthElementofTwoSortedArrays(a2, b2, k2)) # Output: 7

a3 = [1, 2, 3], b3 = [4, 5, 6, 7, 8], k3 = 4
print(kthElementofTwoSortedArrays(a3, b3, k3)) # Output: 4

a4 = [10, 20, 30, 40], b4 = [5, 15, 25, 35], k4 = 3
print(kthElementofTwoSortedArrays(a4, b4, k4)) # Output: 15

a5 = [1, 1, 1, 1], b5 = [2, 2, 2, 2], k5 = 5
print(kthElementofTwoSortedArrays(a5, b5, k5)) # Output: 2

a6 = [1, 2, 3, 4, 5], b6 = [6, 7, 8, 9, 10], k6 = 8
print(kthElementofTwoSortedArrays(a6, b6, k6)) # Output: 8

a7 = [1], b7 = [2, 3, 4, 5], k7 = 2
print(kthElementofTwoSortedArrays(a7, b7, k7)) # Output: 2

a8 = [1, 2, 3, 4, 5], b8 = [1], k8 = 3
print(kthElementofTwoSortedArrays(a8, b8, k8)) # Output: 3

a9 = [1, 3, 5, 7, 9, 11], b9 = [2, 4, 6, 8, 10, 12], k9 = 10
print(kthElementofTwoSortedArrays(a9, b9, k9)) # Output: 10

a10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], b10 = [11, 12, 13, 14, 15], k10 = 12
print(kthElementofTwoSortedArrays(a10, b10, k10)) # Output: 12